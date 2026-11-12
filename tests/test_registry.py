from pathlib import Path

import pytest

from builder import registry as r

ROOT = Path(__file__).resolve().parents[1]


def ent(id_, kind="市区町村", parent="", lg="", corp="", name="x"):
    return dict(
        id=id_, kind=kind, name=name, parent=parent, lg_code=lg, corporate_number=corp, website=""
    )


def src(sid="s", covers="lg:131016", status="取込予定", scope="全般", provider="lg:131016"):
    return dict(
        source_id=sid,
        name="n",
        provider=provider,
        covers=covers,
        scope=scope,
        kind="opendata",
        format="csv",
        url="https://example.jp/",
        license="CC BY",
        publish="本文",
        update="随時",
        status=status,
        checked="2026-11-12",
        note="",
    )


TOKYO = ent("lg:130001", "都道府県", lg="130001", corp="8000020130001")
CHIYODA = ent("lg:131016", parent="lg:130001", lg="131016", corp="8000020131016")
CHUO = ent("lg:131024", parent="lg:130001", lg="131024", corp="8000020131024")


@pytest.mark.parametrize("code", ["130001", "131016", "140007", "010006", "011002"])
def test_lg_check_digit(code):
    assert r.lg_check_digit(code[:5]) == code[5]


@pytest.mark.parametrize("corp", ["2000012010019", "8000012010038", "1000012090004"])
def test_corporate_check_digit(corp):
    """国の機関の法人番号（Wikidata の値）で検査数字の計算を確かめる。"""
    assert r.corporate_check_digit(corp[1:]) == corp[0]


def test_lg_corporate_number():
    assert r.lg_corporate_number("130001") == "8000020130001"
    assert r.lg_corporate_number("131024") == "8000020131024"


def test_expand_wildcard():
    assert r.expand("lg:13*", [TOKYO, CHIYODA, CHUO]) == {"lg:130001", "lg:131016", "lg:131024"}
    assert r.expand("lg:131016;lg:131024", [TOKYO, CHIYODA, CHUO]) == {"lg:131016", "lg:131024"}


def test_valid_registry_has_no_errors():
    assert r.validate([TOKYO, CHIYODA], [src()]) == []


@pytest.mark.parametrize(
    "entities, sources, expected",
    [
        ([TOKYO, CHIYODA, CHIYODA], [], "id が重複"),
        ([CHIYODA], [], "parent lg:130001 が entities に無い"),
        ([TOKYO, {**CHIYODA, "lg_code": "131017", "id": "lg:131017"}], [], "lg_code の検査数字"),
        ([TOKYO, {**CHIYODA, "corporate_number": "9000020131016"}], [], "corporate_number"),
        ([TOKYO, CHIYODA], [src(covers="lg:14*")], "当たる団体が無い"),
        ([TOKYO, CHIYODA], [src(covers="lg:131016;lg:131025")], "'lg:131025' に当たる団体が無い"),
        ([TOKYO, {**CHIYODA, "corporate_number": ""}], [], "13 桁でない"),
        ([TOKYO, {**CHIYODA, "corporate_number": "8000020130001"}], [], "lg_code から計算した値"),
        ([ent("gov:", "国")], [], "13 桁でない"),
        ([TOKYO, CHIYODA], [src(status="済")], "status"),
        ([TOKYO, CHIYODA], [src(scope="")], "scope が空"),
        ([TOKYO, CHIYODA], [src(provider="lg:999999")], "provider"),
    ],
)
def test_validate_catches(entities, sources, expected):
    assert any(expected in e for e in r.validate(entities, sources))


def test_coverage_marks():
    sources = [
        src("all", covers="lg:131016"),
        src("kids", covers="lg:131024", scope="子育て"),
        src("todo", covers="lg:130001", status="調査中", provider="lg:130001"),
    ]
    rows = {
        line.split(" | ")[0].lstrip("| "): line.split(" | ")[2]
        for line in r.coverage(
            [
                {**TOKYO, "name": "東京都"},
                {**CHIYODA, "name": "千代田区"},
                {**CHUO, "name": "中央区"},
            ],
            sources,
        ).splitlines()
        if line.startswith("| ") and "区分" not in line and line.count("|") == 5
    }
    assert rows == {"東京都": "△", "千代田区": "○", "中央区": "◐"}


def test_merge_keeps_manual_values_and_fills_blanks():
    existing = [{**CHIYODA, "website": "https://manual.example/", "name": ""}]
    generated = [
        {**CHIYODA, "website": "https://wikidata.example/", "name": "千代田区"},
        TOKYO,
    ]
    merged = {e["id"]: e for e in r.merge_entities(existing, generated)}
    assert merged["lg:131016"]["website"] == "https://manual.example/"
    assert merged["lg:131016"]["name"] == "千代田区"
    assert "lg:130001" in merged


def test_pick_website_prefers_japanese_https():
    urls = ["https://www.mof.go.jp/english/", "http://www.mof.go.jp/"]
    assert r.pick_website(urls) == "https://www.mof.go.jp/"


def test_repository_registry_is_valid_and_coverage_is_fresh():
    """コミットされている registry/ が検証を通り、COVERAGE.md が最新であること。"""
    entities, sources = r.load(ROOT)
    assert r.validate(entities, sources) == []
    expected = r.coverage(entities, sources)
    actual = (ROOT / "registry" / "COVERAGE.md").read_text(encoding="utf-8")
    assert actual == expected, "uv run seido registry coverage で作り直す"


def test_publish_must_be_known_and_full_text_needs_license():
    assert any("publish" in e for e in r.validate([TOKYO, CHIYODA], [{**src(), "publish": "全部"}]))
    unknown = {**src(), "publish": "本文", "license": "不明"}
    assert any("license が不明" in e for e in r.validate([TOKYO, CHIYODA], [unknown]))
