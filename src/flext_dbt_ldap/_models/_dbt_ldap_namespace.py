"""Dbt ldap namespace module.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_models/_dbt_ldap_namespace
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap import m


class _DbtLdapNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)
