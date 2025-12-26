"""Constants for flext-dbt-ldap tests.

Provides TestsFlextDbtLdapConstants, extending FlextTestsConstants with flext-dbt-ldap-specific
constants using COMPOSITION INHERITANCE.

Inheritance hierarchy:
- FlextTestsConstants (flext_tests) - Provides .Tests.* namespace
- FlextDbtLdapConstants (production) - Provides .DbtLdap.* namespace

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_tests.constants import FlextTestsConstants

from flext_dbt_ldap.constants import FlextDbtLdapConstants


class TestsFlextDbtLdapConstants(FlextTestsConstants, FlextDbtLdapConstants):
    """Constants for flext-dbt-ldap tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsConstants - for test infrastructure (.Tests.*)
    2. FlextDbtLdapConstants - for domain constants (.DbtLdap.*)

    Access patterns:
    - tc.Tests.Docker.* (container testing)
    - tc.Tests.Matcher.* (assertion messages)
    - tc.Tests.Factory.* (test data generation)
    - tc.DbtLdap.* (domain constants from production)
    - tc.TestDbt.* (project-specific test data)

    Rules:
    - NEVER duplicate constants from FlextTestsConstants or FlextDbtLdapConstants
    - Only flext-dbt-ldap-specific test constants allowed
    - All generic constants come from FlextTestsConstants
    - All production constants come from FlextDbtLdapConstants
    """

    class Paths:
        """Test path constants."""

        TEST_INPUT_DIR: Final[str] = "tests/fixtures/data/input"
        TEST_OUTPUT_DIR: Final[str] = "tests/fixtures/data/output"
        TEST_TEMP_PREFIX: Final[str] = "flext_dbt_ldap_test_"
        TEST_PROFILES_DIR: Final[str] = "tests/fixtures/profiles"

    class TestDbt:
        """DBT test constants."""

        TEST_TARGET: Final[str] = "dev"
        TEST_PROFILE: Final[str] = "test_profile"
        TEST_PROJECT_DIR: Final[str] = "tests/fixtures/dbt_project"
        TEST_MODEL_NAME: Final[str] = "test_model"
        TEST_SOURCE_NAME: Final[str] = "test_source"

    class TestLdap:
        """LDAP test constants."""

        TEST_HOST: Final[str] = "localhost"
        TEST_PORT: Final[int] = 389
        TEST_BASE_DN: Final[str] = "dc=test,dc=com"
        TEST_BIND_DN: Final[str] = "cn=admin,dc=test,dc=com"
        TEST_BIND_PASSWORD: Final[str] = "test_password"

    class TestTransformation:
        """Transformation test constants."""

        TEST_SCHEMA_MAPPING: Final[dict[str, str]] = {
            "users": "stg_users",
            "groups": "stg_groups",
        }
        TEST_BATCH_SIZE: Final[int] = 1000


# Short aliases per FLEXT convention
tc = TestsFlextDbtLdapConstants  # Primary test constants alias
c = TestsFlextDbtLdapConstants  # Alternative alias for compatibility

__all__ = [
    "TestsFlextDbtLdapConstants",
    "c",
    "tc",
]
