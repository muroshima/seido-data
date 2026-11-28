import pytest

from builder import store
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


def test_duplicate_in_later_unit_writes_nothing(tmp_path):
    """後ろの自治体で重複が見つかっても、前の自治体だけ書き換わった状態にしない。"""
    units = {"131016": [rec("131016", "a")], "131024": [rec("131024", "x"), rec("131024", "x")]}
    with pytest.raises(ValueError, match="重複"):
        write_units(tmp_path, INFO, units)
    assert not (tmp_path / "raw").exists() and not (tmp_path / "seido").exists()


FACT = SourceInfo(name="f", title="t", url="u", license="不明", attribution="a", publish="事実")
PAGE = (
    "児童手当は、中学生までの子どもを育てている方に支給します。"
    "支給額は、3歳未満は月額15,000円、3歳以上は月額10,000円です。"
    "申請は区役所の子ども家庭課の窓口で受け付けています。"
)


def fact(sections: dict, source_text: str | None = PAGE) -> Record:
    s = Seido(title="児童手当", support=None, url=None, source_updated=None, sections=sections)
    raw = {"url": "https://example.jp/", "title": "児童手当", "content_sha256": "0" * 64}
    return Record("131016", "区", "a", raw, s, source_text=source_text)


def test_facts_are_written_with_notice_and_hash(tmp_path):
    r = fact({"対象者": "中学生までの子を育てる人", "支援内容": "3歳未満 月15,000円"})
    write_units(tmp_path, FACT, {"131016": [r]})
    md = (tmp_path / "seido/13/131016/f/a.md").read_text(encoding="utf-8")
    assert "本文は掲載せず" in md and "## 支援内容" in md
    assert not (tmp_path / "raw/f/131016/a.json").read_text(encoding="utf-8").count("支給")
    # 本文だけが変わっても seido/ に差分が出る
    r.raw["content_sha256"] = "1" * 64
    _, seido = write_units(tmp_path, FACT, {"131016": [r]})
    assert seido.changed == ["seido/13/131016/f/a.md"]


@pytest.mark.parametrize(
    "record, match",
    [
        (
            fact({"支援内容": "支給額は、3歳未満は月額15,000円、3歳以上は月額10,000円です。"}),
            "続けて一致",
        ),
        (fact({"概要": "児童の養育"}), "事実の項目ではない"),
        (fact({"対象者": "x" * 201}), "200 文字"),
        (fact({"対象者": "子育て世帯"}, source_text=None), "照合できない"),
        (fact({"対象者": "子育て世帯"}, source_text=" \n "), "照合できない"),
    ],
)
def test_facts_only_source_rejects_copies(tmp_path, record, match):
    with pytest.raises(ValueError, match=match):
        write_units(tmp_path, FACT, {"131016": [record]})
    assert not (tmp_path / "raw").exists()


def test_facts_only_source_rejects_text_in_raw(tmp_path):
    r = fact({})
    r.raw["body"] = PAGE
    with pytest.raises(ValueError, match="body"):
        write_units(tmp_path, FACT, {"131016": [r]})


def test_index_csv_rereads_only_changed_files(tmp_path, monkeypatch):
    """一覧を作り直すとき、前回から変わっていないファイルは読み直さない。"""
    d = tmp_path / "seido/13/132101/src"
    d.mkdir(parents=True)
    (d / "a.md").write_text("---\ntitle: 児童手当\n---\n", encoding="utf-8")
    (d / "b.md").write_text("---\ntitle: 医療費\n---\n", encoding="utf-8")
    read = []
    real = store.read_front
    monkeypatch.setattr(store, "read_front", lambda p: read.append(p.name) or real(p))
    first = store.index_csv(tmp_path, "13")
    (d / "b.md").write_text("---\ntitle: 医療費の助成\n---\n", encoding="utf-8")
    second = store.index_csv(tmp_path, "13")
    assert read == ["a.md", "b.md", "b.md"]
    assert "医療費の助成" in second and "医療費の助成" not in first
