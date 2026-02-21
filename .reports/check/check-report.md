# FLEXT Check Report

**Generated**: 2026-02-21 18:34:24 UTC  
**Projects**: 1  
**Gates**: lint, format, pyrefly, mypy, pyright, security, markdown, go  

## Summary

| Project | Lint | Format | Pyrefly | Mypy | Pyright | Security | Markdown | Go | Total | Status |
|---------|------|------|------|------|------|------|------|------|-------|--------|
| flext-dbt-ldap | 0 | 0 | 13 | 0 | 13 | 0 | 0 | 0 | 26 | **FAIL** |

**Total errors**: 26  
**Failed projects**: 1/1  

## flext-dbt-ldap

### pyrefly (13 errors)

```
tests/__init__.py:11:1 [missing-import] Could not find import of `tests.constants`
  Looked in these locations (from config in `/home/marlonsc/flext/flext-dbt-ldap/pyproject.toml`):
  Search path (from config file): ["/home/marlonsc/flext/typings", "/home/marlonsc/flext/typings/generated", "/home/marlonsc/flext/flext-dbt-ldap/src", "/home/marlonsc/flext/flext-dbt-ldap/tests", "/home/marlonsc/flext/flext-dbt-ldap/examples", "/home/marlonsc/flext/flext-dbt-ldap/scripts"]
  Import root (inferred from project layout): "/home/marlonsc/flext/flext-dbt-ldap/src"
  Site package path queried from interpreter: ["/usr/lib/python3.13", "/usr/lib/python3.13/lib-dynload", "/home/marlonsc/flext/.venv/lib/python3.13/site-packages", "/home/marlonsc/flext/algar-oud-mig/src", "/home/marlonsc/flext/flexcore/src", "/home/marlonsc/flext/src", "/home/marlonsc/flext", "/home/marlonsc/flext/flext-api/src", "/home/marlonsc/flext/flext-auth/src", "/home/marlonsc/flext/flext-cli/src", "/home/marlonsc/flext/flext-core/src", "/home/marlonsc/flext/flext-db-oracle/src", "/home/marlonsc/flext/flext-dbt-ldap/src", "/home/marlonsc/flext/flext-dbt-ldif/src", "/home/marlonsc/flext/flext-dbt-oracle/src", "/home/marlonsc/flext/flext-dbt-oracle-wms/src", "/home/marlonsc/flext/flext-grpc/src", "/home/marlonsc/flext/flext-ldap/src", "/home/marlonsc/flext/flext-ldif/src", "/home/marlonsc/flext/flext-meltano/src", "/home/marlonsc/flext/flext-observability/src", "/home/marlonsc/flext/flext-oracle-oic/src", "/home/marlonsc/flext/flext-oracle-wms/src", "/home/marlonsc/flext/flext-plugin/src", "/home/marlonsc/flext/flext-quality/src", "/home/marlonsc/flext/flext-tap-ldap/src", "/home/marlonsc/flext/flext-tap-ldif/src", "/home/marlonsc/flext/flext-tap-oracle/src", "/home/marlonsc/flext/flext-tap-oracle-oic/src", "/home/marlonsc/flext/flext-tap-oracle-wms/src", "/home/marlonsc/flext/flext-target-ldap/src", "/home/marlonsc/flext/flext-target-ldif/src", "/home/marlonsc/flext/flext-target-oracle/src", "/home/marlonsc/flext/flext-target-oracle-oic/src", "/home/marlonsc/flext/flext-target-oracle-wms/src", "/home/marlonsc/flext/flext-web/src", "/home/marlonsc/flext/gruponos-meltano-native/src"]
tests/e2e/conftest.py:52:20 [missing-attribute] Object of class `FlextTestsDocker` has no attribute `start_compose_service`
tests/e2e/conftest.py:83:19 [missing-attribute] Object of class `FlextTestsDocker` has no attribute `stop_compose_service`
tests/e2e/conftest.py:149:26 [missing-attribute] Object of class `Coroutine` has no attribute `communicate`
tests/e2e/conftest.py:150:16 [missing-attribute] Object of class `Coroutine` has no attribute `returncode`
tests/e2e/conftest.py:152:27 [missing-argument] Missing argument `env` in function `_run_db`
tests/e2e/conftest.py:152:36 [no-matching-overload] No matching overload found for function `str.__new__` called with arguments: (type[str], Path, dict[str, str])
  Possible overloads:
  (cls: type[str], object: object = '') -> str
  (cls: type[str], object: Buffer, encoding: str = 'utf-8', errors: str = 'strict') -> str [closest match]
tests/e2e/conftest.py:161:12 [bad-return] Returned type `e2e.conftest.run_dbt_command.CompletedProcess` is not assignable to declared return type `subprocess.CompletedProcess[str]`
tests/e2e/conftest.py:166:10 [missing-attribute] Object of class `object` has no attribute `cursor`
tests/e2e/conftest.py:174:10 [missing-attribute] Object of class `object` has no attribute `cursor`
tests/e2e/conftest.py:191:10 [missing-attribute] Object of class `object` has no attribute `cursor`
tests/e2e/conftest.py:203:10 [missing-attribute] Object of class `object` has no attribute `cursor`
tests/protocols.py:25:11 [bad-override] Class member `TestsFlextDbtLdapProtocols.Tests` overrides parent class `FlextTestsProtocols` in an inconsistent manner
  `TestsFlextDbtLdapProtocols.Tests` has type `type[TestsFlextDbtLdapProtocols.Tests]`, which is not assignable to `type[FlextTestsProtocols.Tests]`, the type of `FlextTestsProtocols.Tests`
```

