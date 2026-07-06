# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._constants.attributes import FlextDbtLdapConstantsAttributes
    from flext_dbt_ldap._constants.base import FlextDbtLdapConstantsBase
    from flext_dbt_ldap._constants.search import FlextDbtLdapConstantsSearch
    from flext_dbt_ldap._constants.transformation import (
        FlextDbtLdapConstantsTransformation,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".attributes": ("FlextDbtLdapConstantsAttributes",),
        ".base": ("FlextDbtLdapConstantsBase",),
        ".search": ("FlextDbtLdapConstantsSearch",),
        ".transformation": ("FlextDbtLdapConstantsTransformation",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
