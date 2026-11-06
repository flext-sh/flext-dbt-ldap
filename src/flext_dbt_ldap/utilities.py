# AUTO-GENERATED FILE — Regenerate with: make gen
"""Thin public utilities facade for flext-dbt-ldap.

Project-specific helpers are composed from private mixins; inherited parents
provide the generic LDAP and Meltano utility surfaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import u as flext_ldap_u
from flext_meltano import u as flext_meltano_u

from flext_dbt_ldap._utilities import (
    FlextDbtLdapUtilitiesIntegration,
    FlextDbtLdapUtilitiesMacros,
)


class FlextDbtLdapUtilities(flext_meltano_u, flext_ldap_u):
    """Thin dbt-ldap utilities facade following the canonical MRO pattern."""

    class DbtLdap(
        FlextDbtLdapUtilitiesIntegration,
        FlextDbtLdapUtilitiesMacros,
    ):
        """Project-specific dbt-ldap utility surface."""


u = FlextDbtLdapUtilities
__all__: list[str] = ["FlextDbtLdapUtilities", "u"]
