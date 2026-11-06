"""DBT LDAP protocol contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


class FlextDbtLdapProtocolsBase:
    """DBT LDAP protocol contracts composed into ``p.DbtLdap``."""

    @runtime_checkable
    class DataFrameLike(Protocol):
        """Protocol for DataFrame-like objects used in DBT Python models."""

        def __len__(self) -> int:
            """Return the number of rows in the DataFrame."""
            ...


__all__: list[str] = ["FlextDbtLdapProtocolsBase"]
