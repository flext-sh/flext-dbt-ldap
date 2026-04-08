"""FLEXT DBT LDAP Utilities — LDAP extraction and DBT transformation.

Absorbed from dbt_client.py into u.DbtLdap namespace.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence

from pydantic import PrivateAttr

from flext_core import FlextLogger
from flext_dbt_ldap import FlextDbtLdapServiceBase, FlextDbtLdapSettings, c, m, r, t
from flext_ldap import (
    FlextLdapSettings,
    ldap,
)

logger = FlextLogger(__name__)


class FlextDbtLdapUtilitiesClient(FlextDbtLdapServiceBase):
    """LDAP extraction and DBT transformation mixin.

    Mixed into FlextDbtLdap via MRO. State set by facade __init__.
    """

    _ldap_api: ldap = PrivateAttr()

    @staticmethod
    def create_ldap_api(config: FlextDbtLdapSettings) -> ldap:
        """Create a ldap API instance from DBT LDAP settings."""
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
            },
        )
        return ldap(config_overrides=ldap_settings.model_dump())

    def extract_ldap_entries(
        self,
        search_base: str | None = None,
        search_filter: str = c.Ldap.Filters.ALL_ENTRIES_FILTER,
        attributes: t.StrSequence | None = None,
    ) -> r[Sequence[t.DbtLdap.LdapEntryMapping]]:
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
                return r[Sequence[t.DbtLdap.LdapEntryMapping]].fail(
                    f"LDAP extraction failed: {result.error}",
                )
            return result
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            logger.exception("Unexpected error during LDAP extraction")
            return r[Sequence[t.DbtLdap.LdapEntryMapping]].fail(
                f"LDAP extraction error: {e}",
            )

    def run_full_pipeline(
        self,
        search_base: str | None = None,
        search_filter: str = c.Ldap.Filters.ALL_ENTRIES_FILTER,
        attributes: t.StrSequence | None = None,
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdap.DbtLdapPipelineResult]:
        """Run complete LDAP to DBT transformation pipeline."""
        logger.info("Starting full LDAP-to-DBT pipeline")
        extract_result = self.extract_ldap_entries(
            search_base,
            search_filter,
            attributes,
        )
        if extract_result.is_failure:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                extract_result.error or "LDAP extraction failed",
            )
        entries = extract_result.value or []
        validate_result = self.validate_ldap_data(entries)
        if validate_result.is_failure:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                validate_result.error or "LDAP validation failed",
            )
        transform_result = self.transform_with_dbt(entries, model_names)
        if transform_result.is_failure:
            return r[m.DbtLdap.DbtLdapPipelineResult].fail(
                transform_result.error or "DBT transformation failed",
            )
        pipeline_result = m.DbtLdap.DbtLdapPipelineResult(
            extracted_entries=len(entries)
        )
        logger.info("Full LDAP-to-DBT pipeline completed successfully")
        return r[m.DbtLdap.DbtLdapPipelineResult].ok(pipeline_result)

    def transform_with_dbt(
        self,
        entries: Sequence[t.DbtLdap.LdapEntryMapping],
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdap.DbtRunStatus]:
        """Transform LDAP data using DBT models."""
        try:
            run_result = self._run_selected_models(model_names)
            if run_result.is_failure:
                return r[m.DbtLdap.DbtRunStatus].fail(
                    run_result.error or "DBT transformation failed",
                )
            logger.info(
                "Running DBT transformations on %d LDAP entries, models=%s",
                len(entries),
                ", ".join(model_names) if model_names else "",
            )
            _ = self._prepare_ldap_data_for_dbt(entries)
            result_data = m.DbtLdap.DbtRunStatus(
                status=c.Meltano.StreamStatus.COMPLETED,
                models_run=run_result.value,
                entries_processed=len(entries),
            )
            logger.info("DBT transformation completed successfully")
            return r[m.DbtLdap.DbtRunStatus].ok(result_data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            logger.exception("Unexpected error during DBT transformation")
            return r[m.DbtLdap.DbtRunStatus].fail(f"DBT transformation error: {e}")

    def _run_selected_models(
        self,
        model_names: t.StrSequence | None = None,
    ) -> r[t.StrSequence]:
        """Run selected DBT models through the canonical service runtime."""
        model_list: list[str] = list(model_names) if model_names else []
        run_result = self.run_models(models=model_list or None)
        if run_result.is_failure:
            return r[t.StrSequence].fail(
                run_result.error or "DBT model execution failed",
            )
        return r[t.StrSequence].ok(model_list)

    def validate_ldap_data(
        self,
        entries: Sequence[t.DbtLdap.LdapEntryMapping],
    ) -> r[m.DbtLdap.ValidationMetrics]:
        """Validate LDAP data quality for DBT processing."""
        try:
            logger.info("Validating %d LDAP entries for data quality", len(entries))
            required_attributes = self.config.required_attributes
            total_entries = len(entries)
            valid_dns = 0
            valid_entries = 0
            for entry in entries:
                if entry.get(c.Ldap.LdapAttributeNames.DN):
                    valid_dns += 1
                if all(attr in entry and entry[attr] for attr in required_attributes):
                    valid_entries += 1
            quality_score = valid_entries / total_entries if total_entries > 0 else 0.0
            metrics = m.DbtLdap.ValidationMetrics(
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
                return r[m.DbtLdap.ValidationMetrics].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )
            return r[m.DbtLdap.ValidationMetrics].ok(metrics)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            logger.exception("Unexpected error during LDAP validation")
            return r[m.DbtLdap.ValidationMetrics].fail(f"LDAP validation error: {e}")

    def _map_entry_attributes(
        self,
        entry: t.DbtLdap.LdapEntryMapping,
    ) -> t.ConfigurationMapping:
        """Map LDAP entry attributes using configuration mapping."""
        dn_attr = c.Ldap.LdapAttributeNames.DN
        dn_str = str(entry.get(dn_attr, [""])[0]) if entry.get(dn_attr) else ""
        mapped_attrs: t.MutableConfigurationMapping = {dn_attr: dn_str}
        for ldap_attr, dbt_attr in self.config.ldap_attribute_mapping.items():
            if ldap_attr in entry:
                values_obj = entry[ldap_attr]
                first_value = values_obj[0] if values_obj else ""
                mapped_attrs[dbt_attr] = first_value
        for attr, values in entry.items():
            if attr not in self.config.ldap_attribute_mapping and attr != dn_attr:
                first_value = values[0] if values else ""
                mapped_attrs[attr] = first_value
        return mapped_attrs

    def _matches_schema(
        self,
        entry: t.DbtLdap.LdapEntryMapping,
        schema_name: str,
    ) -> bool:
        """Check if LDAP entry matches schema type."""
        object_classes: t.StrSequence = [
            str(x) for x in entry.get(c.Ldap.LdapAttributeNames.OBJECT_CLASS, [])
        ]
        schema_mapping: Mapping[str, t.StrSequence] = {
            c.DbtLdap.USERS: c.DbtLdap.USERS_CLASSES,
            c.DbtLdap.GROUPS: c.DbtLdap.GROUPS_CLASSES,
            c.DbtLdap.ORG_UNITS: c.DbtLdap.ORG_UNITS_CLASSES,
        }
        expected_classes = schema_mapping.get(schema_name, [])
        return any(cls in object_classes for cls in expected_classes)

    def _prepare_ldap_data_for_dbt(
        self,
        entries: Sequence[t.DbtLdap.LdapEntryMapping],
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
        self,
        *,
        base_dn: str,
        search_filter: str,
        attributes: t.StrSequence | None,
    ) -> r[Sequence[t.DbtLdap.LdapEntryMapping]]:
        """Synchronously perform LDAP search using flext-ldap API."""
        try:
            search_options = m.Ldap.SearchOptions(
                base_dn=base_dn,
                filter_str=search_filter,
                attributes=list(attributes) if attributes else None,
            )
            result = self._ldap_api.search(search_options=search_options)
            if result.is_success and result.value:
                entries = result.value.entries
                return r[Sequence[t.DbtLdap.LdapEntryMapping]].ok(entries)
            return r[Sequence[t.DbtLdap.LdapEntryMapping]].fail(
                result.error or "Search returned no results",
            )
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[Sequence[t.DbtLdap.LdapEntryMapping]].fail(
                f"LDAP search failed: {e}",
            )


__all__: t.StrSequence = ["FlextDbtLdapUtilitiesClient"]
