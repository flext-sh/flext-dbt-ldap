"""Test constants for flext-dbt-ldap tests."""

from __future__ import annotations

from typing import Final

from flext_tests import FlextTestsConstants

from flext_dbt_ldap import FlextDbtLdapConstants


class TestsFlextDbtLdapConstants(FlextTestsConstants, FlextDbtLdapConstants):
    """Constants for flext-dbt-ldap tests."""

    class DbtLdap(FlextDbtLdapConstants.DbtLdap):
        """DBT LDAP domain test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """DBT LDAP-specific test constants."""

            class E2E:
                """E2E constants for DBT LDAP tests."""

                POSTGRES_READY_MAX_RETRIES: Final[int] = 30


c = TestsFlextDbtLdapConstants
__all__: list[str] = ["TestsFlextDbtLdapConstants", "c"]
