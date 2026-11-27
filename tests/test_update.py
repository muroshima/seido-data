"""seido update: 対応表の取得元を回し、書き出してコミットする流れ。"""

import shutil
import subprocess
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pytest

from builder import cli, registry
from builder.model import Record, Seido
from builder.sources import Fetched

ROOT = Path(__file__).resolve().parents[1]


def rec(lg: str, rid: str) -> Record:
    s = Seido(title=rid, support="金銭", url=None, source_updated=None, sections={"概要": rid})
    return Record(lg_code=lg, lg_name="", record_id=rid, raw={"t": rid}, seido=s)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """registry/ だけを持つ git リポジトリ。取得元は 2 つで、片方は失敗する。"""
    shutil.copytree(ROOT / "registry", tmp_path / "registry")
    run = lambda *a: subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True)  # noqa: E731
    run("init", "-q")
    run("config", "user.name", "t")
    run("config", "user.email", "t@example.invalid")
    run("add", "registry")
    run("commit", "-qm", "init")

    def fetch_ok(row):
        return Fetched(date(2026, 1, 1), {"132101": [rec("132101", "a")]})

    def fetch_ng(row):
        raise OSError("timeout")

    def fetch_outside(row):
        return Fetched(date(2026, 1, 1), {"131016": [rec("131016", "z")]})  # covers は 131148

    loaders = {
        "tokyo-ods-support-132101": SimpleNamespace(fetch=fetch_ok),
        "tokyo-ods-support-132136": SimpleNamespace(fetch=fetch_ng),
        "tokyo-ods-support-131148": SimpleNamespace(fetch=fetch_outside),
    }
    monkeypatch.setattr(cli, "loader_for", lambda row: loaders.get(row["source_id"]))
    return tmp_path, run


def test_one_failure_does_not_stop_others(repo):
    root, run = repo
    ids = ["tokyo-ods-support-132136", "tokyo-ods-support-131148", "tokyo-ods-support-132101"]
    assert cli.main(["--root", str(root), "update", *ids, "--commit"]) == 2
    log = subprocess.run(
        ["git", "log", "-1", "--format=%ad%n%B", "--date=iso"],
        cwd=root,
        capture_output=True,
        text=True,
    ).stdout
    assert log.startswith("2026-01-01 00:00:00 +0900")
    assert "Source: tokyo-ods-support-132101" in log
    md = (root / "seido/13/132101/tokyo-ods-support-132101/a.md").read_text(encoding="utf-8")
    assert "lg_name: 小金井市" in md  # 自治体名は対応表から入れる
    # covers の範囲外を返した取得元は何も書かない
    assert not (root / "seido/13/131016/tokyo-ods-support-131148").exists()


def test_refuses_dirty_index(repo):
    root, run = repo
    (root / "README.md").write_text("x")
    run("add", "README.md")
    assert cli.main(["--root", str(root), "update", "tokyo-ods-support-132101", "--commit"]) == 1
    assert not (root / "seido").exists()


def test_unknown_source_is_rejected(repo):
    root, _ = repo
    assert cli.main(["--root", str(root), "update", "no-such-source"]) == 1


def test_daily_skips_stopped_and_not_ingesting():
    """--daily は「取込中」かつ更新が止まっていない取得元だけを回す。"""
    _, sources = registry.load(ROOT)
    daily = cli.daily_sources(sources)
    assert "tokyo-kosodate-registry" not in daily  # 取込中だが更新停止
    assert "tokyo-hojokin-search" not in daily  # 取込予定
    assert "tokyo-ods-support-131148" not in daily  # 取込中だが更新停止
    assert {"fussa-opendata-kyufu", "taito-teate-josei"} <= set(daily)
    by_id = {s["source_id"]: s for s in sources}
    assert all(by_id[i]["status"] == "取込中" and not cli.stopped_at(by_id[i]) for i in daily)


def test_stopped_source_commits_at_stopped_date(repo, monkeypatch):
    """更新が止まった取得元は、ローダーの観測日ではなく止まった日でコミットする。"""
    root, _ = repo
    stopped = SimpleNamespace(
        fetch=lambda row: Fetched(date(2026, 1, 1), {"131148": [rec("131148", "a")]})
    )
    monkeypatch.setattr(
        cli, "loader_for", lambda row: {"tokyo-ods-support-131148": stopped}.get(row["source_id"])
    )
    assert cli.main(["--root", str(root), "update", "tokyo-ods-support-131148", "--commit"]) == 0
    log = subprocess.run(
        ["git", "log", "-1", "--format=%ad", "--date=short"],
        cwd=root,
        capture_output=True,
        text=True,
    ).stdout.strip()
    assert log == "2025-03-31"


