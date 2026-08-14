# Portfolio Case Study

## Problem

Multi-tenant document databases evolve over time. Hard-coded schemas and tenant-specific exporters become fragile, and successful execution does not prove that the output is complete.

## Goal

Create a configuration-driven pattern where changing source documents can be normalized while preserving tenant provenance and proving row-level completeness through independent reconciliation.

## Engineering Approach

- discover sources dynamically
- treat tenant identity as provenance, not business data
- flatten nested documents deterministically
- compute a union schema
- apply centrally configured exclusions
- export spreadsheet-friendly UTF-8
- reconcile independently

## Quality Engineering Applied to Data

The key shift is that data movement is tested as a release-quality problem. A pipeline run is not successful merely because it completed without an exception; source, filter, eligibility and export counts must mathematically reconcile.

## Public-Safe Design

All tenants, emails and records in this repository are synthetic examples.
