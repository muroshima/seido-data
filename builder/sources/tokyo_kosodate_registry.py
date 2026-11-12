"""東京都「東京デジタル2030ビジョン（こどもDX）子育て支援制度レジストリ」0-6歳制度。

更新を終了したスナップショット（以降はデジタル庁のレジストリへ移行）。内容が変わらないので
日次では回さず、履歴の起点として 1 度だけ取り込む。コミット日は更新が止まった時点にする。
"""

import json

from .. import ckan, http
from ..model import Record, Seido, iso_date, join
from . import Fetched, stopped_at


def fetch(row: dict[str, str]) -> Fetched:
    as_of = stopped_at(row)
    if as_of is None:
        raise ValueError("更新が止まった時点（update 列の「停止（YYYY-MM-DD 時点）」）が要る")
    files = [r for r in ckan.resources(row["url"]) if (r.get("format") or "").upper() == "JSON"]
    if len(files) != 1:
        raise RuntimeError(f"JSON のファイルが 1 つではない: {[r['url'] for r in files]}")
    units: dict[str, list[Record]] = {}
    for item in json.loads(http.get(files[0]["url"])):
        record = to_record(item)
        units.setdefault(record.lg_code, []).append(record)
    return Fetched(observed=as_of, units=units)


def to_record(item: dict) -> Record:
    lg_code, _, lg_name = item["area"]["areaCode"].partition(";")
    return Record(
        lg_code=lg_code,
        lg_name=lg_name,
        record_id=item["basicInformation"]["psid"],
        raw=item,
        seido=to_seido(item),
    )


def to_seido(item: dict) -> Seido | None:
    support = item.get("support") or {}
    kinds = [
        k
        for k, key in (("金銭", "monetarySupport"), ("現物", "materiallySupport"))
        if support.get(key)
    ]
    if not kinds:
        return None  # 相談窓口など、金銭・現物の支援でないもの

    name = item.get("institutionName") or {}
    title = name.get("canonicalName") or ""
    if name.get("shortName") and name["shortName"] != title:
        title = f"{title}（{name['shortName']}）"

    target = item.get("target") or {}
    regulation = item.get("regulation") or {}
    contact = item.get("contact") or {}
    link = item.get("localGovernmentLink") or {}

    return Seido(
        title=title,
        support="・".join(kinds),
        url=link.get("uri"),
        source_updated=iso_date(item.get("updateDate")),
        sections={
            "概要": item.get("summary"),
            "対象者": join(target.get("targetPersons"), target.get("conditions")),
            "支援内容": join(
                support.get("monetarySupport"),
                support.get("materiallySupport"),
            ),
            "利用方法": join(item.get("utilization"), item.get("procedureMethod")),
            "持ち物": item.get("belongings"),
            "根拠法令": join(
                regulation.get("regulationName"), regulation.get("regulationArticle"), sep=" "
            ),
            "問い合わせ": join(contact.get("contactName"), contact.get("contactPhone"), sep="\n"),
        },
    )
