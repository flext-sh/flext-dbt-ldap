"""Test constants for flext-dbt-ldap tests.

Centralized constants for test fixtures, factories, and test data.
Does NOT duplicate src/flext_dbt_ldap/constants.py - only test-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class TestConstants:
    """Centralized test constants following flext-core nested class pattern."""

    class Paths:
        """Test path constants."""

        TEST_INPUT_DIR: Final[str] = "tests/fixtures/data/input"
        TEST_OUTPUT_DIR: Final[str] = "tests/fixtures/data/output"
        TEST_TEMP_PREFIX: Final[str] = "flext_dbt_ldap_test_"
        TEST_PROFILES_DIR: Final[str] = "tests/fixtures/profiles"

    class Dbt:
        """DBT test constants."""

        TEST_TARGET: Final[str] = "dev"
        TEST_PROFILE: Final[str] = "test_profile"
        TEST_PROJECT_DIR: Final[str] = "tests/fixtures/dbt_project"
        TEST_MODEL_NAME: Final[str] = "test_model"
        TEST_SOURCE_NAME: Final[str] = "test_source"

    class Ldap:
        """LDAP test constants."""

        TEST_HOST: Final[str] = "localhost"
        TEST_PORT: Final[int] = 389
        TEST_BASE_DN: Final[str] = "dc=test,dc=com"
        TEST_BIND_DN: Final[str] = "cn=REDACTED_LDAP_BIND_PASSWORD,dc=test,dc=com"
        TEST_BIND_PASSWORD: Final[str] = "test_password"

    class Transformation:
        """Transformation test constants."""

        TEST_SCHEMA_MAPPING: Final[dict[str, str]] = {
            "users": "stg_users",
            "groups": "stg_groups",
        }
        TEST_BATCH_SIZE: Final[int] = 1000
