import urllib.error

import pytest

from builder import webpage
from builder.sources import webindex

SITE = "https://www.city.example.lg.jp"
ROW = {"covers": "lg:131016", "format": "html", "url": f"{SITE}/kosodate/teate/index.html"}


def page(title: str, text: str = "", links: list[tuple[str, str]] = ()) -> webpage.Page:
    return webpage.Page(title=title, text=text or f"{title}の本文", links=list(links))


@pytest.fixture
def site(monkeypatch):
    """URL → Page（例外なら取得失敗）のサイトを差し替える。robots.txt は /secret/ を禁止。"""

    def setup(pages: dict):
        def fetch(url):
            if isinstance(pages[url], Exception):
                raise pages[url]
            return pages[url]

        monkeypatch.setattr(webindex.webpage, "fetch", fetch)
        monkeypatch.setattr(
            webindex.http, "get", lambda url, params=None: b"User-agent: *\nDisallow: /secret/\n"
        )
        webindex.robots.cache_clear()

    return setup


def gone(url):
    return urllib.error.HTTPError(url, 404, "Not Found", {}, None)


def test_collects_program_pages_and_skips_menus(site):
    site(
        {
            ROW["url"]: page(
                "子育ての手当",
                links=[
                    (f"{SITE}/a0020/kosodate/jidouteate.html", "児童手当"),
                    (f"{SITE}/kosodate/teate/iryo/index.html", "医療費の助成"),  # 配下の一覧
                    (f"{SITE}/kurashi/index.html", "くらし"),  # サイトのメニュー
                    (f"{SITE}/kosodate/teate/form.pdf", "申請書"),
                    (f"{SITE}/cgi-bin/inquiry.php", "問い合わせ"),
                    (f"{SITE}/secret/x.html", "robots で禁止"),
                    ("https://other.example.jp/x.html", "外部サイト"),
                    (f"{SITE}/kosodate/teate/old.html", "リンク切れ"),
                ],
            ),
            f"{SITE}/kosodate/teate/iryo/index.html": page(
                "医療費の助成", links=[(f"{SITE}/kosodate/teate/iryo/kodomo.html", "子ども医療費")]
            ),
            f"{SITE}/a0020/kosodate/jidouteate.html": page("児童手当"),
            f"{SITE}/kosodate/teate/iryo/kodomo.html": page("子ども医療費助成"),
            f"{SITE}/kosodate/teate/old.html": gone(f"{SITE}/kosodate/teate/old.html"),
        }
    )
    records = webindex.fetch(ROW).units["131016"]
    assert sorted(r.raw["title"] for r in records) == ["児童手当", "子ども医療費助成"]
    r = next(r for r in records if r.raw["title"] == "児童手当")
    assert set(r.raw) == {"url", "title", "content_sha256", "content_length"}
    assert r.source_text == "児童手当の本文" and r.seido.sections == {}


def test_plain_index_page_does_not_follow_sub_listings(site):
    """一覧ページが普通のページ（台東区 /benri/teate-josei.html）なら、配下の一覧を辿らない。"""
    row = {**ROW, "url": f"{SITE}/benri/teate-josei.html"}
    site(
        {
            row["url"]: page(
                "手当・助成",
                links=[
                    (f"{SITE}/benri/faq/index.html", "よくある質問"),
                    (f"{SITE}/kosodate/jidouteate.html", "児童手当"),
                ],
            ),
            f"{SITE}/kosodate/jidouteate.html": page("児童手当"),
        }
    )
    assert [r.raw["title"] for r in webindex.fetch(row).units["131016"]] == ["児童手当"]


def test_other_errors_fail_the_source(site):
    site(
        {
            ROW["url"]: page("一覧", links=[(f"{SITE}/kosodate/jidouteate.html", "児童手当")]),
            f"{SITE}/kosodate/jidouteate.html": OSError("timeout"),
        }
    )
    with pytest.raises(OSError):
        webindex.fetch(ROW)


def test_record_id_is_stable_and_readable():
    a = webindex.record_id(f"{SITE}/kosodate/jidouteate.html")
    assert a.startswith("jidouteate-") and a == webindex.record_id(
        f"{SITE}/kosodate/jidouteate.html"
    )
    assert a != webindex.record_id(f"{SITE}/other/jidouteate.html")


