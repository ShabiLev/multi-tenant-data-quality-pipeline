from __future__ import annotations

import re
from pathlib import Path
from .models import Tenant

DB_PATTERN = re.compile(r"^prod-(?P<code>[a-z0-9]+)-customer-db$")


def discover_tenants(root: Path, tenant_names: dict[str, str]) -> list[Tenant]:
    tenants: list[Tenant] = []
    for item in sorted(p for p in root.iterdir() if p.is_dir()):
        match = DB_PATTERN.match(item.name)
        if not match:
            continue
        code = match.group("code")
        tenants.append(Tenant(code=code, name=tenant_names.get(code), source_database=item.name))
    return tenants
