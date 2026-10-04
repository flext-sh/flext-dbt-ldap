"""Behavior contract for the dbt LDAP connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_connection_profile
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import p

from flext_dbt_ldap import FlextDbtLdapServiceBase, m


def test_connection_profile_returns_typed_ldap_wire_shape() -> None:
    """Test connection profile returns typed ldap wire shape."""
    profile = FlextDbtLdapServiceBase().connection_profile

    assert isinstance(profile, m.DbtLdap.DbtConnectionProfile)
    assert isinstance(profile, p.Meltano.DbtConnectionProfile)
    assert profile.model_dump() == {
        "type": "ldap",
        "host": profile.host,
        "port": profile.port,
        "use_tls": profile.use_tls,
        "base_dn": profile.base_dn,
        "project": "dbt-ldap",
    }
