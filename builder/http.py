"""取得元に負荷をかけないための HTTP ヘルパー。

同じホストへのリクエストは MIN_INTERVAL 秒以上あける。取得元は並列に取るので、
ホストごとのロックで同じホストへのリクエストを 1 本ずつに絞る。

- URL の日本語（山添村の `/life/身体障害者手帳`）はパーセントエンコードしてから送る
- 中間証明書を送らないサーバ（多可町）のために、certs/intermediates.pem の中間証明書を足して
  検証する。足すのは中間証明書だけで、ルートまでの検証は今までどおり OS の証明書で行う
"""

import json
import ssl
import threading
import time
import urllib.parse
import urllib.request
from functools import cache
from pathlib import Path

USER_AGENT = "seido-builder/0.1 (+https://github.com/muroshima/seido-data)"
MIN_INTERVAL = 1.0
TIMEOUT = 120

_last_request: dict[str, float] = {}
_host_locks: dict[str, threading.Lock] = {}
_guard = threading.Lock()
# 時間切れで取り込みを打ち切るときに立てる。立っていたら次のリクエストを送らない
STOP = threading.Event()


# URL に使える ASCII の文字（と、エンコード済みの %）はそのまま残す
URL_SAFE = ":/?#[]@!$&'()*+,;=%~"
INTERMEDIATES = Path(__file__).parent / "certs" / "intermediates.pem"


@cache
def _context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.load_verify_locations(cafile=INTERMEDIATES)
    # 中間証明書を信頼の起点にしない（ルートまで辿れたときだけ通す）
    ctx.verify_flags &= ~getattr(ssl, "VERIFY_X509_PARTIAL_CHAIN", 0)
    return ctx


def _lock(host: str) -> threading.Lock:
    with _guard:
        return _host_locks.setdefault(host, threading.Lock())


def get(url: str, params: dict[str, str] | None = None, retries: int = 3) -> bytes:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    url = urllib.parse.quote(url, safe=URL_SAFE)
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
                with urllib.request.urlopen(req, timeout=TIMEOUT, context=_context()) as res:
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
