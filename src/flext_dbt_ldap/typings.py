"""FLEXT DBT LDAP Types - Domain-specific type definitions.

Only Literal types and truly domain-specific complex types.
All structured data uses Pydantic models via FlextDbtLdapModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldap import FlextLdapTypes
from flext_meltano import FlextMeltanoTypes

from flext_dbt_ldap import c


class FlextDbtLdapTypes(FlextMeltanoTypes, FlextLdapTypes):
    """DBT LDAP-specific type definitions extending FlextTypes.

    All structured data uses Pydantic models in models.py.
    This module only contains Literal types and type variables.
    """

    class DbtTransformation:
        """DBT LDAP transformation type contracts."""

        type DataValidation = dict[str, str | list[str] | bool]
        "Data validation configuration contract."

    class DbtLdap:
        """DBT LDAP settings type contracts."""

        type SettingsDict = dict[str, bool | float | str | None]
        "DBT LDAP logging settings configuration contract."

    class Project:
        """DBT LDAP-specific project types."""

        type DbtLdapProjectType = c.DbtLdapProjectType
        "DBT LDAP project type literal."


t = FlextDbtLdapTypes
__all__ = ["FlextDbtLdapTypes", "t"]
