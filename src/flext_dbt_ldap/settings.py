"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_dbt_ldap import c, m, t


@FlextSettings.auto_register("dbt-ldap")
class FlextDbtLdapSettings(FlextSettings):
    """Runtime settings for DBT LDAP transformations."""

    model_config: ClassVar[SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_", extra="ignore"
    )

    # LDAP connection settings
    ldap_host: Annotated[str, m.Field(description="LDAP server hostname")] = c.LOCALHOST
    ldap_port: Annotated[int, m.Field(description="LDAP server port")] = (
        c.Ldap.ConnectionDefaults.PORT
    )
    ldap_use_tls: Annotated[
        bool,
        m.Field(
            description="Use TLS for LDAP connection",
        ),
    ] = c.Ldap.ConnectionDefaults.DEFAULT_USE_TLS
    ldap_bind_dn: Annotated[
        SecretStr | None, m.Field(description="LDAP bind DN for authentication")
    ] = None
    ldap_bind_password: Annotated[
        SecretStr | None, m.Field(description="LDAP bind password")
    ] = None
    ldap_base_dn: Annotated[
        str,
        m.Field(
            description="LDAP base DN for searches",
        ),
    ] = c.Ldap.Defaults.EXAMPLE_BASE_DN

    # DBT project settings
    dbt_project_dir: Annotated[
        str, m.Field(description="Path to DBT project directory")
    ] = "."

    # Data quality settings
    min_quality_threshold: Annotated[
        float,
        m.Field(
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ] = c.DbtLdap.DEFAULT_QUALITY_THRESHOLD
    required_attributes: Annotated[
        t.StrSequence,
        m.Field(
            description="Required LDAP attributes for validation",
        ),
    ] = m.Field(default_factory=list)

    # Attribute mapping
    ldap_attribute_mapping: Annotated[
        t.StrMapping,
        m.Field(
            description="Mapping of LDAP attributes to DBT model attributes",
        ),
    ] = m.Field(default_factory=dict)

    # Schema mapping
    ldap_schema_mapping: Annotated[
        t.StrMapping,
        m.Field(
            description="Mapping of LDAP schemas to DBT tables",
        ),
    ] = m.Field(default_factory=dict)
