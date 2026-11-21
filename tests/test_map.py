"""取り込んでいる市区町村の地図。"""

from pathlib import Path

from builder import cli, registry
from builder import map as m

ROOT = Path(__file__).resolve().parents[1]


def boundaries(*features):
    layer = [
        {"rings": [[139000, 35000, 139100, 35000, 139100, 35100, 139000, 35000]], **f}
        for f in features
    ]
    return {
        "attribution": "出典",
        "scale": 1000,
        "layers": {"全国": layer, "関東": layer, "関西": layer},
    }


def test_ward_of_designated_city_is_filled_when_city_is_covered():
    data = boundaries(
        {"code": "14101", "name": "鶴見区", "city": "横浜市"},
        {"code": "14201", "name": "横須賀市"},
    )
    svg = m.render(data, codes=set(), names={("14", "横浜市")})
    assert svg.count(f'fill="{m.COVERED}"') == 4  # 3 枚の地図の鶴見区と凡例
    assert "全国 2" in svg


def test_northern_territories_are_not_counted():
    data = boundaries({"code": "01695", "name": "色丹村"}, {"code": "13101", "name": "千代田区"})
    assert "全国 1<" in m.render(data, codes={"13101"}, names=set())


def test_simplify_keeps_corners_and_drops_near_straight_points():
    ring = [[0, 0], [1, 0.001], [2, 0], [2, 2], [0, 2], [0, 0]]
    assert m._simplify(ring, 0.01) == [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]]


def test_repository_map_is_fresh():
    """コミットされている registry/coverage-map.svg が対応表と一致すること。"""
    entities, sources = registry.load(ROOT)
    actual = (ROOT / "registry" / "coverage-map.svg").read_text(encoding="utf-8")
    assert actual == cli.coverage_map(ROOT, entities, sources), "uv run seido registry coverage"
