from __future__ import annotations

from flext_dbt_ldap import m


class _DbtLdapNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)
