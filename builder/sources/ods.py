"""自治体標準オープンデータセット「支援制度（給付金）情報」形式のファイル。

対応表の 1 行が 1 自治体のデータセットに当たる。url は CKAN のデータセットか、ファイルの
掲載ページ（福生市など、自治体のサイトに直接置かれているもの）。データセット内の CSV・XLSX の
うち、ヘッダーがこの形式のものを全部読み、その自治体の制度一覧として置き換える。
"""

import csv
import hashlib
import io
import re

import openpyxl

from .. import ckan, http, webpage
from ..model import Record, Seido, iso_date, join, safe_id
from . import Fetched, today

# 自治体標準オープンデータセット データ項目定義書B「支援制度情報」の列。自治体によって
# 「タイトル_制度名_」「No」のように記号が揺れるので、記号を除いた形で突き合わせる。
# 全国地方公共団体コードと ID は省かれていることがある（対応表の covers と制度名で補う）。
REQUIRED = {"支援制度種別", "タイトル（制度名）"}
SUPPORT_TARGET = {"1": "個人", "2": "事業者", "3": "自治体"}
LG = re.compile(r"^lg:(\d{6})$")


def fetch(row: dict[str, str]) -> Fetched:
    m = LG.match(row["covers"])
    if not m:
        raise ValueError(f"covers は 1 自治体（lg:<団体コード>）: {row['covers']!r}")
    lg_code = m.group(1)
    records: list[Record] = []
    seen: dict[str, dict] = {}  # ID → raw（複数ファイルをまたいで一意にする）
    matched = 0
    for res in resources(row["url"]):
        fmt = (res.get("format") or "").upper()
        if fmt not in ("CSV", "XLSX"):
            continue
        body = http.get(res["url"])
        header, rows = read_csv(body) if fmt == "CSV" else read_xlsx(body)
        if not {canon(k) for k in REQUIRED} <= {canon(k) for k in header}:
            continue  # 別形式のファイル（施設一覧など）
        matched += 1
        for raw in rows:
            line = canonical_row(raw)
            if not line.get("タイトル（制度名）"):
                continue
            code = line.get("全国地方公共団体コード")
            if code and code != lg_code:
                raise ValueError(f"全国地方公共団体コード {code} が covers {lg_code} と違う")
            record = to_record(raw, line, lg_code, seen)
            if record:
                records.append(record)
    if not matched:
        raise RuntimeError("この形式のファイルが 1 つも無い（形式が変わった可能性）")
    # 0 件でも置き換える（最後の制度が消えたことを削除として残す）
    return Fetched(observed=today(), units={lg_code: records})


def resources(url: str) -> list[dict]:
    """CKAN のデータセットならそのファイル、そうでなければ掲載ページの「支援制度」のリンク。"""
    if "/dataset/" in url:
        return ckan.resources(url)
    return webpage.resources(url, "支援制度")


def read_csv(body: bytes) -> tuple[list[str], list[dict[str, str]]]:
    for enc in ("utf-8-sig", "cp932"):
        try:
            text = body.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("文字コードを判定できない")
    reader = csv.DictReader(io.StringIO(text))
    header = list(reader.fieldnames or [])
    # raw/ に元の内容を残すため、ここでは空白を削らない（正規化は canonical_row でする）
    rows = [{k or "": v or "" for k, v in row.items()} for row in reader]
    return header, rows


def read_xlsx(body: bytes) -> tuple[list[str], list[dict[str, str]]]:
    ws = openpyxl.load_workbook(io.BytesIO(body), read_only=True, data_only=True).worksheets[0]
    it = ws.iter_rows(values_only=True)
    header = ["" if c is None else str(c) for c in next(it, [])]
    return header, [
        {k: ("" if v is None else str(v)) for k, v in zip(header, row, strict=False) if k.strip()}
        for row in it
        if any(v not in (None, "") for v in row)
    ]


def canon(key: str) -> str:
    return re.sub(r"[\s（）()_．.・]", "", key)


CANONICAL = {
    canon(k): k
    for k in (
        "全国地方公共団体コード ID 地方公共団体名 制度所管組織 支援制度ID 支援制度種別 "
        "タイトル（制度名） サブタイトル（通称等） 対象者 対象者条件 収入条件 家族構成条件 "
        "制度概要 内容 給付上限額 最大金利 借入限度額 償還期限 最大補助率 利用・申請方法 "
        "手続書類 募集時期 公募開始日 公募終了日 受付開始日 受付終了日 受付備考 根拠法令 "
        "詳細参照先 実施組織・支援機関 公開状態 公開日 連絡先名称 連絡先電話番号 URL"
    ).split()
}


def canonical_row(raw: dict[str, str]) -> dict[str, str]:
    """列名を定義書の表記に揃え、値の前後の空白を削る（raw は変えない）。"""
    return {CANONICAL.get(canon(k), k.strip()): v.strip() for k, v in raw.items()}


def to_record(
    raw: dict[str, str], row: dict[str, str], lg_code: str, seen: dict[str, dict]
) -> Record | None:
    """seen はその自治体で使った ID → raw。同じ内容の行が別ファイルにもあれば None を返す。"""
    title = row["タイトル（制度名）"]
    base = safe_id(
        row.get("ID")
        or row.get("支援制度ID")
        or "t" + hashlib.sha1(title.encode()).hexdigest()[:12]  # ID 列が無い自治体
    )
    record_id, n = base, 1
    while record_id in seen:
        if seen[record_id] == raw:
            return None  # 同じ制度が別形式のファイルにも載っている
        n += 1  # 同じ ID・同名で中身の違う制度
        record_id = f"{base}-{n}"
    seen[record_id] = raw
    return Record(
        lg_code=lg_code,
        lg_name=row.get("地方公共団体名", ""),
        record_id=record_id,
        raw=raw,
        seido=to_seido(row),
    )


def to_seido(row: dict[str, str]) -> Seido | None:
    if row.get("公開状態", "").upper() == "FALSE":
        return None
    g = row.get
    amount = "\n".join(
        f"{k}: {g(k)}"
        for k in ("給付上限額", "最大補助率", "借入限度額", "最大金利", "償還期限")
        if g(k)
    )
    period = "\n".join(
        f"{k}: {g(k)}"
        for k in ("募集時期", "公募開始日", "公募終了日", "受付開始日", "受付終了日", "受付備考")
        if g(k)
    )
    return Seido(
        title=join(
            g("タイトル（制度名）"),
            g("サブタイトル（通称等）") and f"（{g('サブタイトル（通称等）')}）",
            sep="",
        ),
        support=None,  # この形式には金銭・現物の区別が無い
        url=g("URL") or g("詳細参照先") or None,
        source_updated=iso_date(g("公開日")),
        sections={
            "支援の対象": SUPPORT_TARGET.get(g("支援制度種別", ""), g("支援制度種別")),
            "概要": g("制度概要"),
            "対象者": join(
                g("対象者"), g("対象者条件"), g("収入条件"), g("家族構成条件"), sep="\n"
            ),
            "支援内容": join(g("内容"), amount),
            "期間": period,
            "利用方法": join(g("利用・申請方法"), g("手続書類") and f"手続書類: {g('手続書類')}"),
            "根拠法令": g("根拠法令"),
            "問い合わせ": join(
                g("実施組織・支援機関") or g("制度所管組織"),
                g("連絡先名称"),
                g("連絡先電話番号"),
                sep="\n",
            ),
        },
    )
