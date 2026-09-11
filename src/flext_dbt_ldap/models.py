"""Thin dbt-ldap models facade composed via MRO."""

from __future__ import annotations

from flext_ldap import FlextLdapModels
from flext_meltano import m

from ._models.configuration import FlextDbtLdapModelsConfiguration
from ._models.dimensions import FlextDbtLdapModelsDimensions
from ._models.results import FlextDbtLdapModelsResults
from ._models.schema import FlextDbtLdapModelsSchema


class FlextDbtLdapModels(m, FlextLdapModels):
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
