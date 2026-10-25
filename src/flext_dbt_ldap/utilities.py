# AUTO-GENERATED FILE — Regenerate with: make gen
"""Thin public utilities facade for flext-dbt-ldap.

Project-specific helpers are composed from private mixins; inherited parents
provide the generic LDAP and Meltano utility surfaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import FlextLdapUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_dbt_ldap._utilities import (
    FlextDbtLdapUtilitiesEntry,
    FlextDbtLdapUtilitiesIntegration,
    FlextDbtLdapUtilitiesMacros,
)


class FlextDbtLdapUtilities(FlextMeltanoUtilities, FlextLdapUtilities):
    """Thin dbt-ldap utilities facade following the canonical MRO pattern."""

    class DbtLdap(
        FlextDbtLdapUtilitiesIntegration,
        FlextDbtLdapUtilitiesEntry,
        FlextDbtLdapUtilitiesMacros,
    ):
        """Project-specific dbt-ldap utility surface."""


u = FlextDbtLdapUtilities
__all__: list[str] = ["FlextDbtLdapUtilities", "u"]
