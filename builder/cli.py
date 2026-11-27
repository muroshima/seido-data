"""seido registry <check|coverage|entities> / seido update <source_id ...|--daily> [--commit]
/ seido index / seido fill [--commit]

registry: 対応表（registry/）を検証し、カバー状況を書き出し、団体の一覧を生成する。
update:   対応表の取得元から取り込み、raw/ と seido/ を置き換える。--commit を付けると、
          変化があった取得元ごとに 1 コミット作る。コミット日は「観測日 00:00 JST」。
index:    seido/ の制度ファイルから一覧（seido/index.csv）を作り直す。update は自動で作り直す。
fill:     GPU が空いている間に、update が抽出を見送ったページだけを取り直して LLM に回す。
trial:    取得元の候補を書き込まずに試し取りし、採否を出す。--apply で対応表に反映する。
regress:  取り込み方を変えたとき、新旧のコードで取得元ごとの結果を比べる。
"""

import argparse
import json
import os
import subprocess
import sys
import time
import traceback
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from datetime import date
from pathlib import Path

from . import BUILDER_VERSION, backlog, extract, http, registry, trial
from . import map as map_
from .model import SourceInfo
from .sources import Fetched, loader_for, source_info, stopped_at
from .store import Stats, write_index, write_units

FETCH_WORKERS = 16  # 同時に取りに行く取得元の数
# 実行を始めてからこの秒数を過ぎたら、まだ取れていない取得元は次の実行に回す（push まで終えるため）
RUN_BUDGET = int(os.environ.get("SEIDO_RUN_BUDGET") or 0) or None
# 失敗した取得元と理由を書き出すファイル（ワークフローが Issue で知らせる）
FAILED_FILE = os.environ.get("SEIDO_FAILED_FILE")


class SharpDrop(Exception):
    """前回より制度ページが大きく減った。サイトの作り替えで一覧が空になったときなど。"""


def sharp_drop(before: int, after: int) -> bool:
    """前回 before 件 → 今回 after 件を、書き込まずに止めるべき減り方とみなすか。

    0 件になったとき、または 6 件以上あったものが半分未満になったとき。
    """
    return before > 0 and (after == 0 or (before >= 6 and after < before / 2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="seido")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="cmd", required=True)
    reg = sub.add_parser("registry", help="対応表（registry/）を扱う")
    reg_sub = reg.add_subparsers(dest="action", required=True)
    reg_sub.add_parser("check", help="entities.csv と sources.csv を検証する")
    reg_sub.add_parser("coverage", help="registry/COVERAGE.md と coverage-map.svg を書き出す")
    bnd = reg_sub.add_parser(
        "boundaries", help="国土数値情報から地図の境界（registry/boundaries.json）を作り直す"
    )
    bnd.add_argument("--cache", type=Path, required=True, help="zip を置くディレクトリ")
    ent = reg_sub.add_parser("entities", help="総務省と Wikidata から entities.csv を更新する")
    ent.add_argument("--pref", action="append", default=[], help="都道府県コード 2 桁（複数可）")
    ent.add_argument("--gov", action="store_true", help="国の府省庁も入れる")
    up = sub.add_parser("update", help="取得元から取り込んで raw/ と seido/ を更新する")
    up.add_argument("source_ids", nargs="*", help="sources.csv の source_id")
    up.add_argument(
        "--daily", action="store_true", help="取込中で、更新が止まっていない取得元を全部回す"
    )
    up.add_argument("--commit", action="store_true", help="変化があれば git commit する")
    up.add_argument(
        "--extract",
        action="store_true",
        help="事実だけの取得元で、新しいページと変わったページから LLM で制度の情報を取り出す",
    )
    up.add_argument(
        "--allow-drop",
        action="append",
        default=[],
        metavar="SOURCE_ID",
        help="制度ページが前回より大きく減っても書き込む取得元（複数可）",
    )
    sub.add_parser("index", help="seido/index.csv（制度の一覧）を作り直す")
    fl = sub.add_parser(
        "fill", help="巡回はせず、制度の情報をまだ取り出していないページだけを LLM に回す"
    )
    fl.add_argument("--commit", action="store_true", help="取得元ごとに git commit する")
    tr = sub.add_parser("trial", help="取得元の候補を書き込まずに試し取りし、採否を出す")
    tr.add_argument("source_ids", nargs="*", help="sources.csv の source_id")
    tr.add_argument(
        "--add", type=Path, help="対応表に無い候補の行（sources.csv と同じ列の CSV）。全行を試す"
    )
    tr.add_argument(
        "--apply",
        action="store_true",
        help="結果を sources.csv に反映する（取り込めるものを取込中にし、checked と note を書く）",
    )
    rg = sub.add_parser(
        "regress", help="取得元ごとの取り込み結果を JSON に書き出す／2 つの JSON を比べる"
    )
    rg.add_argument(
        "source_ids", nargs="*", help="sources.csv の source_id（省略時は取込中の web）"
    )
    rg.add_argument("--cache", type=Path, help="取ったページを置くディレクトリ（新旧で共有する）")
    rg.add_argument("--out", type=Path, help="書き出す JSON")
    rg.add_argument("--compare", nargs=2, type=Path, metavar=("OLD", "NEW"), help="2 つを比べる")
    args = parser.parse_args(argv)

    if args.cmd == "index":
        write_index(args.root)
        return 0
    if args.cmd == "update":
        return update(
            args.root,
            args.source_ids,
            args.daily,
            args.commit,
            args.extract,
            frozenset(args.allow_drop),
        )
    if args.cmd == "trial":
        return run_trial(args.root, args.source_ids, args.add, args.apply)
    if args.cmd == "regress":
        return run_regress(args)
    if args.cmd == "fill":
        entities, sources = registry.load(args.root)
        budget = extract.EXTRACT_BUDGET or 3600
        return backlog.run(args.root, sources, entities, budget, args.commit)
    return registry_command(args)


