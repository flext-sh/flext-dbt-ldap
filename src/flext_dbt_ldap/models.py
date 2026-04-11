"""Thin dbt-ldap models facade composed via MRO."""

from __future__ import annotations

from flext_dbt_ldap._models.configuration import FlextDbtLdapModelsConfiguration
from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema
from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoModels


class FlextDbtLdapModels(FlextMeltanoModels, FlextLdapModels):
    """Project-specific dbt-ldap models composed on top of parent facades."""

    class DbtLdap(
        FlextDbtLdapModelsDimensions,
        FlextDbtLdapModelsSchema,
        FlextDbtLdapModelsConfiguration,
        FlextDbtLdapModelsResults,
    ):
        """DBT LDAP domain model namespace."""


__all__ = ["FlextDbtLdapModels", "m"]

m = FlextDbtLdapModels