def test_web_sources_are_extracted_regardless_of_publish(repo, monkeypatch):
    """千代田区のように本文の利用が自由な取得元でも、巡回したなら事実を取り出す。"""
    root, _ = repo
    calls = []

    def fill(root_, sid, records, llm_session, deadline=None):
        calls.append(sid)
        return 0

    with_text = rec("131016", "a")
    with_text.source_text = "本文"
    monkeypatch.setattr(cli.extract, "fill", fill)
    monkeypatch.setattr(
        cli,
        "loader_for",
        lambda row: SimpleNamespace(
            fetch=lambda r: (
                Fetched(date(2026, 1, 1), {"131016": [with_text]})
                if r["source_id"] == "chiyoda-teate-josei"
                else Fetched(date(2026, 1, 1), {"132101": [rec("132101", "b")]})
            )
        ),
    )
    ids = ["chiyoda-teate-josei", "tokyo-ods-support-132101"]
    assert cli.main(["--root", str(root), "update", *ids]) == 0
    assert calls == ["chiyoda-teate-josei"]  # 本文を持たない CSV の取り込みは対象外


def test_busy_gpu_writes_crawl_results_and_stops_waiting(repo, monkeypatch):
    """GPU が空かない日は巡回の結果だけを書き、同じ実行のほかの取得元では GPU を待たない。"""
    root, _ = repo
    sessions = []

    def fill(root_, sid, records, llm_session, deadline=None):
        sessions.append((sid, llm_session))
        if llm_session is not None:
            raise cli.extract.GPUBusy("GPU が 3600 秒空かなかった")
        return 0

    def web(lg):
        r = rec(lg, "a")
        r.raw = {"url": "u", "title": "a", "content_sha256": "0", "content_length": 2}
        r.seido.sections = {}
        r.source_text = "本文"
        return Fetched(date(2026, 1, 1), {lg: [r]})

    monkeypatch.setattr(cli.extract, "fill", fill)
    monkeypatch.setattr(
        cli,
        "loader_for",
        lambda row: SimpleNamespace(
            fetch=lambda r: web({"chiyoda-teate-josei": "131016"}.get(r["source_id"], "131024"))
        ),
    )
    ids = ["chiyoda-teate-josei", "chuo-kosodate-teate"]
    assert cli.main(["--root", str(root), "update", *ids, "--extract"]) == 0
    assert [(sid, s is None) for sid, s in sessions] == [
        ("chiyoda-teate-josei", False),  # GPU を待って空かなかった
        ("chiyoda-teate-josei", True),  # 巡回の結果だけを書く
        ("chuo-kosodate-teate", True),  # もう待たない
    ]
    assert (root / "seido/13/131016/chiyoda-teate-josei/a.md").exists()
    assert (root / "seido/13/131024/chuo-kosodate-teate/a.md").exists()


def test_ollama_failure_is_not_treated_as_busy_gpu(repo, monkeypatch):
    """GPU は取れたが Ollama が起動しないなどの失敗は、その取得元の失敗として扱う。"""
    root, _ = repo

    def fill(root_, sid, records, llm_session, deadline=None):
        if llm_session is not None:
            raise TimeoutError("Ollama が起動しない")
        return 0

    r = rec("131016", "a")
    r.source_text = "本文"
    monkeypatch.setattr(cli.extract, "fill", fill)
    monkeypatch.setattr(
        cli,
        "loader_for",
        lambda row: SimpleNamespace(fetch=lambda _: Fetched(date(2026, 1, 1), {"131016": [r]})),
    )
    assert cli.main(["--root", str(root), "update", "chiyoda-teate-josei", "--extract"]) == 2
    assert not (root / "seido").exists()


