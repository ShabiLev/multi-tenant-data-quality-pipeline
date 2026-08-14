# Multi-Tenant Data Quality Pipeline

A configuration-driven Python reference implementation for discovering multi-tenant MongoDB-style datasets, flattening evolving documents into canonical rows, and independently reconciling exported results.

This public showcase uses **synthetic tenants and JSON fixtures only**. It demonstrates the Quality Engineering principles behind data pipelines without exposing private databases, connection strings, customer names or production data.

## What It Demonstrates

- Tenant discovery by naming convention
- Provenance columns on every canonical row
- Dynamic schema union across heterogeneous documents
- Nested document flattening
- Configuration-driven filtering
- Deterministic CSV/Excel-ready canonical output
- Independent reconciliation of source vs eligible vs exported counts
- Unit tests for discovery, filtering, flattening and reconciliation
- CI quality gate

## Data Flow

```text
Synthetic Tenant Sources
        ↓
Tenant Discovery
        ↓
Config Filters
        ↓
Dynamic Schema Discovery
        ↓
Canonical Row Builder
        ↓
Export Sink
        ↓
Independent Reconciliation
```

## Quick Start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
pytest
python -m src.cli --input samples --output output
```

## Synthetic Tenants

- `prod-acme-customer-db`
- `prod-contoso-customer-db`
- `prod-globex-customer-db`

## Public-Safe Design

This repository is a clean reference implementation. It contains no private Git history, production hostnames, MongoDB URIs, SQL credentials, customer data or proprietary tenant identifiers.

> Data quality is a release-quality problem: transformations are not complete until their outputs reconcile against independently computed expectations.
