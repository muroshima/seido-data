"""巡回で取り込めなかった取得元を、Issue で知らせる。

update.yml が、`seido update` の書き出した失敗の一覧（SEIDO_FAILED_FILE。取得元と理由の
タブ区切り）を渡して呼ぶ。ラベル LABEL の開いた Issue があればコメントを足し、無ければ
Issue を立てる。直したら Issue を閉じる。次に失敗したときは新しい Issue が立つ。
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

LABEL = "巡回の失敗"
JST = timezone(timedelta(hours=9))


def body(lines: list[str], run_url: str, today: str) -> str:
    rows = []
    for line in lines:
        sid, _, reason = line.partition("\t")
        rows.append(f"| `{sid}` | {reason.replace('|', '｜')} |")
    return "\n".join(
        [
            f"{today} の巡回で、{len(rows)} 件の取得元を取り込めなかった"
            "（その回は書き換えていない）。",
            "",
            "| 取得元 | 理由 |",
            "|---|---|",
            *rows,
            "",
            f"ログ: {run_url}",
        ]
    )


def api(method: str, path: str, data: dict | None = None):
    req = urllib.request.Request(
        f"{os.environ['GITHUB_API_URL']}/repos/{os.environ['GITHUB_REPOSITORY']}{path}",
        method=method,
        data=None if data is None else json.dumps(data).encode(),
        headers={
            "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def main(path: str) -> None:
    if not os.path.exists(path):
        return
    lines = [line for line in open(path, encoding="utf-8").read().splitlines() if line]
    if not lines:
        return
    today = datetime.now(JST).date().isoformat()
    text = body(lines, os.environ["RUN_URL"], today)
    try:
        api("POST", "/labels", {"name": LABEL, "color": "d93f0b"})
    except urllib.error.HTTPError as e:
        if e.code != 422:  # 422 は既にある
            raise
    label = urllib.request.quote(LABEL)
    issues = api("GET", f"/issues?state=open&labels={label}&per_page=1")
    if issues:
        api("POST", f"/issues/{issues[0]['number']}/comments", {"body": text})
        print(f"#{issues[0]['number']} にコメントした")
    else:
        issue = api(
            "POST",
            "/issues",
            {"title": "巡回で取り込めなかった取得元がある", "body": text, "labels": [LABEL]},
        )
        print(f"#{issue['number']} を立てた")


if __name__ == "__main__":
    main(sys.argv[1])
