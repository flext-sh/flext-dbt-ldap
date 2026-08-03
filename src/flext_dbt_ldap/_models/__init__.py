# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .configuration import (
        FlextDbtLdapModelsConfiguration as FlextDbtLdapModelsConfiguration,
    )
    from .dimensions import FlextDbtLdapModelsDimensions as FlextDbtLdapModelsDimensions
    from .results import FlextDbtLdapModelsResults as FlextDbtLdapModelsResults
    from .schema import FlextDbtLdapModelsSchema as FlextDbtLdapModelsSchema
    from .shared import FlextDbtLdapModelsShared as FlextDbtLdapModelsShared

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".configuration": ("FlextDbtLdapModelsConfiguration",),
    ".dimensions": ("FlextDbtLdapModelsDimensions",),
    ".results": ("FlextDbtLdapModelsResults",),
    ".schema": ("FlextDbtLdapModelsSchema",),
    ".shared": ("FlextDbtLdapModelsShared",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtLdapModelsConfiguration",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
