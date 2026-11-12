"""seido registry <check|coverage|entities>

対応表（registry/）を検証し、カバー状況を書き出し、団体の一覧を生成する。
"""

import argparse
import sys
from pathlib import Path

from . import registry


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
    args = parser.parse_args(argv)

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


if __name__ == "__main__":
    sys.exit(main())
