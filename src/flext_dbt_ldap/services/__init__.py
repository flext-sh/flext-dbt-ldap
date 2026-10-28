# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap.services.client import FlextDbtLdapClient
    from flext_dbt_ldap.services.sync import FlextDbtLdapSync


__all__: tuple[str, ...] = ("FlextDbtLdapClient", "FlextDbtLdapSync")

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdapClient": ".client",
        "FlextDbtLdapSync": ".sync",
    }),
    public_exports=__all__,
)
