"""自治体の Web ページから、リンクと本文を取り出す。

- 掲載ページのリンクから、日付入りの名前で置かれた CSV・XLSX を見つける（福生市など）
- 支援制度の一覧ページから制度ページへのリンクを集め、制度ページの本文を取り出す

本文は `<main>` の中だけを使う。無ければ、よくある本文領域の id、次に class、それも無ければ
`<body>` から header・nav・footer を除いた部分を使う。サイト共通のメニューやパンくずを本文に
混ぜないため。
選んだ領域に文字が無ければ（id が中身の無い目印の要素に付いているなど）、次の候補に移る。

文字コードは UTF-8 として読めればそれを使い、読めなければ meta の charset、それも無ければ
Shift_JIS（cp932）とみなす（古座川町・佐用町）。
"""

import io
import re
import urllib.parse
from dataclasses import dataclass, field
from html import unescape
from html.parser import HTMLParser

from pypdf import PdfReader

from . import http

META_CHARSET = re.compile(rb'<meta[^>]+charset=["\']?([\w-]+)', re.IGNORECASE)
# href の `&section_id=` を、HTML の解釈で `§ion_id=` と読まないよう `&amp;` に直す（佐用町）。
# `;` の無い名前付き文字参照を、HTML の仕様どおりに文字へ変えてしまうため
BARE_AMP = re.compile(r"&(?=[A-Za-z][A-Za-z0-9_]*=)")
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
    "ContentPane",  # 甲賀市
    "detail-td-main",  # 新温泉町
    "maincotents",  # 天川村（綴りはサイトのまま）
    "Wrapp",  # 明日香村（id="Content_TXT" は問い合わせ先の箱だけ）
)
# id が無く class でしか見分けられない本文領域
CONTENT_CLASSES = (
    "main_naka",  # 羽村市の一覧ページ
    "main_area",  # 小平市
    "main",  # 三鷹市（id="contents" は本文への目印の <p class="skip">）
    "wrapper-contents",  # 足利市・下野市・鹿沼市など（栃木・群馬に多い CMS の本文の列）
    "main_section",  # 曽爾村・那智勝浦町・新宮市
    "mainColumn",  # 川上村
)
# 本文領域の中にあるパンくず・関連リンク・フッター（練馬区は本文と同じ要素の中に置く）、
# 同じ階層の分類メニュー（日の出町）
SKIP_CLASSES = {
    "pankuzu",
    "lobgbox",
    "footbg",
    "page_right",
    "boxKeywordSearch",  # 八王子市（id="content" の中の検索欄・パンくず）
    "boxBreadcrumb",
    "bread-rubbish",  # 足利市などの CMS のパンくず
    "genre-contents-office",  # 同じ CMS の一覧の、記事ごとの担当課へのリンク
    "pagenavi",  # 佐用町のページ送り
    "postprint",  # 天川村の印刷用ページへのリンク
    "pph__container",  # 曽爾村などの CMS のパンくず
    "side-menugroup__edge",  # 同じ CMS の、本文の中の他の分類のメニュー
    "info__update",
    "sns-share-buttons",
}
SKIP_IDS = {
    "side",  # 八王子市のサイドメニュー（分野の一覧）
    "SIDE",  # 佐用町のランキング
    "BREADNAV",  # 佐用町のパンくず
    "pankz",  # 天川村のパンくず
    "searchbox",  # 黒滝村
    "panlist",
    "breadCrumbs",  # 川上村
}
# 本文に h1 が無いサイトの、題名の要素（曽爾村・那智勝浦町）
TITLE_CLASSES = {"info__title"}
# 読み飛ばす aside のうち、担当課の問い合わせ先だけは残す（町田市 contact・日の出町など kakuka）
KEEP_ASIDE = {"contact", "kakuka"}
# 本文へ飛ぶための目印（「ここから本文です」）。本文の id が付いていても本文ではない
SKIP_LINK_CLASS = "skip"
# aside は本文の外の補足（町田市の日替わりの「これにも注目」と評価欄。毎日本文が変わって見えていた）
SKIP_TAGS = {"script", "style", "noscript", "template", "nav", "header", "footer", "aside"}
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
    # <title> の先頭の段（「浄化槽設置整備事業補助金｜東吉野村」の「浄化槽設置整備事業補助金」）。
    # 本文に見出しもリンク文も無いとき（東吉野村の画像だけのリンク）の題名
    doc_title: str = ""
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
        self.header_h1: list[str] = []  # 領域の中の <header> にある h1（こまえ子育てねっと）
        self.h1_count = 0
        self.class_title: list[str] = []  # TITLE_CLASSES の要素の文字
        self._title_at: int | None = None
        self._href: str | None = None
        self._anchor: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        if not self.active:
            if (
                not self.done
                and SKIP_LINK_CLASS not in classes
                and self.in_scope(tag, a.get("id") or "", classes)
            ):
                self.active, self.stack = True, [tag]
            return
        if tag in VOID_TAGS:
            if tag == "br" and self.skip_at is None:
                self.text.append("\n")
            return
        self.stack.append(tag)
        if self.skip_at is None and (
            (tag in SKIP_TAGS and not (tag == "aside" and (classes | {a.get("id")}) & KEEP_ASIDE))
            or classes & SKIP_CLASSES
            or a.get("id") in SKIP_IDS
        ):
            self.skip_at = len(self.stack)
        if self.skip_at is not None:
            if tag == "h1" and self.stack[self.skip_at - 1] == "header":
                self._in_h1 = True
            return
        if tag in BLOCK_TAGS:
            self.text.append("\n")
        if tag == "a":
            self._href, self._anchor = a.get("href"), []
        if tag == "h1":
            self._in_h1 = True
            self.h1_count += 1
        if self._title_at is None and classes & TITLE_CLASSES:
            self._title_at = len(self.stack)

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
            if tag == "h1":
                self._in_h1 = False
            return
        if tag == "a" and self._href is not None:
            self.links.append((self._href, squash("".join(self._anchor))))
            self._href = None
        if tag == "h1":
            self._in_h1 = False
        if level == self._title_at:
            self._title_at = None
        if tag in BLOCK_TAGS:
            self.text.append("\n")

    def handle_data(self, data):
        if self.active and self.skip_at is not None and self._in_h1:
            self.header_h1.append(data)
        if not self.active or self.skip_at is not None:
            return
        self.text.append(data)
        if self._href is not None:
            self._anchor.append(data)
        if self._in_h1:
            self.h1.append(data)
        if self._title_at is not None:
            self.class_title.append(data)


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def pdf_text(data: bytes) -> str:
    """PDF の文字。文字を持たない（画像だけの）PDF は空になる。"""
    reader = PdfReader(io.BytesIO(data))
    return squash(" ".join(p.extract_text() or "" for p in reader.pages))


