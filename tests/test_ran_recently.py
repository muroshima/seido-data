"""update.yml の予備の定期実行は、18 時間以内に別の巡回があれば何もしない。"""

import importlib.util
from datetime import UTC, datetime
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "ran_recently", Path(__file__).resolve().parents[1] / "scripts" / "ran_recently.py"
)
ran_recently = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ran_recently)

NOW = datetime(2026, 11, 27, 18, 30, tzinfo=UTC)  # 03:30 JST


def run(id, created_at, conclusion=None):
    return {"id": id, "created_at": created_at, "conclusion": conclusion}


def test_skips_when_kicked_run_started_today():
    runs = [run(2, "2026-11-27T18:23:00Z"), run(1, "2026-11-27T18:23:10Z", "success")]
    assert [r["id"] for r in ran_recently.recent(runs, 2, NOW)] == [1]


def test_runs_when_last_run_was_yesterday():
    runs = [run(2, "2026-11-27T18:23:00Z"), run(1, "2026-11-26T18:23:00Z", "success")]
    assert ran_recently.recent(runs, 2, NOW) == []


def test_cancelled_run_does_not_count():
    runs = [run(2, "2026-11-27T18:23:00Z"), run(1, "2026-11-27T18:00:00Z", "cancelled")]
    assert ran_recently.recent(runs, 2, NOW) == []


def test_failed_run_counts():
    # 一部の取得元が失敗しても、取れた分はコミットしている。同じ日にもう一度は回さない
    runs = [run(2, "2026-11-27T18:23:00Z"), run(1, "2026-11-27T18:00:00Z", "failure")]
    assert [r["id"] for r in ran_recently.recent(runs, 2, NOW)] == [1]
