# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap.services.client import FlextDbtLdapClientMixin
    from flext_dbt_ldap.services.sync import FlextDbtLdapSyncMixin


__all__: tuple[str, ...] = ("FlextDbtLdapClientMixin", "FlextDbtLdapSyncMixin")

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".client": ("FlextDbtLdapClientMixin",),
            ".sync": ("FlextDbtLdapSyncMixin",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
