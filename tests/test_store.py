import pytest

from builder.model import Record, Seido, SourceInfo
from builder.store import write_units

INFO = SourceInfo(name="src", title="t", url="u", license="CC BY", attribution="a")


def rec(lg: str, rid: str, title: str = "制度", seido: bool = True) -> Record:
    s = Seido(title=title, support="金銭", url=None, source_updated=None, sections={"概要": title})
    return Record(
        lg_code=lg, lg_name="区", record_id=rid, raw={"t": title}, seido=s if seido else None
    )


def test_add_change_remove(tmp_path):
    write_units(tmp_path, INFO, {"131016": [rec("131016", "a"), rec("131016", "b")]})
    raw, seido = write_units(
        tmp_path, INFO, {"131016": [rec("131016", "a", "変更"), rec("131016", "c")]}
    )
    assert seido.added == ["seido/13/131016/src/c.md"]
    assert seido.changed == ["seido/13/131016/src/a.md"]
    assert seido.removed == ["seido/13/131016/src/b.md"]
    assert len(raw.added) == 1 and len(raw.changed) == 1 and len(raw.removed) == 1


def test_rerun_is_noop(tmp_path):
    units = {"131016": [rec("131016", "a")]}
    write_units(tmp_path, INFO, units)
    raw, seido = write_units(tmp_path, INFO, units)
    assert raw.empty and seido.empty


def test_missing_unit_is_untouched(tmp_path):
    """取得に失敗した自治体（units に無い）は削除扱いにしない。"""
    write_units(tmp_path, INFO, {"131016": [rec("131016", "a")], "131024": [rec("131024", "x")]})
    _, seido = write_units(tmp_path, INFO, {"131016": [rec("131016", "a")]})
    assert seido.empty
    assert (tmp_path / "seido/13/131024/src/x.md").exists()


def test_non_support_goes_to_raw_only(tmp_path):
    raw, seido = write_units(tmp_path, INFO, {"131016": [rec("131016", "a", seido=False)]})
    assert raw.added == ["raw/src/131016/a.json"]
    assert seido.empty


def test_duplicate_id_rejected(tmp_path):
    with pytest.raises(ValueError, match="重複"):
        write_units(tmp_path, INFO, {"131016": [rec("131016", "a"), rec("131016", "a")]})


def test_record_id_is_file_safe():
    assert (
        rec("131016", "psid3.0+8000020131016+10+UM54").record_id == "psid3.0_8000020131016_10_UM54"
    )


def test_lg_code_must_be_6_digits():
    with pytest.raises(ValueError):
        rec("13101", "a")
