# FLEXT Check Report

**Generated**: 2026-02-21 05:23:55 UTC  
**Projects**: 1  
**Gates**: lint, format, pyrefly, mypy, pyright, security, markdown, go  

## Summary

| Project | Lint | Format | Pyrefly | Mypy | Pyright | Security | Markdown | Go | Total | Status |
|---------|------|------|------|------|------|------|------|------|-------|--------|
| flext-dbt-ldap | 0 | 0 | 0 | 84 | 1 | 0 | 0 | 0 | 85 | **FAIL** |

**Total errors**: 85  
**Failed projects**: 1/1  

## flext-dbt-ldap

### mypy (84 errors)

```
src/flext_dbt_ldap/constants.py:227:0 [misc] Cannot assign multiple types to name "c" without an explicit "type[...]" annotation
src/flext_dbt_ldap/settings.py:52:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLdap"
src/flext_dbt_ldap/settings.py:56:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLdap"
src/flext_dbt_ldap/settings.py:86:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtProcessing"
src/flext_dbt_ldap/settings.py:91:19 [name-defined] Name "c.DbtLogLevelLiteral" is not defined
src/flext_dbt_ldap/settings.py:128:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:133:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:138:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:143:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:148:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:153:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:158:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:163:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:168:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:173:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:179:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:184:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:189:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:194:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:199:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:204:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:209:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:214:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:219:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:225:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:230:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:235:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:240:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:245:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:250:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:255:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:260:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:265:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:271:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:276:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:281:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:286:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:291:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:296:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:301:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:306:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:311:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:317:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:322:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:327:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:332:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:337:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:342:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:347:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
src/flext_dbt_ldap/settings.py:352:16 [attr-defined] "type[FlextConstants]" has no attribute "DbtLogging"
... and 34 more errors
```

### pyright (1 errors)

```
/tmp/flext-merge/flext-dbt-ldap/src/flext_dbt_ldap/settings.py:91:20 [reportInvalidTypeForm] Variable not allowed in type expression
```
