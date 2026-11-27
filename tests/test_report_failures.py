"""巡回で取り込めなかった取得元を知らせる Issue の本文。"""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "report_failures", Path(__file__).resolve().parents[1] / "scripts" / "report_failures.py"
)
report_failures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report_failures)


def test_body_lists_sources_and_reasons():
    lines = ["kumagaya-sumai-josei\tHTTPError: HTTP Error 404: Not Found", "a\tx | y"]
    text = report_failures.body(lines, "https://example.invalid/run/1", "2026-11-25")
    assert text.startswith("2026-11-25 の巡回で、2 件の取得元を取り込めなかった")
    assert "| `kumagaya-sumai-josei` | HTTPError: HTTP Error 404: Not Found |" in text
    assert "| `a` | x ｜ y |" in text  # 表が崩れないように
    assert text.endswith("ログ: https://example.invalid/run/1")
