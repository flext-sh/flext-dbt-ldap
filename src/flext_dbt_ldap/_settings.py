"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtLdapSettings(FlextMeltanoSettings):
    """Runtime settings for DBT LDAP transformations."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_",
        extra="ignore",
    )

    # LDAP connection settings
    ldap_host: Annotated[str, Field(description="LDAP server hostname")] = "localhost"
    ldap_port: Annotated[int, Field(description="LDAP server port")] = 389
    ldap_use_tls: Annotated[
        bool,
        Field(description="Use TLS for LDAP connection"),
    ] = False
    ldap_bind_dn: Annotated[
        SecretStr | None,
        Field(description="LDAP bind DN for authentication"),
    ] = None
    ldap_bind_password: Annotated[
        SecretStr | None,
        Field(description="LDAP bind password"),
    ] = None
    ldap_base_dn: Annotated[
        str,
        Field(description="LDAP base DN for searches"),
    ] = "dc=example,dc=com"

    # DBT project settings
    dbt_project_dir: Annotated[
        str,
        Field(description="Path to DBT project directory"),
    ] = "."

    # Data quality settings
    min_quality_threshold: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ] = 0.8
    required_attributes: Annotated[
        list[str],
        Field(description="Required LDAP attributes for validation"),
    ] = Field(default_factory=list)

    # Attribute mapping
    ldap_attribute_mapping: Annotated[
        dict[str, str],
        Field(description="Mapping of LDAP attributes to DBT model attributes"),
    ] = Field(default_factory=dict)

    # Schema mapping
    ldap_schema_mapping: Annotated[
        dict[str, str],
        Field(description="Mapping of LDAP schemas to DBT tables"),
    ] = Field(default_factory=dict)


settings: FlextDbtLdapSettings = FlextDbtLdapSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_ldap import settings``."""
