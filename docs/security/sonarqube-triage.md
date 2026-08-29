# Triagem SonarCloud — flext-sh/flext-dbt-ldap

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.3`

## Resumo

**28 issues** — BLOCKER 0, CRITICAL 23, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 24 · **Debt total: 117min**

| regra | issues |
|---|---|
| `plsql:S1192` | 23 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:12` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        8      create_timestamp, modify_timestamp, title
        9  ) VALUES
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
>>>    12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:12` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        8      create_timestamp, modify_timestamp, title
        9  ) VALUES
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
>>>    12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
```

**Decisão**: pendente

### 3 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:13` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        9  ) VALUES
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
>>>    13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
```

**Decisão**: pendente

### 4 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:13` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
        9  ) VALUES
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
>>>    13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
```

**Decisão**: pendente

### 5 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:14` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
>>>    14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
```

**Decisão**: pendente

### 6 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:14` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
>>>    14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
```

**Decisão**: pendente

### 7 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:14` · **Effort**: 4min

> Define a constant instead of duplicating this literal 5 times.

```sql
       10  (
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
>>>    14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
```

**Decisão**: pendente

### 8 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:15` · **Effort**: 4min

> Define a constant instead of duplicating this literal 4 times.

```sql
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
>>>    15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
```

**Decisão**: pendente

### 9 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:15` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       11      '2024-01-01 12:00:00+00', '2024-01-01 12:00:00+00', 1, 1,
       12      'uid=john.doe,ou=users,dc=test,dc=com', 'john.doe', 'John Doe', 'Doe', 'John',
       13      'john.doe@test.com', '1001', 'active', 'engineering', '+1-555-1234', '+1-555-5678',
       14      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
