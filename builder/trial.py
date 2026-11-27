"""取得元の候補を試し取りして採否を決める（seido trial）と、取り込み方を変えたときの新旧比較
（seido regress）。

trial:   対応表の行（または候補の CSV の行）を、書き込まずに取り込み、取得元ごとのページ数と題名、
         題名のうち制度らしいものの割合を出す。--apply で対応表の status・checked・note に反映する
regress: 取得元ごとに、取り込んだページの ID・題名・本文のハッシュを JSON に書き出す。
         取ったバイト列はディスクに保存するので、旧のコード（git worktree）と新のコードで
         同じページを読んで比べられる
"""

import csv
import hashlib
import json
import re
import sys
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from . import http
from .sources import loader_for

WORKERS = 16
# 題名のうち制度らしいもの（PROGRAM に当たり NOISE に当たらない）の割合がこれ以上なら取り込む
ADOPT = 0.4
# これ未満は題名を見て確かめる
CHECK = 0.6
PROGRAM = re.compile(
    r"手当|助成|補助|給付|支援|医療|減免|免除|貸付|貸与|融資|奨励|奨学|祝金|祝い金|年金|手帳|"
    r"費|料|割引|無料|支給|交付|扶養|控除|軽減|還付|利子|資金|ひとり親|保険|健診|検診|受給|証|"
    r"サービス|事業|制度|利用|貸し出し|レンタル|配布|配付|ポイント|クーポン|券"
)
NOISE = re.compile(
    r"会議|審議会|委員会|議事録|計画|募集|説明会|イベント|講座|教室|お知らせ|新着|"
    r"見つからない|サイトマップ|アクセス|組織|課$|係$|センター$|入札|採用|報告|結果|統計|"
    r"アンケート|パブリックコメント|よくある|FAQ|リンク|トップ|ホーム|一覧$"
)
# note の末尾に足す試行の結果。取り直したら置き換える
TRIAL_NOTE = re.compile(r"(^| / )\d{4}-\d{2}-\d{2} の試行で[^/]*$")


def is_program(title: str) -> bool:
    return bool(PROGRAM.search(title)) and not NOISE.search(title)


@dataclass
class Result:
    source_id: str
    titles: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def ratio(self) -> float:
        return sum(map(is_program, self.titles)) / len(self.titles) if self.titles else 0.0

    def adopt(self, fmt: str) -> bool:
        """取込中にしてよいか。1 ページだけの行（html-page）は、取れれば取り込む。"""
        if self.error or not self.titles:
            return False
        return fmt == "html-page" or self.ratio >= ADOPT

    def verdict(self, fmt: str) -> str:
        if not self.adopt(fmt):
            return "NG"
        return "OK" if fmt == "html-page" or self.ratio >= CHECK else "CHECK"


def titles_of(fetched) -> list[str]:
    return [
        (r.seido.title if r.seido else None) or r.raw.get("title") or ""
        for records in fetched.units.values()
        for r in records
    ]


def try_row(row: dict) -> Result:
    loader = loader_for(row)
    if loader is None:
        return Result(row["source_id"], error="取り込み方が無い（kind・format を確かめる）")
    try:
        return Result(row["source_id"], titles_of(loader.fetch(row)))
    except Exception as e:  # noqa: BLE001 1 つの失敗で、ほかを止めない
        return Result(row["source_id"], error=f"{type(e).__name__}: {e}"[:200])


def trial(rows: list[dict]) -> list[Result]:
    with ThreadPoolExecutor(WORKERS) as pool:
        return list(pool.map(try_row, rows))


def report(rows: list[dict], results: list[Result], out=None) -> None:
    out = out or sys.stdout
    for row, res in zip(rows, results, strict=True):
        head = f"{res.verdict(row['format'])}\t{res.source_id}\tn={len(res.titles)}"
        if res.error:
            print(f"{head}\t{res.error}", file=out)
            continue
        noise = [t for t in res.titles if not is_program(t)]
        print(f"{head}\t制度らしい題名 {res.ratio:.0%}\t" + " | ".join(noise[:6]), file=out)
        for t in res.titles[:40]:
            print(f"    {t}", file=out)


