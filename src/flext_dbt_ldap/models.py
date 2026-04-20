"""Thin dbt-ldap models facade composed via MRO."""

from __future__ import annotations

from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoModels

from flext_dbt_ldap import (
    FlextDbtLdapModelsConfiguration,
    FlextDbtLdapModelsDimensions,
    FlextDbtLdapModelsResults,
    FlextDbtLdapModelsSchema,
)


class FlextDbtLdapModels(FlextMeltanoModels, FlextLdapModels):
    """Project-specific dbt-ldap models composed on top of parent facades."""

    class DbtLdap(
        FlextDbtLdapModelsDimensions,
        FlextDbtLdapModelsSchema,
        FlextDbtLdapModelsConfiguration,
        FlextDbtLdapModelsResults,
    ):
        """DBT LDAP domain model namespace."""


__all__: list[str] = ["FlextDbtLdapModels", "m"]

m = FlextDbtLdapModels
