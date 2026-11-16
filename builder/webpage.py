"""自治体の Web ページから、リンクと本文を取り出す。

- 掲載ページのリンクから、日付入りの名前で置かれた CSV・XLSX を見つける（福生市など）
- 支援制度の一覧ページから制度ページへのリンクを集め、制度ページの本文を取り出す

本文は `<main>` の中だけを使う。無ければ、よくある本文領域の id、次に class、それも無ければ
`<body>` から header・nav・footer を除いた部分を使う。サイト共通のメニューやパンくずを本文に混ぜないため。
選んだ領域に文字が無ければ（id が中身の無い目印の要素に付いているなど）、次の候補に移る。
"""

import re
import urllib.parse
from dataclasses import dataclass, field
from html.parser import HTMLParser

from . import http

FILE_EXT = re.compile(r"\.(csv|xlsx)$", re.IGNORECASE)
# 自治体サイトの CMS でよく使われる本文領域の id
CONTENT_IDS = (
    "tmp_contents",
    "contents",
    "content",
    "main",
    "main_body",
    "mainContents",
    "primary",  # 新宿区
    "main_outline",  # あきる野市・日の出町・檜原村
    "mol_contents",  # 羽村市の制度ページ
    "contentsWrap",  # 八丈町
    "wrap",  # 練馬区（本文への目印 CONT は中身の無い要素）
)
# id が無く class でしか見分けられない本文領域
CONTENT_CLASSES = (
    "main_naka",  # 羽村市の一覧ページ
    "main_area",  # 小平市
)
# 本文領域の中にあるパンくず・関連リンク・フッター（練馬区は本文と同じ要素の中に置く）
SKIP_CLASSES = {"pankuzu", "lobgbox", "footbg"}
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
    """1 つの領域（scope）の中の文字とリンクを集める。scope は (タグ, id, class の集合) の判定関数。

    閉じタグが省略された HTML（`<li>` など）でも領域の終わりを取り違えないよう、開いている
    タグをスタックで持ち、閉じタグが来たら対応する開きタグまでまとめて閉じる。
    """

    def __init__(self, in_scope, whole: bool = False) -> None:
        super().__init__(convert_charrefs=True)
        self.in_scope = in_scope
        self.whole = whole  # 文書全体を見る（領域を探さない）
        self.active = whole
        self.done = False
        self.stack: list[str] = []
        self.skip_at: int | None = None  # SKIP_TAGS の要素を開いたときのスタックの深さ
        self.text: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.h1: list[str] = []
        self._href: str | None = None
        self._anchor: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        if not self.active:
            if not self.done and self.in_scope(tag, a.get("id") or "", classes):
                self.active, self.stack = True, [tag]
            return
        if tag in VOID_TAGS:
            if tag == "br" and self.skip_at is None:
                self.text.append("\n")
            return
        self.stack.append(tag)
        if self.skip_at is None and (tag in SKIP_TAGS or classes & SKIP_CLASSES):
            self.skip_at = len(self.stack)
        if self.skip_at is not None:
            return
        if tag in BLOCK_TAGS:
            self.text.append("\n")
        if tag == "a":
            self._href, self._anchor = a.get("href"), []
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag):
        if not self.active or tag in VOID_TAGS or tag not in self.stack:
            return
        while self.stack:
            level = len(self.stack)
            closed = self.stack.pop()
            self._close(closed, level)
            if closed == tag:
                break
        if not self.stack and not self.whole:
            self.active, self.done = False, True  # 領域が閉じた。この先は拾わない

    def _close(self, tag: str, level: int) -> None:
        if self.skip_at is not None:
            if level == self.skip_at:
                self.skip_at = None
            return
        if tag == "a" and self._href is not None:
            self.links.append((self._href, squash("".join(self._anchor))))
            self._href = None
        if tag == "h1":
            self._in_h1 = False
        if tag in BLOCK_TAGS:
            self.text.append("\n")

    def handle_data(self, data):
        if not self.active or self.skip_at is not None:
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
    scopes = []
    if "<main" in html.lower():
        scopes.append(lambda tag, _id, _cls: tag == "main")
    for i in CONTENT_IDS:
        if re.search(rf'id=["\']{i}["\']', html):
            scopes.append(lambda _tag, id_, _cls, want=i: id_ == want)
    for c in CONTENT_CLASSES:
        if re.search(rf'class=["\'][^"\']*\b{c}\b', html):
            scopes.append(lambda _tag, _id, cls, want=c: want in cls)
    scopes.append(lambda tag, _id, _cls: tag == "body")
    for scope in scopes:
        collector = _Collector(scope)
        collector.feed(html)
        lines = [squash(line) for line in "".join(collector.text).split("\n")]
        if any(lines):
            break
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
    collector = _Collector(lambda _tag, _id, _cls: False, whole=True)
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
