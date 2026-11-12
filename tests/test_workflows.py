"""self-hosted runner を、外部から起動できるワークフローで使っていないこと。

self-hosted runner は自宅 PC で動く。pull_request などで起動するワークフローが使うと、
公開後にフォークからの PR で PC 上の任意のコードが実行されうる。
"""

from pathlib import Path

import yaml

WORKFLOWS = Path(__file__).resolve().parents[1] / ".github" / "workflows"
# self-hosted runner を使ってよいトリガー（リポジトリに書き込める人しか起動できないもの）
TRUSTED = {"schedule", "workflow_dispatch"}


def runs_on_self_hosted(job: dict) -> bool:
    runs_on = job.get("runs-on", "")
    labels = runs_on if isinstance(runs_on, list) else [runs_on]
    return any("self-hosted" in str(label) for label in labels)


def triggers(workflow: dict) -> set[str]:
    # PyYAML は `on:` を True として読む
    on = workflow.get("on", workflow.get(True))
    if isinstance(on, str):
        return {on}
    return set(on or [])


def test_workflows_exist():
    assert list(WORKFLOWS.glob("*.yml"))


def test_self_hosted_only_with_trusted_triggers():
    for path in WORKFLOWS.glob("*.y*ml"):
        workflow = yaml.safe_load(path.read_text(encoding="utf-8"))
        untrusted = triggers(workflow) - TRUSTED
        for name, job in (workflow.get("jobs") or {}).items():
            if runs_on_self_hosted(job):
                assert not untrusted, (
                    f"{path.name} の {name}: self-hosted を {untrusted} で起動できる"
                )
