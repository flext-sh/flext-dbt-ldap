# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._models.configuration import FlextDbtLdapModelsConfiguration
    from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
    from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
    from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema
    from flext_dbt_ldap._models.shared import FlextDbtLdapModelsShared
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".configuration": ("FlextDbtLdapModelsConfiguration",),
        ".dimensions": ("FlextDbtLdapModelsDimensions",),
        ".results": ("FlextDbtLdapModelsResults",),
        ".schema": ("FlextDbtLdapModelsSchema",),
        ".shared": ("FlextDbtLdapModelsShared",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
