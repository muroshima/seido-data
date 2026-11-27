"""seido discover: 公式サイトから制度の一覧ページの候補を探す。"""

from datetime import date

from builder import discover

SITE = "https://www.town.example.lg.jp/"
TOP = [
    (SITE + "kurashi/index.html", "くらし"),
    (SITE + "kosodate/index.html", "子育て・教育"),
    (SITE + "news/1.html", "新着情報"),
    ("https://other.example.jp/josei.html", "助成金の一覧"),  # 別のホスト
]
PAGES = {
    SITE + "kurashi/index.html": [
        (SITE + "kurashi/josei/index.html", "助成・補助・手当の一覧"),
        (SITE + "kurashi/form.pdf", "補助金の申請書"),
        (SITE + "kurashi/kekka.html", "補助金の交付決定"),
    ],
    SITE + "kosodate/index.html": [(SITE + "kosodate/teate.html", "子育ての手当")],
}


def test_find_collects_listing_links_from_top_and_categories(monkeypatch):
    monkeypatch.setattr(discover, "allowed", lambda url: True)
    monkeypatch.setattr(discover, "page_links", lambda url: TOP if url == SITE else PAGES[url])
    found = discover.find(SITE)
    # 一覧ページの候補があれば、個別のページ（kosodate/teate.html）は候補にしない
    assert [(c.url, c.text, c.format) for c in found] == [
        (SITE + "kurashi/josei/index.html", "助成・補助・手当の一覧", "html")
    ]


def test_choose_drops_sub_listings_and_falls_back_to_pages():
    found = {
        SITE + "josei/index.html": "助成の一覧",
        SITE + "josei/kodomo/index.html": "子どもの手当",
    }
    assert [c.url for c in discover.choose(found)] == [SITE + "josei/index.html"]
    pages = discover.choose({SITE + "a.html": "児童手当", SITE + "b.html": "医療費の助成"})
    assert [(c.url, c.format) for c in pages] == [
        (SITE + "b.html", "html-page"),
        (SITE + "a.html", "html-page"),
    ]


def test_targets_skip_entities_with_own_sources():
    entities = [
        {"id": "lg:011002", "lg_code": "011002", "website": SITE, "kind": "市区町村"},
        {"id": "lg:012025", "lg_code": "012025", "website": SITE, "kind": "市区町村"},
        {"id": "lg:131016", "lg_code": "131016", "website": SITE, "kind": "市区町村"},
    ]
    sources = [
        {"source_id": "own", "covers": "lg:011002", "status": "取込中"},
        {"source_id": "nation", "covers": "lg:*", "status": "取込中"},  # 全国のものは数えない
    ]
    assert [e["id"] for e in discover.targets(entities, sources, ["01"])] == ["lg:012025"]


def test_rows_for_makes_unique_ids_and_guesses_scope():
    entity = {
        "id": "lg:303810",
        "lg_code": "303810",
        "name": "美浜町",
        "website": "https://www.town.mihama.wakayama.jp/",
    }
    taken = {"mihama-d1"}  # 福井の美浜町
    rows = discover.rows_for(
        entity,
        [discover.Candidate("https://www.town.mihama.wakayama.jp/a.html", "子育ての手当")],
        taken,
        date(2026, 11, 27),
    )
    assert rows[0]["source_id"] == "mihama-30-d1"
    assert rows[0]["scope"] == "子育て"
    assert (rows[0]["status"], rows[0]["license"], rows[0]["publish"]) == (
        "取込予定",
        "不明",
        "事実",
    )


def test_slug():
    assert discover.slug("https://www.town.sumita.iwate.jp/") == "sumita"
    assert discover.slug("https://www.odaitown.jp/") == "odaitown"
    assert discover.slug("https://betsukai.jp/") == "betsukai"


def test_rows_for_skips_ids_already_taken():
    entity = {
        "id": "lg:012025",
        "lg_code": "012025",
        "name": "函館市",
        "website": "https://www.city.hakodate.hokkaido.jp/",
    }
    taken = {"hakodate-x", "hakodate-01-d1"}
    rows = discover.rows_for(
        entity,
        [discover.Candidate("https://www.city.hakodate.hokkaido.jp/a/", "手当")],
        taken,
        date(2026, 11, 28),
    )
    assert rows[0]["source_id"] == "hakodate-01-d2"
