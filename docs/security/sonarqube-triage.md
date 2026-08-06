# Triagem SonarCloud — flext-sh/flext-dbt-ldap

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.3`

## Resumo

**28 issues** — BLOCKER 0, CRITICAL 23, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 24

| regra | issues |
|---|---|
| `plsql:S1192` | 23 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 12 | |
| 2 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 12 | |
| 3 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 13 | |
| 4 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 13 | |
| 5 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 14 | |
| 6 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 14 | |
| 7 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 14 | |
| 8 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 15 | |
| 9 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 15 | |
| 10 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 20 | |
| 11 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 20 | |
| 12 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 21 | |
| 13 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 23 | |
| 14 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 28 | |
| 15 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 28 | |
| 16 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 36 | |
| 17 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 36 | |
| 18 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 70 | |
| 19 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/e2e/sql/02-insert-test-data.sql` | 123 | |
| 20 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/generic/test_data_quality.sql` | 7 | |
| 21 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/generic/test_data_quality.sql` | 34 | |
| 22 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/test_macros.sql` | 6 | |
| 23 | CRITICAL | CODE_SMELL | `plsql:S1192` | `tests/test_macros.sql` | 125 | |
| 24 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 25 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 26 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 27 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 28 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-dbt-ldap.json`

