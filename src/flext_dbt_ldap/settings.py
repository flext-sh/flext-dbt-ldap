"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_core import FlextSettings, u
from flext_dbt_ldap import c, m, t
from flext_meltano import FlextMeltanoSettings


@FlextSettings.auto_register("dbt-ldap")
class FlextDbtLdapSettings(FlextMeltanoSettings):
    """Runtime settings for DBT LDAP transformations."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_", extra="ignore"
    )

    # LDAP connection settings
    ldap_host: Annotated[str, u.Field(description="LDAP server hostname")] = c.LOCALHOST
    ldap_port: Annotated[int, u.Field(description="LDAP server port")] = c.Ldap.PORT
    ldap_use_tls: Annotated[
        bool,
        u.Field(
            description="Use TLS for LDAP connection",
        ),
    ] = c.Ldap.DEFAULT_USE_TLS
    ldap_bind_dn: Annotated[
        t.SecretStr | None, u.Field(description="LDAP bind DN for authentication")
    ] = None
    ldap_bind_password: Annotated[
        t.SecretStr | None, u.Field(description="LDAP bind password")
    ] = None
    ldap_base_dn: Annotated[
        str,
        u.Field(
            description="LDAP base DN for searches",
        ),
    ] = c.Ldap.EXAMPLE_BASE_DN

    # DBT project settings
    dbt_project_dir: Annotated[
        str, u.Field(description="Path to DBT project directory")
    ] = "."

    # Data quality settings
    min_quality_threshold: Annotated[
        float,
        u.Field(
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ] = c.DbtLdap.DEFAULT_QUALITY_THRESHOLD
    required_attributes: Annotated[
        t.StrSequence,
        u.Field(
            description="Required LDAP attributes for validation",
        ),
    ] = u.Field(default_factory=list)

    # Attribute mapping
    ldap_attribute_mapping: Annotated[
        t.StrMapping,
        u.Field(
            description="Mapping of LDAP attributes to DBT model attributes",
        ),
    ] = u.Field(default_factory=dict)

    # Schema mapping
    ldap_schema_mapping: Annotated[
        t.StrMapping,
        u.Field(
            description="Mapping of LDAP schemas to DBT tables",
        ),
    ] = u.Field(default_factory=dict)
