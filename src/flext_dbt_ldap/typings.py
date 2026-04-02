"""FLEXT Dbt LDAP Types — MRO composition of parent type namespaces.

Only LdapEntryMapping is domain-specific and actively used.
All other structured data uses Pydantic models via FlextDbtLdapModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping

from flext_ldap import FlextLdapTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtLdapTypes(FlextMeltanoTypes, FlextLdapTypes):
    """MRO facade composing Meltano + LDAP type namespaces."""

    class DbtLdap:
        """DBT LDAP domain type contracts."""

        type LdapEntryMapping = Mapping[str, FlextMeltanoTypes.StrSequence]
        "Single LDAP entry: attribute name → list of string values."


t = FlextDbtLdapTypes
__all__ = ["FlextDbtLdapTypes", "t"]
