"""CKAN のオープンデータカタログ（東京都など）からデータセットのファイルを引く。"""

import urllib.parse

from . import http


def resources(dataset_url: str) -> list[dict]:
    """https://<host>/dataset/<id> のデータセットに載っているファイル（format, url, name）。"""
    parts = urllib.parse.urlsplit(dataset_url)
    path = parts.path.rstrip("/")
    if "/dataset/" not in path:
        raise ValueError(f"CKAN のデータセット URL ではない: {dataset_url}")
    dataset_id = path.rsplit("/", 1)[1]
    api = f"{parts.scheme}://{parts.netloc}/api/3/action/package_show"
    res = http.get_json(api, {"id": dataset_id})
    if not res.get("success"):
        raise RuntimeError(f"{dataset_url}: {res.get('error')}")
    return res["result"]["resources"]
