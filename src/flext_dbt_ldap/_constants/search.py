"""FlextDbtLdapConstantsSearch - LDAP search and filter constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar


class FlextDbtLdapConstantsSearch:
    """Project-specific LDAP search filters and configurations."""

    FILTER_USER: ClassVar[str] = "(objectClass=person)"
    FILTER_GROUP: ClassVar[str] = "(objectClass=group)"
    FILTER_MEMBERSHIP: ClassVar[str] = "(|(objectClass=person)(objectClass=group))"

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

    LDAPS_DEFAULT_PORT: ClassVar[int] = 636


__all__: list[str] = ["FlextDbtLdapConstantsSearch"]
