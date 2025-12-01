"""FLEXT DBT LDAP Types - Domain-specific DBT LDAP type definitions.

This module provides DBT LDAP-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ PEP 695 type syntax strict
- Extends FlextTypes properly
- Uses FlextTypes.JsonValue and other FlextTypes directly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Literal

from flext_core import FlextTypes
from flext_ldap import FlextLdapTypes

# =============================================================================
# DBT LDAP-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDAP operations
# =============================================================================
# Only TypeVars allowed outside class - following FLEXT standards


# DBT LDAP domain TypeVars
class FlextDbtLdapTypes(FlextTypes):
    """DBT LDAP-specific type definitions extending FlextTypes.

    Domain-specific type system for DBT LDAP data transformation operations.
    Contains ONLY complex DBT LDAP-specific types, no simple aliases.
    Uses Python 3.13+ PEP 695 type syntax strict.
    Composes with FlextTypes.JsonValue, FlextTypes.GeneralValueType, etc.
    """

    # =========================================================================
    # CORE DBT LDAP TYPES - Complex types using FlextTypes composition
    # =========================================================================

    class DbtLdapCore:
        """Core DBT LDAP types extending FlextTypes.

        Uses FlextTypes.JsonValue and FlextTypes.GeneralValueType for composition.
        No simple aliases - all types are complex and domain-specific.
        """

        # String list type - used for LDAP attributes (multi-valued)
        type StringList = Sequence[str]
        """Sequence of strings - used for LDAP multi-valued attributes."""

        # Boolean dictionary type - used for validation results
        type BoolDict = Mapping[str, bool]
        """Mapping of string keys to boolean values - used for validation results."""

        # Configuration and settings types - using FlextTypes.JsonValue
        type ConfigDict = Mapping[
            str, FlextTypes.JsonValue | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT LDAP configuration dictionary type."""
        type ConnectionDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP connection dictionary type."""
        type LdapConfigDict = Mapping[str, FlextTypes.JsonValue]
        """LDAP configuration dictionary type."""
        type DbtConfigDict = Mapping[str, FlextTypes.JsonValue]
        """DBT configuration dictionary type."""
        type ProjectDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP project dictionary type."""

        # Data processing types - using FlextTypes.JsonValue
        type DataDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP data dictionary type."""
        type ModelDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP model dictionary type."""
        type SourceDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP source dictionary type."""
        type TransformDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP transformation dictionary type."""
        type ValidationDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP validation dictionary type."""

        # Template and structured response types
        type TemplateDict = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT LDAP template dictionary type."""
        type ResponseDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP response dictionary type."""
        type ResultDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP result dictionary type."""
        type MetricsDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP metrics dictionary type."""

        # Operation and context types - PEP 695 strict syntax
        type OperationDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP operation dictionary type."""
        type ContextDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP context dictionary type."""
        type SettingsDict = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP settings dictionary type."""

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types using FlextTypes
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types using FlextTypes composition."""

        type ProjectConfiguration = Mapping[
            str, FlextTypes.JsonValue | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT project configuration type."""
        type ModelConfiguration = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT model configuration type."""
        type SourceConfiguration = Mapping[
            str, str | Sequence[Mapping[str, FlextTypes.JsonValue]]
        ]
        """DBT source configuration type."""
        type ProfileConfiguration = Mapping[str, FlextTypes.JsonValue]
        """DBT profile configuration type."""
        type MacroConfiguration = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT macro configuration type."""
        type TestConfiguration = Mapping[str, str | bool | Sequence[str]]
        """DBT test configuration type."""

    # =========================================================================
    # LDAP CONNECTION TYPES - Using FlextLdapTypes for LDAP-specific types
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types using FlextLdapTypes composition."""

        # Use FlextLdapTypes.Protocol.ConnectionConfig for LDAP connection
        type ConnectionConfig = FlextLdapTypes.Protocol.ConnectionConfig
        """LDAP connection configuration type - uses FlextLdapTypes."""
        type AuthenticationConfig = Mapping[
            str, str | Mapping[str, FlextTypes.JsonValue]
        ]
        """LDAP authentication configuration type."""
        type ServerConfig = Mapping[str, str | int | bool | Sequence[str]]
        """LDAP server configuration type."""
        type TlsConfig = Mapping[str, bool | str | Mapping[str, FlextTypes.JsonValue]]
        """LDAP TLS configuration type."""
        type PoolingConfig = Mapping[
            str, int | bool | Mapping[str, FlextTypes.JsonValue]
        ]
        """LDAP pooling configuration type."""
        type TimeoutConfig = Mapping[str, int | float]
        """LDAP timeout configuration type."""

    # =========================================================================
    # LDAP DATA TYPES - Using FlextLdapTypes for Entry types
    # =========================================================================

    class LdapData:
        """LDAP data complex types using FlextLdapTypes composition."""

        # Use FlextLdapTypes.Protocol.Entry for LDAP entries
        type LdapEntry = FlextLdapTypes.Protocol.Entry
        """LDAP entry type - uses FlextLdapTypes.Protocol.Entry."""
        type LdapAttributes = Mapping[str, str | Sequence[str] | bytes]
        """LDAP attributes type."""
        type LdapQuery = Mapping[
            str, str | Sequence[str] | int | Mapping[str, FlextTypes.JsonValue]
        ]
        """LDAP query type."""
        type LdapSchema = Mapping[
            str, str | Sequence[Mapping[str, FlextTypes.JsonValue]]
        ]
        """LDAP schema type."""
        type LdapOperationResult = Mapping[
            str, bool | str | int | Mapping[str, FlextTypes.JsonValue]
        ]
        """LDAP operation result type."""

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types."""

        type TransformationConfig = Mapping[
            str, FlextTypes.JsonValue | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT transformation configuration type."""
        type FieldMapping = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT field mapping type."""
        type DataValidation = Mapping[
            str, bool | str | Sequence[str] | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT data validation type."""
        type TransformationRule = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT transformation rule type."""
        type OutputFormat = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT output format type."""
        type ProcessingStep = Mapping[
            str, str | int | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT processing step type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types."""

        type ModelDefinition = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT model definition type."""
        type ModelExecution = Mapping[
            str, str | bool | int | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT model execution type."""
        type ModelDependency = Mapping[
            str, str | Sequence[str] | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT model dependency type."""
        type ModelTest = Mapping[str, str | bool | Mapping[str, FlextTypes.JsonValue]]
        """DBT model test type."""
        type ModelDocumentation = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT model documentation type."""
        type ModelMaterialization = Mapping[
            str, str | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT model materialization type."""

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types."""

        type SourceDefinition = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT source definition type."""
        type SourceConnection = Mapping[
            str, FlextTypes.JsonValue | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT source connection type."""
        type SourceTable = Mapping[
            str, str | Sequence[Mapping[str, FlextTypes.JsonValue]]
        ]
        """DBT source table type."""
        type SourceFreshness = Mapping[
            str, str | int | Mapping[str, FlextTypes.JsonValue]
        ]
        """DBT source freshness type."""
        type SourceTest = Mapping[str, str | bool | Sequence[str]]
        """DBT source test type."""
        type SourceSchema = Mapping[str, str | Mapping[str, FlextTypes.JsonValue]]
        """DBT source schema type."""

    # =========================================================================
    # DBT LDAP PROJECT TYPES - Domain-specific project types
    # =========================================================================

    class Project:
        """DBT LDAP-specific project types."""

        # DBT LDAP-specific project types - PEP 695 strict syntax
        type DbtLdapProjectType = Literal[
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

        # DBT LDAP-specific project configurations - using FlextTypes.JsonValue
        type DbtLdapProjectConfig = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP project configuration type."""
        type LdapTransformConfig = Mapping[str, str | int | bool | Sequence[str]]
        """LDAP transformation configuration type."""
        type DirectoryAnalyticsConfig = Mapping[
            str, bool | str | Mapping[str, FlextTypes.JsonValue]
        ]
        """Directory analytics configuration type."""
        type DbtLdapPipelineConfig = Mapping[str, FlextTypes.JsonValue]
        """DBT LDAP pipeline configuration type."""


# =============================================================================
# PUBLIC API EXPORTS - DBT LDAP TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdapTypes",
]
