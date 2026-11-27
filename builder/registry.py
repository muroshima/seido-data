"""対応表（registry/）の読み書き・検証・カバー状況の集計。

entities.csv は「制度を持つ団体」の一覧、sources.csv は「その制度をどこから取るか」の一覧。
取り込みを書く前にここを埋め、どの団体がまだ取れていないかを見えるようにする。
"""

import csv
import fnmatch
import io
import re
from collections import Counter
from datetime import date
from pathlib import Path

from . import http

ENTITY_FIELDS = ["id", "kind", "name", "parent", "lg_code", "corporate_number", "website"]
SOURCE_FIELDS = [
    "source_id",
    "name",
    "provider",
    "covers",
    "scope",
    "kind",
    "format",
    "url",
    "license",
    "publish",
    "update",
    "status",
    "checked",
    "note",
]
ENTITY_KINDS = ("国", "都道府県", "市区町村")
SOURCE_KINDS = ("api", "opendata", "web")
# 取込中: 日次で取り込んでいる / 取込予定: 取り込める・実装待ち / 調査中: 中身や条件を確認中
# 要利用申請: 取り込むには申請や契約が要る / 対象外: 調べた結果、支援制度の一覧ではない
STATUSES = ("取込中", "取込予定", "調査中", "要利用申請", "対象外")
USABLE = ("取込中", "取込予定")
# scope は取得元が扱う制度の範囲。全般 = 分野を限定しない形式（網羅しているとは限らない）。
# それ以外は分野・対象を書く（例: 子育て（0-6歳）、事業者向け補助金）
SCOPE_ALL = "全般"
# publish は公開する範囲。本文 = 取得元の文章を raw/ と seido/ に置く（利用規約が二次利用を
# 認めるものだけ）。事実 = 制度名・URL・本文のハッシュと、取り出した制度の情報（対象者・
# 金額・期間など）だけを置く。取得元の文章は置かない
PUBLISH = ("本文", "事実")

LG_CODE = re.compile(r"^\d{6}$")
CORP = re.compile(r"^\d{13}$")
SOURCE_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def lg_check_digit(code5: str) -> str:
    """全国地方公共団体コードの検査数字（6 桁目）。"""
    total = sum(int(d) * w for d, w in zip(code5, (6, 5, 4, 3, 2), strict=True))
    return str((11 - total % 11) % 10)


def corporate_check_digit(base12: str) -> str:
    """法人番号の検査数字（先頭 1 桁）。base12 は残り 12 桁。"""
    digits = [int(d) for d in reversed(base12)]  # 下の桁から P1, P2, ...
    total = sum(d * (1 if i % 2 == 0 else 2) for i, d in enumerate(digits))
    return str(9 - total % 9)


def lg_corporate_number(lg_code: str) -> str:
    """地方公共団体の法人番号は「検査数字 + 000020 + 団体コード」。"""
    base = f"000020{lg_code}"
    return corporate_check_digit(base) + base


