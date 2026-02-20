# FLEXT Check Report

**Generated**: 2026-02-20 00:03:35 UTC  
**Projects**: 1  
**Gates**: lint, format, pyrefly, mypy, pyright, security, markdown, go  

## Summary

| Project | Lint | Format | Pyrefly | Mypy | Pyright | Security | Markdown | Go | Total | Status |
|---------|------|------|------|------|------|------|------|------|-------|--------|
| flext-dbt-ldap | 0 | 0 | 0 | 1 | 1 | 2 | 0 | 0 | 4 | **FAIL** |

**Total errors**: 4  
**Failed projects**: 1/1  

## flext-dbt-ldap

### mypy (1 errors)

```
src/flext_dbt_ldap/utilities.py:126:23 [return-value] Incompatible return value type (got "<typing special form>", expected "type")
```

### pyright (1 errors)

```
/home/marlonsc/flext/flext-dbt-ldap/src/flext_dbt_ldap/utilities.py:126:24 [reportReturnType] Type "Annotated" is not assignable to return type "type"
  "Annotated" is not assignable to "type"
```

### security (2 errors)

```
src/flext_dbt_ldap/utilities.py:194:0 [B608] Possible SQL injection vector through string-based query construction.
src/flext_dbt_ldap/utilities.py:289:0 [B608] Possible SQL injection vector through string-based query construction.
```
