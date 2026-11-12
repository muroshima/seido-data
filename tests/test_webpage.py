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
