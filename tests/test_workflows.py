"""自宅 PC の self-hosted runner を、外部から起動できるワークフローで使っていないこと。

self-hosted runner は自宅 PC で動く。pull_request などで起動するワークフローが使うと、
公開後にフォークからの PR で PC 上の任意のコードが実行されうる。

runner には self-hosted・Linux・X64・seido のラベルが付いていて、どれを指定しても選ばれうる。
だから「危ないラベルを禁止する」のではなく、信頼できないトリガーのジョブには GitHub が用意する
ランナーのラベルだけを許す。式（${{ }}）での指定は中身が分からないので許さない。
"""

import re
from pathlib import Path

import pytest
import yaml

WORKFLOWS = Path(__file__).resolve().parents[1] / ".github" / "workflows"
# self-hosted runner を使ってよいトリガー（リポジトリに書き込める人しか起動できないもの）
TRUSTED = {"schedule", "workflow_dispatch"}
GITHUB_HOSTED = re.compile(r"^(ubuntu|windows|macos)-[0-9a-z.-]+$")


def github_hosted_only(job: dict) -> bool:
    runs_on = job.get("runs-on")
    if isinstance(runs_on, str):
        labels = [runs_on]
    elif isinstance(runs_on, list):
        labels = runs_on
    else:
        return False  # group 指定（dict）や未指定は、どのランナーか確かめられない
    return bool(labels) and all(GITHUB_HOSTED.match(str(label)) for label in labels)


def triggers(workflow: dict) -> set[str]:
    # PyYAML は `on:` を True として読む
    on = workflow.get("on", workflow.get(True))
    if isinstance(on, str):
        return {on}
    return set(on or [])


def check(workflow: dict) -> list[str]:
    untrusted = triggers(workflow) - TRUSTED
    if not untrusted:
        return []
    return [
        f"{name}: {sorted(untrusted)} で起動できるのに runs-on が GitHub のランナーに限られていない"
        for name, job in (workflow.get("jobs") or {}).items()
        if not github_hosted_only(job)
    ]


def test_workflows_exist():
    assert list(WORKFLOWS.glob("*.yml"))


@pytest.mark.parametrize("path", sorted(WORKFLOWS.glob("*.y*ml")), ids=lambda p: p.name)
def test_self_hosted_only_with_trusted_triggers(path):
    assert check(yaml.safe_load(path.read_text(encoding="utf-8"))) == []


@pytest.mark.parametrize(
    "runs_on",
    [
        "seido",
        ["seido"],
        "Linux",
        ["self-hosted", "seido"],
        "${{ matrix.runner }}",
        {"group": "home"},
        [],
    ],
)
def test_check_rejects_non_github_hosted(runs_on):
    workflow = {True: {"pull_request": None}, "jobs": {"j": {"runs-on": runs_on}}}
    assert check(workflow)


def test_check_allows_github_hosted_and_trusted():
    assert check({True: ["pull_request"], "jobs": {"j": {"runs-on": "ubuntu-latest"}}}) == []
    assert check({True: {"schedule": []}, "jobs": {"j": {"runs-on": ["seido"]}}}) == []
