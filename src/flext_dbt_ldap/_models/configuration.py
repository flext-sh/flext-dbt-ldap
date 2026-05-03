"""DBT project and execution configuration models for dbt-ldap."""

from __future__ import annotations

from types import MappingProxyType
from typing import Annotated

from flext_dbt_ldap import c, t
from flext_meltano import m, u


class FlextDbtLdapModelsConfiguration:
    """Configuration-oriented dbt-ldap models."""

    class DbtProjectConfig(m.Value):
        """DBT project configuration."""

        name: Annotated[str, u.Field(description="DBT project name")]
        version: Annotated[str, u.Field(description="DBT project version")] = (
            c.Meltano.CONSTANTS_VERSION
        )
        profile: Annotated[str, u.Field(description="DBT profile name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        model_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT models")
        ] = c.DbtLdap.DEFAULT_MODEL_PATHS
        analysis_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT analyses")
        ] = c.DbtLdap.DEFAULT_ANALYSIS_PATHS
        test_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT tests")
        ] = c.DbtLdap.DEFAULT_TEST_PATHS
        seed_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT seeds")
        ] = c.DbtLdap.DEFAULT_SEED_PATHS
        macro_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT macros")
        ] = c.DbtLdap.DEFAULT_MACRO_PATHS
        snapshot_paths: Annotated[
            t.StrSequence, u.Field(description="Directories containing DBT snapshots")
        ] = c.DbtLdap.DEFAULT_SNAPSHOT_PATHS
        target_path: Annotated[
            str, u.Field(description="Directory used for DBT build artifacts")
        ] = c.Meltano.PREFIX_TARGET
        clean_targets: Annotated[
            t.StrSequence,
            u.Field(description="Directories cleaned by DBT maintenance commands"),
        ] = c.DbtLdap.DEFAULT_CLEAN_TARGETS
        target_schema: Annotated[
            str, u.Field(description="Default database schema for DBT relations")
        ] = c.DbtLdap.DEFAULT_DBT_SCHEMA
        tags: Annotated[
            t.StrSequence,
            u.Field(description="Tags applied to generated DBT resources"),
        ] = u.Field(default_factory=tuple)
        materialized: Annotated[
            str, u.Field(description="Default DBT materialization strategy")
        ] = c.Meltano.DBT_MATERIALIZATION_TABLE

    class DbtSourceFreshness(m.Value):
        """DBT source freshness configuration."""

        warn_after: Annotated[
            t.IntMapping, u.Field(description="Warning freshness thresholds")
        ] = u.Field(default_factory=lambda: MappingProxyType({}))
        error_after: Annotated[
            t.IntMapping, u.Field(description="Error freshness thresholds")
        ] = u.Field(default_factory=lambda: MappingProxyType({}))

    class DbtSourceDefinition(m.Value):
        """Complete DBT source definition."""

        name: Annotated[str, u.Field(description="DBT source name")]
        description: Annotated[str, u.Field(description="DBT source description")] = (
            c.DEFAULT_EMPTY_STRING
        )
        tables: Annotated[
            t.SequenceOf[t.JsonMapping],
            u.Field(description="Tables declared for the DBT source"),
        ] = u.Field(default_factory=tuple)

    class DbtConfig(m.Value):
        """General DBT execution configuration."""

        target: Annotated[
            str, u.Field(description="Named DBT target to execute against")
        ] = c.DbtLdap.DEFAULT_TARGET
        profiles_dir: Annotated[
            str, u.Field(description="Path to the DBT profiles directory")
        ] = c.DbtLdap.DEFAULT_PROFILES_DIR
        project_dir: Annotated[
            str, u.Field(description="Path to the DBT project directory")
        ] = c.DEFAULT_EMPTY_STRING