def registry_command(args: argparse.Namespace) -> int:
    root: Path = args.root
    if args.action == "boundaries":
        data = map_.build_boundaries(args.cache)
        (root / "registry" / "boundaries.json").write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
        )
        print({k: len(v) for k, v in data["layers"].items()})
        return 0
    if args.action == "entities":
        path = root / "registry" / "entities.csv"
        existing = registry.read(path, registry.ENTITY_FIELDS) if path.exists() else []
        generated = registry.generate_entities(args.pref, args.gov)
        merged = registry.merge_entities(existing, generated)
        registry.write(path, registry.ENTITY_FIELDS, merged)
        print(f"entities: {len(existing)} → {len(merged)} 件")
        return 0

    entities, sources = registry.load(root)
    errors = registry.validate(entities, sources)
    for e in errors:
        print(e, file=sys.stderr)
    if errors:
        return 1
    if args.action == "coverage":
        (root / "registry" / "COVERAGE.md").write_text(
            registry.coverage(entities, sources), encoding="utf-8"
        )
        (root / "registry" / "coverage-map.svg").write_text(
            coverage_map(root, entities, sources), encoding="utf-8"
        )
    print(f"entities {len(entities)} 件 / sources {len(sources)} 件")
    return 0


def run_trial(root: Path, source_ids: list[str], add: Path | None, do_apply: bool) -> int:
    path = root / "registry" / "sources.csv"
    rows = trial.read_rows(path)
    by_id = {r["source_id"]: r for r in rows}
    unknown = [i for i in source_ids if i not in by_id]
    if unknown:
        print(f"対応表に無い取得元: {unknown}", file=sys.stderr)
        return 1
    tried = [by_id[i] for i in source_ids] + (trial.read_rows(add) if add else [])
    if not tried:
        print("試す取得元を source_id か --add で指定する", file=sys.stderr)
        return 1
    results = trial.trial(tried)
    trial.report(tried, results)
    if do_apply:
        trial.write_rows(path, trial.apply(rows, tried, results, date.today()))
        entities, sources = registry.load(root)
        if errors := registry.validate(entities, sources):
            print("\n".join(errors), file=sys.stderr)
            return 1
        print("sources.csv に反映した。`seido registry coverage` で COVERAGE.md を作り直す")
    return 0


def run_regress(args) -> int:
    if args.compare:
        old, new = (json.loads(p.read_text(encoding="utf-8")) for p in args.compare)
        lines = trial.compare(old, new)
        print("\n".join(lines))
        print(f"違いのある取得元: {len(lines)} / {len(old.keys() | new.keys())}")
        return 0
    if not (args.cache and args.out):
        print("--cache と --out を指定する（比べるときは --compare）", file=sys.stderr)
        return 1
    _, sources = registry.load(args.root)
    if args.source_ids:
        rows = [s for s in sources if s["source_id"] in set(args.source_ids)]
    else:
        rows = [s for s in sources if s["status"] == "取込中" and s["kind"] == "web"]
    trial.regress([r for r in rows if loader_for(r)], args.cache, args.out)
    print(f"{len(rows)} 取得元を {args.out} に書き出した")
    return 0


