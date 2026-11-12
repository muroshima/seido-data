"""制度ページの本文から、制度の情報（事実）だけをローカル LLM で取り出す。

publish が「事実」の取得元で使う。取り出した項目が原文の書き写しにならないよう、
原文と長く一致した項目は 1 度だけ言い換えを頼み、それでも一致すれば空にする。

LLM は自宅 PC の Ollama。GPU は Kaggle のジョブと共有なので、GPU のロック
（/tmp/kaggle-gpu.lock）を取ってからサーバーを起動し、終わったら止める。
"""

import contextlib
import fcntl
import json
import os
import re
import subprocess
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from .model import FACT_MAX_CHARS, FACT_SECTIONS, VERBATIM_LIMIT, longest_common_run

MODEL = os.environ.get("SEIDO_LLM_MODEL", "qwen3:8b-q4_K_M")
OLLAMA_BIN = os.environ.get("SEIDO_OLLAMA_BIN", str(Path.home() / ".local/ollama/bin/ollama"))
OLLAMA_HOST = os.environ.get("SEIDO_OLLAMA_HOST", "127.0.0.1:11435")
GPU_LOCK = os.environ.get("SEIDO_GPU_LOCK", "/tmp/kaggle-gpu.lock")
GPU_LOCK_WAIT = int(os.environ.get("SEIDO_GPU_LOCK_WAIT", str(2 * 3600)))
MAX_INPUT_CHARS = 8000
# これより本文が短いページ（外部へのリンクを置いただけのページなど）は LLM に回さない。
# 小さなモデルは、書かれていないことを一般論で埋めてしまう
MIN_INPUT_CHARS = 200

FIELDS = {
    "対象者": "誰が対象か。年齢・所得・居住などの条件",
    "支援内容": "何がもらえるか・何が減るか。金額・割合・上限",
    "期間": "申請・受付の期間や締切。対象となる期間",
    "利用方法": "どこに・どうやって申請するか。主な必要書類",
    "問い合わせ": "担当の部署名と電話番号",
}
SYSTEM = (
    "あなたは自治体の支援制度のページから事実だけを取り出す係です。"
    "原文の文章をそのまま写さず、短い要点に言い換えてください。"
    f"各項目は {FACT_MAX_CHARS // 2} 字以内。"
    "ページに書かれていないことは必ず空文字にし、推測で補わない。"
    "「自治体に問い合わせる」「継続的」「各機関」のような、どの制度にも当てはまる一般論で埋めない。"
)
SCHEMA = {
    "type": "object",
    "properties": {k: {"type": "string", "description": v} for k, v in FIELDS.items()},
    "required": list(FIELDS),
}


@dataclass
class Facts:
    sections: dict[str, str]


class Ollama:
    def __init__(self, host: str = OLLAMA_HOST, model: str = MODEL) -> None:
        self.url = f"http://{host}/api/chat"
        self.model = model

    def ask(self, title: str, text: str, note: str = "") -> dict:
        prompt = f"制度名: {title}\n\nページ本文:\n{text[:MAX_INPUT_CHARS]}"
        if note:
            prompt += f"\n\n注意: {note}"
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
            ],
            "format": SCHEMA,
            "stream": False,
            "think": False,
            "options": {"temperature": 0},
        }
        req = urllib.request.Request(
            self.url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=600) as res:
            return json.loads(json.loads(res.read())["message"]["content"])


def extract(llm, title: str, text: str) -> Facts:
    """1 ページ分。書き写しになった項目は言い換えを頼み直し、それでもだめなら空にする。"""
    answer = llm.ask(title, text)
    copied = verbatim_fields(answer, text)
    if copied:
        retry = llm.ask(
            title,
            text,
            note=f"前の回答の {'・'.join(copied)} が原文の書き写しでした。"
            "原文と違う言葉で短く要約してください。",
        )
        answer.update({k: retry.get(k, "") for k in copied})
    sections = {}
    for key in FACT_SECTIONS:
        value = str(answer.get(key) or "").strip()[:FACT_MAX_CHARS]
        if value and longest_common_run(value, text) < VERBATIM_LIMIT and grounded(value, text):
            sections[key] = value
    return Facts(sections=sections)


