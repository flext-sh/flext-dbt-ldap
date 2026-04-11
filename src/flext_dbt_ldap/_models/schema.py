"""Schema, validation, and transformation settings models for dbt-ldap."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from flext_dbt_ldap import c, t
from flext_meltano import FlextMeltanoModels


class FlextDbtLdapModelsSchema:
    """Schema and transformation models for dbt-ldap."""

    class DbtSourceSchema(FlextMeltanoModels.Value):
        """DBT source schema definition."""

        version: Annotated[str, Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        sources: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            Field(description="DBT source definitions"),
        ] = Field(default_factory=list)

    class DbtModelDefinition(FlextMeltanoModels.Value):
        """DBT model definition."""

        version: Annotated[str, Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            Field(description="DBT model definitions"),
        ] = Field(default_factory=list)

    class DbtTestConfig(FlextMeltanoModels.Value):
        """DBT test configuration."""

        version: Annotated[str, Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            Field(description="DBT test model definitions"),
        ] = Field(default_factory=list)
        columns: Annotated[
            t.DbtLdap.LdapEntryMapping,
            Field(description="Column-level DBT tests keyed by attribute name"),
        ] = Field(default_factory=dict)

    class ProjectStructureValidation(FlextMeltanoModels.Value):
        """DBT project structure validation result."""

        results: Annotated[
            t.BoolMapping,
            Field(description="Validation results keyed by project artifact"),
        ] = Field(default_factory=dict)

    class OptimizationHints(FlextMeltanoModels.Value):
        """Query optimization hints."""

        add_indexes: Annotated[
            bool, Field(description="Whether index recommendations should be applied")
        ] = False
        index_columns: Annotated[
            t.StrSequence, Field(description="Columns recommended for indexing")
        ] = Field(default_factory=list)
        partition_by: Annotated[
            str, Field(description="Suggested partition key for large tables")
        ] = c.DEFAULT_EMPTY_STRING
        filter_early: Annotated[
            bool,
            Field(description="Whether filters should be pushed earlier in the query"),
        ] = False

    class TransformationConfig(FlextMeltanoModels.Value):
        """Transformation configuration."""

        source_table: Annotated[
            str, Field(description="Source table used by the transformation")
        ] = c.DEFAULT_EMPTY_STRING
        transformations: Annotated[
            t.StrMapping, Field(description="Column transformation expressions")
        ] = Field(default_factory=dict)
        filters: Annotated[
            t.StrSequence,
            Field(description="Filter expressions applied before transformation"),
        ] = Field(default_factory=list)

    class TransformationRule(FlextMeltanoModels.Value):
        """Transformation rule definition."""

        name: Annotated[str, Field(description="Transformation rule name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        rules: Annotated[
            t.StrMapping, Field(description="Named transformation rules")
        ] = Field(default_factory=dict)

    class DataValidationConfig(FlextMeltanoModels.Value):
        """Data validation configuration."""

        min_quality_threshold: Annotated[
            t.NonNegativeFloat,
            Field(description="Minimum validation score accepted for LDAP data"),
        ] = c.DbtLdap.DEFAULT_QUALITY_THRESHOLD
        required_attributes: Annotated[
            t.StrSequence,
            Field(description="LDAP attributes required for a valid entry"),
        ] = Field(default_factory=list)
        validate_dns: Annotated[
            bool, Field(description="Whether distinguished names must be present")
        ] = True
        columns: Annotated[
            t.DbtLdap.LdapEntryMapping,
            Field(description="Column validation configuration keyed by attribute"),
        ] = Field(default_factory=dict)

    class LdapSchema(FlextMeltanoModels.Value):
        """LDAP schema configuration."""

        object_classes: Annotated[
            t.StrSequence,
            Field(description="LDAP object classes associated with the schema"),
        ] = Field(default_factory=list)
        required_attributes: Annotated[
            t.StrSequence, Field(description="LDAP attributes required by the schema")
        ] = Field(default_factory=list)

    class LdapQuery(FlextMeltanoModels.Value):
        """LDAP query configuration."""

        base_dn: Annotated[str, Field(description="LDAP base DN for the query")] = (
            c.DEFAULT_EMPTY_STRING
        )
        filter_str: Annotated[str, Field(description="LDAP search filter")] = (
            c.Ldap.Filters.ALL_ENTRIES_FILTER
        )
        attributes: Annotated[
            t.StrSequence, Field(description="LDAP attributes requested by the query")
        ] = Field(default_factory=list)
        scope: Annotated[str, Field(description="LDAP search scope")] = (
            c.Ldap.SearchDefaults.DEFAULT_SCOPE
        )
