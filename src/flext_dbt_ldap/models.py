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
    FlextDbtLdapModelsConfig,
    FlextDbtLdapModelsDbt,
    FlextDbtLdapModelsDimensions,
    FlextDbtLdapModelsResults,
    FlextDbtLdapModelsSchema,
    FlextDbtLdapModelsShared,
)


class FlextDbtLdapModels(flext_meltano_m, m):
    """Project-specific dbt-ldap models composed on top of parent facades."""

    class DbtLdap(
        FlextDbtLdapModelsConfig,
        FlextDbtLdapModelsDbt,
        FlextDbtLdapModelsDimensions,
        FlextDbtLdapModelsResults,
        FlextDbtLdapModelsShared,
        FlextDbtLdapModelsSchema,
    ):
        """DBT LDAP domain model namespace."""


m = FlextDbtLdapModels
__all__: list[str] = ["FlextDbtLdapModels", "m"]
