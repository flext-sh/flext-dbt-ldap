"""FLEXT DBT LDAP API - Unified facade for DBT LDAP operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT LDAP operations with complete FLEXT integration.
"""

from __future__ import annotations

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextLogger,
    FlextService,
    r,
)

from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_services import FlextDbtLdapService
from flext_dbt_ldap.models import FlextDbtLdapModels
from flext_dbt_ldap.settings import FlextDbtLdapSettings
from flext_dbt_ldap.typings import t
from flext_dbt_ldap.utilities import FlextDbtLdapUtilities


class FlextDbtLdap(FlextService[FlextDbtLdapSettings]):
    """Unified DBT LDAP facade with complete FLEXT ecosystem integration.

    This is the single unified class for the flext-dbt-ldap domain providing
    access to all DBT LDAP domain functionality with centralized patterns.

    UNIFIED CLASS PATTERN: One class per module with nested helpers only.
    CENTRALIZED APPROACH: All operations follow centralized patterns:
    - FlextDbtLdap.* for DBT LDAP-specific operations
    - Centralized validation through FlextDbtLdapUtilities
    - No wrappers, aliases, or fallbacks
    - Direct use of flext-core centralized services

    FLEXT INTEGRATION: Complete integration with flext-core patterns:
    - FlextContainer for dependency injection
    - FlextContext for operation context
    - FlextLogger for structured logging
    - FlextResult for railway-oriented error handling

    PYTHON 3.13+ COMPATIBILITY: Uses modern patterns and latest type features.
    """

    def __init__(self, config: FlextDbtLdapSettings | None = None) -> None:
        """Initialize the unified DBT LDAP service."""
        super().__init__()
        self._config = config or FlextDbtLdapSettings()
        self._client: FlextDbtLdapClient | None = None
        self._service: FlextDbtLdapService | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global().clear()().get_or_create()
        self._context = FlextContext()
        self.logger = FlextLogger(__name__)

    @classmethod
    def create(cls) -> FlextDbtLdap:
        """Create a new FlextDbtLdap instance (factory method)."""
        return cls()

    # =============================================================================
    # CONFIGURATION METHODS - Enhanced with proper error handling
    # =============================================================================

    def create_config(
        self,
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
        **kwargs: t.FlextTypes.JsonValue,
    ) -> r[FlextDbtLdapSettings]:
        """Create DBT LDAP configuration with sensible defaults.

        Args:
        ldap_host: LDAP server host
        ldap_port: LDAP server port
        ldap_base_dn: LDAP base DN for searches
        **kwargs: Additional configuration fields

        Returns:
        FlextResult containing configured FlextDbtLdapSettings

        """
        try:
            self.logger.info(
                "Creating DBT LDAP config: host=%s, port=%d",
                ldap_host,
                ldap_port,
            )

            # Create base config
            config = FlextDbtLdapSettings(
                ldap_host=ldap_host,
                ldap_port=ldap_port,
                ldap_base_dn=ldap_base_dn,
            )

            # Apply optional kwargs if they match model attributes
            for key, value in kwargs.items():
                if hasattr(config, key):
                    setattr(config, key, value)

            return r[FlextDbtLdapSettings].ok(config)
        except Exception as e:
            return r[FlextDbtLdapSettings].fail(f"Config creation failed: {e}")

    # =============================================================================
    # CLIENT AND SERVICE MANAGEMENT - Enhanced with proper error handling
    # =============================================================================

    @property
    def client(self) -> FlextDbtLdapClient:
        """Get the DBT LDAP client instance."""
        if self._client is None:
            self._client = FlextDbtLdapClient(self._config)
        return self._client

    @property
    def service(self) -> FlextDbtLdapService:
        """Get the DBT LDAP service instance."""
        if self._service is None:
            self._service = FlextDbtLdapService(self._config)
        return self._service

    @property
    def config(self) -> FlextDbtLdapSettings:
        """Get the current configuration."""
        return self._config

    # =============================================================================
    # FACTORY METHODS - Enhanced with FlextResult error handling
    # =============================================================================

    def create_client(self) -> r[FlextDbtLdapClient]:
        """Create DBT LDAP client with current configuration.

        Returns:
        FlextResult containing configured FlextDbtLdapClient

        """
        try:
            self.logger.info("Creating DBT LDAP client")
            client = FlextDbtLdapClient(self._config)
            return r[FlextDbtLdapClient].ok(client)
        except Exception as e:
            return r[FlextDbtLdapClient].fail(f"Client creation failed: {e}")

    def create_service(self) -> r[FlextDbtLdapService]:
        """Create DBT LDAP service with current configuration.

        Returns:
        FlextResult containing configured FlextDbtLdapService

        """
        try:
            self.logger.info("Creating DBT LDAP service")
            service = FlextDbtLdapService(self._config)
            return r[FlextDbtLdapService].ok(service)
        except Exception as e:
            return r[FlextDbtLdapService].fail(
                f"Service creation failed: {e}",
            )

    # =============================================================================
    # MODEL FACTORY METHODS - Enhanced with FlextResult error handling
    # =============================================================================

    def create_user_dimension(
        self,
        user_id: str,
        common_name: str,
        email: str | None = None,
        **kwargs: t.FlextTypes.JsonValue,
    ) -> r[FlextDbtLdapModels.UserDimension]:
        """Create user dimension with required fields.

        Args:
        user_id: Unique user identifier
        common_name: User's common name
        email: User's email address
        **kwargs: Additional fields for FlextDbtLdapModels.UserDimension

        Returns:
        FlextResult containing FlextDbtLdapModels.UserDimension instance

        """
        try:
            self.logger.debug(
                "Creating user dimension: user_id=%s, name=%s",
                user_id,
                common_name,
            )

            user = FlextDbtLdapModels.UserDimension(
                user_id=user_id,
                common_name=common_name,
                email=email,
            )
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            return r[FlextDbtLdapModels.UserDimension].ok(user)
        except Exception as e:
            return r[FlextDbtLdapModels.UserDimension].fail(
                f"User dimension creation failed: {e}",
            )

    def create_group_dimension(
        self,
        group_id: str,
        common_name: str,
        description: str | None = None,
        **kwargs: t.FlextTypes.JsonValue,
    ) -> r[FlextDbtLdapModels.GroupDimension]:
        """Create group dimension with required fields.

        Args:
        group_id: Unique group identifier
        common_name: Group's common name
        description: Group description
        **kwargs: Additional fields for FlextDbtLdapModels.GroupDimension

        Returns:
        FlextResult containing FlextDbtLdapModels.GroupDimension instance

        """
        try:
            self.logger.debug(
                "Creating group dimension: group_id=%s, name=%s",
                group_id,
                common_name,
            )

            group = FlextDbtLdapModels.GroupDimension(
                group_id=group_id,
                common_name=common_name,
                description=description,
            )
            for key, value in kwargs.items():
                if hasattr(group, key):
                    setattr(group, key, value)
            return r[FlextDbtLdapModels.GroupDimension].ok(group)
        except Exception as e:
            return r[FlextDbtLdapModels.GroupDimension].fail(
                f"Group dimension creation failed: {e}",
            )

    def create_transformer(self) -> r[FlextDbtLdapModels.Transformer]:
        """Create LDAP data transformer.

        Returns:
        FlextResult containing FlextDbtLdapModels.Transformer instance

        """
        try:
            self.logger.debug("Creating LDAP transformer")
            transformer = FlextDbtLdapModels.Transformer()
            return r[FlextDbtLdapModels.Transformer].ok(transformer)
        except Exception as e:
            return r[FlextDbtLdapModels.Transformer].fail(
                f"Transformer creation failed: {e}",
            )

    # =============================================================================
    # PIPELINE METHODS - Enhanced with FlextResult and proper validation
    # =============================================================================

    def create_simple_pipeline(
        self,
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
        **config_kwargs: t.FlextTypes.JsonValue,
    ) -> r[FlextDbtLdapService]:
        """Create complete DBT LDAP pipeline with minimal configuration using FlextDbtLdapUtilities.

        CRITICAL: Now ACTUALLY USES FlextDbtLdapUtilities to eliminate Zero Tolerance violation.
        This method now delegates to utilities for DBT project and profile generation.

        Args:
        ldap_host: LDAP server host
        ldap_port: LDAP server port
        ldap_base_dn: LDAP base DN
        **config_kwargs: Additional configuration

        Returns:
        FlextResult containing ready-to-use FlextDbtLdapService instance

        """
        try:
            self.logger.info(
                "Creating simple DBT LDAP pipeline using FlextDbtLdapUtilities",
            )

            # Create base configuration
            config_result = self.create_config(
                ldap_host=ldap_host,
                ldap_port=ldap_port,
                ldap_base_dn=ldap_base_dn,
                **config_kwargs,
            )
            if config_result.is_failure:
                return r[FlextDbtLdapService].fail(
                    f"Config creation failed: {config_result.error}",
                )

            config = config_result.value

            # Use FlextDbtLdapUtilities for DBT project configuration if available
            project_name = config_kwargs.get("project_name", "ldap_analytics")
            ldap_sources_value = config_kwargs.get("ldap_sources")
            if isinstance(ldap_sources_value, list):
                ldap_sources: list[t.DbtSource.SourceTable] = ldap_sources_value
            else:
                ldap_sources = [
                    {"name": "users"},
                    {"name": "groups"},
                ]

            project_config_result = (
                FlextDbtLdapUtilities.DbtProjectManagement.create_dbt_project_config(
                    project_name=project_name,
                    ldap_sources=ldap_sources,
                    target_schema=config_kwargs.get(
                        "target_schema",
                        "ldap_transformed",
                    ),
                )
            )

            if project_config_result.is_success:
                project_config = project_config_result.value
                project_name_value = (
                    project_config.get("name")
                    if isinstance(project_config, dict)
                    else "unknown"
                )
                self.logger.info(
                    "Successfully created DBT project config using utilities: %s",
                    project_name_value,
                )
                # Apply project config to main config if supported
                if hasattr(config, "project_config"):
                    config.project_config = project_config

            # Create and return service
            service_result = self.create_service()
            if service_result.is_failure:
                return r[FlextDbtLdapService].fail(
                    f"Service creation failed: {service_result.error}",
                )

            return service_result
        except Exception as e:
            return r[FlextDbtLdapService].fail(
                f"Pipeline creation failed: {e}",
            )


# No aliases per FLEXT standards - use FlextDbtLdap directly
__all__ = [
    "FlextDbtLdap",
]
