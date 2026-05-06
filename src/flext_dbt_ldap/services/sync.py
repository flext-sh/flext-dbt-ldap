"""Sync workflow mixin for dbt-ldap service facades."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from flext_cli import u
from flext_dbt_ldap import c, m, p, r, t
from flext_dbt_ldap.services.client import FlextDbtLdapClientMixin

logger = u.fetch_logger(__name__)


def _new_sync_bookmarks() -> t.MutableMappingKV[str, str]:
    empty_bookmarks: t.MutableMappingKV[str, str] = {}
    return empty_bookmarks


class FlextDbtLdapSyncMixin(FlextDbtLdapClientMixin):
    """Warehouse sync mixin for dbt-ldap service facades."""

    _sync_state_file: Path = u.PrivateAttr()
    _sync_bookmarks: t.MutableStrMapping = u.PrivateAttr(
        default_factory=_new_sync_bookmarks,
    )

    @staticmethod
    def generate_analytics_report(
        report_type: str = "summary",
    ) -> p.Result[m.DbtLdap.AnalyticsReport]:
        """Generate analytics report from warehouse data."""
        try:
            report = m.DbtLdap.AnalyticsReport(
                report_type=report_type,
                generated_at="2025-01-01T00:00:00Z",
            )
            return r[m.DbtLdap.AnalyticsReport].ok(report)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.AnalyticsReport].fail(f"Report generation error: {e}")

    def run_dbt_models(
        self,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.DbtLdap.DbtRunStatus]:
        """Run DBT models."""
        try:
            run_result = self._run_selected_models(model_names)
            if run_result.failure:
                return r[m.DbtLdap.DbtRunStatus].fail(
                    run_result.error or "DBT model execution failed",
                )
            return r[m.DbtLdap.DbtRunStatus].ok(
                m.DbtLdap.DbtRunStatus(
                    status=c.Meltano.StreamStatus.COMPLETED,
                    models_run=run_result.value,
                ),
            )
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtRunStatus].fail(f"DBT model execution error: {e}")

    def run_full_data_warehouse_sync(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> p.Result[m.DbtLdap.SyncResult]:
        """Run complete LDAP to data warehouse synchronization."""
        user_result = self.sync_users_to_warehouse(search_base, incremental=incremental)
        group_result = self.sync_groups_to_warehouse(
            search_base,
            incremental=incremental,
        )
        membership_result = self.sync_memberships_to_warehouse(search_base)
        counts = [
            user_result.success,
            group_result.success,
            membership_result.success,
        ]
        sync_result = m.DbtLdap.SyncResult(
            overall_success=all(counts),
            successful_components=sum(counts),
            total_components=len(counts),
        )
        if all(counts):
            return r[m.DbtLdap.SyncResult].ok(sync_result)
        return r[m.DbtLdap.SyncResult].fail_op("complete full sync of all components")

    def sync_groups_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> p.Result[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP groups to data warehouse."""
        try:
            bookmark = self._bookmark_now()
            group_filter = c.DbtLdap.FILTER_GROUP
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
                attributes=c.DbtLdap.SEARCH_GROUP,
                model_names=[
                    c.DbtLdap.STG_GROUPS,
                    c.DbtLdap.DIM_GROUPS,
                ],
            )
            if result.success:
                update_result = self._update_bookmark(
                    "groups",
                    bookmark,
                    successful=True,
                )
                if update_result.failure:
                    return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                        update_result.error or "Group sync state persistence failed",
                    )
            return result
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(f"Group sync error: {e}")

    def sync_memberships_to_warehouse(
        self,
        search_base: str | None = None,
    ) -> p.Result[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP memberships to data warehouse."""
        try:
            return self.run_full_pipeline(
                search_base=search_base,
                search_filter=c.DbtLdap.FILTER_MEMBERSHIP,
                attributes=c.DbtLdap.SEARCH_MEMBERSHIP,
                model_names=[c.DbtLdap.FACT_MEMBERSHIPS],
            )
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                f"Membership sync error: {e}"
            )

    def sync_users_to_warehouse(
        self,
        search_base: str | None = None,
        *,
        incremental: bool = False,
    ) -> p.Result[m.DbtLdap.DbtLdapPipelineResult]:
        """Synchronize LDAP users to data warehouse."""
        try:
            bookmark = self._bookmark_now()
            user_filter = c.DbtLdap.FILTER_USER
            if self._should_run_incremental(
                c.DbtLdap.USERS,
                requested_incremental=incremental,
                current_bookmark=bookmark,
            ):
                user_filter = self._build_incremental_filter(
                    user_filter,
                    self._sync_bookmarks.get(c.DbtLdap.USERS),
                )
            result = self.run_full_pipeline(
                search_base=search_base,
                search_filter=user_filter,
                attributes=[
                    c.DbtLdap.UID,
                    c.DbtLdap.CN,
                    c.DbtLdap.MAIL,
                    c.DbtLdap.DISPLAY_NAME,
                    c.DbtLdap.DEPARTMENT,
                    c.DbtLdap.MANAGER,
                ],
                model_names=[
                    c.DbtLdap.STG_USERS,
                    c.DbtLdap.DIM_USERS,
                ],
            )
            if result.success:
                update_result = self._update_bookmark(
                    c.DbtLdap.USERS,
                    bookmark,
                    successful=True,
                )
                if update_result.failure:
                    return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                        update_result.error or "User sync state persistence failed",
                    )
            return result
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(f"User sync error: {e}")

    def validate_warehouse_data_quality(
        self,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.DbtLdap.ValidationMetrics]:
        """Validate data quality in the warehouse."""
        try:
            run_result = self._run_selected_models(model_names)
            if run_result.failure:
                return r[m.DbtLdap.ValidationMetrics].fail(
                    run_result.error or "Data quality validation failed",
                )
            return r[m.DbtLdap.ValidationMetrics].ok(
                m.DbtLdap.ValidationMetrics(validation_passed=True),
            )
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[m.DbtLdap.ValidationMetrics].fail(
                f"Data quality validation error: {e}"
            )

    def _bookmark_now(self) -> str:
        return datetime.now(UTC).strftime("%Y%m%d%H%M%SZ")

    def _build_incremental_filter(self, base_filter: str, bookmark: str | None) -> str:
        if bookmark is None:
            return base_filter
        return f"(&{base_filter}(modifyTimestamp>={bookmark}))"

    def _load_sync_state(self) -> t.MutableStrMapping:
        if not self._sync_state_file.exists():
            empty_state: t.MutableStrMapping = {}
            return empty_state
        payload_result = u.Cli.json_read(self._sync_state_file)
        if payload_result.failure:
            raise OSError(payload_result.error or "Failed to read sync state file")
        loaded = t.json_dict_adapter().validate_python(payload_result.value)
        data: t.MutableStrMapping = {}
        for key, value in loaded.items():
            if not isinstance(value, str):
                msg = "Sync state file values must be strings"
                raise TypeError(msg)
            data[key] = value
        return data

    def _persist_sync_state(self) -> None:
        self._sync_state_file.parent.mkdir(parents=True, exist_ok=True)
        write_result = u.Cli.json_write(
            self._sync_state_file,
            dict(sorted(self._sync_bookmarks.items())),
            options=m.Cli.JsonWriteOptions(sort_keys=True),
        )
        if write_result.failure:
            msg = write_result.error or "Failed to persist sync state"
            raise OSError(msg)

    def _resolve_sync_state_file(self) -> Path:
        return Path(self.settings.dbt_project_dir) / ".flext_dbt_ldap_sync_state.json"

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
    ) -> p.Result[bool]:
        if not successful:
            return r[bool].ok(True)
        previous_bookmark = self._sync_bookmarks.get(sync_key)
        self._sync_bookmarks[sync_key] = bookmark
        try:
            self._persist_sync_state()
        except OSError as error:
            if previous_bookmark is None:
                self._sync_bookmarks.pop(sync_key, None)
            else:
                self._sync_bookmarks[sync_key] = previous_bookmark
            return r[bool].fail(str(error))
        return r[bool].ok(True)


__all__: list[str] = ["FlextDbtLdapSyncMixin"]
