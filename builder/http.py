"""取得元に負荷をかけないための HTTP ヘルパー。

同じホストへのリクエストは MIN_INTERVAL 秒以上あける。
"""

import json
import time
import urllib.parse
import urllib.request

USER_AGENT = "seido-builder/0.1 (+https://github.com/muroshima/seido-data)"
MIN_INTERVAL = 1.0
TIMEOUT = 120

_last_request: dict[str, float] = {}


def get(url: str, params: dict[str, str] | None = None, retries: int = 3) -> bytes:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    host = urllib.parse.urlsplit(url).netloc
    for attempt in range(retries):
        wait = _last_request.get(host, 0) + MIN_INTERVAL - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
                return res.read()
        except OSError:
            if attempt == retries - 1:
                raise
            time.sleep(5 * (attempt + 1))
        finally:
            _last_request[host] = time.monotonic()
    raise AssertionError("unreachable")


def get_json(url: str, params: dict[str, str] | None = None):
    return json.loads(get(url, params))
