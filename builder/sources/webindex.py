"""自治体の支援制度の一覧ページを巡回し、制度ページごとに 1 件のレコードを作る。

対応表の 1 行が 1 自治体の 1 つの一覧ページに当たる（kind=web, format=html）。

- 一覧ページの本文領域から、同じサイトの HTML ページへのリンクを集める
- 一覧ページが index.html や / で終わる索引なら、その配下の下位の一覧を 1 階層だけ辿る。
  辿った先に制度ページへのリンクが無ければ、それ自体を制度ページとして扱う
- 配下にない一覧ページへのリンク（サイトのカテゴリメニュー）は辿らない
- 制度ページは本文のハッシュだけを raw/ に置き、本文は照合用に Record.source_text に持つ

制度の情報（対象者・金額など）はここでは埋めない。別の段階（LLM の抽出）で埋める。
"""

import hashlib
import re
import urllib.error
import urllib.parse
import urllib.robotparser
from functools import cache

from .. import http, webpage
from ..model import Record, Seido
from . import Fetched, today

LG = re.compile(r"^lg:(\d{6})$")
NOT_HTML = re.compile(r"\.(pdf|docx?|xlsx?|csv|zip|jpe?g|png|gif|txt|pptx?)$", re.IGNORECASE)
NOT_PAGE = re.compile(r"/cgi-bin/|/cgi-\w+/|/search/|/form/", re.IGNORECASE)
MAX_PAGES = 300
GONE = (404, 410)


def fetch(row: dict[str, str]) -> Fetched:
    m = LG.match(row["covers"])
    if not m:
        raise ValueError(f"covers は 1 自治体（lg:<団体コード>）: {row['covers']!r}")
    lg_code = m.group(1)
    index_url = row["url"]
    if not allowed(index_url):
        # 一覧ページ自体が robots.txt で禁止されている。既存のレコードは残す
        raise PermissionError(f"robots.txt で禁止されている: {index_url}")
    index = webpage.fetch(index_url)

    pages: dict[str, str] = {}  # 制度ページの URL → リンク文
    for url, text in candidates(index_url, index.links):
        if is_listing(url):
            # 下位の一覧は、一覧ページ自体がディレクトリの索引（index.html・/）のときだけ辿る。
            # 普通のページ（台東区の /benri/teate-josei.html など）の配下には無関係な一覧がある
            if url != index_url and is_listing(index_url) and under(url, index_url):
                try:
                    sub = webpage.fetch(url)
                except urllib.error.HTTPError as e:
                    if e.code in GONE:
                        continue  # 下位の一覧へのリンク切れ
                    raise
                found = [(u, t) for u, t in candidates(url, sub.links) if not is_listing(u)]
                if not found:
                    # 制度ページへのリンクが無い。/ で終わる URL の制度ページ（八丈町の WordPress）
                    pages.setdefault(url, text)
                for u, t in found:
                    pages.setdefault(u, t)
        else:
            pages.setdefault(url, text)
    if len(pages) > MAX_PAGES:
        raise RuntimeError(f"制度ページの候補が {len(pages)} 件と多すぎる（一覧の判定を見直す）")

    records = []
    for url, link_text in sorted(pages.items()):
        try:
            page = webpage.fetch(url)
        except urllib.error.HTTPError as e:
            if e.code in GONE:
                continue  # 一覧からのリンク切れ。制度ページは存在しない
            raise
        records.append(to_record(lg_code, url, page.title or link_text, page.text))
    return Fetched(observed=today(), units={lg_code: records})


def candidates(base_url: str, links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """同じサイトの HTML ページへのリンク（重複と自分自身を除く）。"""
    host = urllib.parse.urlsplit(base_url).netloc
    seen, found = {base_url}, []
    for url, text in links:
        parts = urllib.parse.urlsplit(url)
        if parts.scheme not in ("http", "https") or parts.netloc != host:
            continue
        if NOT_HTML.search(parts.path) or NOT_PAGE.search(parts.path) or url in seen:
            continue
        if not allowed(url):
            continue
        seen.add(url)
        found.append((url, text))
    return found


@cache
def robots(origin: str) -> urllib.robotparser.RobotFileParser | None:
    """サイトの robots.txt。取れなければ None（制限なしとして扱う）。"""
    parser = urllib.robotparser.RobotFileParser()
    try:
        parser.parse(http.get(f"{origin}/robots.txt").decode("utf-8", "replace").splitlines())
    except urllib.error.HTTPError as e:
        if e.code in GONE or e.code == 403:
            return None
        raise
    return parser


def allowed(url: str) -> bool:
    parts = urllib.parse.urlsplit(url)
    parser = robots(f"{parts.scheme}://{parts.netloc}")
    return parser is None or parser.can_fetch(http.USER_AGENT, url)


def is_listing(url: str) -> bool:
    path = urllib.parse.urlsplit(url).path
    return path.endswith("/") or path.endswith("/index.html") or path.endswith("/index.htm")


def under(url: str, index_url: str) -> bool:
    """url が一覧ページのディレクトリの配下にあるか。"""
    base = urllib.parse.urlsplit(index_url).path.rsplit("/", 1)[0] + "/"
    return urllib.parse.urlsplit(url).path.startswith(base)


def record_id(url: str) -> str:
    """URL のパスとクエリから作る、変わらない ID（読めるように末尾の名前を残す）。"""
    parts = urllib.parse.urlsplit(url)
    name = re.sub(r"\.\w+$", "", parts.path.rstrip("/").rsplit("/", 1)[-1]) or "index"
    # ?id=1 と ?id=2 のように、クエリで制度を分けるサイトがある
    key = parts.path + (f"?{parts.query}" if parts.query else "")
    return f"{name[:40]}-{hashlib.sha1(key.encode()).hexdigest()[:8]}"


def to_record(lg_code: str, url: str, title: str, text: str) -> Record:
    body = text.encode()
    return Record(
        lg_code=lg_code,
        lg_name="",
        record_id=record_id(url),
        raw={
            "url": url,
            "title": title,
            "content_sha256": hashlib.sha256(body).hexdigest(),
            "content_length": len(text),
        },
        seido=Seido(title=title, support=None, url=url, source_updated=None, sections={}),
        source_text=text,
    )
