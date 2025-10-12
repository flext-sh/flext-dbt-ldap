"""FLEXT DBT LDAP Types - Domain-specific DBT LDAP type definitions.

This module provides DBT LDAP-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# DBT LDAP-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDAP operations
# =============================================================================


# DBT LDAP domain TypeVars
class FlextDbtLdapTypes(FlextCore.Types):
    """DBT LDAP-specific type definitions extending FlextCore.Types.

    Domain-specific type system for DBT LDAP data transformation operations.
    Contains ONLY complex DBT LDAP-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # CORE DBT LDAP TYPES - Commonly used type aliases extending FlextCore.Types
    # =========================================================================

    class Core(FlextCore.Types):
        """Core DBT LDAP types extending FlextCore.Types.

        Replaces generic FlextCore.Types.Dict with semantic DBT LDAP types.
        """

        # Configuration and settings types
        type ConfigDict = dict[str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict]
        type ConnectionDict = FlextCore.Types.Dict
        type LdapConfigDict = FlextCore.Types.Dict
        type DbtConfigDict = FlextCore.Types.Dict
        type ProjectDict = FlextCore.Types.Dict

        # Data processing types
        type DataDict = FlextCore.Types.Dict
        type ModelDict = FlextCore.Types.Dict
        type SourceDict = FlextCore.Types.Dict
        type TransformDict = FlextCore.Types.Dict
        type ValidationDict = FlextCore.Types.Dict

        # Template and structured response types
        type TemplateDict = dict[str, str | FlextCore.Types.Dict]
        type ResponseDict = FlextCore.Types.Dict
        type ResultDict = FlextCore.Types.Dict
        type MetricsDict = FlextCore.Types.Dict

        # Operation and context types
        type OperationDict = FlextCore.Types.Dict
        type ContextDict = FlextCore.Types.Dict
        type SettingsDict = FlextCore.Types.Dict

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types."""

        type ProjectConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type ModelConfiguration = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConfiguration = dict[str, str | list[FlextCore.Types.Dict]]
        type ProfileConfiguration = dict[str, FlextCore.Types.ConfigValue]
        type MacroConfiguration = dict[str, str | FlextCore.Types.Dict]
        type TestConfiguration = dict[str, str | bool | FlextCore.Types.StringList]

    # =========================================================================
    # LDAP CONNECTION TYPES - LDAP server connection configuration
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | FlextCore.Types.Dict]
        type AuthenticationConfig = dict[
            str, str | dict[str, FlextCore.Types.JsonValue]
        ]
        type ServerConfig = dict[str, str | int | bool | FlextCore.Types.StringList]
        type TlsConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type PoolingConfig = dict[str, int | bool | FlextCore.Types.Dict]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # LDAP DATA TYPES - LDAP entry and attribute types
    # =========================================================================

    class LdapData:
        """LDAP data complex types."""

        type LdapEntry = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type LdapAttributes = dict[str, str | FlextCore.Types.StringList | bytes]
        type LdapFilter = str
        type LdapQuery = dict[
            str, str | FlextCore.Types.StringList | int | FlextCore.Types.Dict
        ]
        type LdapSchema = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type LdapOperationResult = dict[str, bool | str | int | FlextCore.Types.Dict]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types."""

        type TransformationConfig = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type FieldMapping = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type DataValidation = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type TransformationRule = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type OutputFormat = dict[str, str | FlextCore.Types.Dict]
        type ProcessingStep = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | FlextCore.Types.Dict]
        type ModelDependency = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ModelTest = dict[str, str | bool | dict[str, FlextCore.Types.JsonValue]]
        type ModelDocumentation = dict[str, str | FlextCore.Types.Dict]
        type ModelMaterialization = dict[
            str, str | dict[str, FlextCore.Types.ConfigValue]
        ]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConnection = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type SourceTable = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type SourceFreshness = dict[str, str | int | FlextCore.Types.Dict]
        type SourceTest = dict[str, str | bool | FlextCore.Types.StringList]
        type SourceSchema = dict[str, str | dict[str, FlextCore.Types.JsonValue]]

    # =========================================================================
    # DBT LDAP PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """DBT LDAP-specific project types extending FlextCore.Types.Project.

        Adds DBT LDAP transformation-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        DBT LDAP domain owns LDAP data transformation-specific types.
        """

        # DBT LDAP-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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
        type DbtLdapProjectConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type LdapTransformConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type DirectoryAnalyticsConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type DbtLdapPipelineConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT LDAP TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextDbtLdapTypes",
]
