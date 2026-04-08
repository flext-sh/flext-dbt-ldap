# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Constants package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_dbt_ldap._constants.attributes as _flext_dbt_ldap__constants_attributes

    attributes = _flext_dbt_ldap__constants_attributes
    import flext_dbt_ldap._constants.base as _flext_dbt_ldap__constants_base
    from flext_dbt_ldap._constants.attributes import FlextDbtLdapConstantsAttributes

    base = _flext_dbt_ldap__constants_base
    import flext_dbt_ldap._constants.search as _flext_dbt_ldap__constants_search
    from flext_dbt_ldap._constants.base import FlextDbtLdapConstantsBase

    search = _flext_dbt_ldap__constants_search
    import flext_dbt_ldap._constants.transformation as _flext_dbt_ldap__constants_transformation
    from flext_dbt_ldap._constants.search import FlextDbtLdapConstantsSearch

    transformation = _flext_dbt_ldap__constants_transformation
    from flext_dbt_ldap._constants.transformation import (
        FlextDbtLdapConstantsTransformation,
    )
_LAZY_IMPORTS = {
    "FlextDbtLdapConstantsAttributes": (
        "flext_dbt_ldap._constants.attributes",
        "FlextDbtLdapConstantsAttributes",
    ),
    "FlextDbtLdapConstantsBase": (
        "flext_dbt_ldap._constants.base",
        "FlextDbtLdapConstantsBase",
    ),
    "FlextDbtLdapConstantsSearch": (
        "flext_dbt_ldap._constants.search",
        "FlextDbtLdapConstantsSearch",
    ),
    "FlextDbtLdapConstantsTransformation": (
        "flext_dbt_ldap._constants.transformation",
        "FlextDbtLdapConstantsTransformation",
    ),
    "attributes": "flext_dbt_ldap._constants.attributes",
    "base": "flext_dbt_ldap._constants.base",
    "search": "flext_dbt_ldap._constants.search",
    "transformation": "flext_dbt_ldap._constants.transformation",
}

__all__ = [
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
    "attributes",
    "base",
    "search",
    "transformation",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
