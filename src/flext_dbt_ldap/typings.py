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
    # CORE DBT LDAP TYPES - Commonly used type aliases extending FlextTypes
    # =========================================================================

    class Core(FlextTypes):
        """Core DBT LDAP types extending FlextTypes.

        Replaces generic FlextTypes.Dict with semantic DBT LDAP types.
        """

        # Configuration and settings types
        type ConfigDict = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type ConnectionDict = FlextTypes.Dict
        type LdapConfigDict = FlextTypes.Dict
        type DbtConfigDict = FlextTypes.Dict
        type ProjectDict = FlextTypes.Dict

        # Data processing types
        type DataDict = FlextTypes.Dict
        type ModelDict = FlextTypes.Dict
        type SourceDict = FlextTypes.Dict
        type TransformDict = FlextTypes.Dict
        type ValidationDict = FlextTypes.Dict

        # Template and structured response types
        type TemplateDict = dict[str, str | FlextTypes.Dict]
        type ResponseDict = FlextTypes.Dict
        type ResultDict = FlextTypes.Dict
        type MetricsDict = FlextTypes.Dict

        # Operation and context types
        type OperationDict = FlextTypes.Dict
        type ContextDict = FlextTypes.Dict
        type SettingsDict = FlextTypes.Dict

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types."""

        type ProjectConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConfiguration = dict[str, str | list[FlextTypes.Dict]]
        type ProfileConfiguration = dict[str, FlextTypes.ConfigValue]
        type MacroConfiguration = dict[str, str | FlextTypes.Dict]
        type TestConfiguration = dict[str, str | bool | FlextTypes.StringList]

    # =========================================================================
    # LDAP CONNECTION TYPES - LDAP server connection configuration
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | FlextTypes.Dict]
        type AuthenticationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ServerConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type TlsConfig = dict[str, bool | str | FlextTypes.Dict]
        type PoolingConfig = dict[str, int | bool | FlextTypes.Dict]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # LDAP DATA TYPES - LDAP entry and attribute types
    # =========================================================================

    class LdapData:
        """LDAP data complex types."""

        type LdapEntry = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type LdapAttributes = dict[str, str | FlextTypes.StringList | bytes]
        type LdapFilter = str
        type LdapQuery = dict[str, str | FlextTypes.StringList | int | FlextTypes.Dict]
        type LdapSchema = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type LdapOperationResult = dict[str, bool | str | int | FlextTypes.Dict]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types."""

        type TransformationConfig = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type FieldMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataValidation = dict[
            str, bool | str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type TransformationRule = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type OutputFormat = dict[str, str | FlextTypes.Dict]
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | FlextTypes.Dict]
        type ModelDependency = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type ModelDocumentation = dict[str, str | FlextTypes.Dict]
        type ModelMaterialization = dict[str, str | dict[str, FlextTypes.ConfigValue]]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConnection = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SourceFreshness = dict[str, str | int | FlextTypes.Dict]
        type SourceTest = dict[str, str | bool | FlextTypes.StringList]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]

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
        type DbtLdapProjectConfig = dict[str, FlextTypes.ConfigValue | object]
        type LdapTransformConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type DirectoryAnalyticsConfig = dict[str, bool | str | FlextTypes.Dict]
        type DbtLdapPipelineConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT LDAP TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextDbtLdapTypes",
]