def apply(
    registry_rows: list[dict], tried: list[dict], results: list[Result], today: date
) -> list[dict]:
    """試行の結果を対応表の行に当てる。

    取り込めるものは取込中にし、取り込めないものは status を変えない。対応表に無い行は、
    取り込めるものだけ足す（seido discover の候補には、制度の一覧でないページも混じるため）。
    対応表の行と source_id が同じで provider が違う候補があれば、何も反映せずに止める。
    """
    by_id = {r["source_id"]: r for r in registry_rows}
    clash = [
        row["source_id"]
        for row in tried
        if row["source_id"] in by_id and row["provider"] != by_id[row["source_id"]]["provider"]
    ]
    if clash:  # 古い対応表で作った候補の ID が、あとで足された別団体の行と重なった
        raise ValueError(f"別の団体の行と source_id が重なる: {', '.join(clash)}")
    out = list(registry_rows)
    for row, res in zip(tried, results, strict=True):
        target = by_id.get(row["source_id"])
        if target is None:
            if not res.adopt(row["format"]):
                continue
            target = dict(row)
            out.append(target)
        else:
            target.update({k: v for k, v in row.items() if k not in ("status", "checked", "note")})
        if res.adopt(row["format"]):
            target["status"] = "取込中"
        target["checked"] = today.isoformat()
        if res.error:
            found = f"失敗（{res.error[:80]}）"
        elif row["format"] == "html-page":
            found = f"{len(res.titles)}ページ"
        else:
            found = f"{len(res.titles)}ページ・制度らしい題名{res.ratio:.0%}"
        note = TRIAL_NOTE.sub("", target.get("note", "")).strip()
        target["note"] = " / ".join(filter(None, [note, f"{today.isoformat()} の試行で{found}"]))
    return out


def read_rows(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, rows: list[dict]) -> None:
    with open(path, encoding="utf-8", newline="") as f:
        fields = next(csv.reader(f))
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def cache_http(directory: Path) -> None:
    """http.get の結果をディスクに置き、2 回目からはそれを読む。エラーの応答も覚える。"""
    directory.mkdir(parents=True, exist_ok=True)
    real_get = http.get

    def get(url: str, params: dict | None = None, retries: int = 3) -> bytes:
        key = hashlib.sha1((url + json.dumps(params, sort_keys=True)).encode()).hexdigest()
        path = directory / key
        if path.exists():
            data = path.read_bytes()
            if data.startswith(b"!ERR"):
                raise urllib.error.HTTPError(url, int(data[4:7]), "cached", {}, None)  # type: ignore[arg-type]
            return data
        try:
            data = real_get(url, params, retries)
        except urllib.error.HTTPError as e:
            path.write_bytes(b"!ERR%03d" % e.code)
            raise
        path.write_bytes(data)
        return data

    http.get = get  # type: ignore[assignment]


def fingerprint(row: dict) -> tuple[str, dict]:
    loader = loader_for(row)
    try:
        fetched = loader.fetch(row)
    except Exception as e:  # noqa: BLE001
        return row["source_id"], {"error": f"{type(e).__name__}: {e}"[:200]}
    pages = {
        r.record_id: [r.raw.get("title"), r.raw.get("content_sha256")]
        for records in fetched.units.values()
        for r in records
    }
    return row["source_id"], {"pages": pages}


def regress(rows: list[dict], cache: Path, out: Path) -> None:
    cache_http(cache)
    with ThreadPoolExecutor(WORKERS) as pool:
        result = dict(pool.map(fingerprint, rows))
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1, sort_keys=True), "utf-8")


def compare(old: dict, new: dict) -> list[str]:
    """取得元ごとの違い。ページの増減、題名の違い、本文のハッシュの違い、失敗の違い。"""
    lines = []
    for sid in sorted(old.keys() | new.keys()):
        a, b = old.get(sid), new.get(sid)
        if a == b:
            continue
        if a is None or b is None:
            lines.append(f"{sid}: {'新' if a is None else '旧'}だけにある")
            continue
        if "error" in a or "error" in b:
            lines.append(f"{sid}: 旧 {a.get('error', 'ok')} / 新 {b.get('error', 'ok')}")
            continue
        pa, pb = a["pages"], b["pages"]
        diffs = []
        if added := sorted(pb.keys() - pa.keys()):
            diffs.append(f"追加 {len(added)} {added[:3]}")
        if removed := sorted(pa.keys() - pb.keys()):
            diffs.append(f"削除 {len(removed)} {removed[:3]}")
        both = pa.keys() & pb.keys()
        if titles := [f"{pa[k][0]} → {pb[k][0]}" for k in sorted(both) if pa[k][0] != pb[k][0]]:
            diffs.append(f"題名 {len(titles)} {titles[:2]}")
        if hashes := [k for k in sorted(both) if pa[k][1] != pb[k][1]]:
            diffs.append(f"本文 {len(hashes)} {hashes[:3]}")
        lines.append(f"{sid}: " + " / ".join(diffs))
    return lines
