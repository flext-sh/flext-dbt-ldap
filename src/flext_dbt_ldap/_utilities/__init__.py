# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._utilities.entry import FlextDbtLdapUtilitiesEntry
    from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
    from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros


__all__: tuple[str, ...] = (
    "FlextDbtLdapUtilitiesEntry",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdapUtilitiesEntry": ".entry",
        "FlextDbtLdapUtilitiesIntegration": ".integration",
        "FlextDbtLdapUtilitiesMacros": ".macros",
    }),
    public_exports=__all__,
)
