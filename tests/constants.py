"""Test constants for flext-dbt-ldap tests."""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_dbt_ldap import FlextDbtLdapConstants


class FlextDbtLdapTestConstants(FlextTestsConstants, FlextDbtLdapConstants):
    """Constants for flext-dbt-ldap tests."""


c = FlextDbtLdapTestConstants
__all__ = ["FlextDbtLdapTestConstants", "c"]