### pyright (13 errors)

```
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:52:33 [reportAttributeAccessIssue] Cannot access attribute "start_compose_service" for class "FlextTestsDocker"
  Attribute "start_compose_service" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:83:32 [reportAttributeAccessIssue] Cannot access attribute "stop_compose_service" for class "FlextTestsDocker"
  Attribute "stop_compose_service" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:149:34 [reportAttributeAccessIssue] Cannot access attribute "communicate" for class "CoroutineType[Any, Any, Process]"
  Attribute "communicate" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:150:24 [reportAttributeAccessIssue] Cannot access attribute "returncode" for class "CoroutineType[Any, Any, Process]"
  Attribute "returncode" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:152:20 [reportCallIssue] Argument missing for parameter "env"
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:152:37 [reportArgumentType] Argument of type "Path" cannot be assigned to parameter "object" of type "ReadableBuffer" in function "__new__"
  "Path" is incompatible with protocol "Buffer"
    "__buffer__" is not present
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:152:50 [reportArgumentType] Argument of type "dict[str, str]" cannot be assigned to parameter "encoding" of type "str" in function "__new__"
  "dict[str, str]" is not assignable to "str"
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:161:12 [reportReturnType] Type "CompletedProcess" is not assignable to return type "CompletedProcess[str]"
  "CompletedProcess" is not assignable to "CompletedProcess[str]"
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:166:15 [reportAttributeAccessIssue] Cannot access attribute "cursor" for class "object"
  Attribute "cursor" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:174:15 [reportAttributeAccessIssue] Cannot access attribute "cursor" for class "object"
  Attribute "cursor" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:191:15 [reportAttributeAccessIssue] Cannot access attribute "cursor" for class "object"
  Attribute "cursor" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/e2e/conftest.py:203:15 [reportAttributeAccessIssue] Cannot access attribute "cursor" for class "object"
  Attribute "cursor" is unknown
/home/marlonsc/flext/flext-dbt-ldap/tests/protocols.py:25:11 [reportIncompatibleVariableOverride] "Tests" overrides symbol of same name in class "FlextTestsProtocols"
  "tests.protocols.TestsFlextDbtLdapProtocols.Tests" is not assignable to "flext_tests.protocols.FlextTestsProtocols.Tests"
  Type "type[tests.protocols.TestsFlextDbtLdapProtocols.Tests]" is not assignable to type "type[flext_tests.protocols.FlextTestsProtocols.Tests]"
```
