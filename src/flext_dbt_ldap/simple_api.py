"""FLEXT DBT LDAP API - Unified facade for DBT LDAP operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextService, r

from flext_dbt_ldap import m
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_services import FlextDbtLdapService
from flext_dbt_ldap.settings import FlextDbtLdapSettings
from flext_dbt_ldap.utilities import FlextDbtLdapUtilities


class FlextDbtLdap(FlextService[FlextDbtLdapSettings]):
    """Unified DBT LDAP facade with complete FLEXT ecosystem integration."""

    def __init__(self, config: FlextDbtLdapSettings | None = None) -> None:
        """Initialize the unified DBT LDAP service."""
        super().__init__()
        self._dbt_ldap_config: FlextDbtLdapSettings = (
            config if config is not None else FlextDbtLdapSettings.model_validate({})
        )
        self._config = self._dbt_ldap_config
        self._client: FlextDbtLdapClient | None = None
        self._service: FlextDbtLdapService | None = None

    @property
    def client(self) -> FlextDbtLdapClient:
        """Get the DBT LDAP client instance."""
        if self._client is None:
            ldap_api = FlextDbtLdapClient.create_ldap_api(self.config)
            self._client = FlextDbtLdapClient(self.config, ldap_api=ldap_api)
        return self._client

    @property
    @override
    def config(self) -> FlextDbtLdapSettings:
        """Get the current configuration."""
        return self._dbt_ldap_config

    @property
    def service(self) -> FlextDbtLdapService:
        """Get the DBT LDAP service instance."""
        if self._service is None:
            self._service = FlextDbtLdapService(self.config)
        return self._service

    @classmethod
    def create(cls) -> FlextDbtLdap:
        """Create a new FlextDbtLdap instance (factory method)."""
        return cls()

    def create_client(self) -> r[FlextDbtLdapClient]:
        """Create DBT LDAP client with current configuration."""
        try:
            self.logger.info("Creating DBT LDAP client")
            ldap_api = FlextDbtLdapClient.create_ldap_api(self.config)
            client = FlextDbtLdapClient(self.config, ldap_api=ldap_api)
            return r[FlextDbtLdapClient].ok(client)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextDbtLdapClient].fail(f"Client creation failed: {e}")

    def create_config(
        self,
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
    ) -> r[FlextDbtLdapSettings]:
        """Create DBT LDAP configuration with sensible defaults."""
        try:
            self.logger.info(
                "Creating DBT LDAP config: host=%s, port=%d",
                ldap_host,
                ldap_port,
            )
            config = FlextDbtLdapSettings.model_validate({
                "ldap_host": ldap_host,
                "ldap_port": ldap_port,
                "ldap_base_dn": ldap_base_dn,
            })
            return r[FlextDbtLdapSettings].ok(config)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextDbtLdapSettings].fail(f"Config creation failed: {e}")

    def create_group_dimension(
        self,
        group_id: str,
        common_name: str,
        description: str | None = None,
    ) -> r[m.GroupDimension]:
        """Create group dimension with required fields."""
        try:
            self.logger.debug(
                "Creating group dimension: group_id=%s, name=%s",
                group_id,
                common_name,
            )
            group = m.GroupDimension(
                group_id=group_id,
                common_name=common_name,
                description=description,
            )
            return r[m.GroupDimension].ok(group)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[m.GroupDimension].fail(f"Group dimension creation failed: {e}")

    def create_service(self) -> r[FlextDbtLdapService]:
        """Create DBT LDAP service with current configuration."""
        try:
            self.logger.info("Creating DBT LDAP service")
            service = FlextDbtLdapService(self.config)
            return r[FlextDbtLdapService].ok(service)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextDbtLdapService].fail(f"Service creation failed: {e}")

    def create_simple_pipeline(
        self,
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
    ) -> r[FlextDbtLdapService]:
        """Create complete DBT LDAP pipeline with minimal configuration."""
        try:
            self.logger.info(
                "Creating simple DBT LDAP pipeline using FlextDbtLdapUtilities",
            )
            config_result = self.create_config(
                ldap_host=ldap_host,
                ldap_port=ldap_port,
                ldap_base_dn=ldap_base_dn,
            )
            if config_result.is_failure:
                return r[FlextDbtLdapService].fail(
                    f"Config creation failed: {config_result.error}",
                )
            ldap_sources = [
                m.DbtSourceTable(name="users"),
                m.DbtSourceTable(name="groups"),
            ]
            project_config_result = (
                FlextDbtLdapUtilities.DbtLdap.create_dbt_project_config(
                    project_name="ldap_analytics",
                    ldap_sources=ldap_sources,
                    target_schema="ldap_transformed",
                )
            )
            if project_config_result.is_success:
                self.logger.info(
                    "Created DBT project config: %s",
                    project_config_result.value.name
                    if project_config_result.value
                    else "unknown",
                )
            return self.create_service()
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextDbtLdapService].fail(f"Pipeline creation failed: {e}")

    def create_transformer(self) -> r[m.DbtLdap]:
        """Create LDAP data transformer."""
        try:
            self.logger.debug("Creating LDAP transformer")
            transformer = m.DbtLdap()
            return r[m.DbtLdap].ok(transformer)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[m.DbtLdap].fail(f"Transformer creation failed: {e}")

    def create_user_dimension(
        self,
        user_id: str,
        common_name: str,
        email: str | None = None,
    ) -> r[m.UserDimension]:
        """Create user dimension with required fields."""
        try:
            self.logger.debug(
                "Creating user dimension: user_id=%s, name=%s",
                user_id,
                common_name,
            )
            user = m.UserDimension(
                user_id=user_id,
                common_name=common_name,
                email=email,
            )
            return r[m.UserDimension].ok(user)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[m.UserDimension].fail(f"User dimension creation failed: {e}")

    @override
    def execute(self) -> r[FlextDbtLdapSettings]:
        """Execute DBT LDAP domain service logic."""
        client_result = self.create_client()
        if client_result.is_failure:
            return r[FlextDbtLdapSettings].fail(
                f"Failed to create client: {client_result.error}",
            )
        return r[FlextDbtLdapSettings].ok(self.config)


__all__ = ["FlextDbtLdap"]
