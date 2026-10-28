"""DBT LDAP config namespace models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class FlextModelsDbtLdapConfig:
    """Config namespace models for model-less ``config/*.yaml`` exposure."""

    class DbtLdapNamespace(BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain."""

        model_config = ConfigDict(extra="allow", frozen=True)


__all__: list[str] = ["FlextModelsDbtLdapConfig"]
