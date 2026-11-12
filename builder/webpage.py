"""自治体の Web ページから、リンクと本文を取り出す。

- 掲載ページのリンクから、日付入りの名前で置かれた CSV・XLSX を見つける（福生市など）
- 支援制度の一覧ページから制度ページへのリンクを集め、制度ページの本文を取り出す

本文は `<main>` の中だけを使う。無ければ、よくある本文領域の id、それも無ければ `<body>` から
header・nav・footer を除いた部分を使う。サイト共通のメニューやパンくずを本文に混ぜないため。
"""

import re
import urllib.parse
from dataclasses import dataclass, field
from html.parser import HTMLParser

from . import http

FILE_EXT = re.compile(r"\.(csv|xlsx)$", re.IGNORECASE)
# 自治体サイトの CMS でよく使われる本文領域の id
CONTENT_IDS = ("tmp_contents", "contents", "content", "main", "main_body", "mainContents")
SKIP_TAGS = {"script", "style", "noscript", "template", "nav", "header", "footer"}
VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "source",
    "wbr",
}
BLOCK_TAGS = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "dt", "dd", "table", "br"}


@dataclass
class Page:
    title: str = ""
    text: str = ""
    links: list[tuple[str, str]] = field(default_factory=list)  # (絶対 URL, リンク文)


class _Collector(HTMLParser):
    """1 つの領域（scope）の中の文字とリンクを集める。scope は (タグ, id) の判定関数。"""

    def __init__(self, in_scope) -> None:
        super().__init__(convert_charrefs=True)
        self.in_scope = in_scope
        self.depth = 0  # scope の中なら 1 以上
        self.skip = 0
        self.text: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.h1: list[str] = []
        self._href: str | None = None
        self._anchor: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.depth == 0:
            if self.in_scope(tag, a.get("id") or ""):
                self.depth = 1
            return
        if tag in VOID_TAGS:
            if tag == "br":
                self.text.append("\n")
            return
        self.depth += 1
        if tag in SKIP_TAGS or self.skip:
            self.skip += 1
            return
        if tag in BLOCK_TAGS:
            self.text.append("\n")
        if tag == "a":
            self._href, self._anchor = a.get("href"), []
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag):
        if self.depth == 0 or tag in VOID_TAGS:
            return
        self.depth -= 1
        if self.skip:
            self.skip -= 1
            return
        if tag == "a" and self._href is not None:
            self.links.append((self._href, squash("".join(self._anchor))))
            self._href = None
        if tag == "h1":
            self._in_h1 = False
        if tag in BLOCK_TAGS:
            self.text.append("\n")

    def handle_data(self, data):
        if self.depth == 0 or self.skip:
            return
        self.text.append(data)
        if self._href is not None:
            self._anchor.append(data)
        if self._in_h1:
            self.h1.append(data)


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse(html: str, base_url: str) -> Page:
    """本文領域の見出し・文字・リンクを取り出す。"""
    lowered = html.lower()
    if "<main" in lowered:
        collector = _Collector(lambda tag, _id: tag == "main")
    else:
        ids = [i for i in CONTENT_IDS if re.search(rf'id=["\']{i}["\']', html)]
        if ids:
            collector = _Collector(lambda _tag, id_, want=ids[0]: id_ == want)
        else:
            collector = _Collector(lambda tag, _id: tag == "body")
    collector.feed(html)
    lines = [squash(line) for line in "".join(collector.text).split("\n")]
    return Page(
        title=squash("".join(collector.h1)),
        text="\n".join(line for line in lines if line),
        links=[
            (urllib.parse.urldefrag(urllib.parse.urljoin(base_url, href))[0], text)
            for href, text in collector.links
            if href and not href.startswith(("mailto:", "tel:", "javascript:", "#"))
        ],
    )


def fetch(url: str) -> Page:
    return parse(http.get(url).decode("utf-8", errors="replace"), url)


def links(html: str, base_url: str) -> list[tuple[str, str]]:
    """ページ全体のリンク（絶対 URL, リンク文）。"""
    collector = _Collector(lambda tag, _id: tag == "html")
    collector.depth = 1  # html タグが省略されていても全体を見る
    collector.feed(html)
    return [(urllib.parse.urljoin(base_url, href), text) for href, text in collector.links if href]


def resources(page_url: str, link_text: str) -> list[dict]:
    """リンク文に link_text を含む CSV・XLSX（CKAN の resources と同じ形）。"""
    html = http.get(page_url).decode("utf-8", errors="replace")
    found = []
    for url, text in links(html, page_url):
        m = FILE_EXT.search(urllib.parse.urlsplit(url).path)
        if m and link_text in text:
            found.append({"format": m.group(1).upper(), "url": url, "name": text})
    return found
