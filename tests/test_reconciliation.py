from src.models import Reconciliation


def test_reconciliation_passes_when_equations_hold():
    result = Reconciliation(source_rows=10, filtered_rows=2, eligible_rows=8, exported_rows=8)
    assert result.passed


def test_reconciliation_fails_on_export_drift():
    result = Reconciliation(source_rows=10, filtered_rows=2, eligible_rows=8, exported_rows=7)
    assert not result.passed
