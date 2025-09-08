"""DBT configuration for LDAP transformations.

Provides configuration management for DBT LDAP projects using flext-core patterns.
Integrates with flext-ldap for connection settings and flext-meltano for DBT execution.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConfig, FlextLogger, FlextTypes
from flext_ldap import FlextLDAPConnectionConfig
from flext_meltano.config import FlextMeltanoConfig

logger = FlextLogger(__name__)


class FlextDbtLdapConfig(FlextConfig):
    """Configuration for DBT LDAP transformations.

    Combines LDAP connection settings with DBT execution configuration.
    Uses composition to integrate flext-ldap and flext-meltano configurations.
    """

    # LDAP Connection Settings (from flext-ldap)
    ldap_host: str = "localhost"
    ldap_port: int = 389
    ldap_use_tls: bool = False
    ldap_bind_dn: str = ""
    ldap_bind_password: str = ""
    ldap_base_dn: str = ""

    # DBT Execution Settings (from flext-meltano)
    dbt_project_dir: str = "."
    dbt_profiles_dir: str = "."
    dbt_target: str = "dev"
    dbt_threads: int = 1
    dbt_log_level: str = "info"

    # LDAP-specific DBT Settings
    ldap_schema_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "users": "stg_users",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
    }

    ldap_attribute_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
    }

    # Data Quality Settings
    min_quality_threshold: float = 0.8
    required_attributes: ClassVar[FlextTypes.Core.StringList] = ["cn", "objectClass"]
    validate_dns: bool = True

    def get_ldap_config(self) -> FlextLDAPConnectionConfig:
        """Get LDAP configuration for flext-ldap integration."""
        return FlextLDAPConnectionConfig(
            server=self.ldap_host,
            port=self.ldap_port,
            base_dn=self.ldap_base_dn,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        return FlextMeltanoConfig(
            project_root=self.dbt_project_dir,
            environment=self.dbt_target,
        )

    def get_ldap_quality_config(self) -> FlextTypes.Core.Dict:
        """Get data quality configuration for LDAP validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_attributes": self.required_attributes,
            "validate_dns": self.validate_dns,
        }


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdapConfig",
]
