"""取得元に負荷をかけないための HTTP ヘルパー。

同じホストへのリクエストは MIN_INTERVAL 秒以上あける。取得元は並列に取るので、
ホストごとのロックで同じホストへのリクエストを 1 本ずつに絞る。
"""

import json
import threading
import time
import urllib.parse
import urllib.request

USER_AGENT = "seido-builder/0.1 (+https://github.com/muroshima/seido-data)"
MIN_INTERVAL = 1.0
TIMEOUT = 120

_last_request: dict[str, float] = {}
_host_locks: dict[str, threading.Lock] = {}
_guard = threading.Lock()
# 時間切れで取り込みを打ち切るときに立てる。立っていたら次のリクエストを送らない
STOP = threading.Event()


def _lock(host: str) -> threading.Lock:
    with _guard:
        return _host_locks.setdefault(host, threading.Lock())


def get(url: str, params: dict[str, str] | None = None, retries: int = 3) -> bytes:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    host = urllib.parse.urlsplit(url).netloc
    with _lock(host):
        for attempt in range(retries):
            if STOP.is_set():
                raise TimeoutError("時間切れで取り込みを打ち切った")
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
