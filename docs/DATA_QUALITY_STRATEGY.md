# Data Quality Strategy

## Quality Risks

- silent row loss
- schema drift
- tenant provenance loss
- filtering after schema discovery
- non-deterministic transformations
- encoding problems in exported files

## Controls

- strict tenant discovery pattern
- filtering before export eligibility
- provenance on every row
- union schema calculation
- UTF-8 with BOM for spreadsheet interoperability
- reconciliation equations enforced as code
- unit tests for critical transformations

## Release Gate

The pipeline is releasable only when automated tests pass and every processed tenant satisfies reconciliation.
