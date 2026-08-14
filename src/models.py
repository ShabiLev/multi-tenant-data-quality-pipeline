from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Tenant:
    code: str
    name: str | None
    source_database: str


@dataclass(frozen=True)
class Reconciliation:
    source_rows: int
    filtered_rows: int
    eligible_rows: int
    exported_rows: int

    @property
    def passed(self) -> bool:
        return (
            self.source_rows - self.filtered_rows == self.eligible_rows
            and self.eligible_rows == self.exported_rows
        )
