import contextlib

import pytest

from builder import extract
from builder.model import SourceInfo
from builder.sources import webindex
from builder.store import read_sections, write_units

PAGE = (
    "児童手当は、中学生までの子どもを育てている方に支給します。"
    "支給額は、3歳未満は月額15,000円、3歳以上は月額10,000円です。"
    "申請は区役所の子ども家庭課の窓口で受け付けています。"
)
GOOD = {
    "is_program": True,
    "対象者": "中学生までの子を育てる人",
    "支援内容": "3歳未満は月1万5千円、3歳以上は月1万円",
    "期間": "",
    "利用方法": "子ども家庭課の窓口で申請",
    "問い合わせ": "",
}
COPIED = {**GOOD, "支援内容": "支給額は、3歳未満は月額15,000円、3歳以上は月額10,000円です。"}
INFO = SourceInfo(name="w", title="t", url="u", license="不明", attribution="a", publish="事実")


class FakeLLM:
    def __init__(self, *answers):
        self.answers = list(answers)
        self.calls = []

    def ask(self, title, text, note=""):
        self.calls.append(note)
        return dict(self.answers.pop(0))


def test_extract_keeps_short_facts_only():
    facts = extract.extract(FakeLLM(GOOD), "児童手当", PAGE)
    assert facts.is_program
    assert facts.sections == {k: v for k, v in GOOD.items() if k != "is_program" and v}


def test_copied_field_is_asked_again_and_dropped_if_still_copied():
    llm = FakeLLM(COPIED, COPIED)
    facts = extract.extract(llm, "児童手当", PAGE)
    assert len(llm.calls) == 2 and "支援内容" in llm.calls[1]
    assert "支援内容" not in facts.sections and "対象者" in facts.sections


def test_copied_field_is_replaced_by_retry():
    facts = extract.extract(FakeLLM(COPIED, GOOD), "児童手当", PAGE)
    assert facts.sections["支援内容"] == GOOD["支援内容"]


def record(url="https://www.city.example.lg.jp/kosodate/jidouteate.html", text=PAGE):
    return webindex.to_record("131016", url, "児童手当", text)


def session_of(llm):
    @contextlib.contextmanager
    def open_session():
        yield llm

    return open_session


def test_fill_calls_llm_only_for_new_or_changed_pages(tmp_path):
    first = FakeLLM(GOOD)
    r = record()
    assert extract.fill(tmp_path, "w", [r], session_of(first)) == 1
    write_units(tmp_path, INFO, {"131016": [r]})

    # 本文が同じなら前回の項目を使い、LLM を呼ばない
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM())) == 0
    assert again.seido.sections == r.seido.sections

    # 本文が変わったら LLM に回す
    changed = record(text=PAGE + "令和8年4月から所得制限をなくしました。")
    assert extract.fill(tmp_path, "w", [changed], session_of(FakeLLM(GOOD))) == 1


def test_fill_keeps_non_programs_out_of_seido(tmp_path):
    r = record()
    extract.fill(tmp_path, "w", [r], session_of(FakeLLM({**GOOD, "is_program": False})))
    assert r.seido is None
    write_units(tmp_path, INFO, {"131016": [r]})
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM())) == 0
    assert again.seido is None


def test_fill_retries_pages_crawled_without_extraction(tmp_path):
    """巡回だけして項目が空のまま書いたページは、次に抽出するとき LLM に回す。"""
    r = record()
    assert extract.fill(tmp_path, "w", [r], None) == 0
    write_units(tmp_path, INFO, {"131016": [r]})
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM(GOOD))) == 1
    assert again.seido.sections


def test_fill_without_llm_keeps_previous_facts(tmp_path):
    r = record()
    extract.fill(tmp_path, "w", [r], session_of(FakeLLM(GOOD)))
    write_units(tmp_path, INFO, {"131016": [r]})
    again = record()
    extract.fill(tmp_path, "w", [again], None)
    assert again.seido.sections == r.seido.sections


def test_read_sections_round_trip(tmp_path):
    r = record()
    extract.fill(tmp_path, "w", [r], session_of(FakeLLM(GOOD)))
    write_units(tmp_path, INFO, {"131016": [r]})
    md = next((tmp_path / "seido").rglob("*.md"))
    assert read_sections(md) == r.seido.sections


def test_session_times_out_when_gpu_is_busy(tmp_path, monkeypatch):
    import fcntl

    lock = tmp_path / "gpu.lock"
    monkeypatch.setattr(extract, "GPU_LOCK", str(lock))
    monkeypatch.setattr(extract, "GPU_LOCK_WAIT", 0)
    with open(lock, "a") as held:
        fcntl.flock(held, fcntl.LOCK_EX)
        with pytest.raises(TimeoutError, match="GPU"):
            with extract.session():
                pass
