# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._constants.attributes import FlextDbtLdapConstantsAttributes
    from flext_dbt_ldap._constants.base import FlextDbtLdapConstantsBase
    from flext_dbt_ldap._constants.search import FlextDbtLdapConstantsSearch
    from flext_dbt_ldap._constants.transformation import (
        FlextDbtLdapConstantsTransformation,
    )


__all__: tuple[str, ...] = (
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".attributes": ("FlextDbtLdapConstantsAttributes",),
            ".base": ("FlextDbtLdapConstantsBase",),
            ".search": ("FlextDbtLdapConstantsSearch",),
            ".transformation": ("FlextDbtLdapConstantsTransformation",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
