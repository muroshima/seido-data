"""取得元ごとの取り込み。対応表（registry/sources.csv）の 1 行が 1 つの取得元になる。

各モジュールは fetch(row) -> Fetched を持つ。row は sources.csv の行。
取得に失敗したら例外を投げる。その取得元は 1 件も書き換えない。
"""

import fnmatch
import re
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta, timezone

from ..model import Record, SourceInfo

JST = timezone(timedelta(hours=9))
STOPPED = re.compile(r"停止（(\d{4}-\d{2}-\d{2}) 時点）")


@dataclass
class Fetched:
    """units は「この取得元で置き換えてよい自治体 → その自治体の全レコード」。

    observed は「この内容がその日に存在した」と言える日。コミット日に使う。
    """

    observed: date
    units: dict[str, list[Record]]


def loaders():
    from . import ods, tokyo_kosodate_registry

    return {
        "tokyo-kosodate-registry": tokyo_kosodate_registry,
        "tokyo-ods-support-*": ods,
    }


def loader_for(source_id: str):
    for pattern, module in loaders().items():
        if fnmatch.fnmatchcase(source_id, pattern):
            return module
    return None


def source_info(row: dict[str, str], entities: list[dict[str, str]]) -> SourceInfo:
    provider = next(e["name"] for e in entities if e["id"] == row["provider"])
    stopped = stopped_at(row)
    as_of = f"（{stopped.isoformat()} 時点）" if stopped else ""
    return SourceInfo(
        name=row["source_id"],
        title=row["name"],
        url=row["url"],
        license=row["license"],
        attribution=f"{provider}「{row['name']}」{as_of}を加工して作成",
        publish=row["publish"],
    )


def stopped_at(row: dict[str, str]) -> date | None:
    """更新が止まった取得元なら、その時点の日付。"""
    m = STOPPED.fullmatch(row["update"])
    return date.fromisoformat(m.group(1)) if m else None


def today() -> date:
    return datetime.now(UTC).astimezone(JST).date()
