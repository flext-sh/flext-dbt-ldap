"""FLEXT Dbt LDAP Types — MRO composition of parent type namespaces.

All structured data uses Pydantic models via FlextDbtLdapModels (m).
Canonical mapping/sequence types are inherited from t.Ldap and t.*.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import FlextLdapTypes
from flext_meltano import t


class FlextDbtLdapTypes(t, FlextLdapTypes):
    """MRO facade composing Meltano + LDAP type namespaces."""

    class DbtLdap:
        """DBT LDAP domain type contracts."""


t = FlextDbtLdapTypes
__all__: list[str] = ["FlextDbtLdapTypes", "t"]
