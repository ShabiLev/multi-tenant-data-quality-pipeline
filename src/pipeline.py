from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from .discovery import discover_tenants
from .filters import should_exclude
from .flatten import flatten
from .models import Reconciliation
from .schema import union_schema


def load_json_documents(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_pipeline(input_root: Path, output_root: Path, config: dict[str, Any]) -> dict[str, Reconciliation]:
    output_root.mkdir(parents=True, exist_ok=True)
    tenant_names = config.get("tenants", {})
    rules = config.get("filters", [])
    reconciliations: dict[str, Reconciliation] = {}

    for tenant in discover_tenants(input_root, tenant_names):
        source_file = input_root / tenant.source_database / "customers.json"
        docs = load_json_documents(source_file)
        filtered = [doc for doc in docs if should_exclude(doc, rules)]
        eligible = [doc for doc in docs if not should_exclude(doc, rules)]

        rows: list[dict[str, Any]] = []
        for doc in eligible:
            row = {
                "tenantCode": tenant.code,
                "tenantName": tenant.name or "",
                "sourceDatabase": tenant.source_database,
                **flatten(doc),
            }
            rows.append(row)

        fields = union_schema(rows)
        output_file = output_root / f"{tenant.code}-customers.csv"
        with output_file.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

        rec = Reconciliation(
            source_rows=len(docs),
            filtered_rows=len(filtered),
            eligible_rows=len(eligible),
            exported_rows=len(rows),
        )
        if not rec.passed:
            raise RuntimeError(f"Reconciliation failed for {tenant.code}: {rec}")
        reconciliations[tenant.code] = rec

    return reconciliations
