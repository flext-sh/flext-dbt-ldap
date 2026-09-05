# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .entry import FlextDbtLdapUtilitiesEntry
    from .integration import FlextDbtLdapUtilitiesIntegration
    from .macros import FlextDbtLdapUtilitiesMacros
__all__: tuple[str, ...] = (
    "FlextDbtLdapUtilitiesEntry",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".entry": ("FlextDbtLdapUtilitiesEntry",),
            ".integration": ("FlextDbtLdapUtilitiesIntegration",),
            ".macros": ("FlextDbtLdapUtilitiesMacros",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
