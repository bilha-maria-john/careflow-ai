# This is a simple in‑memory store for demo purposes.
# In a real app, this would connect to Firestore / Supabase / etc.

_records: list[dict] = []


def save_record(record_type: str, data: dict) -> None:
    _records.append({"type": record_type, "data": data})


def get_all_records() -> list[dict]:
    return _records