def test_query_pages_get_distinct_ids():
    a = webindex.record_id(f"{SITE}/detail.php?id=1")
    b = webindex.record_id(f"{SITE}/detail.php?id=2")
    assert a != b and a.startswith("detail-")


def test_index_disallowed_by_robots_fails(site):
    site({})
    with pytest.raises(PermissionError):
        webindex.fetch({**ROW, "url": f"{SITE}/secret/index.html"})


def test_gone_sub_listing_is_skipped(site):
    site(
        {
            ROW["url"]: page(
                "一覧",
                links=[
                    (f"{SITE}/kosodate/teate/old/index.html", "消えた下位の一覧"),
                    (f"{SITE}/kosodate/jidouteate.html", "児童手当"),
                ],
            ),
            f"{SITE}/kosodate/teate/old/index.html": gone(f"{SITE}/kosodate/teate/old/index.html"),
            f"{SITE}/kosodate/jidouteate.html": page("児童手当"),
        }
    )
    assert [r.raw["title"] for r in webindex.fetch(ROW).units["131016"]] == ["児童手当"]


def test_sub_listing_without_program_links_is_a_program_page(site):
    """/ で終わる制度ページ（八丈町の WordPress）は、リンクが無ければ制度ページとして扱う。"""
    row = {**ROW, "url": f"{SITE}/kosodate/josei-teate/"}
    site(
        {
            row["url"]: page(
                "助成・手当",
                links=[
                    (f"{SITE}/kosodate/josei-teate/jidoteate/", "児童手当のご案内"),
                    (f"{SITE}/kosodate/", "妊娠・出産・子育て"),  # 配下にない分類
                ],
            ),
            f"{SITE}/kosodate/josei-teate/jidoteate/": page(
                "児童手当のご案内", links=[(f"{SITE}/kosodate/", "妊娠・出産・子育て")]
            ),
        }
    )
    assert [r.raw["title"] for r in webindex.fetch(row).units["131016"]] == ["児童手当のご案内"]


def test_single_page_source_is_one_program_page(site):
    """一覧の無い村は、制度ページそのものを 1 件として取り込み、リンクは辿らない。"""
    row = {**ROW, "url": f"{SITE}/life/welfare.html", "format": "html-page"}
    site(
        {
            row["url"]: page(
                "福祉", "乳幼児医療助成と補聴器購入助成", [(f"{SITE}/life/other.html", "別ページ")]
            )
        }
    )
    records = webindex.fetch(row).units["131016"]
    assert [(r.raw["url"], r.raw["title"]) for r in records] == [(row["url"], "福祉")]
    assert records[0].source_text == "乳幼児医療助成と補聴器購入助成"


def test_single_page_without_heading_uses_source_name(site):
    row = {**ROW, "url": f"{SITE}/life/welfare.html", "format": "html-page", "name": "福祉"}
    site({row["url"]: page("", "乳幼児医療助成")})
    assert [r.raw["title"] for r in webindex.fetch(row).units["131016"]] == ["福祉"]


def test_pdf_source_is_one_program_page_named_by_source(site, monkeypatch):
    """制度の説明が PDF にしか無いときは、PDF の文字を本文として 1 件にする。"""
    row = {**ROW, "url": f"{SITE}/data/hojo/gaiyou.pdf", "format": "pdf", "name": "起業支援"}
    site({})
    monkeypatch.setattr(webindex.webpage, "pdf_text", lambda data: "起業する方に上限300万円")
    records = webindex.fetch(row).units["131016"]
    assert [(r.raw["url"], r.raw["title"]) for r in records] == [(row["url"], "起業支援")]
    assert records[0].source_text == "起業する方に上限300万円"


def test_same_page_linked_with_http_and_https_is_one_record(site):
    links = [
        (f"{SITE}/kosodate/teate/a.html", "児童手当"),
        (f"{SITE.replace('https', 'http')}/kosodate/teate/a.html", "児童手当"),
    ]
    site({ROW["url"]: page("手当", links=links), links[0][0]: page("児童手当")})
    assert [r.raw["title"] for r in webindex.fetch(ROW).units["131016"]] == ["児童手当"]
