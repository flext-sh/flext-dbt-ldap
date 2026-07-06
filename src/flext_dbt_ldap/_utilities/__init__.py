# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._utilities.entry import (
        FlextDbtLdapUtilitiesEntry as FlextDbtLdapUtilitiesEntry,
    )
    from flext_dbt_ldap._utilities.integration import (
        FlextDbtLdapUtilitiesIntegration as FlextDbtLdapUtilitiesIntegration,
    )
    from flext_dbt_ldap._utilities.macros import (
        FlextDbtLdapUtilitiesMacros as FlextDbtLdapUtilitiesMacros,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".entry": ("FlextDbtLdapUtilitiesEntry",),
        ".integration": ("FlextDbtLdapUtilitiesIntegration",),
        ".macros": ("FlextDbtLdapUtilitiesMacros",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
