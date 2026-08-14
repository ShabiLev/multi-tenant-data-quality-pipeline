from __future__ import annotations

from typing import Any


def flatten(document: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in document.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            output.update(flatten(value, full_key))
        elif isinstance(value, list):
            output[full_key] = value
        else:
            output[full_key] = value
    return output
