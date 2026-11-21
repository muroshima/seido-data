"""取り込んでいる市区町村を塗った地図（registry/coverage-map.svg）。

境界は国土交通省「国土数値情報（行政区域）」を簡略化して registry/boundaries.json に置く。
`seido registry boundaries` で作り直す（全国 47 都道府県の zip、合わせて約 800 MB を取る）。
地図は境界ファイルと対応表から作るので、ネットワークなしで `seido registry coverage` が作り直せる。

政令指定都市は区ごとの境界しか無いので、区に市の名前を持たせ、市が取り込まれていれば区を塗る。
"""

import io
import json
import math
import urllib.request
import zipfile
from pathlib import Path

N03_URL = "https://nlftp.mlit.go.jp/ksj/gml/data/N03/N03-2024/N03-20240101_{pref}_GML.zip"
ATTRIBUTION = "国土交通省「国土数値情報（行政区域データ）」（2024年1月1日時点）を加工して作成"
SCALE = 1000  # 座標は 0.001 度単位の整数で持つ

# (名前, 経度の範囲, 緯度の範囲, 簡略化の許容誤差[度], 描く幅[px])
JAPAN = ("全国", (122.5, 148.5), (24.0, 45.7), 0.01, 520)
# 関東は伊豆諸島まで入れる（東京都の島しょ）
KANTO = ("関東", (138.3, 141.0), (32.3, 37.2), 0.002, 250)
KANSAI = ("関西", (134.2, 136.5), (33.4, 35.8), 0.002, 230)
PANELS = (JAPAN, KANTO, KANSAI)
LABELS = {KANTO[0]: "関東（伊豆諸島まで）"}
# 北方領土の 6 村（色丹村など）。地図には描くが、全国の市区町村の数には入れない
NORTHERN_TERRITORIES = {"01695", "01696", "01697", "01698", "01699", "01700"}
MIN_AREA = 2e-5  # これより小さい島（平方度、約 0.2 km²）は描かない

COVERED = "#d62728"
OTHER = "#d9d9d9"
TEXT = "#666666"


# --- 境界の作成 -------------------------------------------------------------------------


def build_boundaries(cache: Path) -> dict:
    """国土数値情報の行政区域から、地図ごとに簡略化した境界を作る。zip は cache に置く。"""
    layers: dict[str, list[dict]] = {name: [] for name, *_ in PANELS}
    for pref in range(1, 48):
        for feature in _municipalities(_n03_zip(cache, f"{pref:02d}")):
            for name, lon, lat, tolerance, _ in PANELS:
                rings = []
                for ring in feature["rings"]:
                    if not _overlaps(ring, lon, lat):
                        continue
                    simple = _simplify(ring, tolerance)
                    if len(simple) >= 4 and abs(_area(simple)) >= MIN_AREA:
                        rings.append([round(v * SCALE) for point in simple for v in point])
                if rings:
                    layers[name].append({**feature["meta"], "rings": rings})
    return {"attribution": ATTRIBUTION, "scale": SCALE, "layers": layers}


def _n03_zip(cache: Path, pref: str) -> Path:
    path = cache / f"N03-20240101_{pref}_GML.zip"
    if not path.exists():
        cache.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(N03_URL.format(pref=pref), timeout=600) as res:
            path.write_bytes(res.read())
    return path


def _municipalities(zip_path: Path) -> list[dict]:
    """市区町村ごとの外周（穴は描かない）。所属未定地は除く。"""
    with zipfile.ZipFile(zip_path) as z:
        name = next(n for n in z.namelist() if n.endswith(".geojson"))
        data = json.load(io.TextIOWrapper(z.open(name), encoding="utf-8"))
    by_code: dict[str, dict] = {}
    for f in data["features"]:
        p = f["properties"]
        code = p["N03_007"]
        if not code or p["N03_004"] == "所属未定地":
            continue
        g = f["geometry"]
        polygons = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        entry = by_code.setdefault(code, {"meta": _meta(p), "rings": []})
        entry["rings"] += [polygon[0] for polygon in polygons]
    return list(by_code.values())


def _meta(p: dict) -> dict:
    # 政令指定都市の区は N03_004 が市、N03_005 が区。区には市の名前を持たせる
    if p["N03_005"]:
        return {"code": p["N03_007"], "name": p["N03_005"], "city": p["N03_004"]}
    return {"code": p["N03_007"], "name": p["N03_004"]}


def _overlaps(ring: list, lon: tuple, lat: tuple) -> bool:
    xs = [pt[0] for pt in ring]
    ys = [pt[1] for pt in ring]
    return max(xs) >= lon[0] and min(xs) <= lon[1] and max(ys) >= lat[0] and min(ys) <= lat[1]


def _area(ring: list) -> float:
    return sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(ring, ring[1:], strict=False)) / 2


