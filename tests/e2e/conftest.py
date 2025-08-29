"""E2E test configuration and fixtures for dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Generator
from pathlib import Path
from subprocess import CompletedProcess

import docker
import psycopg
import pytest
from flext_core import FlextLogger

logger = FlextLogger(__name__)


@pytest.fixture(scope="session")
def docker_client() -> docker.DockerClient:
    """Get Docker client."""
    return docker.from_env()


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).parent.parent.parent


@pytest.fixture(scope="session")
def postgres_container(
    _docker_client: docker.DockerClient,
    project_root: Path,
) -> Generator[None]:
    """Start PostgreSQL container for testing."""
    compose_file = project_root / "docker-compose.yml"
    # Start containers
    logger.info("Starting PostgreSQL container...")

    async def _run(
        cmd_list: list[str],
        cwd: str | None = None,
        timeout_seconds: int = 120,
    ) -> int:
        process = await asyncio.create_subprocess_exec(
            *cmd_list,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd,
        )
        try:
            await asyncio.wait_for(process.communicate(), timeout=timeout_seconds)
        except TimeoutError:
            process.kill()
            await process.communicate()
            raise
        return process.returncode

    asyncio.run(
        _run(
            [
                "/usr/bin/docker-compose",
                "-f",
                str(compose_file),
                "up",
                "-d",
                "postgres",
            ],
            cwd=str(project_root),
        ),
    )
    # Wait for PostgreSQL to be ready
    max_retries = 30
    for i in range(max_retries):
        try:
            conn = psycopg.connect(
                host="localhost",
                port=25432,
                dbname="dbt_ldap_test",
                user="dbt_user",
                password="dbt_password",
            )
            conn.close()
            logger.info("PostgreSQL is ready")
            break
        except (RuntimeError, ValueError, TypeError):
            if i == max_retries - 1:
                raise
            logger.info("Waiting for PostgreSQL... (%s/%s)", i + 1, max_retries)
            time.sleep(2)
    yield
    # Stop containers
    logger.info("Stopping PostgreSQL container...")
    asyncio.run(
        _run(
            ["/usr/bin/docker-compose", "-f", str(compose_file), "down", "-v"],
            cwd=str(project_root),
        ),
    )


@pytest.fixture
def db_connection(_postgres_container: None) -> Generator[object]:
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
    command: list[str],
    project_dir: Path,
    profiles_dir: Path,
    dbt_vars: dict[str, object] | None = None,
) -> CompletedProcess[str]:
    """Run dbt command with proper configuration."""
    env = {
        "DBT_PROFILES_DIR": str(profiles_dir),
        "DBT_PROJECT_DIR": str(project_dir),
    }
    cmd = ["dbt", *command]
    if dbt_vars:
        var_string = " ".join(f"{k}:{v}" for k, v in dbt_vars.items())
        cmd.extend(["--vars", var_string])

    async def _run_db(
        cmd_list: list[str],
        cwd: str,
        env: dict[str, str],
    ) -> tuple[int, str, str]:
        process = await asyncio.create_subprocess_exec(
            *cmd_list,
            cwd=cwd,
            env=env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return process.returncode, stdout.decode(), stderr.decode()

    rc, out, err = asyncio.run(_run_db(cmd, str(project_dir), env))

    class CompletedProcess:
        def __init__(self, returncode: int, stdout: str, stderr: str) -> None:
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

    return CompletedProcess(rc, out, err)


def query_database(conn: object, query: str) -> list[tuple[object, ...]]:
    """Execute query and return results."""
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchall()
        return list(result)


def table_exists(conn: object, schema: str, table: str) -> bool:
    """Check if table exists in database."""
    with conn.cursor() as cur:
        cur.execute(
            """
          SELECT EXISTS (
              SELECT 1 FROM information_schema.tables
              WHERE table_schema = %s AND table_name = %s
          )
          """,
            (schema, table),
        )
        result = cur.fetchone()
        return bool(result[0]) if result else False


def count_rows(conn: object, schema: str, table: str) -> int:
    """Count rows in table."""
    with conn.cursor() as cur:
        cur.execute('SELECT COUNT(*) FROM "%s"."%s"', (schema, table))
        result = cur.fetchone()
        return int(result[0]) if result else 0


def get_column_names(conn: object, schema: str, table: str) -> list[str]:
    """Get column names for table."""
    with conn.cursor() as cur:
        cur.execute(
            """
          SELECT column_name
          FROM information_schema.columns
          WHERE table_schema = %s AND table_name = %s
          ORDER BY ordinal_position
          """,
            (schema, table),
        )
        return [row[0] for row in cur.fetchall()]
