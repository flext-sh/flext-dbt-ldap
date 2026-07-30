# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Constants package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .attributes import (
        FlextDbtLdapConstantsAttributes as FlextDbtLdapConstantsAttributes,
    )
    from .base import FlextDbtLdapConstantsBase as FlextDbtLdapConstantsBase
    from .search import FlextDbtLdapConstantsSearch as FlextDbtLdapConstantsSearch
    from .transformation import (
        FlextDbtLdapConstantsTransformation as FlextDbtLdapConstantsTransformation,
    )

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".attributes": ("FlextDbtLdapConstantsAttributes",),
    ".base": ("FlextDbtLdapConstantsBase",),
    ".search": ("FlextDbtLdapConstantsSearch",),
    ".transformation": ("FlextDbtLdapConstantsTransformation",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
