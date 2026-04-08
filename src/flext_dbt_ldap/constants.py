"""FLEXT DBT LDAP Constants - Thin MRO Facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap import (
    FlextDbtLdapConstantsAttributes,
    FlextDbtLdapConstantsBase,
    FlextDbtLdapConstantsSearch,
    FlextDbtLdapConstantsTransformation,
)
from flext_ldap import FlextLdapConstants
from flext_meltano import FlextMeltanoConstants


class FlextDbtLdapConstants(
    FlextMeltanoConstants,
    FlextLdapConstants,
):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern.

    This class acts as a facade, composing all constant subclasses via MRO.
    All constants are accessible via inheritance—do not duplicate parent attributes.

    LDAP protocol constants are inherited from c.Ldap via MRO:
    - c.Ldap.ConnectionDefaults (PORT, TIMEOUT)
    - c.Ldap.LdapAttributeNames (DN, OBJECT_CLASS, COMMON_NAME — protocol-only)
    - c.Ldap.Filters.ALL_ENTRIES_FILTER (protocol-level wildcard)

    Domain-specific constants (attributes, filters, models, data types) live in this class.
    """

    class DbtLdap(
        FlextDbtLdapConstantsTransformation,
        FlextDbtLdapConstantsSearch,
        FlextDbtLdapConstantsAttributes,
        FlextDbtLdapConstantsBase,
    ):
        """Class."""


c = FlextDbtLdapConstants

__all__ = ["FlextDbtLdapConstants", "c"]
