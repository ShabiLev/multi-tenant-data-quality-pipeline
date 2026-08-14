from __future__ import annotations

from collections.abc import Iterable


def union_schema(rows: Iterable[dict]) -> list[str]:
    keys: set[str] = set()
    for row in rows:
        keys.update(row.keys())
    provenance = ["tenantCode", "tenantName", "sourceDatabase"]
    dynamic = sorted(k for k in keys if k not in provenance)
    return provenance + dynamic
