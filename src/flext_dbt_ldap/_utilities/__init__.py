# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import defer_lazy_bases, install_lazy_exports

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
    {
        "FlextDbtLdapUtilitiesEntry": ".entry",
        "FlextDbtLdapUtilitiesIntegration": ".integration",
        "FlextDbtLdapUtilitiesMacros": ".macros",
    },
    public_exports=__all__,
    deferred_members={
        "FlextDbtLdapUtilitiesEntry": (
            "_log",
            "active_entry",
            "group_entry",
            "user_entry",
        ),
        "FlextDbtLdapUtilitiesIntegration": (
            "_log",
            "transform_groups",
            "transform_memberships",
            "transform_users",
            "_extract_group_memberships",
            "_extract_user_memberships",
            "_transform_entries_to_dimensions",
        ),
        "FlextDbtLdapUtilitiesMacros": ("user_active",),
    },
)

defer_lazy_bases(
    __name__,
    {
        "FlextDbtLdapUtilitiesIntegration": ((".", "FlextDbtLdapUtilitiesEntry"),),
    },
)
