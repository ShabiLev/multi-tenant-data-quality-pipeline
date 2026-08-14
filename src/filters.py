from __future__ import annotations

from typing import Any


def get_nested(document: dict[str, Any], dotted_path: str) -> Any:
    value: Any = document
    for part in dotted_path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def should_exclude(document: dict[str, Any], rules: list[dict[str, Any]]) -> bool:
    for rule in rules:
        value = get_nested(document, rule["field"])
        if not isinstance(value, str):
            continue
        candidate = value.casefold() if rule.get("case_insensitive", True) else value
        if "starts_with" in rule:
            prefix = str(rule["starts_with"])
            prefix = prefix.casefold() if rule.get("case_insensitive", True) else prefix
            if candidate.startswith(prefix):
                return True
    return False
