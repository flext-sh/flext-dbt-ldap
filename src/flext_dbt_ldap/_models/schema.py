"""Schema, validation, and transformation settings models for dbt-ldap."""

from __future__ import annotations

from types import MappingProxyType
from typing import Annotated

from flext_dbt_ldap import c, t
from flext_meltano import m, u


class FlextDbtLdapModelsSchema:
    """Schema and transformation models for dbt-ldap."""

    class DbtModelDefinition(m.Value):
        """DBT model definition."""

        version: Annotated[str, u.Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.SequenceOf[t.JsonMapping],
            u.Field(description="DBT model definitions"),
        ] = u.Field(default_factory=tuple)

    class DbtTestConfig(m.Value):
        """DBT test configuration."""

        version: Annotated[str, u.Field(description="DBT schema.yml version")] = (
            c.DbtLdap.DBT_SCHEMA_VERSION
        )
        models: Annotated[
            t.SequenceOf[t.JsonMapping],
            u.Field(description="DBT test model definitions"),
        ] = u.Field(default_factory=tuple)
        columns: Annotated[
            t.Ldap.OperationAttributes,
            u.Field(description="Column-level DBT tests keyed by attribute name"),
        ] = u.Field(default_factory=lambda: MappingProxyType({}))

    class TransformationConfig(m.Value):
        """Transformation configuration."""

        source_table: Annotated[
            str, u.Field(description="Source table used by the transformation")
        ] = c.DEFAULT_EMPTY_STRING
        transformations: Annotated[
            t.StrMapping, u.Field(description="Column transformation expressions")
        ] = u.Field(default_factory=lambda: MappingProxyType({}))
        filters: Annotated[
            t.StrSequence,
            u.Field(description="Filter expressions applied before transformation"),
        ] = u.Field(default_factory=tuple)

    class TransformationRule(m.Value):
        """Transformation rule definition."""

        name: Annotated[str, u.Field(description="Transformation rule name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        rules: Annotated[
            t.StrMapping, u.Field(description="Named transformation rules")
        ] = u.Field(default_factory=lambda: MappingProxyType({}))

    class DataValidationConfig(m.Value):
        """Data validation configuration."""

        min_quality_threshold: Annotated[
            t.NonNegativeFloat,
            u.Field(description="Minimum validation score accepted for LDAP data"),
        ] = c.DbtLdap.DEFAULT_QUALITY_THRESHOLD
        required_attributes: Annotated[
            t.StrSequence,
            u.Field(description="LDAP attributes required for a valid entry"),
        ] = u.Field(default_factory=tuple)
        validate_dns: Annotated[
            bool, u.Field(description="Whether distinguished names must be present")
        ] = True
        columns: Annotated[
            t.Ldap.OperationAttributes,
            u.Field(description="Column validation configuration keyed by attribute"),
        ] = u.Field(default_factory=lambda: MappingProxyType({}))

    class LdapSchema(m.Value):
        """LDAP schema configuration."""

        object_classes: Annotated[
            t.StrSequence,
            u.Field(description="LDAP object classes associated with the schema"),
        ] = u.Field(default_factory=tuple)
        required_attributes: Annotated[
            t.StrSequence, u.Field(description="LDAP attributes required by the schema")
        ] = u.Field(default_factory=tuple)

    class LdapQuery(m.Value):
        """LDAP query configuration."""

        base_dn: Annotated[str, u.Field(description="LDAP base DN for the query")] = (
            c.DEFAULT_EMPTY_STRING
        )
        filter_str: Annotated[str, u.Field(description="LDAP search filter")] = (
            c.Ldap.ALL_ENTRIES_FILTER
        )
        attributes: Annotated[
            t.StrSequence, u.Field(description="LDAP attributes requested by the query")
        ] = u.Field(default_factory=tuple)
        scope: Annotated[str, u.Field(description="LDAP search scope")] = (
            c.Ldap.DEFAULT_SCOPE
        )
