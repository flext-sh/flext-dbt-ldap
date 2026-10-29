# AUTO-GENERATED FILE — Regenerate with: make gen
"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import p as flext_ldap_p
from flext_meltano import p as flext_meltano_p

from flext_dbt_ldap._protocols import FlextDbtLdapProtocolsBase


class FlextDbtLdapProtocols(flext_meltano_p, flext_ldap_p):
    """DBT LDAP protocols extending LDAP and Meltano protocols."""

    class DbtLdap(FlextDbtLdapProtocolsBase):
        """DBT domain protocols."""


p = FlextDbtLdapProtocols
__all__: list[str] = ["FlextDbtLdapProtocols", "p"]
