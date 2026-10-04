# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._models.configuration import FlextDbtLdapModelsConfiguration
    from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
    from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
    from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema
    from flext_dbt_ldap._models.shared import FlextDbtLdapModelsShared


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
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
