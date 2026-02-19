"""FLEXT DBT LDAP Types - Domain-specific type definitions.

Only Literal types and truly domain-specific complex types.
All structured data uses Pydantic models via FlextDbtLdapModels (m).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes


class FlextDbtLdapTypes(FlextTypes):
    """DBT LDAP-specific type definitions extending FlextTypes.

    All structured data uses Pydantic models in models.py.
    This module only contains Literal types and type variables.
    """

    class DbtTransformation:
        """DBT LDAP transformation type contracts."""

        type DataValidation = dict[str, str | list[str] | bool]
        """Data validation configuration contract."""

    class DbtLdap:
        """DBT LDAP settings type contracts."""

        type SettingsDict = dict[str, bool | float | str | None]
        """DBT LDAP logging settings configuration contract."""

    class Project:
        """DBT LDAP-specific project types."""

        type DbtLdapProjectType = Literal[
            "library",
            "application",
            "service",
            "dbt-ldap",
            "ldap-transform",
            "directory-analytics",
            "ldap-dbt-models",
            "dbt-ldap-project",
            "ldap-dimensional",
            "directory-warehouse",
            "ldap-etl",
            "dbt-ldap-pipeline",
            "ldap-analytics",
            "directory-dbt",
            "ldap-data-warehouse",
        ]
        """DBT LDAP project type literal."""


# Alias for simplified usage
t = FlextDbtLdapTypes

__all__ = [
    "FlextDbtLdapTypes",
    "t",
]
