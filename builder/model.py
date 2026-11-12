"""制度 1 件の共通表現と、seido/ に書き出す Markdown への変換。"""

import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from difflib import SequenceMatcher

import yaml

LG_CODE = re.compile(r"^\d{6}$")
UNSAFE = re.compile(r"[^0-9A-Za-z._-]+")


def safe_id(raw_id: str) -> str:
    """取得元の ID をファイル名に使える形にする（psid の `+` など）。"""
    return UNSAFE.sub("_", raw_id).strip("_")


@dataclass
class Seido:
    """seido/ に出す制度 1 件。sections は見出しと本文の組で、出現順に並ぶ。"""

    title: str
    support: str | None
    url: str | None
    source_updated: str | None
    sections: dict[str, str] = field(default_factory=dict)
    # 事実だけの取得元で、sections をどの本文（のハッシュ）から取り出したか
    facts_sha256: str | None = None


@dataclass
class Record:
    """取得元の 1 レコード。raw はそのまま raw/ に書く。seido が None なら seido/ に出さない。"""

    lg_code: str
    lg_name: str
    record_id: str
    raw: dict
    seido: Seido | None
    # 事実だけを持つ取得元で、取り出した項目が原文の書き写しでないかを照合するための原文。
    # どこにも書き出さない
    source_text: str | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if not LG_CODE.match(self.lg_code):
            raise ValueError(f"全国地方公共団体コードは6桁: {self.lg_code!r}")
        self.record_id = safe_id(self.record_id)
        if not self.record_id:
            raise ValueError("record_id が空")


# publish が「事実」の取得元で raw/ に置いてよいキー。本文は置かない
FACT_RAW_KEYS = frozenset({"url", "title", "content_sha256", "content_length"})
# 事実として持つ項目。それぞれ短く、取得元の文章を書き写さない
FACT_SECTIONS = ("対象者", "支援内容", "期間", "利用方法", "問い合わせ")
FACT_MAX_CHARS = 200
# 原文と同じ文字列がこの長さ以上続いたら、書き写しとみなす
VERBATIM_LIMIT = 30


@dataclass
class SourceInfo:
    name: str
    title: str
    url: str
    license: str
    attribution: str
    publish: str = "本文"

    @property
    def facts_only(self) -> bool:
        return self.publish == "事実"


def check_publishable(record: Record, source: SourceInfo) -> None:
    """事実だけを持つ取得元から、本文や書き写しが raw/ や seido/ に入らないようにする。"""
    if not source.facts_only:
        return
    where = f"{source.name} {record.record_id}"
    extra = set(record.raw) - FACT_RAW_KEYS
    if extra:
        raise ValueError(f"{where}: 事実だけの取得元の raw に {sorted(extra)} がある")
    sections = {k: v for k, v in (record.seido.sections if record.seido else {}).items() if v}
    unknown = set(sections) - set(FACT_SECTIONS)
    if unknown:
        raise ValueError(f"{where}: 事実の項目ではない節 {sorted(unknown)} がある")
    if sections and not (record.source_text or "").strip():
        raise ValueError(f"{where}: 原文が無いので、書き写しでないかを照合できない")
    for heading, value in sections.items():
        if len(value) > FACT_MAX_CHARS:
            raise ValueError(f"{where}: 「{heading}」が {FACT_MAX_CHARS} 文字を超える")
        run = longest_common_run(value, record.source_text or "")
        if run >= VERBATIM_LIMIT:
            raise ValueError(f"{where}: 「{heading}」が原文と {run} 文字続けて一致する")


def longest_common_run(a: str, b: str) -> int:
    """a と b に共通する、最も長い連続した文字列の長さ（空白の違いは無視する）。"""
    a, b = re.sub(r"\s+", "", a), re.sub(r"\s+", "", b)
    if not a or not b:
        return 0
    m = SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
    return m.size


def render(record: Record, source: SourceInfo) -> str:
    s = record.seido
    assert s is not None
    front = {
        "title": s.title,
        "lg_code": record.lg_code,
        "lg_name": record.lg_name,
        "support": s.support,
        "url": s.url,
        "source": source.name,
        "source_id": record.record_id,
        "source_updated": s.source_updated,
        "license": source.license,
        "attribution": source.attribution,
    }
    if "content_sha256" in record.raw:
        # 巡回したページ（publish にかかわらず）。本文が変わったことを seido/ の差分に出す
        front["content_sha256"] = record.raw.get("content_sha256")
        # 本文が変わったのにまだ取り出し直していないと、content_sha256 と食い違う
        front["facts_sha256"] = s.facts_sha256
    lines = ["---", yaml.safe_dump(front, allow_unicode=True, sort_keys=False).rstrip(), "---", ""]
    lines += [f"# {s.title}", ""]
    if source.facts_only:
        lines += [
            "取得元の利用規約により本文は掲載せず、制度の情報だけを取り出しています。"
            "正確な内容は `url` のページで確かめてください。",
            "",
        ]
    for heading, body in s.sections.items():
        body = normalize_text(body)
        if body:
            lines += [f"## {heading}", "", body, ""]
    return "\n".join(lines).rstrip() + "\n"


def normalize_text(text: str | None) -> str:
    """改行・空白の揺れで差分が出ないように揃える。中身は変えない。"""
    if not text:
        return ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def join(*parts: str | None, sep: str = "\n\n") -> str:
    return sep.join(p.strip() for p in parts if p and p.strip())


def iso_date(value: str | date | None) -> str | None:
    if not value:
        return None
    text = str(value).strip()
    if re.fullmatch(r"\d{5}", text):
        # Excel の日付シリアル値がそのまま入っていることがある（45292 = 2024-01-01）
        return (date(1899, 12, 30) + timedelta(days=int(text))).isoformat()
    return text[:10]
