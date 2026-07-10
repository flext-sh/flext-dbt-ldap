"""FLEXT DBT LDAP settings — namespaced under ``settings.DbtLdap``.

Universal fields via MRO; project fields in the ``DbtLdap`` group with simple
scalar types (env-settable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtLdapSettings(FlextMeltanoSettings):
    """Runtime settings for DBT LDAP transformations; fields under ``settings.DbtLdap.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _DbtLdap(BaseModel):
        """Namespaced dbt-LDAP settings."""

        ldap_host: Annotated[str, Field(default="localhost", description="LDAP server hostname")]
        ldap_port: Annotated[int, Field(default=389, description="LDAP server port")]
        ldap_use_tls: Annotated[bool, Field(default=False, description="Use TLS for LDAP connection")]
        ldap_bind_dn: Annotated[str, Field(default="", description="LDAP bind DN for authentication")]
        ldap_bind_password: Annotated[str, Field(default="", description="LDAP bind password")]
        ldap_base_dn: Annotated[str, Field(default="dc=example,dc=com", description="LDAP base DN")]
        dbt_project_dir: Annotated[str, Field(default=".", description="Path to DBT project directory")]
        min_quality_threshold: Annotated[
            float,
            Field(default=0.8, ge=0.0, le=1.0, description="Minimum data quality score threshold"),
        ]
        required_attributes: Annotated[
            list[str],
            Field(default_factory=list, description="Required LDAP attributes for validation"),
        ]
        ldap_attribute_mapping: Annotated[
            dict[str, str],
            Field(default_factory=dict, description="Mapping of LDAP attributes to DBT model attributes"),
        ]
        ldap_schema_mapping: Annotated[
            dict[str, str],
            Field(default_factory=dict, description="Mapping of LDAP schemas to DBT tables"),
        ]

    if TYPE_CHECKING:
        DbtLdap: _DbtLdap
    else:
        DbtLdap: _DbtLdap = Field(
            default_factory=_DbtLdap,
            description="Namespaced dbt-LDAP settings.",
        )


settings: FlextDbtLdapSettings = FlextDbtLdapSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_ldap import settings``."""

__all__: list[str] = ["FlextDbtLdapSettings", "settings"]
