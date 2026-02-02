"""FLEXT DBT LDAP Types - Domain-specific DBT LDAP type definitions.

This module provides DBT LDAP-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ PEP 695 type syntax strict
- Extends t properly
- Uses t.JsonValue and other t directly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# DBT LDAP-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDAP operations
# =============================================================================
# Only TypeVars allowed outside class - following FLEXT standards


# DBT LDAP domain TypeVars
class FlextDbtLdapTypes(FlextTypes):
    """DBT LDAP-specific type definitions extending t.

    Domain-specific type system for DBT LDAP data transformation operations.
    Contains ONLY complex DBT LDAP-specific types, no simple aliases.
    Uses Python 3.13+ PEP 695 type syntax strict.
    Composes with t.JsonValue, t.GeneralValueType, etc.
    """

    # =========================================================================
    # CORE DBT LDAP TYPES - Complex types using t composition
    # =========================================================================

    class DbtLdap:
        """Core DBT LDAP types extending t.

        Uses t.JsonValue and t.GeneralValueType for composition.
        No simple aliases - all types are complex and domain-specific.
        """

        # String list type - used for LDAP attributes (multi-valued)
        type StringList = Sequence[str]
        """Sequence of strings - used for LDAP multi-valued attributes."""

        # Boolean dictionary type - used for validation results
        type BoolDict = Mapping[str, bool]
        """Mapping of string keys to boolean values - used for validation results."""

        # Configuration and settings types - using t.JsonValue
        type ConfigDict = Mapping[
            str,
            t.JsonValue | Mapping[str, t.JsonValue],
        ]
        """DBT LDAP configuration dictionary type."""
        type ConnectionDict = Mapping[str, t.JsonValue]
        """DBT LDAP connection dictionary type."""
        type LdapConfigDict = Mapping[str, t.JsonValue]
        """LDAP configuration dictionary type."""
        type DbtConfigDict = Mapping[str, t.JsonValue]
        """DBT configuration dictionary type."""
        type ProjectDict = Mapping[str, t.JsonValue]
        """DBT LDAP project dictionary type."""

        # Data processing types - using t.JsonValue
        type DataDict = Mapping[str, t.JsonValue]
        """DBT LDAP data dictionary type."""
        type ModelDict = Mapping[str, t.JsonValue]
        """DBT LDAP model dictionary type."""
        type SourceDict = Mapping[str, t.JsonValue]
        """DBT LDAP source dictionary type."""
        type TransformDict = Mapping[str, t.JsonValue]
        """DBT LDAP transformation dictionary type."""
        type ValidationDict = Mapping[str, t.JsonValue]
        """DBT LDAP validation dictionary type."""

        # Template and structured response types
        type TemplateDict = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT LDAP template dictionary type."""
        type ResponseDict = Mapping[str, t.JsonValue]
        """DBT LDAP response dictionary type."""
        type ResultDict = Mapping[str, t.JsonValue]
        """DBT LDAP result dictionary type."""
        type MetricsDict = Mapping[str, t.JsonValue]
        """DBT LDAP metrics dictionary type."""

        # Operation and context types - PEP 695 strict syntax
        type OperationDict = Mapping[str, t.JsonValue]
        """DBT LDAP operation dictionary type."""
        type ContextDict = Mapping[str, t.JsonValue]
        """DBT LDAP context dictionary type."""
        type SettingsDict = Mapping[str, t.JsonValue]
        """DBT LDAP settings dictionary type."""

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types using t
    # =========================================================================

    class DbtProject:
        """DBT LDAP project complex types using t composition."""

        type ProjectConfiguration = Mapping[
            str,
            t.JsonValue | Mapping[str, t.JsonValue],
        ]
        """DBT project configuration type."""
        type ModelConfiguration = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT model configuration type."""
        type SourceConfiguration = Mapping[
            str,
            str | Sequence[Mapping[str, t.JsonValue]],
        ]
        """DBT source configuration type."""
        type ProfileConfiguration = Mapping[str, t.JsonValue]
        """DBT profile configuration type."""
        type MacroConfiguration = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT macro configuration type."""
        type TestConfiguration = Mapping[str, str | bool | Sequence[str]]
        """DBT test configuration type."""

    # =========================================================================
    # LDAP CONNECTION TYPES - Using FlextLdapTypes for LDAP-specific types
    # =========================================================================

    class LdapConnection:
        """LDAP connection complex types using direct type composition.

        Note: For ConnectionConfig protocol, use p.Ldap.ConnectionConfigProtocol via alias
        (from flext_dbt_ldap.protocols import p).
        No direct protocol class references - use p alias.
        """

        type AuthenticationConfig = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """LDAP authentication configuration type."""
        type ServerConfig = Mapping[str, str | int | bool | Sequence[str]]
        """LDAP server configuration type."""
        type TlsConfig = Mapping[str, bool | str | Mapping[str, t.JsonValue]]
        """LDAP TLS configuration type."""
        type PoolingConfig = Mapping[
            str,
            int | bool | Mapping[str, t.JsonValue],
        ]
        """LDAP pooling configuration type."""
        type TimeoutConfig = Mapping[str, int | float]
        """LDAP timeout configuration type."""

    # =========================================================================
    # LDAP DATA TYPES - Using FlextLdapTypes for Entry types
    # =========================================================================

    class LdapData:
        """LDAP data complex types using direct type composition.

        Note: For Entry protocol, use p.Ldap.LdapEntryProtocol via alias
        (from flext_dbt_ldap.protocols import p).
        For Entry type alias, use FlextLdapTypes.Ldif.Entry.Instance directly.
        No direct protocol class references - use p alias.
        """

        type LdapAttributes = Mapping[str, str | Sequence[str] | bytes]
        """LDAP attributes type."""
        type LdapQuery = Mapping[
            str,
            str | Sequence[str] | int | Mapping[str, t.JsonValue],
        ]
        """LDAP query type."""
        type LdapSchema = Mapping[
            str,
            str | Sequence[Mapping[str, t.JsonValue]],
        ]
        """LDAP schema type."""
        type LdapOperationResult = Mapping[
            str,
            bool | str | int | Mapping[str, t.JsonValue],
        ]
        """LDAP operation result type."""

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration
    # =========================================================================

    class DbtTransformation:
        """DBT LDAP transformation complex types."""

        type TransformationConfig = Mapping[
            str,
            t.JsonValue | Mapping[str, t.JsonValue],
        ]
        """DBT transformation configuration type."""
        type FieldMapping = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT field mapping type."""
        type DataValidation = Mapping[
            str,
            bool | str | Sequence[str] | Mapping[str, t.JsonValue],
        ]
        """DBT data validation type."""
        type TransformationRule = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT transformation rule type."""
        type OutputFormat = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT output format type."""
        type ProcessingStep = Mapping[
            str,
            str | int | Mapping[str, t.JsonValue],
        ]
        """DBT processing step type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types
    # =========================================================================

    class DbtModel:
        """DBT LDAP model complex types."""

        type ModelDefinition = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT model definition type."""
        type ModelExecution = Mapping[
            str,
            str | bool | int | Mapping[str, t.JsonValue],
        ]
        """DBT model execution type."""
        type ModelDependency = Mapping[
            str,
            str | Sequence[str] | Mapping[str, t.JsonValue],
        ]
        """DBT model dependency type."""
        type ModelTest = Mapping[str, str | bool | Mapping[str, t.JsonValue]]
        """DBT model test type."""
        type ModelDocumentation = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT model documentation type."""
        type ModelMaterialization = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """DBT model materialization type."""

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types
    # =========================================================================

    class DbtSource:
        """DBT LDAP source complex types."""

        type SourceDefinition = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT source definition type."""
        type SourceConnection = Mapping[
            str,
            t.JsonValue | Mapping[str, t.JsonValue],
        ]
        """DBT source connection type."""
        type SourceTable = Mapping[
            str,
            str | Sequence[Mapping[str, t.JsonValue]],
        ]
        """DBT source table type."""
        type SourceFreshness = Mapping[
            str,
            str | int | Mapping[str, t.JsonValue],
        ]
        """DBT source freshness type."""
        type SourceTest = Mapping[str, str | bool | Sequence[str]]
        """DBT source test type."""
        type SourceSchema = Mapping[str, str | Mapping[str, t.JsonValue]]
        """DBT source schema type."""

    # =========================================================================
    # DBT LDAP PROJECT TYPES - Domain-specific project types
    # =========================================================================

    class Project:
        """DBT LDAP-specific project types."""

        # DBT LDAP-specific project types - PEP 695 strict syntax
        type DbtLdapProjectType = Literal[
            # Generic types inherited from t
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

        # DBT LDAP-specific project configurations - using t.JsonValue
        type DbtLdapProjectConfig = Mapping[str, t.JsonValue]
        """DBT LDAP project configuration type."""
        type LdapTransformConfig = Mapping[str, str | int | bool | Sequence[str]]
        """LDAP transformation configuration type."""
        type DirectoryAnalyticsConfig = Mapping[
            str,
            bool | str | Mapping[str, t.JsonValue],
        ]
        """Directory analytics configuration type."""
        type DbtLdapPipelineConfig = Mapping[str, t.JsonValue]
        """DBT LDAP pipeline configuration type."""


# Alias for simplified usage
t = FlextDbtLdapTypes

# Namespace composition via class inheritance
# DbtLdap namespace provides access to nested classes through inheritance
# Access patterns:
# - t.DbtLdap.* for DBT LDAP-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)
# For protocols, use p.Ldap.* via alias (from flext_dbt_ldap.protocols import p)
# For type aliases, use FlextLdapTypes.* directly

__all__ = [
    "FlextDbtLdapTypes",
    "t",
]