def _simplify(points: list, tolerance: float) -> list:
    """Douglas-Peucker。長い海岸線で再帰が深くならないよう、スタックで回す。"""
    if len(points) < 3:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        first, last = stack.pop()
        (x1, y1), (x2, y2) = points[first][:2], points[last][:2]
        dx, dy = x2 - x1, y2 - y1
        norm = math.hypot(dx, dy)
        index, dist = 0, 0.0
        for i in range(first + 1, last):
            x, y = points[i][:2]
            d = (
                abs(dy * x - dx * y + x2 * y1 - y2 * x1) / norm
                if norm
                else math.hypot(x - x1, y - y1)
            )
            if d > dist:
                index, dist = i, d
        if dist > tolerance:
            keep[index] = True
            stack += [(first, index), (index, last)]
    return [p[:2] for p, k in zip(points, keep, strict=True) if k]


# --- 地図の描画 -------------------------------------------------------------------------


def covered_names(entities: list[dict], sources: list[dict], expand) -> tuple[set, set]:
    """取込中の取得元がある市区町村の、5 桁の団体コードと（都道府県コード, 名前）。"""
    ids: set[str] = set()
    for s in sources:
        if s["status"] == "取込中":
            ids |= expand(s["covers"], entities)
    codes, names = set(), set()
    for e in entities:
        if e["id"] in ids and e["kind"] == "市区町村" and e["lg_code"]:
            codes.add(e["lg_code"][:5])
            names.add((e["lg_code"][:2], e["name"]))
    return codes, names


def render(boundaries: dict, codes: set, names: set) -> str:
    """全国と地方の拡大図を横に並べた SVG。取込中の市区町村を赤で塗る。"""
    scale = boundaries["scale"]
    gap, top = 16, 8
    panels, x, height = [], 0, 0
    for name, lon, lat, _, width in PANELS:
        features = boundaries["layers"][name]
        k = width / ((lon[1] - lon[0]) * math.cos(math.radians(sum(lat) / 2)))
        h = round((lat[1] - lat[0]) * k)
        cos = math.cos(math.radians(sum(lat) / 2))
        paths = []
        for f in sorted(features, key=lambda f: f["code"]):
            hit = f["code"] in codes or (f["code"][:2], f.get("city", f["name"])) in names
            d = " ".join(
                "M"
                + " ".join(
                    f"{(r[i] / scale - lon[0]) * cos * k:.1f},{(lat[1] - r[i + 1] / scale) * k:.1f}"
                    for i in range(0, len(r), 2)
                )
                + "Z"
                for r in f["rings"]
            )
            paths.append(f'<path fill="{COVERED if hit else OTHER}" d="{d}"/>')
        label = LABELS.get(name, name)
        extra = f'<text x="4" y="14" font-size="12" fill="{TEXT}">{label}</text>'
        if name == JAPAN[0]:
            # 全国の図に、拡大図の範囲を枠で示す
            for _, zlon, zlat, *_ in PANELS[1:]:
                x0, x1 = ((v - lon[0]) * cos * k for v in zlon)
                y0, y1 = ((lat[1] - v) * k for v in zlat[::-1])
                extra += (
                    f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" '
                    f'height="{y1 - y0:.1f}" fill="none" stroke="{TEXT}" stroke-width="0.8"/>'
                )
        else:
            extra += (
                f'<rect x="0.5" y="0.5" width="{width - 1}" height="{h - 1}" '
                f'fill="none" stroke="{TEXT}" stroke-width="0.8"/>'
            )
        panels.append(
            f'<svg x="{x}" y="{top}" width="{width}" height="{h}" '
            f'viewBox="0 0 {width} {h}" overflow="hidden">'
            f'<g stroke="#ffffff" stroke-width="{0.15 if name == "全国" else 0.3}" '
            f'stroke-linejoin="round">{"".join(paths)}</g>{extra}</svg>'
        )
        x += width + gap
        height = max(height, h)
    japan = boundaries["layers"]["全国"]
    total = len(
        {
            (f["code"][:2], f["city"]) if "city" in f else f["code"]
            for f in japan
            if f["code"] not in NORTHERN_TERRITORIES
        }
    )
    width = x - gap
    y = top + height + 24
    legend = (
        f'<rect x="0" y="{y - 11}" width="12" height="12" fill="{COVERED}"/>'
        f'<text x="18" y="{y}" font-size="13" fill="{TEXT}">取り込んでいる市区町村 '
        f"{len(codes):,} / 全国 {total:,}</text>"
        f'<text x="0" y="{y + 20}" font-size="10" fill="{TEXT}">'
        f"{boundaries['attribution']}</text>"
    )
    full = y + 28
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{full}" '
        f'viewBox="0 0 {width} {full}" font-family="sans-serif">'
        f"<title>seido が取り込んでいる市区町村</title>{''.join(panels)}{legend}</svg>\n"
    )
