"""update.yml の予備の定期実行が、その日の巡回が済んでいるかを見る。

自分以外で HOURS 時間以内に始まった update.yml の実行のうち、update ジョブが実際に動いたもの
（見送り・取り消しでないもの）があれば、GITHUB_OUTPUT に skip=true を書く。guard で見送った
予備の実行は数えない。API が失敗したときは skip=false にする（巡回を飛ばすより、重ねるほうがよい）。
"""

import json
import os
import urllib.request
from datetime import UTC, datetime, timedelta

HOURS = 12
NOT_RUN = {"skipped", "cancelled"}


def api(path: str) -> dict:
    req = urllib.request.Request(
        f"{os.environ['GITHUB_API_URL']}/repos/{os.environ['GITHUB_REPOSITORY']}{path}",
        headers={"Authorization": f"Bearer {os.environ['GH_TOKEN']}"},
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def recent(runs: list[dict], run_id: int, now: datetime) -> list[dict]:
    """HOURS 時間以内に始まった、自分以外の取り消していない実行。"""
    since = now - timedelta(hours=HOURS)
    return [
        r
        for r in runs
        if r["id"] != run_id
        and r["conclusion"] != "cancelled"
        and datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")) > since
    ]


def crawled(jobs: list[dict]) -> bool:
    """update ジョブが実際に動いた（動いている）か。"""
    return any(j["name"] == "update" and j["conclusion"] not in NOT_RUN for j in jobs)


def main() -> None:
    try:
        runs = api("/actions/workflows/update.yml/runs?per_page=20")["workflow_runs"]
        done = [
            r["id"]
            for r in recent(runs, int(os.environ["RUN_ID"]), datetime.now(UTC))
            if crawled(api(f"/actions/runs/{r['id']}/jobs")["jobs"])
        ]
    except Exception as e:  # noqa: BLE001
        print(f"巡回の有無を確かめられなかったので、巡回する（{e}）")
        done = []
    print(f"{HOURS} 時間以内の巡回: {done or 'なし'}")
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"skip={'true' if done else 'false'}\n")


if __name__ == "__main__":
    main()
