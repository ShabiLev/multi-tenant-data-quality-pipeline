from pathlib import Path
from src.discovery import discover_tenants


def test_discovers_only_matching_tenants(tmp_path: Path):
    (tmp_path / "prod-acme-customer-db").mkdir()
    (tmp_path / "other-db").mkdir()
    tenants = discover_tenants(tmp_path, {"acme": "Acme Parking"})
    assert [(t.code, t.name) for t in tenants] == [("acme", "Acme Parking")]
