"""巡回はせず、制度の情報をまだ取り出していないページだけを LLM に回す（seido fill）。

日次の巡回（update）は GPU が空かない日に抽出を見送る。見送ったページは seido/ に
content_sha256 と食い違う facts_sha256（または空）を持って残るので、GPU が空いた時間に
それだけを取り直して取り出す。

- 取り直したページの本文が、前回の巡回のときと同じ（content_sha256 が一致する）ときだけ取り出す。
  変わっていたら触らない。本文の変化は次の巡回で観測として記録する
- 書き換えるのは seido/ の Markdown の項目と facts_sha256 だけ。raw/ と一覧（index.csv）は変わらない
- GPU は Kaggle のジョブを優先する。ロックは CHUNK 秒ごとに手放し、その間に Kaggle のジョブが
  ロックを取っていたら、そこでやめる。初めから GPU が空いていなければ何もしない
"""

import contextlib
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

from . import BUILDER_VERSION, extract, webpage
from .model import Record, Seido, SourceInfo, check_publishable, render
from .sources import source_info, stopped_at
from .sources.webindex import PDF
from .store import read_front, read_sections, seido_dir

# ロックを持ち続ける秒数。過ぎたら手放し、Kaggle のジョブが待っていれば譲る
CHUNK = int(os.environ.get("SEIDO_FILL_CHUNK") or 600)
# 手放してから取り直すまでの秒数。ロックを待っているジョブが先に取れるように空ける
YIELD_SECONDS = 15


def pending(root: Path, source_id: str) -> list[Path]:
    """この取得元の、制度の情報がまだ今の本文から取り出されていないページ。"""
    found = []
    for path in sorted((root / "seido").glob(f"*/*/{source_id}/*.md")):
        front = read_front(path)
        if front.get("content_sha256") and front.get("facts_sha256") != front["content_sha256"]:
            found.append(path)
    return found


def page_text(url: str, fmt: str) -> str:
    """巡回（webindex）と同じやり方で取ったページの本文。"""
    if fmt == PDF:
        from . import http

        return webpage.pdf_text(http.get(url))
    return webpage.fetch(url).text


def load_record(root: Path, source_id: str, path: Path) -> Record:
    """seido/ の Markdown と raw/ の JSON から、書き出したときの Record を組み立て直す。"""
    front = read_front(path)
    raw_path = root / "raw" / source_id / front["lg_code"] / f"{path.stem}.json"
    return Record(
        lg_code=front["lg_code"],
        lg_name=front["lg_name"],
        record_id=path.stem,
        raw=json.loads(raw_path.read_text(encoding="utf-8")),
        seido=Seido(
            title=front["title"],
            support=front.get("support"),
            url=front.get("url"),
            source_updated=front.get("source_updated"),
            sections=read_sections(path),
            facts_sha256=front.get("facts_sha256"),
        ),
    )


def fill_source(
    root: Path, info: SourceInfo, fmt: str, paths: list[Path], llm, deadline: float
) -> tuple[int, int]:
    """1 つの取得元の待ちページを取り出す。(取り出した数, 本文が変わったか取れずに見送った数)。"""
    done = changed = 0
    for path in paths:
        if time.monotonic() > deadline:
            break
        record = load_record(root, info.name, path)
        try:
            text = page_text(record.raw["url"], fmt)
        except Exception:  # noqa: BLE001 消えたページや一時的な失敗は、次の巡回で観測する
            changed += 1
            continue
        if hashlib.sha256(text.encode()).hexdigest() != record.raw["content_sha256"]:
            changed += 1
            continue
        record.source_text = text
        assert record.seido is not None
        record.seido.sections = extract.extract(llm, record.raw["title"], text).sections
        record.seido.facts_sha256 = record.raw["content_sha256"]
        check_publishable(record, info)
        target = seido_dir(root, info.name, record.lg_code) / path.name
        target.write_text(render(record, info), encoding="utf-8")
        done += 1
    return done, changed


@contextlib.contextmanager
def chunked_session():
    """GPU のロックを CHUNK 秒ずつ持つ。llm() が今のクライアントを返し、None なら譲ってやめる。"""
    stack = contextlib.ExitStack()
    state = {"llm": None, "since": 0.0, "first": True}

    def llm():
        if state["llm"] is not None and time.monotonic() - state["since"] < CHUNK:
            return state["llm"]
        if state["llm"] is not None:
            stack.close()  # 手放して、待っているジョブに譲る
            state["llm"] = None
            time.sleep(YIELD_SECONDS)
        try:
            state["llm"] = stack.enter_context(extract.session())
        except extract.GPUBusy:
            return None
        state["since"] = time.monotonic()
        return state["llm"]

    try:
        yield llm
    finally:
        stack.close()


def run(
    root: Path, sources: list[dict], entities: list[dict], budget: float, do_commit: bool
) -> int:
    from .cli import git, uncommitted

    if do_commit and (dirty := uncommitted(root)):
        print(f"未コミットの変更があるのでコミットできない:\n{dirty}", file=sys.stderr)
        return 1
    rows = [
        s for s in sources if s["status"] == "取込中" and not stopped_at(s) and s["kind"] == "web"
    ]
    todo = [(s, p) for s in rows if (p := pending(root, s["source_id"]))]
    print(f"取り出し待ち: {sum(len(p) for _, p in todo)} ページ / {len(todo)} 取得元")
    deadline = time.monotonic() + budget
    total = 0
    failed = []
    extract.GPU_LOCK_WAIT = 0  # 空いていなければ待たない（Kaggle が優先）
    with chunked_session() as llm:
        for row, paths in todo:
            if time.monotonic() > deadline:
                break
            client = llm()
            if client is None:
                print("GPU が使われているので、ここでやめる")
                break
            sid = row["source_id"]
            info = source_info(row, entities)
            # 1 取得元の途中でも CHUNK を過ぎたら譲れるよう、少しずつ回す
            for i in range(0, len(paths), 20):
                client = llm()
                if client is None or time.monotonic() > deadline:
                    break
                try:
                    done, changed = fill_source(
                        root, info, row["format"], paths[i : i + 20], client, deadline
                    )
                except Exception as e:  # noqa: BLE001 1 つの取得元の失敗で、ほかを止めない
                    print(f"{sid}: 取り出し失敗（{e}）", file=sys.stderr)
                    failed.append(sid)
                    break  # 取り出し済みのページは書いたまま（1 ページずつ検査してから書いている）
                total += done
                if done:
                    print(f"{sid}: {done} ページから制度の情報を取り出した")
                if changed:
                    print(
                        f"{sid}: {changed} ページは本文が変わったか取れなかったので次の巡回に回す"
                    )
            if do_commit and git(root, "status", "--porcelain", "--", "seido").strip():
                commit(root, info)
            if client is None:
                print("GPU が使われているので、ここでやめる")
                break
    print(f"合わせて {total} ページから取り出した")
    return 2 if failed else 0


def commit(root: Path, info: SourceInfo) -> None:
    message = "\n".join(
        [
            f"{info.name}: 前回の巡回で取った本文から制度の情報を取り出す",
            "",
            f"Source: {info.name}",
            f"Source-Url: {info.url}",
            f"Extracted: {date.today().isoformat()}",
            f"Builder-Version: {BUILDER_VERSION}",
        ]
    )
    subprocess.run(["git", "add", "--", "seido"], cwd=root, check=True)
    subprocess.run(["git", "commit", "--quiet", "-m", message, "--", "seido"], cwd=root, check=True)
