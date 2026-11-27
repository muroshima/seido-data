"""update.yml の予備の定期実行が、その日の巡回が済んでいるかを見る。

GitHub API の workflow runs（標準入力）から、自分以外で HOURS 時間以内に始まった巡回
（取り消したものを除く）を探し、あれば GITHUB_OUTPUT に skip=true を書く。
"""

import json
import os
import sys
from datetime import UTC, datetime, timedelta

HOURS = 18


def recent(runs: list[dict], run_id: int, now: datetime) -> list[dict]:
    since = now - timedelta(hours=HOURS)
    return [
        r
        for r in runs
        if r["id"] != run_id
        and r["conclusion"] != "cancelled"
        and datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")) > since
    ]


def main() -> None:
    runs = json.load(sys.stdin)["workflow_runs"]
    done = recent(runs, int(os.environ["RUN_ID"]), datetime.now(UTC))
    print(f"{HOURS} 時間以内の巡回: {[r['id'] for r in done] or 'なし'}")
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"skip={'true' if done else 'false'}\n")


if __name__ == "__main__":
    main()
