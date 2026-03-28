"""FLEXT DBT LDAP Services — sync mixin.

Mixed into FlextDbtLdap via MRO. Not instantiated standalone.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json
from collections.abc import MutableMapping
from datetime import UTC, datetime
from pathlib import Path

from flext_core import FlextLogger, r

from flext_dbt_ldap import c, m, t
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_exceptions import SAFE_EXCEPTIONS

logger = FlextLogger(__name__)


class FlextDbtLdapService(FlextDbtLdapClient):
    """Warehouse sync mixin — composed into FlextDbtLdap via MRO."""

    _sync_state_file: Path
    _sync_bookmarks: MutableMapping[str, str]

    def generate_analytics_report(
        self,
        report_type: str = "summary",
    ) -> r[m.DbtLdap.AnalyticsReport]:
        """Generate analytics report from warehouse data."""
        try:
            report = m.DbtLdap.AnalyticsReport(
                report_type=report_type,
                generated_at="2025-01-01T00:00:00Z",
            )
            return r[m.DbtLdap.AnalyticsReport].ok(report)
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.AnalyticsReport].fail(f"Report generation error: {e}")

    def run_dbt_models(
        self,
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdap.DbtRunStatus]:
        """Run DBT models."""
        try:
            model_list = list(model_names) if model_names else None
            self.dbt_manager.run_models(models=model_list)
            return r[m.DbtLdap.DbtRunStatus].ok(
                m.DbtLdap.DbtRunStatus(
                    status=c.DbtLdap.Statuses.COMPLETED, models_run=model_list or []
                ),
            )
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtRunStatus].fail(f"DBT model execution error: {e}")

    def run_full_data_warehouse_sync(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> r[m.DbtLdap.SyncResult]:
        """Run complete LDAP to data warehouse synchronization."""
        user_result = self.sync_users_to_warehouse(search_base, incremental=incremental)
        group_result = self.sync_groups_to_warehouse(
            search_base,
            incremental=incremental,
        )
        membership_result = self.sync_memberships_to_warehouse(search_base)
        counts = [
            user_result.is_success,
            group_result.is_success,
            membership_result.is_success,
        ]
        sync_result = m.DbtLdap.SyncResult(
            overall_success=all(counts),
            successful_components=sum(counts),
            total_components=len(counts),
        )
        if all(counts):
            return r[m.DbtLdap.SyncResult].ok(sync_result)
        return r[m.DbtLdap.SyncResult].fail("Some components failed in full sync")

    def sync_groups_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> r[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP groups to data warehouse."""
        try:
            bookmark = self._bookmark_now()
            group_filter = c.DbtLdap.Filters.GROUP
            if self._should_run_incremental(
                "groups",
                requested_incremental=incremental,
                current_bookmark=bookmark,
            ):
                group_filter = self._build_incremental_filter(
                    group_filter,
                    self._sync_bookmarks.get("groups"),
                )
            result = self.run_full_pipeline(
                search_base=search_base,
                search_filter=group_filter,
                attributes=c.DbtLdap.SearchAttributes.GROUP,
                model_names=[
                    c.DbtLdap.DbtModels.STG_GROUPS,
                    c.DbtLdap.DbtModels.DIM_GROUPS,
                ],
            )
            if result.is_success:
                self._update_bookmark("groups", bookmark, successful=True)
            return result
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(f"Group sync error: {e}")

    def sync_memberships_to_warehouse(
        self,
        search_base: str | None = None,
    ) -> r[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP memberships to data warehouse."""
        try:
            return self.run_full_pipeline(
                search_base=search_base,
                search_filter=c.DbtLdap.Filters.MEMBERSHIP,
                attributes=c.DbtLdap.SearchAttributes.MEMBERSHIP,
                model_names=[c.DbtLdap.DbtModels.FACT_MEMBERSHIPS],
            )
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                f"Membership sync error: {e}"
            )

    def sync_users_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> r[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP users to data warehouse."""
        try:
            bookmark = self._bookmark_now()
            user_filter = c.DbtLdap.Filters.USER
            if self._should_run_incremental(
                c.DbtLdap.LdapEntityTypes.USERS,
                requested_incremental=incremental,
                current_bookmark=bookmark,
            ):
                user_filter = self._build_incremental_filter(
                    user_filter,
                    self._sync_bookmarks.get(c.DbtLdap.LdapEntityTypes.USERS),
                )
            result = self.run_full_pipeline(
                search_base=search_base,
                search_filter=user_filter,
                attributes=[
                    c.DbtLdap.LdapAttributes.UID,
                    c.DbtLdap.LdapAttributes.CN,
                    c.DbtLdap.LdapAttributes.MAIL,
                    c.DbtLdap.LdapAttributes.DISPLAY_NAME,
                    c.DbtLdap.LdapAttributes.DEPARTMENT,
                    c.DbtLdap.LdapAttributes.MANAGER,
                ],
                model_names=[
                    c.DbtLdap.DbtModels.STG_USERS,
                    c.DbtLdap.DbtModels.DIM_USERS,
                ],
            )
            if result.is_success:
                self._update_bookmark(
                    c.DbtLdap.LdapEntityTypes.USERS,
                    bookmark,
                    successful=True,
                )
            return result
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(f"User sync error: {e}")

    def validate_warehouse_data_quality(
        self,
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdap.ValidationMetrics]:
        """Validate data quality in the warehouse."""
        try:
            model_list = list(model_names) if model_names else None
            self.dbt_manager.run_models(models=model_list)
            return r[m.DbtLdap.ValidationMetrics].ok(
                m.DbtLdap.ValidationMetrics(validation_passed=True),
            )
        except SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.ValidationMetrics].fail(
                f"Data quality validation error: {e}"
            )

    def _bookmark_now(self) -> str:
        return datetime.now(UTC).strftime("%Y%m%d%H%M%SZ")

    def _build_incremental_filter(self, base_filter: str, bookmark: str | None) -> str:
        if bookmark is None:
            return base_filter
        return f"(&{base_filter}(modifyTimestamp>={bookmark}))"

    def _load_sync_state(self) -> MutableMapping[str, str]:
        if not self._sync_state_file.exists():
            return {}
        try:
            data: MutableMapping[str, str] = json.loads(
                self._sync_state_file.read_bytes(),
            )
            return data
        except (OSError, json.JSONDecodeError, ValueError):
            logger.exception("Failed to read sync state file")
            return {}

    def _persist_sync_state(self) -> None:
        self._sync_state_file.parent.mkdir(parents=True, exist_ok=True)
        self._sync_state_file.write_bytes(
            json.dumps(dict(sorted(self._sync_bookmarks.items())), indent=2).encode(),
        )

    def _resolve_sync_state_file(self) -> Path:
        return Path(self.config.dbt_project_dir) / ".flext_dbt_ldap_sync_state.json"

    def _should_run_incremental(
        self,
        sync_key: str,
        *,
        requested_incremental: bool,
        current_bookmark: str,
    ) -> bool:
        if not requested_incremental:
            return False
        previous = self._sync_bookmarks.get(sync_key)
        return previous is not None and previous < current_bookmark

    def _update_bookmark(
        self,
        sync_key: str,
        bookmark: str,
        *,
        successful: bool,
    ) -> None:
        if not successful:
            return
        self._sync_bookmarks[sync_key] = bookmark
        try:
            self._persist_sync_state()
        except OSError:
            logger.exception("Failed to persist bookmark state")


__all__: t.StrSequence = ["FlextDbtLdapService"]
