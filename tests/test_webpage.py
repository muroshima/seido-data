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
