"""seido trial / regress: 候補の試し取りと採否、取り込み方を変えたときの新旧比較。"""

import json
import urllib.error
from datetime import date
from types import SimpleNamespace

import pytest
from test_update import rec

from builder import cli, http, trial
from builder.sources import Fetched


def row(sid, fmt="html", status="取込予定", note=""):
    return {"source_id": sid, "format": fmt, "status": status, "checked": "", "note": note}


@pytest.mark.parametrize(
    ("title", "program"),
    [("児童手当の支給", True), ("審議会の開催", False), ("成年後見制度", True), ("組織", False)],
)
def test_is_program(title, program):
    assert trial.is_program(title) is program


def test_verdict():
    ok = trial.Result("a", ["児童手当", "医療費の助成", "おむつの支給"])
    check = trial.Result("b", ["児童手当", "医療費の助成", "お知らせ", "組織"])
    ng = trial.Result("c", ["お知らせ", "組織", "児童手当"])
    assert (ok.verdict("html"), check.verdict("html"), ng.verdict("html")) == ("OK", "CHECK", "NG")
    assert trial.Result("d", error="404").verdict("html") == "NG"
    # 1 ページだけの行は、題名に制度らしい語が無くても取れれば取り込む
    assert trial.Result("e", ["思いやり駐車場"]).verdict("html-page") == "OK"


def test_apply_adopts_and_replaces_previous_trial_note():
    registry_rows = [row("a", note="一覧 / 2026-11-21 の試行で5ページ・制度らしい題名20%")]
    registry_rows.append(row("bad"))
    tried = [row("a"), row("new"), row("bad")]
    results = [
        trial.Result("a", ["児童手当", "医療費の助成"]),
        trial.Result("new", ["お知らせ"]),
        trial.Result("bad", error="HTTPError: 404"),
    ]
    out = {
        r["source_id"]: r for r in trial.apply(registry_rows, tried, results, date(2026, 11, 27))
    }
    assert out["a"]["status"] == "取込中"
    assert out["a"]["note"] == "一覧 / 2026-11-27 の試行で2ページ・制度らしい題名100%"
    assert "new" not in out  # 対応表に無い行は、取り込めるものだけ足す
    assert out["bad"]["note"] == "2026-11-27 の試行で失敗（HTTPError: 404）"


def test_trial_command_does_not_write(tmp_path, monkeypatch, capsys):
    root = tmp_path
    (root / "registry").mkdir()
    sources = cli.Path(__file__).resolve().parents[1] / "registry"
    for name in ("sources.csv", "entities.csv"):
        (root / "registry" / name).write_text((sources / name).read_text())
    fetched = Fetched(date(2026, 1, 1), {"132101": [rec("132101", "teate")]})
    fetched.units["132101"][0].seido.title = "児童手当"
    monkeypatch.setattr(trial, "loader_for", lambda r: SimpleNamespace(fetch=lambda r: fetched))
    before = (root / "registry/sources.csv").read_text()
    assert cli.main(["--root", str(root), "trial", "tokyo-ods-support-132101"]) == 0
    assert "OK\ttokyo-ods-support-132101\tn=1" in capsys.readouterr().out
    assert (root / "registry/sources.csv").read_text() == before
    assert not (root / "seido").exists()


def test_cache_http_reads_the_same_bytes_twice(tmp_path, monkeypatch):
    calls = []

    def real_get(url, params=None, retries=3):
        calls.append(url)
        if url.endswith("gone"):
            raise urllib.error.HTTPError(url, 404, "nf", {}, None)
        return b"page"

    monkeypatch.setattr(http, "get", real_get)
    trial.cache_http(tmp_path)
    for _ in range(2):
        assert http.get("https://example.invalid/a") == b"page"
        with pytest.raises(urllib.error.HTTPError):
            http.get("https://example.invalid/gone")
    assert calls == ["https://example.invalid/a", "https://example.invalid/gone"]


def test_compare():
    old = {
        "a": {"pages": {"x": ["児童手当", "h1"], "y": ["医療", "h2"]}},
        "b": {"pages": {"x": ["t", "h"]}},
        "c": {"error": "HTTPError: 404"},
    }
    new = {
        "a": {"pages": {"x": ["児童手当の支給", "h1"], "z": ["医療", "h3"]}},
        "b": {"pages": {"x": ["t", "h"]}},
        "c": {"pages": {}},
    }
    lines = trial.compare(old, new)
    assert len(lines) == 2
    assert lines[0].startswith("a: 追加 1 ['z'] / 削除 1 ['y'] / 題名 1")
    assert lines[1] == "c: 旧 HTTPError: 404 / 新 ok"


def test_regress_command_writes_fingerprints(tmp_path, monkeypatch):
    fetched = Fetched(date(2026, 1, 1), {"132101": [rec("132101", "a")]})
    fetched.units["132101"][0].raw.update(title="児童手当", content_sha256="h")
    monkeypatch.setattr(trial, "loader_for", lambda r: SimpleNamespace(fetch=lambda r: fetched))
    monkeypatch.setattr(trial, "cache_http", lambda d: None)
    out = tmp_path / "new.json"
    root = cli.Path(__file__).resolve().parents[1]
    args = ["--root", str(root), "regress", "tokyo-ods-support-132101"]
    assert cli.main([*args, "--cache", str(tmp_path / "c"), "--out", str(out)]) == 0
    assert json.loads(out.read_text()) == {
        "tokyo-ods-support-132101": {"pages": {"a": ["児童手当", "h"]}}
    }
