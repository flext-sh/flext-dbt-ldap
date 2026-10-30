"""Compose the canonical layer-zero DBT LDAP configuration declarations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap import FlextDbtLdapModelsConfigNamespace


class FlextModelsDbtLdapConfig(FlextDbtLdapModelsConfigNamespace):
    """Expose the single configuration schema owner through the model family."""


__all__: list[str] = ["FlextModelsDbtLdapConfig"]
