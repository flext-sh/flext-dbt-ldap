"""Behavior contract for the dbt LDAP connection profile."""

from __future__ import annotations

from flext_dbt_ldap import FlextDbtLdapServiceBase, m
from flext_meltano import p


def test_connection_profile_returns_typed_ldap_wire_shape() -> None:
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
