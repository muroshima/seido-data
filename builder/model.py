"""制度 1 件の共通表現と、seido/ に書き出す Markdown への変換。"""

import re
from dataclasses import dataclass, field
from datetime import date

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


@dataclass
class Record:
    """取得元の 1 レコード。raw はそのまま raw/ に書く。seido が None なら seido/ に出さない。"""

    lg_code: str
    lg_name: str
    record_id: str
    raw: dict
    seido: Seido | None

    def __post_init__(self) -> None:
        if not LG_CODE.match(self.lg_code):
            raise ValueError(f"全国地方公共団体コードは6桁: {self.lg_code!r}")
        self.record_id = safe_id(self.record_id)
        if not self.record_id:
            raise ValueError("record_id が空")


@dataclass
class SourceInfo:
    name: str
    title: str
    url: str
    license: str
    attribution: str


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
    lines = ["---", yaml.safe_dump(front, allow_unicode=True, sort_keys=False).rstrip(), "---", ""]
    lines += [f"# {s.title}", ""]
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
    return str(value)[:10]
