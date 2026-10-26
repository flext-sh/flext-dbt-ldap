# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT DBT LDAP Constants - Thin MRO Facade.

from flext_core import FlextConstants as Constants

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import c
from flext_meltano import c as flext_meltano_c

from flext_dbt_ldap._constants import (
    FlextDbtLdapConstantsAttributes,
    FlextDbtLdapConstantsBase,
    FlextDbtLdapConstantsSearch,
    FlextDbtLdapConstantsTransformation,
)


class FlextDbtLdapConstants(flext_meltano_c, c):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern.

    This class acts as a facade, composing all constant subclasses via MRO.
    All constants are accessible via inheritance—do not duplicate parent attributes.

    LDAP protocol constants are inherited from c.Ldap via MRO:
    - c.Ldap.PORT / c.Ldap.TIMEOUT
    - c.Ldap.AttributeName (DN, OBJECT_CLASS, COMMON_NAME — protocol-only)
    - c.Ldap.ALL_ENTRIES_FILTER (protocol-level wildcard)

    Domain-specific constants (attributes, filters, models, types) live here.
    """

    class DbtLdap(
        FlextDbtLdapConstantsAttributes,
        FlextDbtLdapConstantsBase,
        FlextDbtLdapConstantsSearch,
        FlextDbtLdapConstantsTransformation,
    ):
        """DBT LDAP constants namespace composed over the family base."""


c = FlextDbtLdapConstants
__all__: list[str] = ["FlextDbtLdapConstants", "c"]
