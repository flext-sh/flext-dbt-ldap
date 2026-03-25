"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated

from flext_core import FlextLogger, FlextSettings
from pydantic import Field, SecretStr

from flext_dbt_ldap import t

logger = FlextLogger(__name__)


class FlextDbtLdapSettings(FlextSettings):
    """Runtime settings for DBT LDAP transformations."""

    # LDAP connection settings
    ldap_host: Annotated[
        str,
        Field(default="localhost", description="LDAP server hostname"),
    ]
    ldap_port: Annotated[int, Field(default=389, description="LDAP server port")]
    ldap_use_tls: Annotated[
        bool,
        Field(default=False, description="Use TLS for LDAP connection"),
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
        Field(default="dc=example,dc=com", description="LDAP base DN for searches"),
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
            default=0.8,
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


__all__: t.StrSequence = ["FlextDbtLdapSettings"]
