# AUTO-GENERATED FILE — Regenerate with: make gen
"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import FlextLdapProtocols
from flext_meltano import FlextMeltanoProtocols

from flext_dbt_ldap._protocols import FlextDbtLdapProtocolsBase


class FlextDbtLdapProtocols(FlextMeltanoProtocols, FlextLdapProtocols):
    """DBT LDAP protocols extending LDAP and Meltano protocols."""

    class DbtLdap:
        """DBT domain protocols."""

        DataFrameLike = FlextDbtLdapProtocolsBase.DataFrameLike


p = FlextDbtLdapProtocols

__all__: list[str] = ["FlextDbtLdapProtocols", "p"]
