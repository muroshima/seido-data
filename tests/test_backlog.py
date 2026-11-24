"""seido fill: 巡回はせず、抽出を見送ったページだけを取り直して LLM に回す。"""

import contextlib
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import pytest
from test_extract import GOOD, PAGE, FakeLLM

from builder import backlog, cli, extract, registry
from builder.model import Record, Seido
from builder.sources import source_info
from builder.store import read_front, write_units

ROOT = Path(__file__).resolve().parents[1]
SID = "chiyoda-teate-josei"
MD = f"seido/13/131016/{SID}/a.md"


def git(root, *args):
    return subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    ).stdout


@pytest.fixture
def repo(tmp_path):
    """前回の巡回で GPU が空かず、項目を取り出していないページが 1 件ある状態。"""
    shutil.copytree(ROOT / "registry", tmp_path / "registry")
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "t")
    git(tmp_path, "config", "user.email", "t@example.invalid")
    entities, sources = registry.load(tmp_path)
    row = next(s for s in sources if s["source_id"] == SID)
    raw = {
        "url": "https://example.invalid/a.html",
        "title": "児童手当",
        "content_sha256": hashlib.sha256(PAGE.encode()).hexdigest(),
        "content_length": len(PAGE),
    }
    seido = Seido(title="児童手当", support=None, url=raw["url"], source_updated=None)
    record = Record(lg_code="131016", lg_name="千代田区", record_id="a", raw=raw, seido=seido)
    write_units(tmp_path, source_info(row, entities), {"131016": [record]})
    git(tmp_path, "add", "--all")
    git(tmp_path, "commit", "-qm", "init")
    return tmp_path


@pytest.fixture
def llm(monkeypatch):
    fake = FakeLLM(GOOD)

    @contextlib.contextmanager
    def session():
        yield fake

    monkeypatch.setattr(extract, "session", session)
    return fake


def test_fills_page_whose_text_is_unchanged(repo, llm, monkeypatch):
    monkeypatch.setattr(backlog, "page_text", lambda url, fmt: PAGE)
    raw_before = (repo / f"raw/{SID}/131016/a.json").read_text()
    assert cli.main(["--root", str(repo), "fill", "--commit"]) == 0
    front = read_front(repo / MD)
    assert front["facts_sha256"] == front["content_sha256"]
    assert "## 対象者" in (repo / MD).read_text()
    assert (repo / f"raw/{SID}/131016/a.json").read_text() == raw_before  # 観測は書き換えない
    assert git(repo, "status", "--porcelain") == ""
    assert "制度の情報を取り出す" in git(repo, "log", "-1", "--format=%s")


def test_skips_page_whose_text_changed_since_crawl(repo, llm, monkeypatch):
    monkeypatch.setattr(backlog, "page_text", lambda url, fmt: PAGE + "（改定）")
    assert cli.main(["--root", str(repo), "fill", "--commit"]) == 0
    assert read_front(repo / MD)["facts_sha256"] is None
    assert llm.calls == []
    assert len(git(repo, "log", "--format=%h").split()) == 1


def test_does_nothing_when_gpu_is_busy(repo, monkeypatch, tmp_path_factory):
    import fcntl

    lock = tmp_path_factory.mktemp("lock") / "gpu.lock"
    monkeypatch.setattr(extract, "GPU_LOCK", str(lock))
    fetched = []
    monkeypatch.setattr(backlog, "page_text", lambda url, fmt: fetched.append(url) or PAGE)
    with open(lock, "a") as held:
        fcntl.flock(held, fcntl.LOCK_EX)  # Kaggle のジョブが使っている
        assert cli.main(["--root", str(repo), "fill", "--commit"]) == 0
    assert fetched == []  # GPU が空いていなければ、ページも取りに行かない
    assert read_front(repo / MD)["facts_sha256"] is None


def test_gives_gpu_back_between_chunks(repo, monkeypatch):
    """CHUNK を過ぎたらロックを手放し、その間に取られていたら残りは次に回す。"""
    entered = []

    @contextlib.contextmanager
    def session():
        if entered:
            raise extract.GPUBusy("Kaggle のジョブが取った")
        entered.append(1)
        yield FakeLLM(GOOD)

    monkeypatch.setattr(extract, "session", session)
    monkeypatch.setattr(backlog, "CHUNK", 0)
    monkeypatch.setattr(backlog, "YIELD_SECONDS", 0)
    monkeypatch.setattr(backlog, "page_text", lambda url, fmt: PAGE)
    with backlog.chunked_session() as llm:
        assert llm() is not None
        assert llm() is None
    assert json.loads((repo / f"raw/{SID}/131016/a.json").read_text())["title"] == "児童手当"
