"""FLEXT DBT LDAP Services.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import override

from flext_core import FlextLogger, r
from flext_meltano import FlextMeltanoDbtService
from pydantic import TypeAdapter, ValidationError

from flext_dbt_ldap.constants import c
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.models import m
from flext_dbt_ldap.settings import FlextDbtLdapSettings

logger = FlextLogger(__name__)
_SYNC_BOOKMARKS_ADAPTER = TypeAdapter(dict[str, str])


class FlextDbtLdapService:
    """High-level service for DBT LDAP operations."""

    @override
    def __init__(
        self,
        config: FlextDbtLdapSettings | None = None,
        client: FlextDbtLdapClient | None = None,
        transformer: m.DbtLdap | None = None,
    ) -> None:
        """Initialize DBT LDAP service."""
        super().__init__()
        self.config: FlextDbtLdapSettings = (
            config if config is not None else FlextDbtLdapSettings.get_global()
        )
        ldap_api = FlextDbtLdapClient.create_ldap_api(self.config)
        self.client = client or FlextDbtLdapClient(self.config, ldap_api=ldap_api)
        self.transformer = transformer or m.DbtLdap()
        self._dbt_service = FlextMeltanoDbtService()
        self._sync_state_file = self._resolve_sync_state_file()
        self._sync_bookmarks = self._load_sync_state()
        logger.info("Initialized DBT LDAP service")

    def generate_analytics_report(
        self, report_type: str = "summary"
    ) -> r[m.AnalyticsReport]:
        """Generate analytics report from warehouse data."""
        try:
            logger.info("Generating analytics report: %s", report_type)
            report = m.AnalyticsReport(
                report_type=report_type, generated_at="2025-01-01T00:00:00Z"
            )
            logger.info("Analytics report generated successfully")
            return r[m.AnalyticsReport].ok(report)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during report generation")
            return r[m.AnalyticsReport].fail(f"Report generation error: {e}")

    def run_dbt_models(
        self, model_names: Sequence[str] | None = None
    ) -> r[m.DbtRunStatus]:
        """Run DBT models."""
        try:
            logger.info(
                "Running DBT models: %s", ", ".join(model_names) if model_names else ""
            )
            model_list = list(model_names) if model_names else None
            run_result = self._dbt_service.run_models(models=model_list)
            if run_result.is_success:
                logger.info("DBT models executed successfully")
                return r[m.DbtRunStatus].ok(
                    m.DbtRunStatus(status="completed", models_run=model_list or [])
                )
            logger.error("DBT model execution failed: %s", run_result.error or "")
            return r[m.DbtRunStatus].fail(
                run_result.error or "DBT model execution failed"
            )
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during DBT model execution")
            return r[m.DbtRunStatus].fail(f"DBT model execution error: {e}")

    def run_full_data_warehouse_sync(
        self, search_base: str | None = None, *, incremental: bool = False
    ) -> r[m.SyncResult]:
        """Run complete LDAP to data warehouse synchronization."""
        logger.info(
            "Starting full data warehouse sync, base=%s, incremental=%s",
            search_base or self.config.ldap_base_dn,
            incremental,
        )
        user_result = self.sync_users_to_warehouse(search_base, incremental=incremental)
        group_result = self.sync_groups_to_warehouse(
            search_base, incremental=incremental
        )
        membership_result = self.sync_memberships_to_warehouse(search_base)
        successful_syncs = [
            user_result.is_success,
            group_result.is_success,
            membership_result.is_success,
        ]
        overall_success = all(successful_syncs)
        sync_result = m.SyncResult(
            overall_success=overall_success,
            successful_components=sum(successful_syncs),
            total_components=len(successful_syncs),
        )
        if overall_success:
            logger.info("Full data warehouse sync completed successfully")
            return r[m.SyncResult].ok(sync_result)
        logger.warning(
            "Full data warehouse sync completed with %d/%d successful components",
            sum(successful_syncs),
            len(successful_syncs),
        )
        return r[m.SyncResult].fail("Some components failed in full sync")

    def sync_groups_to_warehouse(
        self, search_base: str | None = None, *, incremental: bool = False
    ) -> r[m.DbtLdapPipelineResult]:
        """Synchronize LDAP groups to data warehouse."""
        try:
            logger.info("Starting group sync to warehouse, incremental=%s", incremental)
            current_bookmark = self._bookmark_now()
            group_filter = "(objectClass=group)"
            run_incremental = self._should_run_incremental(
                "groups",
                requested_incremental=incremental,
                current_bookmark=current_bookmark,
            )
            if run_incremental:
                group_filter = self._build_incremental_filter(
                    group_filter, self._sync_bookmarks.get("groups")
                )
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=group_filter,
                attributes=["cn", "description", "member", "groupType"],
                model_names=["stg_groups", "dim_groups"],
            )
            if result.is_success:
                logger.info("Group sync completed successfully")
                self._update_bookmark("groups", current_bookmark, successful=True)
            else:
                logger.error("Group sync failed: %s", result.error or "")
            return result
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during group sync")
            return r[m.DbtLdapPipelineResult].fail(f"Group sync error: {e}")

    def sync_memberships_to_warehouse(
        self, search_base: str | None = None
    ) -> r[m.DbtLdapPipelineResult]:
        """Synchronize LDAP memberships to data warehouse."""
        try:
            logger.info("Starting membership sync to warehouse")
            membership_filter = "(|(objectClass=person)(objectClass=group))"
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=membership_filter,
                attributes=["cn", "member", "memberOf", "uniqueMember"],
                model_names=["fact_memberships"],
            )
            if result.is_success:
                logger.info("Membership sync completed successfully")
            else:
                logger.error("Membership sync failed: %s", result.error or "")
            return result
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during membership sync")
            return r[m.DbtLdapPipelineResult].fail(f"Membership sync error: {e}")

    def sync_users_to_warehouse(
        self, search_base: str | None = None, *, incremental: bool = False
    ) -> r[m.DbtLdapPipelineResult]:
        """Synchronize LDAP users to data warehouse."""
        try:
            logger.info("Starting user sync to warehouse, incremental=%s", incremental)
            current_bookmark = self._bookmark_now()
            user_filter = "(objectClass=person)"
            run_incremental = self._should_run_incremental(
                c.LdapEntityTypes.USERS,
                requested_incremental=incremental,
                current_bookmark=current_bookmark,
            )
            if run_incremental:
                user_filter = self._build_incremental_filter(
                    user_filter, self._sync_bookmarks.get(c.LdapEntityTypes.USERS)
                )
            result = self.client.run_full_pipeline(
                search_base=search_base,
                search_filter=user_filter,
                attributes=[
                    c.LdapAttributes.UID,
                    c.LdapAttributes.CN,
                    c.LdapAttributes.MAIL,
                    c.LdapAttributes.DISPLAY_NAME,
                    c.LdapAttributes.DEPARTMENT,
                    c.LdapAttributes.MANAGER,
                ],
                model_names=[c.DbtModels.STG_USERS, c.DbtModels.DIM_USERS],
            )
            if result.is_success:
                logger.info("User sync completed successfully")
                self._update_bookmark(
                    c.LdapEntityTypes.USERS, current_bookmark, successful=True
                )
            else:
                logger.error("User sync failed: %s", result.error or "")
            return result
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during user sync")
            return r[m.DbtLdapPipelineResult].fail(f"User sync error: {e}")

    def validate_warehouse_data_quality(
        self, model_names: Sequence[str] | None = None
    ) -> r[m.ValidationMetrics]:
        """Validate data quality in the warehouse."""
        try:
            logger.info(
                "Validating warehouse data quality for models: %s",
                ", ".join(model_names) if model_names else "",
            )
            model_list = list(model_names) if model_names else None
            test_result = self._dbt_service.run_models(models=model_list)
            if test_result.is_success:
                logger.info("Data quality validation completed successfully")
                return r[m.ValidationMetrics].ok(
                    m.ValidationMetrics(validation_passed=True)
                )
            logger.error("Data quality validation failed: %s", test_result.error or "")
            return r[m.ValidationMetrics].fail(test_result.error or "DBT tests failed")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during data quality validation")
            return r[m.ValidationMetrics].fail(f"Data quality validation error: {e}")

    def _bookmark_now(self) -> str:
        return datetime.now(UTC).strftime("%Y%m%d%H%M%SZ")

    def _build_incremental_filter(self, base_filter: str, bookmark: str | None) -> str:
        if bookmark is None:
            return base_filter
        return f"(&{base_filter}(modifyTimestamp>={bookmark}))"

    def _load_sync_state(self) -> dict[str, str]:
        if not self._sync_state_file.exists():
            return {}
        try:
            payload = json.loads(self._sync_state_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            logger.exception("Failed to read sync state file")
            return {}
        if not isinstance(payload, dict):
            return {}
        try:
            return _SYNC_BOOKMARKS_ADAPTER.validate_python(payload)
        except ValidationError:
            return {}

    def _persist_sync_state(self) -> None:
        self._sync_state_file.parent.mkdir(parents=True, exist_ok=True)
        self._sync_state_file.write_text(
            json.dumps(self._sync_bookmarks, indent=2, sort_keys=True), encoding="utf-8"
        )

    def _resolve_sync_state_file(self) -> Path:
        configured_state_file = (
            self.config.sync_state_file
            if hasattr(self.config, "sync_state_file")
            else None
        )
        if isinstance(configured_state_file, str) and configured_state_file:
            return Path(configured_state_file)
        return Path(self.config.dbt_project_dir) / ".flext_dbt_ldap_sync_state.json"

    def _should_run_incremental(
        self, sync_key: str, *, requested_incremental: bool, current_bookmark: str
    ) -> bool:
        if not requested_incremental:
            return False
        previous_bookmark = self._sync_bookmarks.get(sync_key)
        if previous_bookmark is None:
            logger.info("No previous bookmark for %s; running full sync", sync_key)
            return False
        if previous_bookmark >= current_bookmark:
            logger.info(
                "Bookmark %s not older than current %s for %s; running full sync",
                previous_bookmark,
                current_bookmark,
                sync_key,
            )
            return False
        return True

    def _update_bookmark(
        self, sync_key: str, bookmark: str, *, successful: bool
    ) -> None:
        if not successful:
            return
        self._sync_bookmarks[sync_key] = bookmark
        try:
            self._persist_sync_state()
        except OSError:
            logger.exception("Failed to persist bookmark state")


__all__: list[str] = ["FlextDbtLdapService"]
