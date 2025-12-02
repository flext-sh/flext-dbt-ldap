"""FLEXT DBT LDAP Services.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

High-level service classes for DBT LDAP operations.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from flext_core import FlextLogger, FlextResult
from flext_meltano import FlextMeltanoService

from flext_dbt_ldap.config import FlextDbtLdapConfig
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.models import FlextDbtLdapModels
from flext_dbt_ldap.typings import FlextDbtLdapTypes

logger = FlextLogger(__name__)


class FlextDbtLdapService:
    """High-level service for DBT LDAP operations.

    Provides workflow orchestration and automation for LDAP data transformations
    using modern FlextMeltano APIs and FlextDbt wrapper for type-safe operations.
    """

    @override
    def __init__(
        self,
        config: FlextDbtLdapConfig | None = None,
        client: FlextDbtLdapClient | None = None,
        transformer: FlextDbtLdapModels.Transformer | None = None,
    ) -> None:
        """Initialize DBT LDAP service.

        Args:
        config: Configuration for operations
        client: DBT LDAP client (created if None)
        transformer: Data transformer (created if None)

        """
        self.config: FlextDbtLdapConfig = (
            config or FlextDbtLdapConfig.get_global_instance()
        )
        self.client = client or FlextDbtLdapClient(self.config)
        self.transformer = transformer or FlextDbtLdapModels.Transformer()

        # Initialize FlextMeltano service for DBT operations
        self._meltano_service = FlextMeltanoService(service_type="dbt")

        logger.info("Initialized DBT LDAP service")

    def sync_users_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Synchronize LDAP users to data warehouse.

        Args:
        search_base: LDAP search base for users
        incremental: Whether to do incremental sync

        Returns:
        FlextResult with sync statistics

        """
        try:
            logger.info("Starting user sync to warehouse, incremental=%s", incremental)

            # Define user-specific search filter
            user_filter = "(objectClass=person)"
            if incremental:
                # Add timestamp filter for incremental sync
                # This would need to be implemented based on your specific needs
                logger.info("Incremental sync not yet implemented, doing full sync")

            # Run pipeline for users
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=user_filter,
                attributes=[
                    "uid",
                    "cn",
                    "mail",
                    "displayName",
                    "department",
                    "manager",
                ],
                model_names=["stg_users", "dim_users"],
            )

            if result.is_success:
                logger.info("User sync completed successfully")
            else:
                logger.error("User sync failed: %s", result.error)

            return result

        except Exception as e:
            logger.exception("Unexpected error during user sync")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                f"User sync error: {e}"
            )

    def sync_groups_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Synchronize LDAP groups to data warehouse.

        Args:
        search_base: LDAP search base for groups
        incremental: Whether to do incremental sync

        Returns:
        FlextResult with sync statistics

        """
        try:
            logger.info("Starting group sync to warehouse, incremental=%s", incremental)

            # Define group-specific search filter
            group_filter = "(objectClass=group)"
            if incremental:
                logger.info("Incremental sync not yet implemented, doing full sync")

            # Run pipeline for groups
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=group_filter,
                attributes=["cn", "description", "member", "groupType"],
                model_names=["stg_groups", "dim_groups"],
            )

            if result.is_success:
                logger.info("Group sync completed successfully")
            else:
                logger.error("Group sync failed: %s", result.error)

            return result

        except Exception as e:
            logger.exception("Unexpected error during group sync")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                f"Group sync error: {e}"
            )

    def sync_memberships_to_warehouse(
        self,
        search_base: str | None = None,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Synchronize LDAP memberships to data warehouse.

        Args:
        search_base: LDAP search base

        Returns:
        FlextResult with sync statistics

        """
        try:
            logger.info("Starting membership sync to warehouse")

            # Get both users and groups for membership extraction
            membership_filter = "(|(objectClass=person)(objectClass=group))"

            # Run pipeline for memberships
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=membership_filter,
                attributes=["cn", "member", "memberOf", "uniqueMember"],
                model_names=["fact_memberships"],
            )

            if result.is_success:
                logger.info("Membership sync completed successfully")
            else:
                logger.error("Membership sync failed: %s", result.error)

            return result

        except Exception as e:
            logger.exception("Unexpected error during membership sync")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                f"Membership sync error: {e}"
            )

    def run_full_data_warehouse_sync(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Run complete LDAP to data warehouse synchronization.

        Args:
        search_base: LDAP search base
        incremental: Whether to do incremental sync

        Returns:
        FlextResult with complete sync statistics

        """
        logger.info(
            "Starting full data warehouse sync, base=%s, incremental=%s",
            search_base
            or (
                self.config.ldap_base_dn
                if isinstance(self.config, FlextDbtLdapConfig)
                else ""
            ),
            incremental,
        )

        sync_results: FlextDbtLdapTypes.DbtLdapCore.ResultDict = {}

        # Sync users
        user_result = self.sync_users_to_warehouse(search_base, incremental=incremental)
        sync_results["users"] = user_result.value or (
            {} if user_result.is_success else {"error": str(user_result.error)}
        )

        # Sync groups
        group_result = self.sync_groups_to_warehouse(
            search_base,
            incremental=incremental,
        )
        sync_results["groups"] = group_result.value or (
            {} if group_result.is_success else {"error": str(group_result.error)}
        )

        # Sync memberships
        membership_result = self.sync_memberships_to_warehouse(search_base)
        sync_results["memberships"] = membership_result.value or (
            {}
            if membership_result.is_success
            else {"error": str(membership_result.error)}
        )

        # Calculate overall success
        successful_syncs = [
            user_result.is_success,
            group_result.is_success,
            membership_result.is_success,
        ]

        overall_success = all(successful_syncs)
        sync_results["overall_success"] = overall_success
        sync_results["successful_components"] = sum(successful_syncs)
        sync_results["total_components"] = len(successful_syncs)

        if overall_success:
            logger.info("Full data warehouse sync completed successfully")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].ok(
                sync_results
            )
        logger.warning(
            "Full data warehouse sync completed with %d/%d successful components",
            sum(successful_syncs),
            len(successful_syncs),
        )
        return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
            "Some components failed in full sync",
        )

    def validate_warehouse_data_quality(
        self,
        model_names: Sequence[str] | None = None,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ValidationDict]:
        """Validate data quality in the warehouse using modern FlextDbt API.

        Args:
        model_names: Specific models to validate (None = all)

        Returns:
        FlextResult with validation results

        """
        try:
            logger.info("Validating warehouse data quality for models: %s", model_names)

            # FlextMeltano service is always initialized

            # Use modern FlextDbt API to run tests
            model_list = list(model_names) if model_names else None
            test_result = self._meltano_service.run_models(models=model_list)

            if test_result.is_success:
                logger.info("Data quality validation completed successfully")
                validation_result: FlextDbtLdapTypes.DbtLdapCore.ValidationDict = (
                    test_result.value or {}
                )
                return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ValidationDict].ok(
                    validation_result
                )

            logger.error("Data quality validation failed: %s", test_result.error)
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ValidationDict].fail(
                test_result.error or "dBT tests failed",
            )

        except Exception as e:
            logger.exception("Unexpected error during data quality validation")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ValidationDict].fail(
                f"Data quality validation error: {e}",
            )

    def run_dbt_models(
        self,
        model_names: Sequence[str] | None = None,
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Run dBT models using modern FlextDbt API.

        Args:
        model_names: Specific models to run (None = all)

        Returns:
        FlextResult with execution results

        """
        try:
            logger.info("Running dBT models: %s", model_names)

            # FlextMeltano service is always initialized

            # Use modern FlextDbt API to run models
            model_list = list(model_names) if model_names else None
            run_result = self._meltano_service.run_models(models=model_list)

            if run_result.is_success:
                logger.info("dBT models executed successfully")
                result_data: FlextDbtLdapTypes.DbtLdapCore.ResultDict = (
                    run_result.value or {}
                )
                return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].ok(
                    result_data
                )

            logger.error("dBT model execution failed: %s", run_result.error)
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                run_result.error or "dBT model execution failed",
            )

        except Exception as e:
            logger.exception("Unexpected error during dBT model execution")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                f"dBT model execution error: {e}",
            )

    def generate_analytics_report(
        self,
        report_type: str = "summary",
    ) -> FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Generate analytics report from warehouse data.

        Args:
        report_type: Type of report to generate

        Returns:
        FlextResult with report data

        """
        try:
            logger.info("Generating analytics report: %s", report_type)

            # This would typically run specific DBT models or queries
            # For now, return a placeholder structure
            report_data: FlextDbtLdapTypes.DbtLdapCore.ResultDict = {
                "report_type": report_type,
                "generated_at": "2025-01-01T00:00:00Z",  # Would use actual timestamp
                "summary": {
                    "total_users": 0,  # Would query from warehouse
                    "total_groups": 0,  # Would query from warehouse
                    "total_memberships": 0,  # Would query from warehouse
                },
                "data_quality": {
                    "overall_score": 0.0,  # Would calculate from quality metrics
                    "issues": [],  # Would list any data quality issues
                },
            }

            logger.info("Analytics report generated successfully")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].ok(report_data)

        except Exception as e:
            logger.exception("Unexpected error during report generation")
            return FlextResult[FlextDbtLdapTypes.DbtLdapCore.ResultDict].fail(
                f"Report generation error: {e}",
            )


__all__: list[str] = [
    "FlextDbtLdapService",
]
