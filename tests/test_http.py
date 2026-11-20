"""取得元を並列に取っても、同じホストへは間隔をあけて 1 本ずつ送ること。"""

import threading
import time
from contextlib import contextmanager

from builder import http


def test_same_host_is_serialized_and_other_hosts_run_in_parallel(monkeypatch):
    monkeypatch.setattr(http, "MIN_INTERVAL", 0.2)
    monkeypatch.setattr(http, "_last_request", {})
    calls: list[tuple[str, float, float]] = []

    @contextmanager
    def fake_urlopen(req, timeout):
        start = time.monotonic()
        time.sleep(0.05)
        calls.append((req.full_url.split("/")[2], start, time.monotonic()))
        yield type("R", (), {"read": lambda self: b"ok"})()

    monkeypatch.setattr(http.urllib.request, "urlopen", fake_urlopen)
    urls = [f"https://a.example/{i}" for i in range(3)] + [
        f"https://b.example/{i}" for i in range(3)
    ]
    threads = [threading.Thread(target=http.get, args=(u,)) for u in urls]
    begin = time.monotonic()
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    for host in ("a.example", "b.example"):
        spans = sorted((s, e) for h, s, e in calls if h == host)
        assert len(spans) == 3
        # 前のリクエストが終わってから MIN_INTERVAL 以上あけて次を送る
        assert all(nxt[0] - prev[1] >= 0.19 for prev, nxt in zip(spans, spans[1:], strict=False))
    # 2 つのホストは並行して進むので、1 本ずつ順に送るより短い（6 本 × 0.25 秒 ≒ 1.5 秒）
    assert time.monotonic() - begin < 1.0
