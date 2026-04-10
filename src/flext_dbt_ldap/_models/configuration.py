"""DBT project and execution configuration models for dbt-ldap."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from flext_dbt_ldap import c, t
from flext_meltano import FlextMeltanoModels


class FlextDbtLdapModelsConfiguration:
    """Configuration-oriented dbt-ldap models."""

    class DbtProjectConfig(FlextMeltanoModels.Value):
        """DBT project configuration."""

        name: Annotated[str, Field(description="DBT project name")]
        version: Annotated[str, Field(description="DBT project version")] = (
            c.Meltano.CONSTANTS_VERSION
        )
        profile: Annotated[str, Field(description="DBT profile name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        model_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT models")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_MODEL_PATHS))
        analysis_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT analyses")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_ANALYSIS_PATHS))
        test_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT tests")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_TEST_PATHS))
        seed_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT seeds")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_SEED_PATHS))
        macro_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT macros")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_MACRO_PATHS))
        snapshot_paths: Annotated[
            t.StrSequence, Field(description="Directories containing DBT snapshots")
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_SNAPSHOT_PATHS))
        target_path: Annotated[
            str, Field(description="Directory used for DBT build artifacts")
        ] = c.Meltano.PREFIX_TARGET
        clean_targets: Annotated[
            t.StrSequence,
            Field(description="Directories cleaned by DBT maintenance commands"),
        ] = Field(default_factory=lambda: list(c.DbtLdap.DEFAULT_CLEAN_TARGETS))
        target_schema: Annotated[
            str, Field(description="Default database schema for DBT relations")
        ] = c.DbtLdap.DEFAULT_DBT_SCHEMA
        tags: Annotated[
            t.StrSequence, Field(description="Tags applied to generated DBT resources")
        ] = Field(default_factory=list)
        materialized: Annotated[
            str, Field(description="Default DBT materialization strategy")
        ] = c.Meltano.DBT_MATERIALIZATION_TABLE

    class DbtProfileConfig(FlextMeltanoModels.Value):
        """DBT profile connection configuration."""

        type: Annotated[str, Field(description="Database adapter type")] = (
            c.DbtLdap.DEFAULT_DBT_ADAPTER
        )
        host: Annotated[str, Field(description="Database host")] = c.LOCALHOST
        user: Annotated[str, Field(description="Database user name")] = (
            c.DbtLdap.DEFAULT_DBT_USER
        )
        password: Annotated[str, Field(description="Database password")] = (
            c.DEFAULT_EMPTY_STRING
        )
        port: Annotated[t.PortNumber, Field(description="Database port")] = (
            c.Meltano.DB_PORT_POSTGRES
        )
        dbname: Annotated[str, Field(description="Database name")] = (
            c.DbtLdap.DEFAULT_DBT_DATABASE
        )
        schema_name: Annotated[
            str, Field(description="Target schema for DBT models")
        ] = c.DbtLdap.DEFAULT_DBT_SCHEMA
        threads: Annotated[
            t.PositiveInt, Field(description="Number of DBT worker threads")
        ] = c.DbtLdap.DEFAULT_DBT_THREADS

    class DbtSourceTable(FlextMeltanoModels.Value):
        """DBT source table definition."""

        name: Annotated[str, Field(description="DBT source table name")]
        description: Annotated[
            str, Field(description="DBT source table description")
        ] = c.DEFAULT_EMPTY_STRING

    class DbtSourceFreshness(FlextMeltanoModels.Value):
        """DBT source freshness configuration."""

        warn_after: Annotated[
            t.IntMapping, Field(description="Warning freshness thresholds")
        ] = Field(default_factory=dict)
        error_after: Annotated[
            t.IntMapping, Field(description="Error freshness thresholds")
        ] = Field(default_factory=dict)

    class DbtSourceDefinition(FlextMeltanoModels.Value):
        """Complete DBT source definition."""

        name: Annotated[str, Field(description="DBT source name")]
        description: Annotated[str, Field(description="DBT source description")] = (
            c.DEFAULT_EMPTY_STRING
        )
        tables: Annotated[
            t.DbtLdap.SerializableMappingSequence,
            Field(description="Tables declared for the DBT source"),
        ] = Field(default_factory=list)

    class DbtConfig(FlextMeltanoModels.Value):
        """General DBT execution configuration."""

        target: Annotated[
            str, Field(description="Named DBT target to execute against")
        ] = c.DbtLdap.DEFAULT_TARGET
        profiles_dir: Annotated[
            str, Field(description="Path to the DBT profiles directory")
        ] = c.DbtLdap.DEFAULT_PROFILES_DIR
        project_dir: Annotated[
            str, Field(description="Path to the DBT project directory")
        ] = c.DEFAULT_EMPTY_STRING
