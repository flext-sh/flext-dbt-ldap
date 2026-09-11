# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Models package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .configuration import FlextDbtLdapModelsConfiguration
    from .dimensions import FlextDbtLdapModelsDimensions
    from .results import FlextDbtLdapModelsResults
    from .schema import FlextDbtLdapModelsSchema
    from .shared import FlextDbtLdapModelsShared
__all__: tuple[str, ...] = (
    "FlextDbtLdapModelsConfiguration",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".configuration": ("FlextDbtLdapModelsConfiguration",),
            ".dimensions": ("FlextDbtLdapModelsDimensions",),
            ".results": ("FlextDbtLdapModelsResults",),
            ".schema": ("FlextDbtLdapModelsSchema",),
            ".shared": ("FlextDbtLdapModelsShared",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
