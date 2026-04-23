"""FLEXT Dbt LDAP Types — MRO composition of parent type namespaces.

Only LdapEntryMapping is domain-specific and actively used.
All other structured data uses Pydantic models via FlextDbtLdapModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableMapping,
    Sequence,
)

from flext_ldap import FlextLdapTypes
from flext_meltano import t


class FlextDbtLdapTypes(t, FlextLdapTypes):
    """MRO facade composing Meltano + LDAP type namespaces."""

    class DbtLdap:
        """DBT LDAP domain type contracts."""

        type LdapAttributeValues = t.StrSequence
        "Multi-valued LDAP attribute payload."
        type LdapEntryMapping = Mapping[str, LdapAttributeValues]
        "Single LDAP entry: attribute name → list of string values."
        type MutableLdapEntryMapping = MutableMapping[str, LdapAttributeValues]
        "Mutable LDAP entry mapping used while normalizing raw records."
        type SerializableMapping = Mapping[str, t.JsonValue]
        "String-keyed serializable DBT payload item."
        type SerializableMappingSequence = Sequence[SerializableMapping]
        "Read-only sequence of serializable DBT payload items."


t = FlextDbtLdapTypes
__all__: list[str] = ["FlextDbtLdapTypes", "t"]
