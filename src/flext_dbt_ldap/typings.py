"""FLEXT DBT LDAP Types - Domain-specific DBT LDAP type definitions.

This module provides DBT LDAP-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# DBT LDAP-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDAP operations
# =============================================================================


# DBT LDAP domain TypeVars
class FlextDbtLdapTypes(FlextTypes):
    """DBT LDAP-specific type definitions extending FlextTypes.

    Domain-specific type system for DBT LDAP data transformation operations.
    Contains ONLY complex DBT LDAP-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # CORE DBT LDAP TYPES - Commonly used type aliases extending FlextTypes.Core
    # =========================================================================

    class Core(FlextTypes.Core):
        """Core DBT LDAP types extending FlextTypes.Core.

        Replaces generic dict[str, object] with semantic DBT LDAP types.
        """

        # Configuration and settings types
        type ConfigDict = dict[str, FlextTypes.Core.ConfigValue | dict[str, object]]
        type ConnectionDict = dict[str, object]
        type LdapConfigDict = dict[str, object]
        type DbtConfigDict = dict[str, object]
        type ProjectDict = dict[str, object]

        # Data processing types
        type DataDict = dict[str, object]
        type ModelDict = dict[str, object]
        type SourceDict = dict[str, object]
        type TransformDict = dict[str, object]
        type ValidationDict = dict[str, object]

        # Template and structured response types
        type TemplateDict = dict[str, str | dict[str, object]]
        type ResponseDict = dict[str, object]
        type ResultDict = dict[str, object]
        type MetricsDict = dict[str, object]

        # Operation and context types
        type OperationDict = dict[str, object]
        type ContextDict = dict[str, object]
        type SettingsDict = dict[str, object]

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types."""

        type ProjectConfiguration = dict[
            str, FlextTypes.Core.ConfigValue | dict[str, object]
        ]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type SourceConfiguration = dict[str, str | list[dict[str, object]]]
        type ProfileConfiguration = dict[str, FlextTypes.Core.ConfigValue]
        type MacroConfiguration = dict[str, str | dict[str, object]]
        type TestConfiguration = dict[str, str | bool | list[str]]

    # =========================================================================
    # LDAP CONNECTION TYPES - LDAP server connection configuration
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | dict[str, object]]
        type AuthenticationConfig = dict[
            str, str | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ServerConfig = dict[str, str | int | bool | list[str]]
        type TlsConfig = dict[str, bool | str | dict[str, object]]
        type PoolingConfig = dict[str, int | bool | dict[str, object]]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # LDAP DATA TYPES - LDAP entry and attribute types
    # =========================================================================

    class LdapData:
        """LDAP data complex types."""

        type LdapEntry = dict[
            str, str | list[str] | dict[str, FlextTypes.Core.JsonValue]
        ]
        type LdapAttributes = dict[str, str | list[str] | bytes]
        type LdapFilter = str
        type LdapQuery = dict[str, str | list[str] | int | dict[str, object]]
        type LdapSchema = dict[str, str | list[dict[str, FlextTypes.Core.JsonValue]]]
        type LdapOperationResult = dict[str, bool | str | int | dict[str, object]]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types."""

        type TransformationConfig = dict[
            str, FlextTypes.Core.JsonValue | dict[str, object]
        ]
        type FieldMapping = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type TransformationRule = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type OutputFormat = dict[str, str | dict[str, object]]
        type ProcessingStep = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.Core.JsonValue]]
        type ModelDocumentation = dict[str, str | dict[str, object]]
        type ModelMaterialization = dict[
            str, str | dict[str, FlextTypes.Core.ConfigValue]
        ]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type SourceConnection = dict[
            str, FlextTypes.Core.ConfigValue | dict[str, object]
        ]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.Core.JsonValue]]]
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]

    # =========================================================================
    # DBT LDAP PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """DBT LDAP-specific project types extending FlextTypes.Project.

        Adds DBT LDAP transformation-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT LDAP domain owns LDAP data transformation-specific types.
        """

        # DBT LDAP-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
            "library",
            "application",
            "service",
            # DBT LDAP-specific types
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

        # DBT LDAP-specific project configurations
        type DbtLdapProjectConfig = dict[str, FlextTypes.Core.ConfigValue | object]
        type LdapTransformConfig = dict[str, str | int | bool | list[str]]
        type DirectoryAnalyticsConfig = dict[str, bool | str | dict[str, object]]
        type DbtLdapPipelineConfig = dict[str, FlextTypes.Core.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT LDAP TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdapTypes",
]