>>>    15      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
```

**Decisão**: pendente

### 10 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:20` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
>>>    20      'uid=jane.smith,ou=users,dc=test,dc=com', 'jane.smith', 'Jane Smith', 'Smith', 'Jane',
       21      'jane.smith@test.com', '1002', 'active', 'sales', '+1-555-2345', '+1-555-6789',
       22      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       23      ARRAY['cn=sales-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
```

**Decisão**: pendente

### 11 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:20` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       16      '2024-01-01 10:00:00+00', '2024-01-01 11:00:00+00', 'Senior Engineer'
       17  ),
       18  (
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
>>>    20      'uid=jane.smith,ou=users,dc=test,dc=com', 'jane.smith', 'Jane Smith', 'Smith', 'Jane',
       21      'jane.smith@test.com', '1002', 'active', 'sales', '+1-555-2345', '+1-555-6789',
       22      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       23      ARRAY['cn=sales-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
```

**Decisão**: pendente

### 12 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:21` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       17  ),
       18  (
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
       20      'uid=jane.smith,ou=users,dc=test,dc=com', 'jane.smith', 'Jane Smith', 'Smith', 'Jane',
>>>    21      'jane.smith@test.com', '1002', 'active', 'sales', '+1-555-2345', '+1-555-6789',
       22      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       23      ARRAY['cn=sales-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
       25  ),
```

**Decisão**: pendente

### 13 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:23` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       19      '2024-01-01 12:00:01+00', '2024-01-01 12:00:01+00', 2, 1,
       20      'uid=jane.smith,ou=users,dc=test,dc=com', 'jane.smith', 'Jane Smith', 'Smith', 'Jane',
       21      'jane.smith@test.com', '1002', 'active', 'sales', '+1-555-2345', '+1-555-6789',
       22      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
>>>    23      ARRAY['cn=sales-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
       25  ),
       26  (
       27      '2024-01-01 12:00:02+00', '2024-01-01 12:00:02+00', 3, 1,
```

**Decisão**: pendente

### 14 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:28` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
       25  ),
       26  (
       27      '2024-01-01 12:00:02+00', '2024-01-01 12:00:02+00', 3, 1,
>>>    28      'uid=bob.wilson,ou=users,dc=test,dc=com', 'bob.wilson', 'Bob Wilson', 'Wilson', 'Bob',
       29      'bob.wilson@test.com', '1003', 'active', 'engineering', '+1-555-3456', '+1-555-7890',
       30      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       31      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=developers,ou=groups,dc=test,dc=com'],
       32      '2024-01-01 10:02:00+00', '2024-01-01 11:02:00+00', 'Software Developer'
```

**Decisão**: pendente

### 15 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:28` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       24      '2024-01-01 10:01:00+00', '2024-01-01 11:01:00+00', 'Sales Manager'
       25  ),
       26  (
       27      '2024-01-01 12:00:02+00', '2024-01-01 12:00:02+00', 3, 1,
>>>    28      'uid=bob.wilson,ou=users,dc=test,dc=com', 'bob.wilson', 'Bob Wilson', 'Wilson', 'Bob',
       29      'bob.wilson@test.com', '1003', 'active', 'engineering', '+1-555-3456', '+1-555-7890',
       30      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       31      ARRAY['cn=engineering-team,ou=groups,dc=test,dc=com', 'cn=developers,ou=groups,dc=test,dc=com'],
       32      '2024-01-01 10:02:00+00', '2024-01-01 11:02:00+00', 'Software Developer'
```

**Decisão**: pendente

### 16 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:36` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       32      '2024-01-01 10:02:00+00', '2024-01-01 11:02:00+00', 'Software Developer'
       33  ),
       34  (
       35      '2024-01-01 12:00:03+00', '2024-01-01 12:00:03+00', 4, 1,
>>>    36      'uid=alice.johnson,ou=users,dc=test,dc=com', 'alice.johnson', 'Alice Johnson', 'Johnson', 'Alice',
       37      'alice.johnson@test.com', '1004', 'active', 'hr', '+1-555-4567', '+1-555-8901',
       38      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       39      ARRAY['cn=hr-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       40      '2024-01-01 10:03:00+00', '2024-01-01 11:03:00+00', 'HR Director'
```

**Decisão**: pendente

### 17 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:36` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       32      '2024-01-01 10:02:00+00', '2024-01-01 11:02:00+00', 'Software Developer'
       33  ),
       34  (
       35      '2024-01-01 12:00:03+00', '2024-01-01 12:00:03+00', 4, 1,
>>>    36      'uid=alice.johnson,ou=users,dc=test,dc=com', 'alice.johnson', 'Alice Johnson', 'Johnson', 'Alice',
       37      'alice.johnson@test.com', '1004', 'active', 'hr', '+1-555-4567', '+1-555-8901',
       38      ARRAY['inetOrgPerson', 'organizationalPerson', 'person', 'top'],
       39      ARRAY['cn=hr-team,ou=groups,dc=test,dc=com', 'cn=managers,ou=groups,dc=test,dc=com'],
       40      '2024-01-01 10:03:00+00', '2024-01-01 11:03:00+00', 'HR Director'
```

**Decisão**: pendente

### 18 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:70` · **Effort**: 4min

> Define a constant instead of duplicating this literal 6 times.

```sql
       66      '2024-01-01 12:01:00+00', '2024-01-01 12:01:00+00', 1, 1,
       67      'cn=engineering-team,ou=groups,dc=test,dc=com', 'engineering-team', 'Engineering Team Members',
       68      ARRAY['uid=john.doe,ou=users,dc=test,dc=com', 'uid=bob.wilson,ou=users,dc=test,dc=com'],
       69      ARRAY['john.doe', 'bob.wilson'],
>>>    70      ARRAY['groupOfNames', 'top'],
       71      '2024-01-01 10:00:00+00', '2024-01-01 11:30:00+00'
       72  ),
       73  (
       74      '2024-01-01 12:01:01+00', '2024-01-01 12:01:01+00', 2, 1,
```

**Decisão**: pendente

### 19 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/e2e/sql/02-insert-test-data.sql:123` · **Effort**: 4min

> Define a constant instead of duplicating this literal 6 times.

```sql
      119  ) VALUES
      120  (
      121      '2024-01-01 12:02:00+00', '2024-01-01 12:02:00+00', 1, 1,
      122      'ou=users,dc=test,dc=com', 'users', 'User accounts', NULL,
>>>   123      ARRAY['organizationalUnit', 'top'],
      124      '2024-01-01 09:00:00+00', '2024-01-01 09:00:00+00'
      125  ),
      126  (
      127      '2024-01-01 12:02:01+00', '2024-01-01 12:02:01+00', 2, 1,
```

**Decisão**: pendente

### 20 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/generic/test_data_quality.sql:7` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        3  -- Test that all users have unique UIDs
        4  select count(*) as failures
        5  from (
        6      select uid, count(*) as cnt
>>>     7  from {{ ref('stg_users') }}
        8      group by uid
        9      having count(*) > 1
       10  ) duplicates
       11  where failures > 0;
```

**Decisão**: pendente

### 21 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/generic/test_data_quality.sql:34` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
       30  
       31  -- Test that organizational units form a valid hierarchy
       32  with recursive ou_check as (
       33      select dn, parent_ou_dn, 1 as depth
>>>    34  from {{ ref('stg_org_units') }}
       35      where parent_ou_dn = '{{ var("ldap_base_dn") }}'
       36  
       37      union all
       38  
```

**Decisão**: pendente

### 22 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/test_macros.sql:6` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
        2  
        3  -- Test parse_dn macro
        4  {% test test_parse_dn %}
        5  with test_data as (
>>>     6      select 'uid=jdoe,ou=users,dc=example,dc=com' as dn
        7  )
        8  select
        9      {{ parse_dn('dn') }}
       10  from test_data
```

**Decisão**: pendente

### 23 · 🟠 CRITICAL · CODE_SMELL · `plsql:S1192`
**Local**: `tests/test_macros.sql:125` · **Effort**: 4min

> Define a constant instead of duplicating this literal 3 times.

```sql
      121      select '["inetOrgPerson", "person", "top"]' as object_classes
      122  )
      123  select *
      124  from test_data
>>>   125  where not {{ has_object_class('object_classes', 'person') }}
      126     or not {{ has_object_class('object_classes', 'inetOrgPerson') }}
      127     or {{ has_object_class('object_classes', 'nonexistent') }}
      128  {% endtest %}
```

**Decisão**: pendente

### 24 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 25 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 26 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 27 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.


**Decisão**: pendente

### 28 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente
