from datetime import datetime


def format_timestamp(ts: str | None = None) -> str:
    if ts is None:
        return datetime.utcnow().isoformat()
    return ts
