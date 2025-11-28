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

    class DbtLdapCore:
        """Core DBT LDAP types extending FlextTypes.

        Replaces generic dict[str, object] with semantic DBT LDAP types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        # Configuration and settings types
        type ConfigDict = dict[str, object | dict[str, object]]
        """DBT LDAP configuration dictionary type."""
        type ConnectionDict = dict[str, object]
        """DBT LDAP connection dictionary type."""
        type LdapConfigDict = dict[str, object]
        """LDAP configuration dictionary type."""
        type DbtConfigDict = dict[str, object]
        """DBT configuration dictionary type."""
        type ProjectDict = dict[str, object]
        """DBT LDAP project dictionary type."""

        # Data processing types
        type DataDict = dict[str, object]
        """DBT LDAP data dictionary type."""
        type ModelDict = dict[str, object]
        """DBT LDAP model dictionary type."""
        type SourceDict = dict[str, object]
        """DBT LDAP source dictionary type."""
        type TransformDict = dict[str, object]
        """DBT LDAP transformation dictionary type."""
        type ValidationDict = dict[str, object]
        """DBT LDAP validation dictionary type."""

        # Template and structured response types
        type TemplateDict = dict[str, str | dict[str, object]]
        """DBT LDAP template dictionary type."""
        type ResponseDict = dict[str, object]
        """DBT LDAP response dictionary type."""
        type ResultDict = dict[str, object]
        """DBT LDAP result dictionary type."""
        type MetricsDict = dict[str, object]
        """DBT LDAP metrics dictionary type."""

        # Operation and context types
        OperationDict: type = dict[str, object]
        """DBT LDAP operation dictionary type."""
        ContextDict: type = dict[str, object]
        """DBT LDAP context dictionary type."""
        SettingsDict: type = dict[str, object]
        """DBT LDAP settings dictionary type."""

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ProjectConfiguration: type = dict[str, object | dict[str, object]]
        """DBT project configuration type."""
        ModelConfiguration: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT model configuration type."""
        SourceConfiguration: type = dict[str, str | list[dict[str, object]]]
        """DBT source configuration type."""
        ProfileConfiguration: type = dict[str, object]
        """DBT profile configuration type."""
        MacroConfiguration: type = dict[str, str | dict[str, object]]
        """DBT macro configuration type."""
        TestConfiguration: type = dict[str, str | bool | list[str]]
        """DBT test configuration type."""

    # =========================================================================
    # LDAP CONNECTION TYPES - LDAP server connection configuration
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ConnectionConfig: type = dict[str, str | int | bool | dict[str, object]]
        """LDAP connection configuration type."""
        AuthenticationConfig: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """LDAP authentication configuration type."""
        ServerConfig: type = dict[str, str | int | bool | list[str]]
        """LDAP server configuration type."""
        TlsConfig: type = dict[str, bool | str | dict[str, object]]
        """LDAP TLS configuration type."""
        PoolingConfig: type = dict[str, int | bool | dict[str, object]]
        """LDAP pooling configuration type."""
        TimeoutConfig: type = dict[str, int | float]
        """LDAP timeout configuration type."""

    # =========================================================================
    # LDAP DATA TYPES - LDAP entry and attribute types
    # =========================================================================

    class LdapData:
        """LDAP data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        LdapEntry: type = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        """LDAP entry type."""
        LdapAttributes: type = dict[str, str | list[str] | bytes]
        """LDAP attributes type."""
        LdapFilter: type = str
        """LDAP filter type."""
        LdapQuery: type = dict[str, str | list[str] | int | dict[str, object]]
        """LDAP query type."""
        LdapSchema: type = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """LDAP schema type."""
        LdapOperationResult: type = dict[str, bool | str | int | dict[str, object]]
        """LDAP operation result type."""

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        TransformationConfig: type = dict[str, FlextTypes.JsonValue | dict[str, object]]
        """DBT transformation configuration type."""
        FieldMapping: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT field mapping type."""
        DataValidation: type = dict[str, bool | str | list[str] | dict[str, object]]
        """DBT data validation type."""
        TransformationRule: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT transformation rule type."""
        OutputFormat: type = dict[str, str | dict[str, object]]
        """DBT output format type."""
        ProcessingStep: type = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        """DBT processing step type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ModelDefinition: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT model definition type."""
        ModelExecution: type = dict[str, str | bool | int | dict[str, object]]
        """DBT model execution type."""
        ModelDependency: type = dict[str, str | list[str] | dict[str, object]]
        """DBT model dependency type."""
        ModelTest: type = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        """DBT model test type."""
        ModelDocumentation: type = dict[str, str | dict[str, object]]
        """DBT model documentation type."""
        ModelMaterialization: type = dict[str, str | dict[str, object]]
        """DBT model materialization type."""

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        SourceDefinition: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT source definition type."""
        SourceConnection: type = dict[str, object | dict[str, object]]
        """DBT source connection type."""
        SourceTable: type = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """DBT source table type."""
        SourceFreshness: type = dict[str, str | int | dict[str, object]]
        """DBT source freshness type."""
        SourceTest: type = dict[str, str | bool | list[str]]
        """DBT source test type."""
        SourceSchema: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT source schema type."""

    # =========================================================================
    # DBT LDAP PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes):
        """DBT LDAP-specific project types extending FlextTypes.

        Adds DBT LDAP transformation-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT LDAP domain owns LDAP data transformation-specific types.
        """

        # DBT LDAP-specific project types extending the generic ones
        # Python 3.13+ best practice: Use TypeAlias for better type checking
        DbtLdapProjectType: type = Literal[
            # Generic types inherited from FlextTypes
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
        """DBT LDAP project type literal."""

        # DBT LDAP-specific project configurations
        DbtLdapProjectConfig: type = dict[str, object]
        """DBT LDAP project configuration type."""
        LdapTransformConfig: type = dict[str, str | int | bool | list[str]]
        """LDAP transformation configuration type."""
        DirectoryAnalyticsConfig: type = dict[str, bool | str | dict[str, object]]
        """Directory analytics configuration type."""
        DbtLdapPipelineConfig: type = dict[str, object]
        """DBT LDAP pipeline configuration type."""


# =============================================================================
# PUBLIC API EXPORTS - DBT LDAP TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdapTypes",
]
