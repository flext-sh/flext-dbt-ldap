# FLEXT Check Report

**Generated**: 2026-02-22 16:12:44 UTC  
**Projects**: 1  
**Gates**: lint, format, pyrefly, mypy, pyright, security, markdown, go  

## Summary

| Project | Lint | Format | Pyrefly | Mypy | Pyright | Security | Markdown | Go | Total | Status |
|---------|------|------|------|------|------|------|------|------|-------|--------|
| flext-dbt-ldap | 1 | 0 | 0 | 54 | 3 | 0 | 0 | 0 | 58 | **FAIL** |

**Total errors**: 58  
**Failed projects**: 1/1  

## flext-dbt-ldap

### lint (1 errors)

```
/home/marlonsc/flext/flext-dbt-ldap/src/flext_dbt_ldap/dbt_client.py:264:9 [PLC0415] `import` should be at the top-level of a file
```

### mypy (54 errors)

```
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "ValidationMetrics":
src/flext_dbt_ldap/models.py:63:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtRunStatus":
src/flext_dbt_ldap/models.py:72:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtLdapPipelineResult":
src/flext_dbt_ldap/models.py:79:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "SyncResult":
src/flext_dbt_ldap/models.py:84:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "PerformanceAnalysis":
src/flext_dbt_ldap/models.py:91:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "ServiceStatus":
src/flext_dbt_ldap/models.py:99:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "AnalyticsReport":
src/flext_dbt_ldap/models.py:106:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtProjectConfig":
src/flext_dbt_ldap/models.py:116:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtProfileConfig":
src/flext_dbt_ldap/models.py:136:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtSourceTable":
src/flext_dbt_ldap/models.py:148:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtSourceSchema":
src/flext_dbt_ldap/models.py:154:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtModelDefinition":
src/flext_dbt_ldap/models.py:160:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtTestConfig":
src/flext_dbt_ldap/models.py:166:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtSourceFreshness":
src/flext_dbt_ldap/models.py:173:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtSourceDefinition":
src/flext_dbt_ldap/models.py:179:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DbtConfig":
src/flext_dbt_ldap/models.py:186:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "ProjectStructureValidation":
src/flext_dbt_ldap/models.py:193:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "OptimizationHints":
src/flext_dbt_ldap/models.py:198:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "TransformationConfig":
src/flext_dbt_ldap/models.py:210:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "TransformationRule":
src/flext_dbt_ldap/models.py:217:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "DataValidationConfig":
src/flext_dbt_ldap/models.py:223:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "LdapSchema":
src/flext_dbt_ldap/models.py:235:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "LdapQuery":
src/flext_dbt_ldap/models.py:241:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "UserDimension":
src/flext_dbt_ldap/models.py:253:-1 [explicit-any] Explicit "Any" is not allowed
src/flext_dbt_ldap/models.py:-1:-1 In member "__mypy-replace" of class "GroupDimension":
src/flext_dbt_ldap/models.py:328:-1 [explicit-any] Explicit "Any" is not allowed
... and 4 more errors
```

### pyright (3 errors)

```
/home/marlonsc/flext/flext-dbt-ldap/src/flext_dbt_ldap/dbt_client.py:317:24 [reportReturnType] Type "FlextResult[list[GeneralValueType]]" is not assignable to return type "r"
  "FlextResult[list[GeneralValueType]]" is not assignable to "FlextResult[list[Entry]]"
    Type parameter "T_co@FlextResult" is invariant, but "list[GeneralValueType]" is not the same as "list[Entry]"
/home/marlonsc/flext/flext-dbt-ldap/src/flext_dbt_ldap/models.py:442:16 [reportUnnecessaryComparison] Condition will always evaluate to False since the types "list[str]" and "None" have no overlap
/home/marlonsc/flext/flext-dbt-ldap/src/flext_dbt_ldap/models.py:444:16 [reportUnnecessaryIsInstance] Unnecessary isinstance call; "list[str]" is always an instance of "list[Unknown]"
```
