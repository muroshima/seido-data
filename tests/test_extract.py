import contextlib
import time

import pytest

from builder import extract
from builder.model import SourceInfo
from builder.sources import webindex
from builder.store import read_sections, write_units

PAGE = (
    "児童手当は、中学生までの子どもを育てている方に支給します。"
    "支給額は、3歳未満は月額15,000円、3歳以上は月額10,000円です。"
    "申請は区役所の子ども家庭課の窓口で受け付けています。"
    "出生や転入の日の翌日から15日以内に申請してください。"
    "申請が遅れると、遅れた月分の手当を受けられなくなりますのでご注意ください。"
    "公務員の方は勤務先から支給されますので、勤務先にお問い合わせください。"
    "所得の状況によっては支給額が変わることがあります。"
)
assert len(PAGE) >= 200
GOOD = {
    "対象者": "中学生までの子どもを育てる人",
    "支援内容": "3歳未満は月額15,000円、3歳以上は月額10,000円",
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
    assert facts.sections == {k: v for k, v in GOOD.items() if v}


def test_ungrounded_fields_are_dropped():
    """ページに無い一般論（「継続的」「自治体に問い合わせる」）で埋めた項目は捨てる。"""
    answer = {**GOOD, "期間": "継続的", "問い合わせ": "自治体または市区町村に問い合わせる"}
    facts = extract.extract(FakeLLM(answer), "児童手当", PAGE)
    assert "期間" not in facts.sections and "問い合わせ" not in facts.sections
    assert facts.sections["支援内容"] == GOOD["支援内容"]


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


def test_fill_retries_pages_crawled_without_extraction(tmp_path):
    """巡回だけして項目が空のまま書いたページは、次に抽出するとき LLM に回す。"""
    r = record()
    assert extract.fill(tmp_path, "w", [r], None) == 0
    write_units(tmp_path, INFO, {"131016": [r]})
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM(GOOD))) == 1
    assert again.seido.sections


def test_fill_does_not_retry_pages_with_no_facts(tmp_path):
    """LLM に回して項目が 1 つも取れなかったページは、本文が同じなら次は回さない。"""
    r = record()
    empty = dict.fromkeys(GOOD, "")
    assert extract.fill(tmp_path, "w", [r], session_of(FakeLLM(empty))) == 1
    assert r.seido.sections == {}
    write_units(tmp_path, INFO, {"131016": [r]})
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM())) == 0


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
        with pytest.raises(extract.GPUBusy):
            with extract.session():
                pass


def test_short_pages_are_not_sent_to_llm(tmp_path):
    """外部へのリンクを置いただけの短いページは LLM に回さず、seido/ に出さない。"""
    r = record(text="日本政策金融公庫の教育ローンのページへ移動します。")
    assert extract.fill(tmp_path, "w", [r], session_of(FakeLLM())) == 0
    assert r.seido is None


def test_changed_page_without_llm_keeps_stale_facts_until_next_extraction(tmp_path):
    """本文が変わっても抽出なしの実行では項目を消さず、次の抽出で取り出し直す。"""
    r = record()
    extract.fill(tmp_path, "w", [r], session_of(FakeLLM(GOOD)))
    write_units(tmp_path, INFO, {"131016": [r]})
    old_sha = r.raw["content_sha256"]

    changed_text = PAGE + "令和8年4月から所得制限をなくしました。"
    crawl_only = record(text=changed_text)
    assert extract.fill(tmp_path, "w", [crawl_only], None) == 0
    assert crawl_only.seido.sections == r.seido.sections  # 消えない
    assert crawl_only.seido.facts_sha256 == old_sha  # 古い本文から取り出したまま
    write_units(tmp_path, INFO, {"131016": [crawl_only]})

    later = record(text=changed_text)
    assert extract.fill(tmp_path, "w", [later], session_of(FakeLLM(GOOD))) == 1
    assert later.seido.facts_sha256 == later.raw["content_sha256"]


def test_full_text_source_does_not_re_extract_unchanged_pages(tmp_path):
    """publish=本文 の取得元（千代田区）でも、保存して読み戻したあと同じ本文なら LLM を呼ばない。"""
    full = SourceInfo(name="w", title="t", url="u", license="CC BY", attribution="a")
    r = record()
    extract.fill(tmp_path, "w", [r], session_of(FakeLLM(GOOD)))
    write_units(tmp_path, full, {"131016": [r]})
    again = record()
    assert extract.fill(tmp_path, "w", [again], session_of(FakeLLM())) == 0
    assert again.seido.sections == r.seido.sections


def test_fill_stops_at_deadline_and_leaves_rest_for_next_run(tmp_path):
    """上限時間を過ぎたら残りのページは取り出さず、次の実行に回す。"""
    llm = FakeLLM(GOOD)
    r = record()
    assert extract.fill(tmp_path, "w", [r], session_of(llm), time.monotonic() - 1) == 0
    assert llm.calls == [] and r.seido.facts_sha256 is None
    # 上限前なら取り出す
    assert extract.fill(tmp_path, "w", [r], session_of(llm), time.monotonic() + 60) == 1
