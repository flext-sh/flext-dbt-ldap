"""FLEXT DBT LDAP Simple API.

Simple API for FLEXT DBT LDAP operations.
"""

from __future__ import annotations

from flext_core import FlextLogger, FlextTypes
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig
from flext_dbt_ldap.dbt_services import FlextDbtLdapService
from flext_dbt_ldap.models import (
    FlextDbtLdapGroupDimension,
    FlextDbtLdapTransformer,
    FlextDbtLdapUserDimension,
)

logger = FlextLogger(__name__)


class FlextDbtLdapSimpleApi:
    """Unified DBT LDAP simple API with factory methods."""

    @staticmethod
    def create_flext_dbt_ldap_config(
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
        **kwargs: object,
    ) -> FlextDbtLdapConfig:
        """Create DBT LDAP configuration with sensible defaults.

        Args:
          ldap_host: LDAP server host
          ldap_port: LDAP server port
          ldap_base_dn: LDAP base DN for searches
          **kwargs: Additional configuration fields accepted by `FlextDbtLdapConfig`
          ldap_use_tls: Use LDAPS
          ldap_bind_dn: Bind DN for authentication
          ldap_bind_password: Bind password
          dbt_project_dir: DBT project directory
          dbt_profiles_dir: DBT profiles directory
          dbt_target: DBT target profile
          dbt_threads: DBT threads
          dbt_log_level: DBT log level

        Returns:
          Configured FlextDbtLdapConfig instance

        """
        logger.info("Creating DBT LDAP config: host=%s, port=%d", ldap_host, ldap_port)

        # Support only known fields to satisfy strict typing
        config = FlextDbtLdapConfig(
            ldap_host=ldap_host,
            ldap_port=ldap_port,
            ldap_base_dn=ldap_base_dn,
        )
        # Apply optional kwargs if they match model attributes
        for key, value in kwargs.items():
            if hasattr(config, key):
                setattr(config, key, value)
        return config

    @staticmethod
    def create_flext_dbt_ldap_client(
        config: FlextDbtLdapConfig | None = None,
    ) -> FlextDbtLdapClient:
        """Create DBT LDAP client with configuration.

        Args:
          config: Configuration (created with defaults if None)

        Returns:
          Configured FlextDbtLdapClient instance

        """
        if config is None:
            config = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_config()

        logger.info("Creating DBT LDAP client")
        return FlextDbtLdapClient(config)

    @staticmethod
    def create_flext_dbt_ldap_service(
        config: FlextDbtLdapConfig | None = None,
    ) -> FlextDbtLdapService:
        """Create DBT LDAP service with configuration.

        Args:
          config: Configuration (created with defaults if None)

        Returns:
          Configured FlextDbtLdapService instance

        """
        if config is None:
            config = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_config()

        logger.info("Creating DBT LDAP service")
        return FlextDbtLdapService(config)

    @staticmethod
    def create_flext_user_dimension(
        user_id: str,
        common_name: str,
        email: str | None = None,
        **kwargs: object,
    ) -> FlextDbtLdapUserDimension:
        """Create user dimension with required fields.

        Args:
          user_id: Unique user identifier
          common_name: User's common name
          email: User's email address
          **kwargs: Additional fields for `FlextDbtLdapUserDimension`
          display_name: Display name
          department: Department name
          manager_dn: Manager DN
          employee_number: Employee number
          phone: Phone number
          is_active: Active flag
          created_date: Created timestamp
          modified_date: Modified timestamp

        Returns:
          FlextDbtLdapUserDimension instance

        """
        logger.debug(
            "Creating user dimension: user_id=%s, name=%s",
            user_id,
            common_name,
        )

        user = FlextDbtLdapUserDimension(
            user_id=user_id,
            common_name=common_name,
            email=email,
        )
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return user

    @staticmethod
    def create_flext_group_dimension(
        group_id: str,
        common_name: str,
        description: str | None = None,
        **kwargs: object,
    ) -> FlextDbtLdapGroupDimension:
        """Create group dimension with required fields.

        Args:
          group_id: Unique group identifier
          common_name: Group's common name
          description: Group description
          **kwargs: Additional fields for `FlextDbtLdapGroupDimension`
          group_type: Group type
          member_count: Number of members
          is_active: Active flag
          created_date: Created timestamp
          modified_date: Modified timestamp

        Returns:
          FlextDbtLdapGroupDimension instance

        """
        logger.debug(
            "Creating group dimension: group_id=%s, name=%s",
            group_id,
            common_name,
        )

        group = FlextDbtLdapGroupDimension(
            group_id=group_id,
            common_name=common_name,
            description=description,
        )
        for key, value in kwargs.items():
            if hasattr(group, key):
                setattr(group, key, value)
        return group

    @staticmethod
    def create_flext_ldap_transformer() -> FlextDbtLdapTransformer:
        """Create LDAP data transformer.

        Returns:
          FlextDbtLdapTransformer instance

        """
        logger.debug("Creating LDAP transformer")
        return FlextDbtLdapTransformer()

    @staticmethod
    def create_simple_dbt_ldap_pipeline(
        ldap_host: str = "localhost",
        ldap_port: int = 389,
        ldap_base_dn: str = "",
        **config_kwargs: object,
    ) -> FlextDbtLdapService:
        """Create complete DBT LDAP pipeline with minimal configuration.

        This is the simplest way to get started with DBT LDAP transformations.

        Args:
          ldap_host: LDAP server host
          ldap_port: LDAP server port
          ldap_base_dn: LDAP base DN
          **config_kwargs: Additional configuration

        Returns:
          Ready-to-use FlextDbtLdapService instance

        """
        logger.info("Creating simple DBT LDAP pipeline")

        config = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_config(
            ldap_host=ldap_host,
            ldap_port=ldap_port,
            ldap_base_dn=ldap_base_dn,
            **config_kwargs,
        )

        return FlextDbtLdapSimpleApi.create_flext_dbt_ldap_service(config)


# Backward compatibility aliases
create_flext_dbt_ldap_config = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_config
create_flext_dbt_ldap_client = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_client
create_flext_dbt_ldap_service = FlextDbtLdapSimpleApi.create_flext_dbt_ldap_service
create_flext_user_dimension = FlextDbtLdapSimpleApi.create_flext_user_dimension
create_flext_group_dimension = FlextDbtLdapSimpleApi.create_flext_group_dimension
create_flext_ldap_transformer = FlextDbtLdapSimpleApi.create_flext_ldap_transformer
create_simple_dbt_ldap_pipeline = FlextDbtLdapSimpleApi.create_simple_dbt_ldap_pipeline


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdapSimpleApi",
    "create_flext_dbt_ldap_client",
    "create_flext_dbt_ldap_config",
    "create_flext_dbt_ldap_service",
    "create_flext_group_dimension",
    "create_flext_ldap_transformer",
    "create_flext_user_dimension",
    "create_simple_dbt_ldap_pipeline",
]