def coverage_map(root: Path, entities: list[dict], sources: list[dict]) -> str:
    boundaries = json.loads((root / "registry" / "boundaries.json").read_text(encoding="utf-8"))
    codes, names = map_.covered_names(entities, sources, registry.expand)
    return map_.render(boundaries, codes, names)


def update(
    root: Path,
    source_ids: list[str],
    daily: bool,
    do_commit: bool,
    do_extract: bool = False,
    allow_drop: frozenset[str] = frozenset(),
) -> int:
    entities, sources = registry.load(root)
    errors = registry.validate(entities, sources)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    by_id = {s["source_id"]: s for s in sources}
    if daily:
        source_ids = daily_sources(sources)
    unknown = [i for i in source_ids if i not in by_id or not loader_for(by_id[i])]
    if unknown or not source_ids:
        print(f"取り込めない取得元: {unknown or '指定なし'}", file=sys.stderr)
        return 1
    if do_commit and (dirty := uncommitted(root)):
        print(f"未コミットの変更があるのでコミットできない:\n{dirty}", file=sys.stderr)
        return 1

    names = {e["id"].removeprefix("lg:"): e["name"] for e in entities if e["lg_code"]}
    failed = []
    gpu_busy = False
    started = time.monotonic()
    budget = extract.EXTRACT_BUDGET
    deadline = started + budget if budget else None
    # 取得（巡回）だけを並列にする。同じホストへは http が 1 本ずつに絞る。
    # 抽出（GPU）・書き出し・コミットは、取得元の順に 1 つずつ行う
    # 対応表は同じ団体の取得元が続けて並ぶので、そのまま投げると同時に動く取得元が同じホストを
    # 待ち合う。ホストごとに 1 つずつ順に投げて、同時に動く取得元のホストを散らす
    pool = ThreadPoolExecutor(FETCH_WORKERS)
    run_deadline = started + RUN_BUDGET if RUN_BUDGET else None
    futures = {
        sid: pool.submit(loader_for(by_id[sid]).fetch, by_id[sid])
        for sid in by_host_round_robin(source_ids, by_id)
    }
    skipped = []
    for sid in source_ids:
        row = by_id[sid]
        info = source_info(row, entities)
        try:
            wait = None if run_deadline is None else max(0.0, run_deadline - time.monotonic())
            try:
                fetched: Fetched = futures[sid].result(timeout=wait)
            except FuturesTimeout:
                skipped.append(sid)
                continue
            # 更新が止まった取得元は、止まった時点の内容としてコミットする
            fetched.observed = stopped_at(row) or fetched.observed
            outside = {f"lg:{lg}" for lg in fetched.units} - registry.expand(
                row["covers"], entities
            )
            if outside:
                raise ValueError(f"covers の範囲外の自治体: {sorted(outside)[:5]}")
            before = len(list((root / "raw" / sid).glob("*/*.json")))
            after = sum(len(records) for records in fetched.units.values())
            if sharp_drop(before, after) and sid not in allow_drop:
                raise SharpDrop(
                    f"制度ページが前回 {before} 件から {after} 件に減った。"
                    "一覧の URL や作りが変わっていないか確かめる"
                    f"（意図した減少なら --allow-drop {sid}）"
                )
            for records in fetched.units.values():
                for r in records:
                    r.lg_name = names.get(r.lg_code, r.lg_name)
            # 巡回で本文を取った取得元（Web の一覧ページ）は、publish にかかわらず事実を取り出す。
            # 本文を持たない取り込み（標準形式の CSV など）は対象にしない
            if any(r.source_text is not None for rs in fetched.units.values() for r in rs):
                for records in fetched.units.values():
                    over = deadline is not None and time.monotonic() > deadline
                    llm_session = extract.session if do_extract and not (gpu_busy or over) else None
                    try:
                        n = extract.fill(root, sid, records, llm_session, deadline)
                    except extract.GPUBusy as e:
                        # GPU が空かない日は巡回の結果だけを書く。前回の項目は残り、
                        # 新しいページや本文が変わったページは次に GPU が空いたときに取り出す。
                        # この実行のほかの取得元でも、もう GPU を待たない
                        print(f"{sid}: 抽出を見送り、巡回の結果だけを書く（{e}）", file=sys.stderr)
                        gpu_busy = True
                        n = extract.fill(root, sid, records, None)
                    if n:
                        print(f"{sid}: {n} ページから制度の情報を取り出した")
            raw_stats, seido_stats = write_units(root, info, fetched.units)
        except Exception as e:  # noqa: BLE001 1 つの取得元の失敗で、ほかを止めない
            print(
                f"{sid}: 取り込み失敗（何も書き換えない）\n{traceback.format_exc()}",
                file=sys.stderr,
            )
            failed.append((sid, f"{type(e).__name__}: {e}"))
            continue
        if not seido_stats.empty:
            write_index(root)  # 一覧も同じコミットに入れる
        summary = describe(seido_stats if not seido_stats.empty else raw_stats)
        print(f"{sid}: 自治体 {len(fetched.units)} / {summary or '変化なし'}")
        if do_commit and not (raw_stats.empty and seido_stats.empty):
            commit(root, info, fetched, summary)
    if skipped:
        # 取りかけの取得元は http が次のリクエストで止める。まだ始まっていないものは取り消す
        http.STOP.set()
        print(
            f"時間切れで次の実行に回した取得元: {len(skipped)} 件 {skipped[:10]}", file=sys.stderr
        )
    pool.shutdown(cancel_futures=True)
    if FAILED_FILE and failed:
        with open(FAILED_FILE, "w", encoding="utf-8") as f:
            for sid, reason in failed:
                f.write(f"{sid}\t{' '.join(reason.split())[:300]}\n")
    # 取れた分はコミットしたうえで、失敗した取得元があればジョブを失敗させて気付けるようにする
    return 2 if failed else 0


