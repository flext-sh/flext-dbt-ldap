"""Thin public utilities facade for flext-dbt-ldap.

Project-specific helpers are composed from private mixins; inherited parents
provide the generic LDAP and Meltano utility surfaces.
"""

from __future__ import annotations

from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros
from flext_ldap import FlextLdapUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextDbtLdapUtilities(FlextMeltanoUtilities, FlextLdapUtilities):
    """Thin dbt-ldap utilities facade following the canonical MRO pattern."""

    class DbtLdap(
        FlextDbtLdapUtilitiesMacros,
        FlextDbtLdapUtilitiesIntegration,
    ):
        """Project-specific dbt-ldap utility surface."""


__all__ = ["FlextDbtLdapUtilities", "u"]

u = FlextDbtLdapUtilities
