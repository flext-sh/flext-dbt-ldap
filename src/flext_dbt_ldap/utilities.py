"""Thin public utilities facade for flext-dbt-ldap.

Project-specific helpers are composed from private mixins; inherited parents
provide the generic LDAP and Meltano utility surfaces.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_ldap import FlextLdapUtilities
from flext_meltano import u

from ._utilities.integration import FlextDbtLdapUtilitiesIntegration
from ._utilities.macros import FlextDbtLdapUtilitiesMacros

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapUtilities(u, FlextLdapUtilities):
    """Thin dbt-ldap utilities facade following the canonical MRO pattern."""

    class DbtLdap(FlextDbtLdapUtilitiesMacros, FlextDbtLdapUtilitiesIntegration):
        """Project-specific dbt-ldap utility surface."""


__all__: t.MutableSequenceOf[str] = ["FlextDbtLdapUtilities", "u"]

u = FlextDbtLdapUtilities
