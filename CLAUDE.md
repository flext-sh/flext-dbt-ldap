# flext-dbt-ldap - FLEXT DBT Adapters

**Hierarchy**: PROJECT
**Parent**: [../CLAUDE.md](../CLAUDE.md) - Workspace standards
**Last Update**: 2025-12-07

---

## Project Overview

**FLEXT-DBT-LDAP** is the dbt project for LDAP directory data transformations using dbt Core with PostgreSQL/DuckDB backends.

**Version**: 2.1.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:

- **flext-meltano**: MANDATORY for ALL DBT operations (ZERO TOLERANCE for direct dbt imports)
- **flext-ldap**: MANDATORY for ALL LDAP operations (ZERO TOLERANCE for direct ldap3 imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)

---

## Essential Commands

```bash
# Setup and validation
make setup                    # Complete development environment setup
make validate                 # Complete validation (lint + type + security + test)
make check                    # Quick check (lint + type)

# Quality gates
make lint                     # Ruff linting
make type-check               # Pyrefly type checking
make security                 # Bandit security scan
make test                     # Run tests
```

---

## Key Patterns

### DBT Transformation

```python
from flext_core import FlextResult
from flext_dbt_ldap import FlextDbtLdap

dbt = FlextDbtLdap()

# Run DBT models
result = dbt.run_models(models=["model1", "model2"])
if result.is_success:
    output = result.unwrap()
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:

- ❌ Direct dbt imports (use flext-meltano)
- ❌ Direct ldap3 imports (use flext-ldap)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:

- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for DBT operations
- ✅ Use flext-ldap for LDAP operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**See Also**:

- [Workspace Standards](../CLAUDE.md)
- [flext-core Patterns](../flext-core/CLAUDE.md)
- [flext-ldap Patterns](../flext-ldap/CLAUDE.md)
- [flext-tap-ldap Patterns](../flext-tap-ldap/CLAUDE.md)
