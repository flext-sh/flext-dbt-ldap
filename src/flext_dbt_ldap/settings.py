"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, FlextSettings
from pydantic import Field, SecretStr

logger = FlextLogger(__name__)


class FlextDbtLdapSettings(FlextSettings):
    """Runtime settings for DBT LDAP transformations."""

    # LDAP connection settings
    ldap_host: str = Field(default="localhost", description="LDAP server hostname")
    ldap_port: int = Field(default=389, description="LDAP server port")
    ldap_use_tls: bool = Field(default=False, description="Use TLS for LDAP connection")
    ldap_bind_dn: SecretStr | None = Field(
        default=None, description="LDAP bind DN for authentication"
    )
    ldap_bind_password: SecretStr | None = Field(
        default=None, description="LDAP bind password"
    )
    ldap_base_dn: str = Field(
        default="dc=example,dc=com", description="LDAP base DN for searches"
    )

    # DBT project settings
    dbt_project_dir: str = Field(
        default=".", description="Path to DBT project directory"
    )

    # Data quality settings
    min_quality_threshold: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Minimum data quality score threshold"
    )
    required_attributes: list[str] = Field(
        default_factory=list, description="Required LDAP attributes for validation"
    )

    # Attribute mapping
    ldap_attribute_mapping: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of LDAP attributes to DBT model attributes",
    )

    # Schema mapping
    ldap_schema_mapping: dict[str, str] = Field(
        default_factory=dict, description="Mapping of LDAP schemas to DBT tables"
    )


__all__: list[str] = ["FlextDbtLdapSettings"]
