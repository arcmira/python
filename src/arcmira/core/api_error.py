# Maintained by hand. scripts/install-generated.py copies this over the
# generated src/arcmira/core/api_error.py so regeneration keeps the format.

from typing import Any, Dict, Optional


def _field(source: Any, name: str) -> Any:
    if isinstance(source, dict):
        return source.get(name)
    return getattr(source, name, None)


class ApiError(Exception):
    headers: Optional[Dict[str, str]]
    status_code: Optional[int]
    body: Any

    def __init__(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        status_code: Optional[int] = None,
        body: Any = None,
    ) -> None:
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def __str__(self) -> str:
        detail = _field(self.body, "error") or self.body
        code = _field(detail, "code")
        message = _field(detail, "message")
        if code is not None and message is not None:
            return f"{self.status_code} {code}: {message}"
        return f"{self.status_code}: {self.body}"
