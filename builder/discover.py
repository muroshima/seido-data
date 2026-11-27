"""自治体の公式サイトから、制度の一覧ページの候補を探す（seido discover）。

entities.csv の website（トップページ）と、そこからリンクされた分類のページ（くらし・子育て・福祉
など）を見て、リンク文に「助成」「補助」「手当」「給付」などを含むページを候補にする。候補は
sources.csv と同じ列の行にして書き出し、`seido trial --add` で試し取りして採否を決める。

- 取得元（取込中・取込予定）がまだ無い団体だけを探す。複数の都道府県にまたがる取得元は数えない
- 公式サイトと同じホストのページだけを候補にする。robots.txt で禁止されたページは見ない
- license は `不明`、publish は `事実` にする（利用規約は人が確かめて直す）
"""

import re
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser

from . import http, webpage
from .registry import USABLE, expand
from .sources.webindex import allowed, is_listing, under

WORKERS = 16
# 1 団体あたりの候補の上限
MAX_CANDIDATES = 8
# 制度の一覧らしいリンク文
LISTING_TEXT = re.compile(r"助成|補助|手当|給付|支援制度|医療費|減免|奨励金|祝金|祝い金")
# 制度の一覧ではないリンク文
NOT_LISTING_TEXT = re.compile(
    r"お知らせ|新着|募集|入札|審議会|会議|計画|結果|報告|交付決定|実績|様式|申請書|ダウンロード"
)
# 一覧を探しに入る分類のページのリンク文（先頭一致）
CATEGORY_TEXT = re.compile(
    r"^(くらし|暮らし|生活|子育て|子ども|こども|健康|福祉|医療|高齢|障が?い|しごと|仕事|産業|"
    r"事業者|住まい|すまい)"
)
MAX_CATEGORIES = 8
# 分野の見当（リンク文から）
SCOPES = (
    (re.compile(r"子育て|子ども|こども|児童|出産|妊娠|ひとり親"), "子育て"),
    (re.compile(r"障が?い|障碍"), "障害"),
    (re.compile(r"高齢|介護|シニア"), "高齢者"),
    (re.compile(r"事業者|企業|産業|商工|農業|創業"), "事業者"),
    (re.compile(r"住宅|住まい|すまい|空き家|リフォーム"), "住まい"),
)
# リンク文に付く、アイコンの代替テキストなど
LINK_NOISE = re.compile(
    r"このリンクは別ウィンドウで開きます|別ウィンドウで開きます|外部リンク|新しいウィンドウ"
)
# ホスト名のうち、source_id に使わない部分
HOST_WORDS = {"www", "city", "town", "vill", "pref", "lg", "jp", "go", "or", "ne", "co", "com"}


@dataclass
class Candidate:
    url: str
    text: str
    format: str = "html"  # 一覧ページは html、個別の制度ページは html-page


def targets(entities: list[dict], sources: list[dict], prefs: list[str]) -> list[dict]:
    """prefs の団体のうち、website があり、自分の取得元（取込中・取込予定）がまだ無いもの。"""
    by_id = {e["id"]: e for e in entities}
    covered: set[str] = set()
    for s in sources:
        if s["status"] not in USABLE:
            continue
        ids = expand(s["covers"], entities)
        if (
            len({by_id[i]["lg_code"][:2] for i in ids}) == 1
        ):  # 複数の都道府県にまたがるものは数えない
            covered |= ids
    return [
        e for e in entities if e["lg_code"][:2] in prefs and e["website"] and e["id"] not in covered
    ]


def same_host(url: str, site: str) -> bool:
    host = urllib.parse.urlsplit(url).netloc.removeprefix("www.")
    return host == urllib.parse.urlsplit(site).netloc.removeprefix("www.")