def test_index_is_committed_with_the_source(repo):
    """制度の一覧（seido/index.csv）は、制度ファイルと同じコミットで更新する。"""
    root, run = repo
    assert cli.main(["--root", str(root), "update", "tokyo-ods-support-132101", "--commit"]) == 0
    files = subprocess.run(
        ["git", "show", "--name-only", "--format=", "HEAD"],
        cwd=root,
        capture_output=True,
        text=True,
    ).stdout.split()
    assert "seido/index.csv" in files
    lines = (root / "seido/index.csv").read_text(encoding="utf-8").splitlines()
    assert lines[0].startswith("path,lg_code,lg_name,title,")
    assert lines[1].startswith(
        "seido/13/132101/tokyo-ods-support-132101/a.md,132101,小金井市,a,金銭,"
    )


def test_repository_index_is_fresh():
    """コミットされている seido/index.csv が制度ファイルと一致すること。"""
    from builder.store import index_csv

    actual = (ROOT / "seido" / "index.csv").read_text(encoding="utf-8")
    assert actual == index_csv(ROOT), "uv run seido index で作り直す"


def test_sources_are_submitted_round_robin_by_host():
    by_id = {
        "a1": {"url": "https://a.example/1"},
        "a2": {"url": "https://a.example/2"},
        "a3": {"url": "https://a.example/3"},
        "b1": {"url": "https://b.example/1"},
        "c1": {"url": "https://c.example/1"},
    }
    assert cli.by_host_round_robin(list(by_id), by_id) == ["a1", "b1", "c1", "a2", "a3"]


def test_sources_not_fetched_in_time_are_left_for_next_run(repo, monkeypatch):
    """実行の上限時間を過ぎたら、取れていない取得元は書き換えずに次の実行に回す。"""
    import threading

    root, run = repo
    release = threading.Event()

    def slow(row):
        release.wait(5)
        return Fetched(date(2026, 1, 1), {"132136": [rec("132136", "s")]})

    loaders = {
        "tokyo-ods-support-132136": SimpleNamespace(fetch=slow),
        "tokyo-ods-support-132101": SimpleNamespace(
            fetch=lambda row: Fetched(date(2026, 1, 1), {"132101": [rec("132101", "a")]})
        ),
    }
    monkeypatch.setattr(cli, "loader_for", lambda row: loaders.get(row["source_id"]))
    monkeypatch.setattr(cli, "RUN_BUDGET", 0.5)
    try:
        ids = ["tokyo-ods-support-132136", "tokyo-ods-support-132101"]
        assert cli.main(["--root", str(root), "update", *ids, "--commit"]) == 0
        assert cli.http.STOP.is_set()
    finally:
        release.set()
        cli.http.STOP.clear()
    assert not (root / "seido/13/132136").exists()
    assert (root / "seido/13/132101/tokyo-ods-support-132101/a.md").exists()


@pytest.mark.parametrize(
    ("before", "after", "drop"),
    [(0, 0, False), (1, 0, True), (3, 1, False), (6, 3, False), (6, 2, True), (49, 0, True)],
)
def test_sharp_drop(before, after, drop):
    assert cli.sharp_drop(before, after) is drop


def test_sharp_drop_stops_writing_and_is_reported(repo, monkeypatch, tmp_path_factory):
    """作り替えたサイトが空の一覧を返しても、前回の制度をまとめて削除しない。"""
    root, run = repo
    sid = "tokyo-ods-support-132101"
    many = Fetched(date(2026, 1, 1), {"132101": [rec("132101", c) for c in "abcdef"]})
    empty = Fetched(date(2026, 1, 2), {"132101": []})
    fetched = iter([many, empty, empty])
    monkeypatch.setattr(
        cli, "loader_for", lambda row: SimpleNamespace(fetch=lambda row: next(fetched))
    )
    failed_file = tmp_path_factory.mktemp("out") / "failed.tsv"
    monkeypatch.setattr(cli, "FAILED_FILE", str(failed_file))
    assert cli.main(["--root", str(root), "update", sid, "--commit"]) == 0
    assert cli.main(["--root", str(root), "update", sid, "--commit"]) == 2
    assert len(list((root / "seido/13/132101" / sid).glob("*.md"))) == 6
    assert failed_file.read_text(encoding="utf-8").startswith(
        f"{sid}\tSharpDrop: 制度ページが前回 6 件から 0 件"
    )
    # 意図した減少なら書き込める
    args = ["--root", str(root), "update", sid, "--commit", "--allow-drop", sid]
    assert cli.main(args) == 0
    assert not list((root / "seido/13/132101" / sid).glob("*.md"))
