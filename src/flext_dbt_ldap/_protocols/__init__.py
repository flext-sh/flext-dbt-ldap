# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._protocols.base import FlextDbtLdapProtocolsBase
    from flext_dbt_ldap._protocols.dbt import FlextDbtLdapProtocolsDbt
    from flext_dbt_ldap._protocols.dimensions import FlextDbtLdapProtocolsDimensions
    from flext_dbt_ldap._protocols.results import FlextDbtLdapProtocolsResults
    from flext_dbt_ldap._protocols.schema import FlextDbtLdapProtocolsSchema
    from flext_dbt_ldap._protocols.shared import FlextDbtLdapProtocolsShared


__all__: tuple[str, ...] = (
    "FlextDbtLdapProtocolsBase",
    "FlextDbtLdapProtocolsDbt",
    "FlextDbtLdapProtocolsDimensions",
    "FlextDbtLdapProtocolsResults",
    "FlextDbtLdapProtocolsSchema",
    "FlextDbtLdapProtocolsShared",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtLdapProtocolsBase": ".base",
        "FlextDbtLdapProtocolsDbt": ".dbt",
        "FlextDbtLdapProtocolsDimensions": ".dimensions",
        "FlextDbtLdapProtocolsResults": ".results",
        "FlextDbtLdapProtocolsSchema": ".schema",
        "FlextDbtLdapProtocolsShared": ".shared",
    },
    public_exports=__all__,
)