class _AllLinks(HTMLParser):
    """ページのすべてのリンク。webpage.links と違い、<header>・<nav> のメニューも読む。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href, self._text = dict(attrs).get("href"), []
        elif tag == "img" and self._href is not None:
            self._text.append(dict(attrs).get("alt") or "")

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append((self._href, " ".join("".join(self._text).split())))
            self._href = None

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)


def page_links(url: str) -> list[tuple[str, str]]:
    collector = _AllLinks()
    collector.feed(webpage.BARE_AMP.sub("&amp;", webpage.decode(http.get(url))))
    found = []
    for href, text in collector.links:
        if (target := webpage.absolute(url, href.strip())) and target.startswith("http"):
            found.append((target, text))
    return found


def find(site: str) -> list[Candidate]:
    """公式サイトのトップと分類のページから、一覧ページの候補を探す。"""
    if not allowed(site):
        return []
    top = page_links(site)
    pages = [site]
    for url, text in top:
        if len(pages) > MAX_CATEGORIES:
            break
        if CATEGORY_TEXT.match(text.strip()) and same_host(url, site) and url not in pages:
            pages.append(url)
    found: dict[str, str] = {}
    for i, page in enumerate(pages):
        try:
            links = top if i == 0 else page_links(page) if allowed(page) else []
        except Exception:  # noqa: BLE001 分類のページが取れなくても、ほかは見る
            continue
        for url, text in links:
            text = " ".join(LINK_NOISE.sub("", text).split())
            if (
                same_host(url, site)
                and len(text) <= 40
                and LISTING_TEXT.search(text)
                and not NOT_LISTING_TEXT.search(text)
                and not url.lower().endswith((".pdf", ".xlsx", ".docx", ".doc", ".xls"))
            ):
                found.setdefault(url, text)
    return choose(found)


def choose(found: dict[str, str]) -> list[Candidate]:
    """一覧ページの候補があればそれだけを、無ければ個別の制度ページを候補にする。

    一覧ページは、ほかの候補の一覧の配下にあるもの（下位の一覧）を除く。取り込みが辿る。
    """
    rank = lambda kv: (-score(kv[1]), len(kv[1]), kv[0])  # noqa: E731
    listings = {u: t for u, t in found.items() if is_listing(u)}
    tops = {
        u: t
        for u, t in listings.items()
        if not any(o != u and is_listing(o) and under(u, o) for o in listings)
    }
    if tops:
        return [Candidate(u, t) for u, t in sorted(tops.items(), key=rank)[:MAX_CANDIDATES]]
    pages = sorted(found.items(), key=rank)[:MAX_CANDIDATES]
    return [Candidate(u, t, "html-page") for u, t in pages]


def score(text: str) -> int:
    """一覧らしさ。「一覧」や、複数の種類の語を含むリンク文を先にする。"""
    return 2 * ("一覧" in text) + len(set(LISTING_TEXT.findall(text)))


def slug(site: str) -> str:
    """source_id の頭。www.town.sumita.iwate.jp → sumita、www.odaitown.jp → odaitown。"""
    labels = urllib.parse.urlsplit(site).netloc.lower().split(".")
    words = [w for w in labels if w not in HOST_WORDS]
    return re.sub(r"[^a-z0-9-]", "-", words[0] if words else labels[0]).strip("-")


def scope_of(text: str) -> str:
    return next((name for pattern, name in SCOPES if pattern.search(text)), "全般")


def rows_for(entity: dict, found: list[Candidate], taken: set[str], today: date) -> list[dict]:
    """候補を sources.csv の行にする。source_id は taken と重ならないようにする。"""
    head = slug(entity["website"])
    if entity.get("kind") == "都道府県":
        head = f"{head}-pref"  # 県と県庁所在地の市はホスト名が同じことが多い（青森県・青森市）
    if any(t.startswith(f"{head}-") for t in taken):
        head = f"{head}-{entity['lg_code'][:2]}"  # 同じ名前の町（美浜町など）
    rows = []
    for n, c in enumerate(found, 1):
        sid = f"{head}-d{n}"
        taken.add(sid)
        rows.append(
            {
                "source_id": sid,
                "name": f"{entity['name']} {c.text}",
                "provider": entity["id"],
                "covers": entity["id"],
                "scope": scope_of(c.text),
                "kind": "web",
                "format": c.format,
                "url": c.url,
                "license": "不明",
                "publish": "事実",
                "update": "随時",
                "status": "取込予定",
                "checked": today.isoformat(),
                "note": f"seido discover の候補（リンク文「{c.text}」）。利用規約は未確認",
            }
        )
    return rows


def discover(entities: list[dict], sources: list[dict], prefs: list[str], today: date):
    """(候補の行, 候補が見つからなかった団体) を返す。"""
    found_by = {}
    todo = targets(entities, sources, prefs)

    def one(e: dict):
        try:
            return e["id"], find(e["website"]), None
        except Exception as ex:  # noqa: BLE001 1 団体の失敗で、ほかを止めない
            return e["id"], [], f"{type(ex).__name__}: {ex}"[:120]

    with ThreadPoolExecutor(WORKERS) as pool:
        for eid, found, error in pool.map(one, todo):
            found_by[eid] = (found, error)
    taken = {s["source_id"] for s in sources}
    rows, missing = [], []
    for e in todo:
        found, error = found_by[e["id"]]
        if found:
            rows += rows_for(e, found, taken, today)
        else:
            missing.append((e, error or "候補なし"))
    return rows, missing
