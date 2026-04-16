"""Schema, validation, and transformation settings models for dbt-ldap."""

from __future__ import annotations

from typing import Annotated

from flext_dbt_ldap import c, t
from flext_meltano import m


class FlextDbtLdapModelsSchema:
    """Schema and transformation models for dbt-ldap."""

    class DbtSourceSchema(m.Value):
        """DBT source schema definition."""

        version: Annotated[str, m.Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        sources: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            m.Field(description="DBT source definitions"),
        ] = m.Field(default_factory=list)

    class DbtModelDefinition(m.Value):
        """DBT model definition."""

        version: Annotated[str, m.Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            m.Field(description="DBT model definitions"),
        ] = m.Field(default_factory=list)

    class DbtTestConfig(m.Value):
        """DBT test configuration."""

        version: Annotated[str, m.Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            m.Field(description="DBT test model definitions"),
        ] = m.Field(default_factory=list)
        columns: Annotated[
            t.DbtLdap.LdapEntryMapping,
            m.Field(description="Column-level DBT tests keyed by attribute name"),
        ] = m.Field(default_factory=dict)

    class ProjectStructureValidation(m.Value):
        """DBT project structure validation result."""

        results: Annotated[
            t.BoolMapping,
            m.Field(description="Validation results keyed by project artifact"),
        ] = m.Field(default_factory=dict)

    class OptimizationHints(m.Value):
        """Query optimization hints."""

        add_indexes: Annotated[
            bool, m.Field(description="Whether index recommendations should be applied")
        ] = False
        index_columns: Annotated[
            t.StrSequence, m.Field(description="Columns recommended for indexing")
        ] = m.Field(default_factory=list)
        partition_by: Annotated[
            str, m.Field(description="Suggested partition key for large tables")
        ] = c.DEFAULT_EMPTY_STRING
        filter_early: Annotated[
            bool,
            m.Field(
                description="Whether filters should be pushed earlier in the query"
            ),
        ] = False

    class TransformationConfig(m.Value):
        """Transformation configuration."""

        source_table: Annotated[
            str, m.Field(description="Source table used by the transformation")
        ] = c.DEFAULT_EMPTY_STRING
        transformations: Annotated[
            t.StrMapping, m.Field(description="Column transformation expressions")
        ] = m.Field(default_factory=dict)
        filters: Annotated[
            t.StrSequence,
            m.Field(description="Filter expressions applied before transformation"),
        ] = m.Field(default_factory=list)

    class TransformationRule(m.Value):
        """Transformation rule definition."""

        name: Annotated[str, m.Field(description="Transformation rule name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        rules: Annotated[
            t.StrMapping, m.Field(description="Named transformation rules")
        ] = m.Field(default_factory=dict)

    class DataValidationConfig(m.Value):
        """Data validation configuration."""

        min_quality_threshold: Annotated[
            t.NonNegativeFloat,
            m.Field(description="Minimum validation score accepted for LDAP data"),
        ] = c.DbtLdap.DEFAULT_QUALITY_THRESHOLD
        required_attributes: Annotated[
            t.StrSequence,
            m.Field(description="LDAP attributes required for a valid entry"),
        ] = m.Field(default_factory=list)
        validate_dns: Annotated[
            bool, m.Field(description="Whether distinguished names must be present")
        ] = True
        columns: Annotated[
            t.DbtLdap.LdapEntryMapping,
            m.Field(description="Column validation configuration keyed by attribute"),
        ] = m.Field(default_factory=dict)

    class LdapSchema(m.Value):
        """LDAP schema configuration."""

        object_classes: Annotated[
            t.StrSequence,
            m.Field(description="LDAP object classes associated with the schema"),
        ] = m.Field(default_factory=list)
        required_attributes: Annotated[
            t.StrSequence, m.Field(description="LDAP attributes required by the schema")
        ] = m.Field(default_factory=list)

    class LdapQuery(m.Value):
        """LDAP query configuration."""

        base_dn: Annotated[str, m.Field(description="LDAP base DN for the query")] = (
            c.DEFAULT_EMPTY_STRING
        )
        filter_str: Annotated[str, m.Field(description="LDAP search filter")] = (
            c.Ldap.Filters.ALL_ENTRIES_FILTER
        )
        attributes: Annotated[
            t.StrSequence, m.Field(description="LDAP attributes requested by the query")
        ] = m.Field(default_factory=list)
        scope: Annotated[str, m.Field(description="LDAP search scope")] = (
            c.Ldap.SearchDefaults.DEFAULT_SCOPE
        )
