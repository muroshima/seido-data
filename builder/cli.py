"""seido registry <check|coverage|entities> / seido update <source_id ...|--daily> [--commit]

registry: 対応表（registry/）を検証し、カバー状況を書き出し、団体の一覧を生成する。
update:   対応表の取得元から取り込み、raw/ と seido/ を置き換える。--commit を付けると、
          変化があった取得元ごとに 1 コミット作る。コミット日は「観測日 00:00 JST」。
"""

import argparse
import os
import subprocess
import sys
import traceback
from pathlib import Path

from . import BUILDER_VERSION, extract, registry
from .model import SourceInfo
from .sources import Fetched, loader_for, source_info, stopped_at
from .store import Stats, write_units


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="seido")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="cmd", required=True)
    reg = sub.add_parser("registry", help="対応表（registry/）を扱う")
    reg_sub = reg.add_subparsers(dest="action", required=True)
    reg_sub.add_parser("check", help="entities.csv と sources.csv を検証する")
    reg_sub.add_parser("coverage", help="registry/COVERAGE.md を書き出す")
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
    args = parser.parse_args(argv)

    if args.cmd == "update":
        return update(args.root, args.source_ids, args.daily, args.commit, args.extract)
    return registry_command(args)


def registry_command(args: argparse.Namespace) -> int:
    root: Path = args.root
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
    print(f"entities {len(entities)} 件 / sources {len(sources)} 件")
    return 0


def update(
    root: Path, source_ids: list[str], daily: bool, do_commit: bool, do_extract: bool = False
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
    for sid in source_ids:
        row = by_id[sid]
        info = source_info(row, entities)
        try:
            fetched: Fetched = loader_for(row).fetch(row)
            # 更新が止まった取得元は、止まった時点の内容としてコミットする
            fetched.observed = stopped_at(row) or fetched.observed
            outside = {f"lg:{lg}" for lg in fetched.units} - registry.expand(
                row["covers"], entities
            )
            if outside:
                raise ValueError(f"covers の範囲外の自治体: {sorted(outside)[:5]}")
            for records in fetched.units.values():
                for r in records:
                    r.lg_name = names.get(r.lg_code, r.lg_name)
            if info.facts_only:
                for records in fetched.units.values():
                    n = extract.fill(root, sid, records, extract.session if do_extract else None)
                    if n:
                        print(f"{sid}: {n} ページから制度の情報を取り出した")
            raw_stats, seido_stats = write_units(root, info, fetched.units)
        except Exception:  # noqa: BLE001 1 つの取得元の失敗で、ほかを止めない
            print(
                f"{sid}: 取り込み失敗（何も書き換えない）\n{traceback.format_exc()}",
                file=sys.stderr,
            )
            failed.append(sid)
            continue
        summary = describe(seido_stats if not seido_stats.empty else raw_stats)
        print(f"{sid}: 自治体 {len(fetched.units)} / {summary or '変化なし'}")
        if do_commit and not (raw_stats.empty and seido_stats.empty):
            commit(root, info, fetched, summary)
    # 取れた分はコミットしたうえで、失敗した取得元があればジョブを失敗させて気付けるようにする
    return 2 if failed else 0


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