def read(path: Path, fields: list[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != fields:
            raise ValueError(f"{path}: 列が {fields} と一致しない: {reader.fieldnames}")
        return list(reader)


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buf.getvalue(), encoding="utf-8")


def load(root: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    reg = root / "registry"
    return read(reg / "entities.csv", ENTITY_FIELDS), read(reg / "sources.csv", SOURCE_FIELDS)


def expand(covers: str, entities: list[dict[str, str]]) -> set[str]:
    """covers（`;` 区切り。`lg:13*` のようなワイルドカード可）を団体 ID の集合にする。"""
    ids = [e["id"] for e in entities]
    found: set[str] = set()
    for pattern in filter(None, (p.strip() for p in covers.split(";"))):
        found |= set(fnmatch.filter(ids, pattern))
    return found


def validate(entities: list[dict[str, str]], sources: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    ids = Counter(e["id"] for e in entities)
    errors += [f"entities: id が重複 {i}" for i, n in ids.items() if n > 1]
    for e in entities:
        where = f"entities {e['id']}"
        if e["kind"] not in ENTITY_KINDS:
            errors.append(f"{where}: kind が {ENTITY_KINDS} のどれでもない")
        if e["parent"] and e["parent"] not in ids:
            errors.append(f"{where}: parent {e['parent']} が entities に無い")
        if e["lg_code"]:
            if (
                not LG_CODE.match(e["lg_code"])
                or lg_check_digit(e["lg_code"][:5]) != e["lg_code"][5]
            ):
                errors.append(f"{where}: lg_code の検査数字が合わない")
            if e["id"] != f"lg:{e['lg_code']}":
                errors.append(f"{where}: 地方公共団体の id は lg:<団体コード>")
        elif e["id"] != f"gov:{e['corporate_number']}":
            errors.append(f"{where}: 国の機関の id は gov:<法人番号>")
        corp = e["corporate_number"]
        if not CORP.match(corp) or corporate_check_digit(corp[1:]) != corp[0]:
            errors.append(f"{where}: corporate_number が 13 桁でないか、検査数字が合わない")
        elif e["lg_code"] and corp != lg_corporate_number(e["lg_code"]):
            errors.append(f"{where}: corporate_number が lg_code から計算した値と違う")
        if e["website"] and not e["website"].startswith("https://"):
            errors.append(f"{where}: website は https://")

    sids = Counter(s["source_id"] for s in sources)
    errors += [f"sources: source_id が重複 {i}" for i, n in sids.items() if n > 1]
    for s in sources:
        where = f"sources {s['source_id']}"
        if not SOURCE_ID.match(s["source_id"]):
            errors.append(f"{where}: source_id は英小文字・数字・ハイフン")
        if s["provider"] not in ids:
            errors.append(f"{where}: provider {s['provider']} が entities に無い")
        patterns = [p.strip() for p in s["covers"].split(";") if p.strip()]
        if not patterns:
            errors.append(f"{where}: covers が空")
        for pattern in patterns:
            if not expand(pattern, entities):
                errors.append(f"{where}: covers の {pattern!r} に当たる団体が無い")
        if s["publish"] not in PUBLISH:
            errors.append(f"{where}: publish が {PUBLISH} のどれでもない")
        elif s["publish"] == "本文" and s["license"].startswith("不明"):
            errors.append(f"{where}: license が不明なのに publish が本文")
        if not s["scope"]:
            errors.append(f"{where}: scope が空（全般、または分野を書く）")
        if s["kind"] not in SOURCE_KINDS:
            errors.append(f"{where}: kind が {SOURCE_KINDS} のどれでもない")
        if s["status"] not in STATUSES:
            errors.append(f"{where}: status が {STATUSES} のどれでもない")
        if not s["url"].startswith("https://"):
            errors.append(f"{where}: url は https://")
        try:
            date.fromisoformat(s["checked"])
        except ValueError:
            errors.append(f"{where}: checked は YYYY-MM-DD")
    return errors


COVERAGE_HEADER = [
    "`uv run seido registry coverage` で生成する。手で編集しない。",
    "",
    "- ○: 取込中・取込予定の取得元があり、制度全般を扱う",
    "- ◐: 取込中・取込予定の取得元はあるが、分野が限られる（子育てだけ、など）",
    "- △: 取得元は見つかっているが、調査中・要利用申請・対象外のみ",
    "- −: 取得元が見つかっていない",
]


# 国の機関をこれ以上扱う取得元は、団体別の表に書かず、まとめて書く（府省をまたぐ取得元）
WIDE = 10


def pref_of(e: dict[str, str]) -> str | None:
    """地方公共団体の都道府県コード 2 桁。国の機関は None。"""
    return e["lg_code"][:2] if e["lg_code"] else None


def coverage(entities: list[dict[str, str]], sources: list[dict[str, str]]) -> dict[str, str]:
    """カバー状況のファイル（registry/ からの相対パス → 中身）。

    COVERAGE.md に全国と都道府県ごとの集計、国の機関、広く扱う取得元を置き、都道府県ごとの
    団体別の表は coverage/<都道府県コード>.md に分ける。広く扱う取得元（複数の都道府県、または
    WIDE 以上の国の機関）は、団体別の表では書かない（多くの行に同じ取得元が並ぶため）。
    """
    by_id = {e["id"]: e for e in entities}
    by_entity: dict[str, list[dict[str, str]]] = {e["id"]: [] for e in entities}
    wide: list[tuple[dict[str, str], set[str]]] = []
    for s in sources:
        ids = expand(s["covers"], entities)
        for i in ids:
            by_entity[i].append(s)
        groups = {pref_of(by_id[i]) for i in ids}
        if len(groups) > 1 or (groups == {None} and len(ids) >= WIDE):
            wide.append((s, ids))
    wide_ids = {s["source_id"] for s, _ in wide}

    def mark(e: dict[str, str]) -> str:
        usable = [s for s in by_entity[e["id"]] if s["status"] in USABLE]
        if any(s["scope"] == SCOPE_ALL for s in usable):
            return "○"
        if usable:
            return "◐"
        return "△" if by_entity[e["id"]] else "−"

    def counts(group: list[dict[str, str]]) -> str:
        c = Counter(mark(e) for e in group)
        return f"{len(group)} | {c['○']} | {c['◐']} | {c['△']} | {c['−']}"

    def table(group: list[dict[str, str]]) -> list[str]:
        lines = ["| 団体 | 区分 | 状況 | 取得元 |", "|---|---|---|---|"]
        for e in group:
            names = ", ".join(
                f"`{s['source_id']}`（{s['scope']}・{s['status']}）"
                for s in by_entity[e["id"]]
                if s["source_id"] not in wide_ids
            )
            lines.append(f"| {e['name']} | {e['kind']} | {mark(e)} | {names} |")
        return lines

    prefs: dict[str, list[dict[str, str]]] = {}
    for e in entities:
        if (p := pref_of(e)) is not None:
            prefs.setdefault(p, []).append(e)
    lines = ["# カバー状況", "", *COVERAGE_HEADER, "", "| 区分 | 団体数 | ○ | ◐ | △ | − |"]
    lines.append("|---|---:|---:|---:|---:|---:|")
    for kind in ENTITY_KINDS:
        group = [e for e in entities if e["kind"] == kind]
        if group:
            lines.append(f"| {kind} | {counts(group)} |")
    lines += [
        "",
        "## 都道府県別",
        "",
        "都道府県と県内の市区町村を合わせた数。団体別の表は都道府県名のリンク先にある。",
        "",
        "| 都道府県 | 団体数 | ○ | ◐ | △ | − |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    files: dict[str, str] = {}
    for p, group in sorted(prefs.items()):
        name = next((e["name"] for e in group if e["kind"] == "都道府県"), p)
        lines.append(f"| [{name}](coverage/{p}.md) | {counts(group)} |")
        files[f"coverage/{p}.md"] = (
            "\n".join(
                [
                    f"# カバー状況（{name}）",
                    "",
                    *COVERAGE_HEADER,
                    "",
                    "複数の都道府県や多くの団体を扱う取得元は、"
                    "[COVERAGE.md](../COVERAGE.md#広く扱う取得元) にまとめて書く。",
                    "",
                    *table(group),
                ]
            )
            + "\n"
        )
    gov = [e for e in entities if pref_of(e) is None]
    if gov:
        lines += ["", "## 国の機関", "", *table(gov)]
    lines += [
        "",
        "## 広く扱う取得元",
        "",
        f"複数の都道府県、または {WIDE} 以上の国の機関を扱う取得元。団体別の表には書かない。",
        "",
        "| 取得元 | 範囲 | 状況 | 団体数 |",
        "|---|---|---|---:|",
    ]
    for s, ids in wide:
        lines.append(
            f"| `{s['source_id']}` {s['name']} | {s['scope']} | {s['status']} | {len(ids)} |"
        )
    files["COVERAGE.md"] = "\n".join(lines) + "\n"
    return files


# --- entities.csv の生成 ----------------------------------------------------------------

SOUMU_PAGE = "https://www.soumu.go.jp/denshijiti/code.html"
WIKIDATA = "https://query.wikidata.org/sparql"
# 支援制度を持つ国の機関。外局は親の府省を parent に置く
GOV_AGENCIES: dict[str, str | None] = {
    "内閣府": None,
    "デジタル庁": None,
    "復興庁": None,
    "総務省": None,
    "法務省": None,
    "外務省": None,
    "財務省": None,
    "文部科学省": None,
    "厚生労働省": None,
    "農林水産省": None,
    "経済産業省": None,
    "国土交通省": None,
    "環境省": None,
    "防衛省": None,
    "こども家庭庁": "内閣府",
    "金融庁": "内閣府",
    "消費者庁": "内閣府",
    "国税庁": "財務省",
    "文化庁": "文部科学省",
    "スポーツ庁": "文部科学省",
    "林野庁": "農林水産省",
    "水産庁": "農林水産省",
    "資源エネルギー庁": "経済産業省",
    "特許庁": "経済産業省",
    "中小企業庁": "経済産業省",
    "観光庁": "国土交通省",
}


# 団体コードはあるが行政を行っていない北方領土の 6 村
# （色丹村・泊村・留夜別村・留別村・紗那村・蘂取村）
NO_ADMINISTRATION = {"016951", "016969", "016977", "016985", "016993", "017001"}


def generate_entities(prefectures: list[str], with_gov: bool) -> list[dict[str, str]]:
    """総務省の団体コード一覧と Wikidata から entities の行を作る（ネットワークを使う）。"""
    rows: list[dict[str, str]] = []
    if with_gov:
        rows += gov_entities()
    for pref in prefectures:
        rows += lg_entities(pref)
    return rows


def gov_entities() -> list[dict[str, str]]:
    labels = " ".join(f'"{n}"@ja' for n in GOV_AGENCIES)
    found = sparql(
        f"SELECT ?label ?corp ?site WHERE {{ VALUES ?label {{ {labels} }} "
        "?item rdfs:label ?label ; wdt:P3225 ?corp . OPTIONAL { ?item wdt:P856 ?site } }"
    )
    info: dict[str, tuple[str, list[str]]] = {}
    for b in found:
        corp, sites = info.get(b["label"], (b["corp"], []))
        info[b["label"]] = (corp, sites + ([b["site"]] if b.get("site") else []))
    missing = set(GOV_AGENCIES) - info.keys()
    if missing:
        raise RuntimeError(f"Wikidata に法人番号が無い: {sorted(missing)}")
    rows = []
    for name, parent in GOV_AGENCIES.items():
        corp, sites = info[name]
        rows.append(
            {
                "id": f"gov:{corp}",
                "kind": "国",
                "name": name,
                "parent": f"gov:{info[parent][0]}" if parent else "",
                "lg_code": "",
                "corporate_number": corp,
                "website": pick_website(sites),
            }
        )
    return rows


def lg_entities(pref: str) -> list[dict[str, str]]:
    import openpyxl

    page = http.get(SOUMU_PAGE).decode("cp932", errors="replace")
    link = re.search(r'href="(/main_content/\d+\.xlsx)"', page)
    if not link:
        raise RuntimeError("総務省のページに団体コード一覧の xlsx が見つからない")
    wb = openpyxl.load_workbook(
        io.BytesIO(http.get("https://www.soumu.go.jp" + link.group(1))), read_only=True
    )
    codes = [
        (str(r[0]), r[1], r[2])
        for r in wb.worksheets[0].iter_rows(min_row=2, values_only=True)
        if r[0] and str(r[0]).startswith(pref) and str(r[0]) not in NO_ADMINISTRATION
    ]
    sites: dict[str, list[str]] = {}
    for b in sparql(
        "SELECT ?code ?site WHERE { ?item wdt:P429 ?code ; wdt:P856 ?site . "
        f'FILTER(STRSTARTS(?code, "{pref}")) }}'
    ):
        sites.setdefault(b["code"], []).append(b["site"])
    pref_id = f"lg:{pref}000{lg_check_digit(pref + '000')}"  # 東京都 130001・神奈川県 140007
    rows = []
    for code, pref_name, city in codes:
        rows.append(
            {
                "id": f"lg:{code}",
                "kind": "市区町村" if city else "都道府県",
                "name": city or pref_name,
                "parent": pref_id if city else "",
                "lg_code": code,
                "corporate_number": lg_corporate_number(code),
                "website": pick_website(sites.get(code, [])),
            }
        )
    return rows


def pick_website(urls: list[str]) -> str:
    """英語版を除き、https の最短 URL を選ぶ。"""
    ja = [u for u in urls if not re.search(r"english|/en(/|$)|/e/|://en\.", u)] or urls
    ja = [u.replace("http://", "https://", 1) for u in ja]
    return min(ja, key=len) if ja else ""


def sparql(query: str) -> list[dict[str, str]]:
    res = http.get_json(WIKIDATA, {"query": query, "format": "json"})
    return [{k: v["value"] for k, v in b.items()} for b in res["results"]["bindings"]]


def merge_entities(
    existing: list[dict[str, str]], generated: list[dict[str, str]]
) -> list[dict[str, str]]:
    """既存の行は手で直した値を残し、空欄だけ埋める。新しい団体は追加する。"""
    by_id = {e["id"]: dict(e) for e in existing}
    for g in generated:
        if g["id"] in by_id:
            row = by_id[g["id"]]
            for k, v in g.items():
                if not row.get(k):
                    row[k] = v
        else:
            by_id[g["id"]] = g
    order = {k: i for i, k in enumerate(ENTITY_KINDS)}
    return sorted(by_id.values(), key=lambda e: (order[e["kind"]], e["lg_code"], e["id"]))
