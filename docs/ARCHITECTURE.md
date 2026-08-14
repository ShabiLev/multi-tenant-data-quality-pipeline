# Architecture

## Pipeline

```text
Discovery → Filter → Schema → Canonicalize → Export → Reconcile
```

### Discovery
Tenant databases are selected by a strict naming convention and mapped to optional friendly names.

### Filtering
Configuration-driven filters execute before canonical export. Filter rules are independent of tenant-specific code.

### Dynamic schema
The exporter computes the union of canonical fields rather than assuming every document has the same shape.

### Provenance
Every exported row begins with:

- `tenantCode`
- `tenantName`
- `sourceDatabase`

### Reconciliation
Reconciliation is computed independently from export output:

```text
source - filtered = eligible
eligible = exported
```

A mismatch is a release blocker rather than a warning.
