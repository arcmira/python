"""A local fake of api.arcmira.com/v1 for the SDK tests.

Bodies come from fixtures/v1.json, which the private monorepo derives from the OpenAPI document;
the mutations below are the cases the tests assert on (ids, paging, a plan gate, a 404, an echoed write).
"""

from __future__ import annotations

import copy
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable
from urllib.parse import parse_qs, urlsplit

FIXTURES = json.loads((Path(__file__).parent / "fixtures" / "v1.json").read_text())


def body(op: str) -> Any:
    return copy.deepcopy(FIXTURES[op]["body"])


def gate_body() -> dict:
    e = copy.deepcopy(FIXTURES["error"])
    e["error"].update(
        type="quota_exceeded",
        code="usage_limit_exceeded",
        message="Momentum needs a Pro plan.",
        gate="plan",
        unlock={"tier": "pro", "url": "https://arcmira.com/pricing?src=sdk", "offer": None},
        doc_url="https://arcmira.com/docs/errors#usage_limit_exceeded",
        request_id="req_gate",
    )
    return e


def not_found_body(code: str, message: str) -> dict:
    e = copy.deepcopy(FIXTURES["error"])
    e["error"].update(type="not_found", code=code, message=message, doc_url=f"https://arcmira.com/docs/errors#{code}", request_id="req_404")
    return e


def _search(m, q, _j):
    b = body("search_transcripts")
    b["query"] = q.get("q", [""])[0]
    b["chunks"][0]["text"] = f"{b['query']} on air"
    b["chunks"][0]["watchUrl"] = "https://arcmira.com/watch?v=dQw4w9WgXcQ&t=1"
    return 200, b


def _entities(m, q, _j):
    b = body("search_entities")
    b["data"][0].update(id="ent_14", name=q.get("q", [""])[0], type="organization", suggested=True, page="https://arcmira.com/org/ramp")
    return 200, b


def _mentions(m, q, _j):
    b = body("list_mentions")
    second = q.get("cursor", [None])[0] == "c2"
    row = b["data"][0]
    b["data"] = [dict(copy.deepcopy(row), id=i) for i in (["men_3"] if second else ["men_1", "men_2"])]
    b["has_more"] = not second
    b["next_cursor"] = None if second else "c2"
    return 200, b


def _momentum(m, _q, _j):
    return (402, gate_body()) if m.group(1) == "ent_gated" else (200, body("get_entity_momentum"))


def _recommendations(m, q, _j):
    if m.group(1) == "ent_gated":
        return 402, gate_body()
    b = body("list_entity_recommendations")
    cls = q.get("mention_class", [None])[0]
    b["data"][0]["mention_class"] = cls if cls and cls != "all" else "endorsement"
    b["data"][0]["verbatim_quote"] = "I think Ramp does this brilliantly."
    b["has_more"] = False
    b["next_cursor"] = None
    return 200, b


def _transcript(m, _q, _j):
    if m.group(1) == "missingvid0":
        return 404, not_found_body("transcript_unavailable", "No transcript for this video.")
    b = body("get_transcript")
    b["lines"] = [{"start": 0, "end": 4, "text": "Welcome back to the show."}, {"start": 4, "end": 9, "text": "Today we talk about agent payments."}]
    return 200, b


def _create_monitor(_m, _q, j):
    b = body("create_monitor")
    b["monitor"]["name"] = (j or {}).get("name", "")
    return FIXTURES["create_monitor"]["status"], b


def _submit_transcription(_m, _q, j):
    b = body("submit_transcription")
    b["request"].update({"id": "2f2b4a3e-8d1c-4c8e-9a0f-1b2c3d4e5f60", "videoId": (j or {}).get("videoId", "")})
    return FIXTURES["submit_transcription"]["status"], b


def _transcription_status(m, _q, _j):
    b = body("get_transcription")
    b.update({"id": m.group(1), "status": "transcribing", "nextPollSeconds": 30})
    return 200, b


def _person_topics(m, _q, _j):
    return (404, not_found_body("entity_not_found", "Entity not found")) if m.group(1) == "nobody" else (200, body("list_person_topics"))


ROUTES: list[tuple[str, re.Pattern, Callable]] = [
    ("GET", re.compile(r"^/v1/health$"), lambda m, q, j: (200, body("get_health"))),
    ("GET", re.compile(r"^/v1/me$"), lambda m, q, j: (200, body("get_me"))),
    ("GET", re.compile(r"^/v1/transcripts/search$"), _search),
    ("GET", re.compile(r"^/v1/entities/search$"), _entities),
    ("GET", re.compile(r"^/v1/mentions$"), _mentions),
    ("GET", re.compile(r"^/v1/mentions/counts$"), lambda m, q, j: (200, body("count_mentions"))),
    ("GET", re.compile(r"^/v1/entities/([^/]+)/momentum$"), _momentum),
    ("GET", re.compile(r"^/v1/entities/([^/]+)/recommendations$"), _recommendations),
    ("GET", re.compile(r"^/v1/channels/([^/]+)/sponsors$"), lambda m, q, j: (200, body("list_channel_sponsors"))),
    ("GET", re.compile(r"^/v1/channels/([^/]+)/videos$"), lambda m, q, j: (200, body("list_channel_videos"))),
    ("GET", re.compile(r"^/v1/channels/([^/]+)/coverage$"), lambda m, q, j: (200, body("get_channel_coverage"))),
    ("GET", re.compile(r"^/v1/transcripts/([^/]+)$"), _transcript),
    ("POST", re.compile(r"^/v1/transcriptions$"), _submit_transcription),
    ("GET", re.compile(r"^/v1/transcriptions/([^/]+)$"), _transcription_status),
    ("POST", re.compile(r"^/v1/monitors$"), _create_monitor),
    ("GET", re.compile(r"^/v1/people/([^/]+)/topics$"), _person_topics),
]


class Fake:
    def __init__(self) -> None:
        self.requests: list[dict] = []
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def _serve(self) -> None:
                parts = urlsplit(self.path)
                query = parse_qs(parts.query)
                length = int(self.headers.get("content-length") or 0)
                raw = self.rfile.read(length) if length else b""
                payload = json.loads(raw) if raw else None
                fake.requests.append({"method": self.command, "path": parts.path, "query": {k: v[0] for k, v in query.items()}, "headers": {k.lower(): v for k, v in self.headers.items()}, "body": payload})
                for method, pattern, handler in ROUTES:
                    match = pattern.match(parts.path)
                    if method == self.command and match:
                        status, out = handler(match, query, payload)
                        break
                else:
                    status, out = 404, not_found_body("route_not_found", f"no fake for {self.command} {parts.path}")
                data = json.dumps(out).encode()
                self.send_response(status)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(data)))
                self.send_header("x-request-id", "req_fake")
                self.end_headers()
                self.wfile.write(data)

            do_GET = _serve
            do_POST = _serve

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.base_url = f"http://127.0.0.1:{self.server.server_address[1]}"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def close(self) -> None:
        self.server.shutdown()
        self.server.server_close()

    @property
    def last(self) -> dict:
        return self.requests[-1]
