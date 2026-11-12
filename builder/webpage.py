"""自治体のサイトに直接置かれたファイルを、掲載ページのリンクから見つける。

ファイル名に日付が入って毎回変わることがあるので、対応表には掲載ページの URL を置く。
"""

import re
import urllib.parse
from html.parser import HTMLParser

from . import http

FILE_EXT = re.compile(r"\.(csv|xlsx)$", re.IGNORECASE)


class _Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((self._href, re.sub(r"\s+", " ", "".join(self._text)).strip()))
            self._href = None


def links(html: str, base_url: str) -> list[tuple[str, str]]:
    """ページ内のリンク（絶対 URL, リンク文）。"""
    parser = _Links()
    parser.feed(html)
    return [(urllib.parse.urljoin(base_url, href), text) for href, text in parser.links]


def resources(page_url: str, link_text: str) -> list[dict]:
    """リンク文に link_text を含む CSV・XLSX（CKAN の resources と同じ形）。"""
    html = http.get(page_url).decode("utf-8", errors="replace")
    found = []
    for url, text in links(html, page_url):
        m = FILE_EXT.search(urllib.parse.urlsplit(url).path)
        if m and link_text in text:
            found.append({"format": m.group(1).upper(), "url": url, "name": text})
    return found
