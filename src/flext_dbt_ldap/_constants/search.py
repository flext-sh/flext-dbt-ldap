"""FlextDbtLdapConstantsSearch - LDAP search and filter constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar, Final


class FlextDbtLdapConstantsSearch:
    """Project-specific LDAP search filters and configurations."""

    FILTER_USER: Final[str] = "(objectClass=person)"
    FILTER_GROUP: Final[str] = "(objectClass=group)"
    FILTER_MEMBERSHIP: Final[str] = "(|(objectClass=person)(objectClass=group))"

    SEARCH_GROUP: ClassVar[tuple[str, ...]] = (
        "cn",
        "description",
        "member",
        "groupType",
    )
    SEARCH_MEMBERSHIP: ClassVar[tuple[str, ...]] = (
        "cn",
        "member",
        "memberOf",
        "uniqueMember",
    )

    LDAPS_DEFAULT_PORT: Final[int] = 636
