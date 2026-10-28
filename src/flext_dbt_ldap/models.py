# AUTO-GENERATED FILE — Regenerate with: make gen
"""Thin dbt-ldap models facade composed via MRO.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import m
from flext_meltano import m as flext_meltano_m

from flext_dbt_ldap._models import (
    FlextModelsDbtLdapConfig,
    FlextModelsDbtLdapDbt,
    FlextModelsDbtLdapDimensions,
    FlextModelsDbtLdapResults,
    FlextModelsDbtLdapSchema,
    FlextModelsDbtLdapShared,
)


class FlextModelsDbtLdap(flext_meltano_m, m):
    """Project-specific dbt-ldap models composed on top of parent facades."""

    class DbtLdap(
        FlextModelsDbtLdapConfig,
        FlextModelsDbtLdapDbt,
        FlextModelsDbtLdapDimensions,
        FlextModelsDbtLdapResults,
        FlextModelsDbtLdapShared,
        FlextModelsDbtLdapSchema,
    ):
        """DBT LDAP domain model namespace."""


m = FlextModelsDbtLdap
__all__: list[str] = ["FlextModelsDbtLdap", "m"]
