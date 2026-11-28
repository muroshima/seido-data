"""raw/ と seido/ への書き出し。

取得に成功した自治体の分だけを置き換える。取得に失敗した自治体のファイルは触らない
（失敗を「全件廃止」と取り違えないため）。
"""

import csv
import io
import json
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .model import Record, SourceInfo, check_publishable, render


@dataclass
class Stats:
    added: list[str] = field(default_factory=list)
    changed: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)

    @property
    def empty(self) -> bool:
        return not (self.added or self.changed or self.removed)


def raw_dir(root: Path, source: str, lg_code: str) -> Path:
    return root / "raw" / source / lg_code


def seido_dir(root: Path, source: str, lg_code: str) -> Path:
    return root / "seido" / lg_code[:2] / lg_code / source


def read_front(path: Path) -> dict:
    """render() が書いた Markdown の frontmatter。"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text[4:].split("\n---\n", 1)[0]) or {}


INDEX_COLUMNS = (
    "path",
    "lg_code",
    "lg_name",
    "title",
    "support",
    "source",
    "source_id",
    "url",
    "license",
    "attribution",
)


# index.csv の行（パスを除く）。巡回は取得元を 1 つコミットするたびに一覧を作り直すので、
# 前回から変わっていないファイル（更新時刻と大きさが同じ）は読み直さない
_index_rows: dict[Path, tuple[tuple[int, int], list]] = {}


def index_csv(root: Path, pref: str) -> str:
    """seido/<pref>/index.csv の中身。制度 1 件 1 行で、frontmatter の主な項目を並べる。"""
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(INDEX_COLUMNS)
    for path in sorted((root / "seido" / pref).glob("*/*/*.md")):
        st = path.stat()
        key = (st.st_mtime_ns, st.st_size)
        cached = _index_rows.get(path)
        if cached is None or cached[0] != key:
            front = read_front(path)
            cached = (key, ["" if front.get(c) is None else front[c] for c in INDEX_COLUMNS[1:]])
            _index_rows[path] = cached
        writer.writerow([path.relative_to(root).as_posix(), *cached[1]])
    return out.getvalue()


def index_prefs(root: Path) -> list[str]:
    """制度ファイルのある都道府県のコード。"""
    return sorted({p.parent.parent.parent.name for p in (root / "seido").glob("*/*/*/*.md")})


def write_index(root: Path) -> None:
    """都道府県ごとの一覧を作り直す。制度ファイルが無くなった都道府県の一覧は消す。"""
    prefs = index_prefs(root)
    for old in (root / "seido").glob("*/index.csv"):
        if old.parent.name not in prefs:
            old.unlink()
    (root / "seido" / "index.csv").unlink(missing_ok=True)  # 2026-11-28 までの全国の一覧
    for pref in prefs:
        path = root / "seido" / pref / "index.csv"
        text = index_csv(root, pref)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")


def read_sections(path: Path) -> dict[str, str]:
    """render() が書いた Markdown から、`## 見出し` ごとの本文を読み戻す。"""
    sections: dict[str, str] = {}
    heading = None
    lines: list[str] = []
    body = path.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    for line in body.split("\n"):
        if line.startswith("## "):
            if heading:
                sections[heading] = "\n".join(lines).strip()
            heading, lines = line[3:].strip(), []
        elif heading:
            lines.append(line)
    if heading:
        sections[heading] = "\n".join(lines).strip()
    return sections


def write_units(
    root: Path, source: SourceInfo, units: dict[str, list[Record]]
) -> tuple[Stats, Stats]:
    """自治体ごとに raw/ と seido/ を置き換え、(raw の増減, seido の増減) を返す。

    重複の検査と書き出す内容の組み立てを全自治体分済ませてから書く。途中で失敗して
    一部の自治体だけ書き換わった状態を作らないため。
    """
    planned = []
    for lg_code, records in sorted(units.items()):
        for r in records:
            check_publishable(r, source)
        ids = [r.record_id for r in records]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            raise ValueError(f"{source.name} {lg_code}: record_id が重複 {sorted(dup)[:5]}")
        raw_files = {
            f"{r.record_id}.json": json.dumps(r.raw, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n"
            for r in records
        }
        seido_files = {
            f"{r.record_id}.md": render(r, source) for r in records if r.seido is not None
        }
        planned.append((lg_code, raw_files, seido_files))

    raw_stats, seido_stats = Stats(), Stats()
    for lg_code, raw_files, seido_files in planned:
        _sync(raw_dir(root, source.name, lg_code), raw_files, raw_stats, root)
        _sync(seido_dir(root, source.name, lg_code), seido_files, seido_stats, root)
    return raw_stats, seido_stats


def _sync(directory: Path, files: dict[str, str], stats: Stats, root: Path) -> None:
    existing = {p.name for p in directory.glob("*")} if directory.exists() else set()
    directory.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        path = directory / name
        rel = str(path.relative_to(root))
        if name not in existing:
            stats.added.append(rel)
        elif path.read_text(encoding="utf-8") != content:
            stats.changed.append(rel)
        else:
            continue
        path.write_text(content, encoding="utf-8")
    for name in sorted(existing - files.keys()):
        path = directory / name
        stats.removed.append(str(path.relative_to(root)))
        path.unlink()
    if not any(directory.iterdir()):
        directory.rmdir()
