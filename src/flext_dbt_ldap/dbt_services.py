"""DBT services for LDAP operations.

Provides high-level service operations for DBT LDAP workflows.
Builds on dbt_client to provide workflow orchestration and automation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextResult, get_logger
from flext_meltano import FlextMeltanoDbtService

from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig
from flext_dbt_ldap.models import FlextDbtLdapTransformer

logger = get_logger(__name__)


class FlextDbtLdapService:
    """High-level service for DBT LDAP operations.

    Provides workflow orchestration and automation for LDAP data transformations.
    """

    def __init__(
        self,
        config: FlextDbtLdapConfig | None = None,
        client: FlextDbtLdapClient | None = None,
        transformer: FlextDbtLdapTransformer | None = None,
    ) -> None:
        """Initialize DBT LDAP service.

        Args:
            config: Configuration for operations
            client: DBT LDAP client (created if None)
            transformer: Data transformer (created if None)

        """
        self.config = config or FlextDbtLdapConfig()
        self.client = client or FlextDbtLdapClient(self.config)
        self.transformer = transformer or FlextDbtLdapTransformer()

        logger.info("Initialized DBT LDAP service")

    def sync_users_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[dict[str, object]]:
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
            return FlextResult[dict[str, object]].fail(f"User sync error: {e}")

    def sync_groups_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[dict[str, object]]:
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
            return FlextResult[dict[str, object]].fail(f"Group sync error: {e}")

    def sync_memberships_to_warehouse(
        self,
        search_base: str | None = None,
    ) -> FlextResult[dict[str, object]]:
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
            return FlextResult[dict[str, object]].fail(f"Membership sync error: {e}")

    def run_full_data_warehouse_sync(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> FlextResult[dict[str, object]]:
        """Run complete LDAP to data warehouse synchronization.

        Args:
            search_base: LDAP search base
            incremental: Whether to do incremental sync

        Returns:
            FlextResult with complete sync statistics

        """
        logger.info(
            "Starting full data warehouse sync, base=%s, incremental=%s",
            search_base or self.config.ldap_base_dn,
            incremental,
        )

        sync_results: dict[str, object] = {}

        # Sync users
        user_result = self.sync_users_to_warehouse(search_base, incremental=incremental)
        sync_results["users"] = (
            user_result.value
            if user_result.is_success
            else {"error": str(user_result.error)}
        )

        # Sync groups
        group_result = self.sync_groups_to_warehouse(
            search_base,
            incremental=incremental,
        )
        sync_results["groups"] = (
            group_result.value
            if group_result.is_success
            else {"error": str(group_result.error)}
        )

        # Sync memberships
        membership_result = self.sync_memberships_to_warehouse(search_base)
        sync_results["memberships"] = (
            membership_result.value
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
            return FlextResult[dict[str, object]].ok(sync_results)
        logger.warning(
            "Full data warehouse sync completed with %d/%d successful components",
            sum(successful_syncs),
            len(successful_syncs),
        )
        return FlextResult[dict[str, object]].fail("Some components failed in full sync")

    def validate_warehouse_data_quality(
        self,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Validate data quality in the warehouse.

        Args:
            model_names: Specific models to validate (None = all)

        Returns:
            FlextResult with validation results

        """
        try:
            logger.info("Validating warehouse data quality for models: %s", model_names)

            # Use DBT service to run tests
            manager = FlextMeltanoDbtService(project_name="flext_dbt_ldap")

            # Create DBT runner first
            runner_result = manager.wrapper_dbt.create_runner()
            if runner_result.is_failure:
                return FlextResult[dict[str, object]].fail(
                    runner_result.error or "Failed to create DBT runner"
                )

            # Run tests with the runner
            result = manager.test_models(runner_result.value, model_names)

            if result.is_success:
                logger.info("Data quality validation completed")
            else:
                logger.error("Data quality validation failed: %s", result.error)

            return result

        except Exception as e:
            logger.exception("Unexpected error during data quality validation")
            return FlextResult[dict[str, object]].fail(f"Data quality validation error: {e}")

    def generate_analytics_report(
        self,
        report_type: str = "summary",
    ) -> FlextResult[dict[str, object]]:
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
            report_data: dict[str, object] = {
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
            return FlextResult[dict[str, object]].ok(report_data)

        except Exception as e:
            logger.exception("Unexpected error during report generation")
            return FlextResult[dict[str, object]].fail(f"Report generation error: {e}")


__all__: list[str] = [
    "FlextDbtLdapService",
]
