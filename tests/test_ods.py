import pytest

from builder.sources import ods

HEADER = "支援制度種別,タイトル（制度名）,ID\n"
ROW = {"covers": "lg:131016", "url": "https://catalog.example/dataset/t131016d1"}


def test_header_variants_are_canonicalized():
    """中野区は「タイトル_制度名_」、小金井市は「タイトル（制度名）」。"""
    a = ods.canonical_row({"タイトル_制度名_": "x", "中小企業施策利用ガイドブックページNo": "1"})
    b = ods.canonical_row({"タイトル（制度名）": "x"})
    assert a["タイトル（制度名）"] == b["タイトル（制度名）"] == "x"


def record(raw: dict, seen: dict):
    return ods.to_record(raw, ods.canonical_row(raw), "131016", seen)


def test_missing_id_is_filled_and_disambiguated():
    """東村山市・青梅市は ID 列が無い。同名で中身の違う制度は -2 を付ける。"""
    seen: dict = {}
    raw1 = {"支援制度種別": "1", "タイトル（制度名）": "緊急通報システム", "内容": "a"}
    r1 = record(raw1, seen)
    r2 = record({**raw1, "内容": "b"}, seen)
    assert r1.record_id.startswith("t") and r2.record_id == f"{r1.record_id}-2"


def test_same_row_in_two_files_is_kept_once():
    seen: dict = {}
    raw = {"支援制度種別": "1", "タイトル（制度名）": "x", "ID": "1"}
    assert record(raw, seen)
    assert record(raw, seen) is None


def test_ids_colliding_after_sanitize_are_disambiguated():
    """a+b と a_b はファイル名にすると同じになる。"""
    seen: dict = {}
    ids = [
        record({"支援制度種別": "1", "タイトル（制度名）": i, "ID": i}, seen).record_id
        for i in ("a+b", "a_b")
    ]
    assert ids == ["a_b", "a_b-2"]


def test_unpublished_row_is_raw_only():
    assert ods.to_seido({"公開状態": "FALSE", "タイトル（制度名）": "x"}) is None


def test_read_csv_cp932():
    body = "支援制度種別,タイトル（制度名）\n1,児童手当\n".encode("cp932")
    assert ods.read_csv(body) == (
        ["支援制度種別", "タイトル（制度名）"],
        [{"支援制度種別": "1", "タイトル（制度名）": "児童手当"}],
    )


@pytest.fixture
def dataset(monkeypatch):
    """データセットのファイル（url → 本文、例外なら取得失敗）を差し替える。"""

    def setup(bodies: dict):
        def get(url, params=None):
            if isinstance(bodies[url], Exception):
                raise bodies[url]
            return bodies[url].encode()

        resources = [{"format": "CSV", "url": u} for u in bodies]
        monkeypatch.setattr(ods.ckan, "resources", lambda url: resources)
        monkeypatch.setattr(ods.http, "get", get)

    return setup


def test_header_only_file_empties_the_unit(dataset):
    """最後の制度が消えたら、その自治体を空で返して削除を反映する。"""
    dataset({"u1": HEADER})
    assert ods.fetch(ROW).units == {"131016": []}


def test_rows_across_files_are_merged(dataset):
    dataset({"u1": HEADER + "1,a,1\n", "u2": HEADER + "1,b,2\n"})
    assert [r.record_id for r in ods.fetch(ROW).units["131016"]] == ["1", "2"]


def test_failed_file_fails_the_source(dataset):
    """1 ファイルでも取れなければ、取得元ごと失敗にする（不完全な一覧で置き換えない）。"""
    dataset({"u1": HEADER + "1,a,1\n", "u2": OSError("timeout")})
    with pytest.raises(OSError):
        ods.fetch(ROW)


def test_no_matching_file_fails(dataset):
    """形式が変わって 1 つも読めないときは、全件削除にしない。"""
    dataset({"u1": "施設名,住所\nx,y\n"})
    with pytest.raises(RuntimeError, match="1 つも無い"):
        ods.fetch(ROW)


def test_other_lg_code_in_rows_fails(dataset):
    dataset({"u1": "支援制度種別,タイトル（制度名）,全国地方公共団体コード\n1,a,131024\n"})
    with pytest.raises(ValueError, match="covers"):
        ods.fetch(ROW)


def test_raw_keeps_original_whitespace(dataset):
    """raw/ には元の値を残し、seido/ 用の値だけ空白を削る。"""
    dataset({"u1": "支援制度種別,タイトル（制度名）,ID\n1,  児童手当 ,1\n"})
    (r,) = ods.fetch(ROW).units["131016"]
    assert r.raw["タイトル（制度名）"] == "  児童手当 "
    assert r.seido.title == "児童手当"
