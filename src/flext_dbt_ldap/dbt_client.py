"""DBT client for LDAP data transformations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from pathlib import Path

from flext_core import FlextLogger, r
from flext_ldap import (
    FlextLdap,
    FlextLdapConnection,
    FlextLdapModels,
    FlextLdapOperations,
    FlextLdapSettings,
)
from flext_meltano import FlextMeltanoDbtService

from flext_dbt_ldap import c, m, t
from flext_dbt_ldap.settings import FlextDbtLdapSettings

logger = FlextLogger(__name__)


class FlextDbtLdapClient:
    """DBT client for LDAP data transformations.

    Provides unified interface for LDAP data extraction, validation,
    and DBT transformation operations.
    """

    def __init__(
        self, config: FlextDbtLdapSettings | None = None, *, ldap_api: FlextLdap
    ) -> None:
        """Initialize DBT LDAP client.

        Args:
        config: Configuration for LDAP and DBT operations
        ldap_api: Injected FlextLdap instance (mandatory)

        """
        super().__init__()
        self.config: FlextDbtLdapSettings = (
            config if config is not None else FlextDbtLdapSettings.get_global()
        )
        self._ldap_api: FlextLdap = ldap_api
        self._dbt_manager: FlextMeltanoDbtService | None = None
        logger.info(
            "Initialized DBT LDAP client",
            config=self.config.model_dump_json(),
        )

    @property
    def dbt_manager(self) -> FlextMeltanoDbtService:
        """Get or create DBT manager instance."""
        if self._dbt_manager is None:
            Path(self.config.dbt_project_dir) if self.config.dbt_project_dir else None
            self._dbt_manager = FlextMeltanoDbtService()
        return self._dbt_manager

    @staticmethod
    def create_ldap_api(config: FlextDbtLdapSettings) -> FlextLdap:
        """Create a FlextLdap API instance from DBT LDAP settings."""
        ldap_bind_dn = (
            config.ldap_bind_dn.get_secret_value() if config.ldap_bind_dn else None
        )
        ldap_bind_password = (
            config.ldap_bind_password.get_secret_value()
            if config.ldap_bind_password
            else None
        )
        ldap_settings = FlextLdapSettings.get_global().model_copy(
            update={
                "host": config.ldap_host,
                "port": config.ldap_port,
                "use_tls": config.ldap_use_tls,
                "bind_dn": ldap_bind_dn or "",
                "bind_password": ldap_bind_password or "",
            }
        )
        connection = FlextLdapConnection(config=ldap_settings)
        operations = FlextLdapOperations(connection=connection)
        return FlextLdap(connection=connection, operations=operations)

    def extract_ldap_entries(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: Sequence[str] | None = None,
    ) -> r[Sequence[Mapping[str, Sequence[str]]]]:
        """Extract LDAP entries for DBT processing."""
        try:
            logger.info(
                "Extracting LDAP entries: base=%s, filter=%s",
                search_base or self.config.ldap_base_dn,
                search_filter,
            )
            result = self._search_entries_sync(
                base_dn=search_base or self.config.ldap_base_dn,
                search_filter=search_filter,
                attributes=attributes,
            )
            if result.is_success:
                logger.info(
                    "Successfully extracted %d LDAP entries",
                    len(result.value) if result.value else 0,
                )
            else:
                logger.error("LDAP extraction failed: %s", result.error or "")
                return r[Sequence[Mapping[str, Sequence[str]]]].fail(
                    f"LDAP extraction failed: {result.error}"
                )
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
            logger.exception("Unexpected error during LDAP extraction")
            return r[Sequence[Mapping[str, Sequence[str]]]].fail(
                f"LDAP extraction error: {e}"
            )

    def run_full_pipeline(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: Sequence[str] | None = None,
        model_names: Sequence[str] | None = None,
    ) -> r[m.DbtLdapPipelineResult]:
        """Run complete LDAP to DBT transformation pipeline."""
        logger.info("Starting full LDAP-to-DBT pipeline")
        extract_result = self.extract_ldap_entries(
            search_base, search_filter, attributes
        )
        if extract_result.is_failure:
            return r[m.DbtLdapPipelineResult].fail(
                extract_result.error or "LDAP extraction failed"
            )
        entries = extract_result.value or []
        validate_result = self.validate_ldap_data(entries)
        if validate_result.is_failure:
            return r[m.DbtLdapPipelineResult].fail(
                validate_result.error or "LDAP validation failed"
            )
        transform_result = self.transform_with_dbt(entries, model_names)
        if transform_result.is_failure:
            return r[m.DbtLdapPipelineResult].fail(
                transform_result.error or "DBT transformation failed"
            )
        pipeline_result = m.DbtLdapPipelineResult(extracted_entries=len(entries))
        logger.info("Full LDAP-to-DBT pipeline completed successfully")
        return r[m.DbtLdapPipelineResult].ok(pipeline_result)

    def transform_with_dbt(
        self,
        entries: Sequence[Mapping[str, Sequence[str]]],
        model_names: Sequence[str] | None = None,
    ) -> r[m.DbtRunStatus]:
        """Transform LDAP data using DBT models."""
        try:
            logger.info(
                "Running DBT transformations on %d LDAP entries, models=%s",
                len(entries),
                ", ".join(model_names) if model_names else "",
            )
            _ = self._prepare_ldap_data_for_dbt(entries)
            model_list = list(model_names) if model_names else None
            dbt_result = self.dbt_manager.run_models(models=model_list)
            if dbt_result.is_failure:
                logger.error("DBT transformation failed: %s", dbt_result.error or "")
                return r[m.DbtRunStatus].fail(
                    f"DBT transformation failed: {dbt_result.error}"
                )
            result_data = m.DbtRunStatus(
                status="completed",
                models_run=model_list or [],
                entries_processed=len(entries),
            )
            logger.info("DBT transformation completed successfully")
            return r[m.DbtRunStatus].ok(result_data)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during DBT transformation")
            return r[m.DbtRunStatus].fail(f"DBT transformation error: {e}")

    def validate_ldap_data(
        self, entries: Sequence[Mapping[str, Sequence[str]]]
    ) -> r[m.ValidationMetrics]:
        """Validate LDAP data quality for DBT processing."""
        try:
            logger.info("Validating %d LDAP entries for data quality", len(entries))
            required_attributes = self.config.required_attributes
            total_entries = len(entries)
            valid_dns = 0
            valid_entries = 0
            for entry in entries:
                if entry.get("dn"):
                    valid_dns += 1
                if all(attr in entry and entry[attr] for attr in required_attributes):
                    valid_entries += 1
            quality_score = valid_entries / total_entries if total_entries > 0 else 0.0
            metrics = m.ValidationMetrics(
                total_entries=total_entries,
                valid_dns=valid_dns,
                valid_entries=valid_entries,
                quality_score=round(quality_score, 3),
                validation_passed=quality_score >= self.config.min_quality_threshold,
            )
            logger.info(
                "LDAP data validation completed: quality_score=%.3f",
                metrics.quality_score,
            )
            if not metrics.validation_passed:
                return r[m.ValidationMetrics].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}"
                )
            return r[m.ValidationMetrics].ok(metrics)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            logger.exception("Unexpected error during LDAP validation")
            return r[m.ValidationMetrics].fail(f"LDAP validation error: {e}")

    def _map_entry_attributes(
        self, entry: Mapping[str, Sequence[str]]
    ) -> t.ConfigurationMapping:
        """Map LDAP entry attributes using configuration mapping."""
        dn_str = str(entry.get("dn", [""])[0]) if entry.get("dn") else ""
        mapped_attrs: t.MutableConfigurationMapping = {"dn": dn_str}
        for ldap_attr, dbt_attr in self.config.ldap_attribute_mapping.items():
            if ldap_attr in entry:
                values_obj = entry[ldap_attr]
                first_value = values_obj[0] if values_obj else ""
                mapped_attrs[dbt_attr] = first_value
        for attr, values in entry.items():
            if attr not in self.config.ldap_attribute_mapping and attr != "dn":
                first_value = values[0] if values else ""
                mapped_attrs[attr] = first_value
        return mapped_attrs

    def _matches_schema(
        self, entry: Mapping[str, Sequence[str]], schema_name: str
    ) -> bool:
        """Check if LDAP entry matches schema type."""
        object_classes: Sequence[str] = [str(x) for x in entry.get("objectClass", [])]
        schema_mapping: Mapping[str, Sequence[str]] = {
            c.LdapEntityTypes.USERS: c.LdapSchemaMapping.USERS_CLASSES,
            c.LdapEntityTypes.GROUPS: c.LdapSchemaMapping.GROUPS_CLASSES,
            c.LdapEntityTypes.ORG_UNITS: c.LdapSchemaMapping.ORG_UNITS_CLASSES,
        }
        expected_classes = schema_mapping.get(schema_name, [])
        return any(cls in object_classes for cls in expected_classes)

    def _prepare_ldap_data_for_dbt(
        self, entries: Sequence[Mapping[str, Sequence[str]]]
    ) -> Mapping[str, Sequence[t.ConfigurationMapping]]:
        """Prepare LDAP entries for DBT processing."""
        prepared_data: MutableMapping[str, Sequence[t.ConfigurationMapping]] = {}
        for schema_name, table_name in self.config.ldap_schema_mapping.items():
            schema_entries = [
                entry for entry in entries if self._matches_schema(entry, schema_name)
            ]
            table_data: Sequence[t.ConfigurationMapping] = [
                self._map_entry_attributes(entry) for entry in schema_entries
            ]
            prepared_data[table_name] = table_data
        logger.debug(
            "Prepared LDAP data for DBT",
            tables=len(prepared_data),
            total_records=sum(len(v) for v in prepared_data.values()),
        )
        return prepared_data

    def _search_entries_sync(
        self, *, base_dn: str, search_filter: str, attributes: Sequence[str] | None
    ) -> r[Sequence[Mapping[str, Sequence[str]]]]:
        """Synchronously perform LDAP search using flext-ldap API."""
        try:
            search_options = FlextLdapModels.Ldap.SearchOptions(
                base_dn=base_dn,
                filter_str=search_filter,
                attributes=list(attributes) if attributes else None,
            )
            result = self._ldap_api.search(search_options=search_options)
            if result.is_success and result.value:
                entries = result.value.entries
                return r[Sequence[Mapping[str, Sequence[str]]]].ok(entries)
            return r[Sequence[Mapping[str, Sequence[str]]]].fail(
                result.error or "Search returned no results"
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
            return r[Sequence[Mapping[str, Sequence[str]]]].fail(
                f"LDAP search failed: {e}"
            )


__all__: Sequence[str] = ["FlextDbtLdapClient"]
