"""E2E test configuration and fixtures for dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
from collections.abc import Generator, Sequence
from pathlib import Path
from types import ModuleType
from typing import LiteralString

import pytest
from flext_tests import tk

from tests import d, m, p, t, u

psycopg: ModuleType = pytest.importorskip("psycopg", reason="psycopg not installed")
sql: ModuleType = psycopg.sql

logger = u.fetch_logger(__name__)
POSTGRES_READY_MAX_RETRIES = 30
type _DbRow = t.VariadicTuple[t.RecursiveContainer]


@pytest.fixture(scope="session")
def flext_docker() -> tk:
    """Get tk unified management instance."""
    return tk()


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).parent.parent.parent


@pytest.fixture(scope="session")
def postgres_container(flext_docker: tk, project_root: Path) -> Generator[None]:
    """Start PostgreSQL container for testing using tk."""
    compose_file = project_root / "docker-compose.yml"
    logger.info("Starting PostgreSQL container using tk...")
    start_result = flext_docker.start_compose_stack(str(compose_file))
    if start_result.failure:
        pytest.skip(f"PostgreSQL container failed to start: {start_result.error}")

    @d.retry(
        max_attempts=POSTGRES_READY_MAX_RETRIES,
        delay_seconds=2.0,
        backoff_strategy="linear",
    )
    def _check_postgres_ready() -> None:
        conn = psycopg.connect(
            host="localhost",
            port=25432,
            dbname="dbt_ldap_test",
            user="dbt_user",
            password="dbt_password",
        )
        conn.close()

    _check_postgres_ready()
    logger.info("PostgreSQL is ready")
    yield
    logger.info("Stopping PostgreSQL container using tk...")

    class _StopResult:
        failure: bool = False
        error: str | None = None

    if hasattr(flext_docker, "stop_compose_stack"):
        stop_fn = getattr(flext_docker, "stop_compose_stack")
        stop_result: _StopResult = stop_fn(str(compose_file))
    else:
        stop_result = _StopResult()
    if stop_result.failure and stop_result.error:
        logger.warning(
            "PostgreSQL container stop reported failure: %s",
            stop_result.error,
        )


@pytest.fixture
def db_connection(__postgres_container: None, /) -> Generator[p.DbConnection]:
    """Get database connection for testing."""
    conn = psycopg.connect(
        host="localhost",
        port=25432,
        dbname="dbt_ldap_test",
        user="dbt_user",
        password="dbt_password",
    )
    conn.autocommit = True
    yield conn
    conn.close()


@pytest.fixture
def dbt_project_dir(project_root: Path) -> Path:
    """Get dbt project directory."""
    return project_root


@pytest.fixture
def dbt_profiles_dir(project_root: Path) -> Path:
    """Get dbt profiles directory."""
    return project_root / "tests" / "e2e" / "profiles"


def run_dbt_command(
    command: t.StrSequence,
    project_dir: Path,
    profiles_dir: Path,
    dbt_vars: t.RecursiveContainerMapping | None = None,
) -> m.Cli.CommandOutput:
    """Run dbt command with proper configuration."""
    env = {
        **os.environ,
        "DBT_PROFILES_DIR": str(profiles_dir),
        "DBT_PROJECT_DIR": str(project_dir),
    }
    cmd = ["dbt", *command]
    if dbt_vars:
        var_string = " ".join((f"{k}:{v}" for k, v in dbt_vars.items()))
        cmd.extend(["--vars", var_string])
    result = u.Cli.run_raw(cmd, cwd=project_dir, env=env)
    if result.success:
        return result.value
    return m.Cli.CommandOutput(
        stdout="",
        stderr=result.error or "dbt execution failed",
        exit_code=1,
    )


def query_database(
    conn: p.DbConnection,
    query: LiteralString,
) -> Sequence[_DbRow]:
    """Execute query and return results."""
    with conn.cursor() as cur:
        _ = cur.execute(sql.SQL(query))
        result = cur.fetchall()
        return list(result)


def table_exists(conn: p.DbConnection, schema: str, table: str) -> bool:
    """Check if table exists in database."""
    with conn.cursor() as cur:
        _ = cur.execute(
            sql.SQL(
                "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = %s AND table_name = %s)",
            ),
            (schema, table),
        )
        result = cur.fetchone()
        return bool(result[0]) if result else False


def count_rows(conn: p.DbConnection, schema: str, table: str) -> int:
    """Count rows in table."""
    with conn.cursor() as cur:
        _ = cur.execute(
            sql.SQL("SELECT COUNT(*) FROM {}.{}").format(
                sql.Identifier(schema),
                sql.Identifier(table),
            ),
        )
        result = cur.fetchone()
        return int(str(result[0])) if result else 0


def get_column_names(
    conn: p.DbConnection,
    schema: str,
    table: str,
) -> t.StrSequence:
    """Get column names for table."""
    with conn.cursor() as cur:
        _ = cur.execute(
            sql.SQL(
                "SELECT column_name FROM information_schema.columns WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position",
            ),
            (schema, table),
        )
        return [str(row[0]) for row in cur.fetchall()]
