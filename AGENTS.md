# AGENTS.md — flext-dbt-ldap

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_dbt_ldap` · deps: `flext-cli`, `flext-core`, `flext-ldap`, `flext-ldif`, `flext-meltano`

## Overview

dbt models for LDAP data transformation. Thin driver over `flext-meltano` dbt runner (ADR-006).

## Structure

```text
src/flext_dbt_ldap/
├── api.py            # FlextDbtLdap (.execute)
├── base.py
├── services/         # client.py (FlextDbtLdapClientMixin), sync.py
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _constants/ _models/ _utilities/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextDbtLdap` | class | `api.py` | facade (`execute`) |
| `FlextDbtLdapClientMixin` | class | `services/client.py` | `run_full_pipeline`, `transform_with_dbt` |

## Conventions (specific to this package)

- dbt connection profiles are **typed `m.*` models**, not dict roundtrips.
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Commands

```bash
make check PROJECT=flext-dbt-ldap
make test  PROJECT=flext-dbt-ldap       # tests/{unit,e2e,generic}
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