TERM = re.compile(r"[一-龥々ァ-ヶー]{2,}|[0-9０-９][0-9０-９,，.]*")


def grounded(value: str, text: str) -> bool:
    """項目に含まれる語の半分以上が原文に出てくるか。

    小さなモデルは、ページに書かれていない一般論（「継続的」「自治体に問い合わせる」など）で
    項目を埋めることがある。原文に根拠の無い項目は捨てる。
    """
    terms = TERM.findall(value)
    if not terms:
        return False
    found = sum(1 for t in terms if t.replace(",", "").replace("，", "") in text.replace(",", ""))
    return found * 2 >= len(terms)


def verbatim_fields(answer: dict, text: str) -> list[str]:
    return [
        k
        for k in FACT_SECTIONS
        if longest_common_run(str(answer.get(k) or ""), text) >= VERBATIM_LIMIT
    ]


@contextlib.contextmanager
def session():
    """GPU のロックを取り、Ollama を起動して Ollama クライアントを渡す。抜けるときに止める。"""
    with open(GPU_LOCK, "a") as lock:
        deadline = time.monotonic() + GPU_LOCK_WAIT
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() > deadline:
                    raise TimeoutError(
                        f"GPU が {GPU_LOCK_WAIT} 秒空かなかった（{GPU_LOCK}）"
                    ) from None
                time.sleep(30)
        server = subprocess.Popen(
            [OLLAMA_BIN, "serve"],
            env={**os.environ, "OLLAMA_HOST": OLLAMA_HOST},
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            wait_ready(f"http://{OLLAMA_HOST}/api/version")
            yield Ollama()
        finally:
            server.terminate()
            server.wait(timeout=60)


def wait_ready(url: str, timeout: float = 60) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            urllib.request.urlopen(url, timeout=5).close()
            return
        except OSError:
            time.sleep(1)
    raise TimeoutError(f"Ollama が起動しない（{url}）")


def fill(root: Path, source_name: str, records: list, llm_session=session) -> int:
    """事実だけの取得元のレコードに、制度の情報を埋める。LLM に回した件数を返す。

    項目をどの本文から取り出したかを facts_sha256 に持つ。今の本文と同じなら前回の項目を使い、
    新しいページ・本文が変わったページ・まだ取り出していないページだけを LLM に回す。
    llm_session が None なら LLM は呼ばず、前回の項目と facts_sha256 をそのまま残す
    （項目は古いままだが消えない。次に LLM を使うときに取り出し直す）。
    一覧ページからリンクされたページは制度の案内として扱う。本文がほとんど無いページだけは
    seido を None にする（raw/ にだけ残る）。
    """
    from .store import read_front, read_sections, seido_dir

    todo = []
    for r in records:
        if r.seido is None:
            continue
        if len(r.source_text or "") < MIN_INPUT_CHARS:
            r.seido = None  # 本文がほとんど無い。制度の案内として扱わない
            continue
        md_path = seido_dir(root, source_name, r.lg_code) / f"{r.record_id}.md"
        if md_path.exists():
            r.seido.sections = read_sections(md_path)
            r.seido.facts_sha256 = read_front(md_path).get("facts_sha256")
        if r.seido.sections and r.seido.facts_sha256 == r.raw["content_sha256"]:
            continue
        todo.append(r)
    if not todo or llm_session is None:
        return 0
    with llm_session() as llm:
        for r in todo:
            r.seido.sections = extract(llm, r.raw["title"], r.source_text or "").sections
            r.seido.facts_sha256 = r.raw["content_sha256"]
    return len(todo)
