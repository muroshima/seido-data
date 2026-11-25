from builder import webpage

HTML = """
<ul>
  <li><a href="../../../_res/p/20260801_01.csv">公共施設一覧 （CSV 28.4KB）</a></li>
  <li><a href="../../../_res/p/20260801_22.csv">支援制度（給付金）情報 （CSV 55.0KB）</a></li>
  <li><a href="/docs/shien.pdf">支援制度の案内（PDF）</a></li>
</ul>
"""
PAGE = "https://www.city.example.lg.jp/municipal/outline/opendata/1019098.html"


def test_resources_follow_link_text(monkeypatch):
    monkeypatch.setattr(webpage.http, "get", lambda url, params=None: HTML.encode())
    assert webpage.resources(PAGE, "支援制度") == [
        {
            "format": "CSV",
            "url": "https://www.city.example.lg.jp/_res/p/20260801_22.csv",
            "name": "支援制度（給付金）情報 （CSV 55.0KB）",
        }
    ]


def test_scope_ends_at_main_even_with_omitted_end_tags():
    """<li> の閉じタグが省略されていても、</main> のあとは拾わない。"""
    html = (
        "<body><nav><a href='/menu'>メニュー</a></nav>"
        "<main><h1>手当</h1><ul><li><a href='/a.html'>児童手当</a><li>医療費助成</ul></main>"
        "<aside><a href='/x.html'>関係ないリンク</a>外の文字</aside></body>"
    )
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.title == "手当"
    assert "医療費助成" in page.text and "外の文字" not in page.text
    assert page.links == [("https://www.city.example.lg.jp/a.html", "児童手当")]


def test_skip_tags_inside_main_are_ignored():
    html = "<main><nav><a href='/p.html'>パンくず</a></nav><p>本文</p><script>x=1</script></main>"
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.text == "本文" and page.links == []


def test_content_id_excludes_site_menu_outside_it():
    """<main> が無いサイト（新宿区）は、本文の id の中だけを読み、共通メニューを拾わない。"""
    html = (
        "<body><div id='gDef'><ul><li><a href='/kurashi/'>くらし</a></ul></div>"
        "<div id='primary'><h1>手当</h1><a href='/a.html'>児童手当</a></div>"
        "<div id='secondary'><a href='/gomi/'>ごみ・資源</a></div></body>"
    )
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.links == [("https://www.city.example.lg.jp/a.html", "児童手当")]


def test_empty_region_falls_back_to_next_candidate():
    """id が中身の無い目印の要素に付いていたら、次の候補（最後は <body>）を読む。"""
    html = "<body><a id='content'></a><div class='list'><a href='/a.html'>児童手当</a></div></body>"
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.links == [("https://www.city.example.lg.jp/a.html", "児童手当")]


def test_content_class_excludes_site_menu_outside_it():
    """本文の id も <main> も無いサイト（羽村市）は、本文の class の中だけを読む。"""
    html = (
        "<body><div class='g_navi'><a href='/kurashi/'>くらし</a></div>"
        "<div class='main_naka cat'><a href='/a.html'>児童手当</a></div>"
        "<div class='foot'><a href='/gomi/'>ごみ</a></div></body>"
    )
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.links == [("https://www.city.example.lg.jp/a.html", "児童手当")]


def test_skip_classes_inside_region_are_ignored():
    """本文と同じ要素の中にあるパンくず・関連リンク（練馬区）は読まない。"""
    html = (
        "<body><div id='wrap'><div class='pankuzu'><a href='/'>トップ</a></div>"
        "<p>児童手当の案内</p><div class='lobgbox losubnavi'><a href='/x.html'>他の分類</a></div>"
        "</div></body>"
    )
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.text == "児童手当の案内"
    assert page.links == []


def test_skip_link_marker_with_content_id_is_not_the_region():
    """本文の id が「ここから本文です」の目印（三鷹市）に付いていたら、本文の class を読む。"""
    html = (
        "<body><p id='contents' class='skip'>ここから本文です</p>"
        "<div class='side'><a href='/x.html'>同じ分類</a></div>"
        "<div class='main'><a href='/a.html'>児童手当</a></div></body>"
    )
    page = webpage.parse(html, "https://www.city.example.lg.jp/")
    assert page.links == [("https://www.city.example.lg.jp/a.html", "児童手当")]