def by_host_round_robin(source_ids: list[str], by_id: dict) -> list[str]:
    """取得元を、ホストごとに 1 つずつ順に並べ直す（同じホストの取得元が続かないように）。"""
    queues: dict[str, list[str]] = {}
    for sid in source_ids:
        queues.setdefault(urllib.parse.urlsplit(by_id[sid]["url"]).netloc, []).append(sid)
    order = []
    while queues:
        for host in list(queues):
            order.append(queues[host].pop(0))
            if not queues[host]:
                del queues[host]
    return order


def daily_sources(sources: list[dict[str, str]]) -> list[str]:
    """日次で回す取得元。取込中で、更新が止まっておらず、取り込みが実装されているもの。"""
    return [
        s["source_id"]
        for s in sources
        if s["status"] == "取込中" and not stopped_at(s) and loader_for(s)
    ]


def describe(stats: Stats) -> str:
    parts = [
        f"{len(v)}件{label}"
        for label, v in (("追加", stats.added), ("更新", stats.changed), ("削除", stats.removed))
        if v
    ]
    return "・".join(parts)


def uncommitted(root: Path) -> str:
    """ステージ済みの変更と、raw/・seido/ の未コミットの変更。

    コミットにはこの取得元の今回の変化だけを入れたいので、ほかの変更が混ざる状態では始めない。
    """
    staged = git(root, "diff", "--cached", "--name-only")
    data = git(root, "status", "--porcelain", "--", "raw", "seido")
    return (staged + data).strip()


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    ).stdout


def commit(root: Path, info: SourceInfo, fetched: Fetched, summary: str) -> None:
    observed = fetched.observed.isoformat()
    message = "\n".join(
        [
            f"{info.name}: {summary}（{observed} 観測）",
            "",
            f"Source: {info.name}",
            f"Source-Url: {info.url}",
            f"Observed: {observed}",
            f"Builder-Version: {BUILDER_VERSION}",
        ]
    )
    when = f"{observed}T00:00:00+09:00"
    env = {**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
    # 1 つの取得元の書き換えは raw/ と seido/ の中に閉じる。それ以外は uncommitted() で弾いている
    git(root, "add", "--all", "--", "raw", "seido")
    subprocess.run(
        ["git", "commit", "--quiet", "-m", message, "--", "raw", "seido"],
        cwd=root,
        env=env,
        check=True,
    )


if __name__ == "__main__":
    sys.exit(main())
