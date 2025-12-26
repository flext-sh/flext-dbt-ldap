"""DBT client for LDAP data transformations with FLEXT ecosystem integration.

This module provides dbt functionality for LDAP directory data transformations
using FLEXT ecosystem patterns for data processing and analytics.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import override

from flext_core import FlextLogger, r
from flext_ldap import FlextLdap, FlextLdapModels
from flext_meltano import FlextMeltanoDbtService

from flext_dbt_ldap.settings import FlextDbtLdapSettings
from flext_dbt_ldap.typings import t

logger = FlextLogger(__name__)


class FlextDbtLdapClient:
    """DBT client for LDAP data transformations.

    Provides unified interface for LDAP data extraction, validation,
    and DBT transformation operations.
    """

    @override
    def __init__(
        self,
        config: FlextDbtLdapSettings | None = None,
    ) -> None:
        """Initialize DBT LDAP client.

        Args:
        config: Configuration for LDAP and DBT operations

        """
        self.config: FlextDbtLdapSettings = (
            config or FlextDbtLdapSettings.get_global_instance()
        )
        # Precisely type the LDAP API to enable method access
        self._ldap_api: FlextLdap = FlextLdap()
        self._dbt_manager: FlextMeltanoDbtService | None = None
        logger.info("Initialized DBT LDAP client with config: %s", self.config)

    @property
    def dbt_manager(self) -> FlextMeltanoDbtService:
        """Get or create DBT manager instance."""
        if self._dbt_manager is None:
            (Path(self.config.dbt_project_dir) if self.config.dbt_project_dir else None)
            self._dbt_manager = FlextMeltanoDbtService()
        return self._dbt_manager

    def extract_ldap_entries(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: Sequence[str] | None = None,
    ) -> r[list[FlextLdapModels.Entry]]:
        """Extract LDAP entries for DBT processing.

        Args:
            search_base: LDAP search base (defaults to config base_dn)
            search_filter: LDAP search filter
            attributes: Attributes to retrieve

        Returns:
            r containing list of LDAP entries

        """
        try:
            logger.info(
                "Extracting LDAP entries: base=%s, filter=%s",
                search_base or self.config.ldap_base_dn,
                search_filter,
            )
            # Use flext-ldap API for extraction via a sync wrapper
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
                logger.error("LDAP extraction failed: %s", result.error)
                return r[list[FlextLdapModels.Entry]].fail(
                    f"LDAP extraction failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during LDAP extraction")
            return r[list[FlextLdapModels.Entry]].fail(
                f"LDAP extraction error: {e}",
            )

    def validate_ldap_data(
        self,
        entries: list[FlextLdapModels.Entry],
    ) -> r[t.DbtLdapCore.ValidationDict]:
        """Validate LDAP data quality for DBT processing.

        Args:
            entries: List of LDAP entries to validate

        Returns:
            r containing validation metrics

        """
        try:
            logger.info("Validating %d LDAP entries for data quality", len(entries))
            # Local validation to avoid cross-package typing mismatches
            required_attributes = self.config.required_attributes
            total_entries = len(entries)
            valid_dns = 0
            valid_entries = 0
            for entry in entries:
                if getattr(entry, "dn", ""):
                    valid_dns += 1
                attrs = getattr(entry, "attributes", {})
                if isinstance(attrs, dict) and all(
                    attr in attrs and attrs[attr] for attr in required_attributes
                ):
                    valid_entries += 1
            quality_score = (
                (valid_entries / total_entries) if total_entries > 0 else 0.0
            )
            metrics: t.DbtLdapCore.ValidationDict = {
                "total_entries": total_entries,
                "valid_dns": valid_dns,
                "valid_entries": valid_entries,
                "quality_score": round(quality_score, 3),
                "validation_passed": quality_score >= self.config.min_quality_threshold,
            }
            logger.info(
                "LDAP data validation completed: quality_score=%.3f",
                metrics["quality_score"],
            )
            if not metrics["validation_passed"]:
                return r[t.DbtLdapCore.ValidationDict].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )
            return r[t.DbtLdapCore.ValidationDict].ok(metrics)
        except Exception as e:
            logger.exception("Unexpected error during LDAP validation")
            return r[t.DbtLdapCore.ValidationDict].fail(
                f"LDAP validation error: {e}",
            )

    def transform_with_dbt(
        self,
        entries: list[FlextLdapModels.Entry],
        model_names: Sequence[str] | None = None,
    ) -> r[t.DbtLdapCore.ResultDict]:
        """Transform LDAP data using DBT models.

        Args:
        entries: LDAP entries to transform
        model_names: Specific DBT models to run (None = all)

        Returns:
        r containing transformation results

        """
        try:
            logger.info(
                "Running DBT transformations on %d LDAP entries, models=%s",
                len(entries),
                model_names,
            )
            # Prepare LDAP data for DBT (convert to DataFrames/tables)
            _ = self._prepare_ldap_data_for_dbt(entries)
            # Use flext-meltano DBT manager for execution
            # Use FlextMeltanoDbtService.run_models directly
            model_list = list(model_names) if model_names else None
            dbt_result = self.dbt_manager.run_models(models=model_list)

            if dbt_result.is_failure:
                logger.error("DBT transformation failed: %s", dbt_result.error)
                return r[t.DbtLdapCore.ResultDict].fail(
                    f"DBT transformation failed: {dbt_result.error}",
                )

            result_data: t.DbtLdapCore.ResultDict = {
                "status": "completed",
                "models_run": model_list or [],
                "entries_processed": len(entries),
                "dbt_results": dbt_result.value or {},
            }
            logger.info("DBT transformation completed successfully")
            return r[t.DbtLdapCore.ResultDict].ok(result_data)
        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return r[t.DbtLdapCore.ResultDict].fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: Sequence[str] | None = None,
        model_names: Sequence[str] | None = None,
    ) -> r[t.DbtLdapCore.ResultDict]:
        """Run complete LDAP to DBT transformation pipeline.

        Args:
            search_base: LDAP search base
            search_filter: LDAP search filter
            attributes: Attributes to retrieve
            model_names: DBT models to run

        Returns:
            r containing complete pipeline results

        """
        logger.info("Starting full LDAP-to-DBT pipeline")
        # Step 1: Extract LDAP data
        extract_result = self.extract_ldap_entries(
            search_base,
            search_filter,
            attributes,
        )
        if extract_result.is_failure:
            return r[t.DbtLdapCore.ResultDict].fail(
                extract_result.error or "LDAP extraction failed",
            )
        entries = extract_result.value or []
        # Step 2: Validate data quality
        validate_result = self.validate_ldap_data(entries)
        if validate_result.is_failure:
            return r[t.DbtLdapCore.ResultDict].fail(
                validate_result.error or "LDAP validation failed",
            )
        # Step 3: Transform with DBT
        transform_result = self.transform_with_dbt(entries, model_names)
        if transform_result.is_failure:
            return r[t.DbtLdapCore.ResultDict].fail(
                transform_result.error or "DBT transformation failed",
            )
        # Combine results
        pipeline_results: t.DbtLdapCore.ResultDict = {
            "extracted_entries": len(entries),
            "validation_metrics": validate_result.value or {},
            "transformation_results": transform_result.value or {},
        }
        logger.info("Full LDAP-to-DBT pipeline completed successfully")
        return r[t.DbtLdapCore.ResultDict].ok(
            pipeline_results,
        )

    def _prepare_ldap_data_for_dbt(
        self,
        entries: list[FlextLdapModels.Entry],
    ) -> dict[str, list[t.DbtLdapCore.DataDict]]:
        """Prepare LDAP entries for DBT processing.

        Converts LDAP entries to format suitable for DBT models.

        Args:
            entries: List of LDAP entries

        Returns:
            Dictionary of prepared data for DBT

        """
        # Apply schema and attribute mapping from config
        prepared_data: dict[str, list[t.DbtLdapCore.DataDict]] = {}
        for schema_name, table_name in self.config.ldap_schema_mapping.items():
            # Filter entries by schema type and prepare for DBT
            schema_entries = [
                entry for entry in entries if self._matches_schema(entry, schema_name)
            ]
            # Convert to tabular format with attribute mapping
            table_data: list[t.DbtLdapCore.DataDict] = [
                self._map_entry_attributes(entry) for entry in schema_entries
            ]
            prepared_data[table_name] = table_data
        logger.debug(
            "Prepared LDAP data for DBT: %s",
            {k: len(v) for k, v in prepared_data.items()},
        )
        return prepared_data

    def _matches_schema(self, entry: FlextLdapModels.Entry, schema_name: str) -> bool:
        """Check if LDAP entry matches schema type."""
        object_classes = entry.object_classes
        schema_mapping = {
            "users": ["person", "user", "inetOrgPerson"],
            "groups": ["group", "groupOfNames", "groupOfUniqueNames"],
            "org_units": ["organizationalUnit", "organization"],
        }
        expected_classes: list[str] = schema_mapping.get(schema_name, [])
        return any(cls in object_classes for cls in expected_classes)

    def _map_entry_attributes(
        self,
        entry: FlextLdapModels.Entry,
    ) -> t.DbtLdapCore.DataDict:
        """Map LDAP entry attributes using configuration mapping."""
        mapped_attrs: t.DbtLdapCore.DataDict = {"dn": entry.dn}
        for ldap_attr, dbt_attr in self.config.ldap_attribute_mapping.items():
            if ldap_attr in entry.attributes:
                values_obj = entry.attributes[ldap_attr]
                first_value = (
                    values_obj[0]
                    if isinstance(values_obj, list) and values_obj
                    else values_obj
                )
                mapped_attrs[dbt_attr] = (
                    first_value
                    if isinstance(first_value, str)
                    else str(first_value or "")
                )
        # Add unmapped attributes with original names
        for attr, values in entry.attributes.items():
            if attr not in self.config.ldap_attribute_mapping:
                first_value = (
                    values[0] if isinstance(values, list) and values else values
                )
                mapped_attrs[attr] = (
                    first_value
                    if isinstance(first_value, str)
                    else str(first_value or "")
                )
        return mapped_attrs

    def _search_entries_sync(
        self,
        *,
        base_dn: str,
        search_filter: str,
        attributes: Sequence[str] | None,
    ) -> r[list[FlextLdapModels.Entry]]:
        """Synchronously perform LDAP search using flext-ldap API."""
        try:
            api = FlextLdap()

            # Create SearchRequest object as required by flext-ldap API
            search_request = FlextLdapModels.SearchRequest(
                base_dn=base_dn,
                filter_str=search_filter,
                attributes=attributes or [],
                scope="subtree",
            )

            # Use API directly (synchronous operation)
            result: r[FlextLdapModels.SearchResponse] = api.search_with_request(
                search_request,
            )

            # Use entries directly from SearchResponse
            if result.is_success and result.value:
                return r[list[FlextLdapModels.Entry]].ok(result.value.entries)

            return r[list[FlextLdapModels.Entry]].fail(
                result.error or "Search returned no results",
            )
        except Exception as e:
            return r[list[FlextLdapModels.Entry]].fail(
                f"LDAP search failed: {e}",
            )


__all__: list[str] = [
    "FlextDbtLdapClient",
]