def minimal_pdf(text: str) -> bytes:
    """文字を 1 行だけ持つ PDF（Helvetica・ASCII）。"""
    stream = f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode()
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792]"
        b" /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream",
    ]
    out, offsets = b"%PDF-1.4\n", []
    for i, body in enumerate(objects, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % i + body + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offsets)
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\n" % (len(objects) + 1)
    out += b"startxref\n%d\n%%%%EOF\n" % xref
    return out


def test_pdf_text_reads_text_layer():
    assert webpage.pdf_text(minimal_pdf("Subsidy up to 300000 yen")) == "Subsidy up to 300000 yen"


def test_heading_in_header_inside_main_is_the_title():
    html = (
        "<body><header><h1>サイト名</h1></header><main>"
        "<header><h1>児童手当</h1></header><p>本文</p></main></body>"
    )
    page = webpage.parse(html, "https://example.jp/a.html")
    assert (page.title, page.text) == ("児童手当", "本文")


def test_heading_in_site_header_is_not_the_title_when_region_is_body():
    page = webpage.parse(
        "<body><header><h1>サイト名</h1></header><p>本文</p></body>", "https://example.jp/"
    )
    assert page.title == ""


def test_search_breadcrumb_and_side_menu_inside_region_are_ignored():
    html = (
        '<body><div id="content"><div class="boxKeywordSearch">検索</div>'
        '<div class="boxBreadcrumb">トップ &gt; 手当</div><div id="main"><h1>特別障害者手当</h1>'
        '<p>月額 30,450円</p></div><div id="side">障害のある方のためにの分類一覧</div></div></body>'
    )
    page = webpage.parse(html, "https://www.city.hachioji.tokyo.jp/a.html")
    assert (page.title, page.text) == ("特別障害者手当", "特別障害者手当\n月額 30,450円")


def test_aside_inside_main_is_ignored():
    """日替わりのおすすめ（aside）で本文が毎日変わって見えないようにする。"""
    html = (
        "<body><main><h1>特別児童扶養手当</h1><p>月額の手当</p>"
        '<aside class="page-bottom__item">これにも注目 障害児福祉手当</aside></main></body>'
    )
    assert webpage.parse(html, "https://www.city.machida.tokyo.jp/a.html").text == (
        "特別児童扶養手当\n月額の手当"
    )


def test_contact_aside_is_kept():
    html = (
        "<body><main><h1>手当</h1><p>月額</p>"
        '<aside class="contact" id="contact"><p>障がい福祉課 電話：042-724-2148</p></aside>'
        '<aside class="kiji_aside kakuka"><p>町民課保険年金係</p></aside>'
        '<aside class="feedback-area">役に立ちましたか</aside></main></body>'
    )
    assert webpage.parse(html, "https://example.jp/a.html").text == (
        "手当\n月額\n障がい福祉課 電話：042-724-2148\n町民課保険年金係"
    )


def test_broken_link_is_skipped():
    """全角コロンの電話番号リンク（横瀬町）で URL の解析が止まらないこと。"""
    html = (
        '<main><a href="//tel：０４９４２５０１１０">電話</a><a href="/a.html">児童手当</a></main>'
    )
    assert webpage.parse(html, "https://www.town.example.jp/").links == [
        ("https://www.town.example.jp/a.html", "児童手当")
    ]


def test_decode_reads_shift_jis_page():
    html = '<meta charset="Shift_JIS"><main><p>児童手当</p></main>'.encode("cp932")
    assert "児童手当" in webpage.decode(html)


def test_decode_falls_back_to_shift_jis_when_meta_says_utf8():
    """佐用町: meta は UTF-8 だが、中身は Shift_JIS。"""
    html = '<meta charset="utf-8"><main><p>子育て支援券</p></main>'.encode("cp932")
    assert "子育て支援券" in webpage.decode(html)


def test_decode_keeps_utf8():
    html = '<meta charset="Shift_JIS"><p>手当</p>'.encode()
    assert webpage.decode(html) == '<meta charset="Shift_JIS"><p>手当</p>'


def test_bare_ampersand_in_query_is_not_an_entity():
    """佐用町: `&section_id=` を `§ion_id=` と読まない。本文の `&` もそのまま。"""
    html = '<main><a href="/r.jsp?a=1&section_id=2&region=3">育児</a><p>A&B=1</p></main>'
    page = webpage.parse(html, "https://example.jp/")
    assert page.links == [("https://example.jp/r.jsp?a=1&section_id=2&region=3", "育児")]
    assert "A&B=1" in page.text
