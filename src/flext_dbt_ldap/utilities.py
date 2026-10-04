"""Thin public utilities facade for flext-dbt-ldap.

Project-specific helpers are composed from private mixins; inherited parents
provide the generic LDAP and Meltano utility surfaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_ldap import FlextLdapUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapUtilities(FlextMeltanoUtilities, FlextLdapUtilities):
    """Thin dbt-ldap utilities facade following the canonical MRO pattern."""

    class DbtLdap(FlextDbtLdapUtilitiesMacros, FlextDbtLdapUtilitiesIntegration):
        """Project-specific dbt-ldap utility surface."""


u = FlextDbtLdapUtilities

__all__: t.MutableSequenceOf[str] = ["FlextDbtLdapUtilities", "u"]
