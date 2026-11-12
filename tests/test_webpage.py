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
