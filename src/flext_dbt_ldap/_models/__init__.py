# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._models.config import FlextModelsDbtLdapConfig
    from flext_dbt_ldap._models.dbt import FlextModelsDbtLdapDbt
    from flext_dbt_ldap._models.dimensions import FlextModelsDbtLdapDimensions
    from flext_dbt_ldap._models.results import FlextModelsDbtLdapResults
    from flext_dbt_ldap._models.schema import FlextModelsDbtLdapSchema
    from flext_dbt_ldap._models.shared import FlextModelsDbtLdapShared


__all__: tuple[str, ...] = (
    "FlextModelsDbtLdapConfig",
    "FlextModelsDbtLdapDbt",
    "FlextModelsDbtLdapDimensions",
    "FlextModelsDbtLdapResults",
    "FlextModelsDbtLdapSchema",
    "FlextModelsDbtLdapShared",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextModelsDbtLdapConfig": ".config",
        "FlextModelsDbtLdapDbt": ".dbt",
        "FlextModelsDbtLdapDimensions": ".dimensions",
        "FlextModelsDbtLdapResults": ".results",
        "FlextModelsDbtLdapSchema": ".schema",
        "FlextModelsDbtLdapShared": ".shared",
    }),
    public_exports=__all__,
)
