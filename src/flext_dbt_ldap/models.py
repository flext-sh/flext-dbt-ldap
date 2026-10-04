"""Thin dbt-ldap models facade composed via MRO.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoModels

from flext_dbt_ldap._models.configuration import FlextDbtLdapModelsConfiguration
from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema


class FlextDbtLdapModels(FlextMeltanoModels, FlextLdapModels):
    """Project-specific dbt-ldap models composed on top of parent facades."""

    class DbtLdap(
        FlextDbtLdapModelsDimensions,
        FlextDbtLdapModelsSchema,
        FlextDbtLdapModelsConfiguration,
        FlextDbtLdapModelsResults,
    ):
        """DBT LDAP domain model namespace."""


m = FlextDbtLdapModels

__all__: list[str] = ["FlextDbtLdapModels", "m"]