def decode(data: bytes) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        pass
    m = META_CHARSET.search(data[:4096])
    charset = m.group(1).decode().lower() if m else ""
    if charset.replace("-", "").replace("_", "") in ("", "utf8", "shiftjis", "sjis", "windows31j"):
        charset = "cp932"  # meta が UTF-8 と言っていても、読めなかった（佐用町）
    try:
        return data.decode(charset, errors="replace")
    except LookupError:
        return data.decode("cp932", errors="replace")


def parse(html: str, base_url: str) -> Page:
    """本文領域の見出し・文字・リンクを取り出す。"""
    html = BARE_AMP.sub("&amp;", html)
    scopes = []
    if "<main" in html.lower():
        scopes.append(lambda tag, _id, _cls: tag == "main")
    for i in CONTENT_IDS:
        if re.search(rf'id=["\']{i}["\']', html):
            scopes.append(lambda _tag, id_, _cls, want=i: id_ == want)
    for c in CONTENT_CLASSES:
        if re.search(rf'class=["\'][^"\']*\b{c}\b', html):
            scopes.append(lambda _tag, _id, cls, want=c: want in cls)
    body = lambda tag, _id, _cls: tag == "body"  # noqa: E731
    scopes.append(body)
    for scope in scopes:
        collector = _Collector(scope)
        collector.feed(html)
        lines = [squash(line) for line in "".join(collector.text).split("\n")]
        if any(lines):
            break
    doc_title = document_title(html)
    title = squash("".join(collector.h1))
    if collector.h1_count >= 2 and doc_title and scope is not body:
        # h1 を本文の小見出しに使うサイト（佐用町の「▶対象者」）。並べると題名にならない。
        # body 全体のときはサイト共通の h1 も混ざるので使わない（豊中市）
        title = doc_title
    if not title and scope is not body:
        # body 全体のときの <header> はサイト共通の見出し（ロゴ）なので使わない
        title = squash("".join(collector.header_h1))
    if not title:
        title = squash("".join(collector.class_title))
    return Page(
        title=title,
        doc_title=doc_title,
        text="\n".join(line for line in lines if line),
        links=[
            (url, text)
            for href, text in collector.links
            if href and not href.startswith(("mailto:", "tel:", "javascript:", "#"))
            if (url := absolute(base_url, href))
        ],
    )


def document_title(html: str) -> str:
    """<title> の先頭の段。「｜」「|」「 - 」の後ろはサイト名なので捨てる。"""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    return squash(re.split(r"[｜|]| - | – ", unescape(m.group(1)))[0])


def absolute(base_url: str, href: str) -> str | None:
    """リンクの絶対 URL（# 以降を除く）。URL として壊れたリンク（横瀬町の `//tel：…`）は None。"""
    try:
        return urllib.parse.urldefrag(urllib.parse.urljoin(base_url, href))[0]
    except ValueError:
        return None


def fetch(url: str) -> Page:
    return parse(decode(http.get(url)), url)


def links(html: str, base_url: str) -> list[tuple[str, str]]:
    """ページ全体のリンク（絶対 URL, リンク文）。"""
    collector = _Collector(lambda _tag, _id, _cls: False, whole=True)
    collector.feed(BARE_AMP.sub("&amp;", html))
    return [(urllib.parse.urljoin(base_url, href), text) for href, text in collector.links if href]


def resources(page_url: str, link_text: str) -> list[dict]:
    """リンク文に link_text を含む CSV・XLSX（CKAN の resources と同じ形）。"""
    html = decode(http.get(page_url))
    found = []
    for url, text in links(html, page_url):
        m = FILE_EXT.search(urllib.parse.urlsplit(url).path)
        if m and link_text in text:
            found.append({"format": m.group(1).upper(), "url": url, "name": text})
    return found
