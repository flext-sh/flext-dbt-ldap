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
    from flext_dbt_ldap._models.config import FlextDbtLdapModelsConfig
    from flext_dbt_ldap._models.dbt import FlextDbtLdapModelsDbt
    from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
    from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
    from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema


__all__: tuple[str, ...] = (
    "FlextDbtLdapModelsConfig",
    "FlextDbtLdapModelsDbt",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdapModelsConfig": ".config",
        "FlextDbtLdapModelsDbt": ".dbt",
        "FlextDbtLdapModelsDimensions": ".dimensions",
        "FlextDbtLdapModelsResults": ".results",
        "FlextDbtLdapModelsSchema": ".schema",
        "FlextDbtLdapModelsShared": ".base",
    }),
    public_exports=__all__,
)
