"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_dbt_ldap import c, t


@FlextSettings.auto_register("dbt-ldap")
class FlextDbtLdapSettings(FlextSettings):
    """Runtime settings for DBT LDAP transformations."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_",
        extra="ignore",
    )

    # LDAP connection settings
    ldap_host: Annotated[
        str,
        Field(default=c.LOCALHOST, description="LDAP server hostname"),
    ]
    ldap_port: Annotated[
        int,
        Field(default=c.Ldap.ConnectionDefaults.PORT, description="LDAP server port"),
    ]
    ldap_use_tls: Annotated[
        bool,
        Field(
            default=c.Ldap.ConnectionDefaults.DEFAULT_USE_TLS,
            description="Use TLS for LDAP connection",
        ),
    ]
    ldap_bind_dn: Annotated[
        SecretStr | None,
        Field(default=None, description="LDAP bind DN for authentication"),
    ]
    ldap_bind_password: Annotated[
        SecretStr | None,
        Field(default=None, description="LDAP bind password"),
    ]
    ldap_base_dn: Annotated[
        str,
        Field(
            default=c.Ldap.Defaults.EXAMPLE_BASE_DN,
            description="LDAP base DN for searches",
        ),
    ]

    # DBT project settings
    dbt_project_dir: Annotated[
        str,
        Field(default=".", description="Path to DBT project directory"),
    ]

    # Data quality settings
    min_quality_threshold: Annotated[
        float,
        Field(
            default=c.DbtLdap.DEFAULT_QUALITY_THRESHOLD,
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ]
    required_attributes: Annotated[
        t.StrSequence,
        Field(
            description="Required LDAP attributes for validation",
        ),
    ] = Field(default_factory=list)

    # Attribute mapping
    ldap_attribute_mapping: Annotated[
        t.StrMapping,
        Field(
            description="Mapping of LDAP attributes to DBT model attributes",
        ),
    ] = Field(default_factory=dict)

    # Schema mapping
    ldap_schema_mapping: Annotated[
        t.StrMapping,
        Field(
            description="Mapping of LDAP schemas to DBT tables",
        ),
    ] = Field(default_factory=dict)
