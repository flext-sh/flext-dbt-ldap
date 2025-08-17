"""DBT client for LDAP operations.

Provides high-level interface for DBT LDAP transformations.
Integrates flext-ldap and flext-meltano for complete data pipeline operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
from pathlib import Path

from flext_core import FlextResult, get_logger
from flext_ldap import FlextLdapApi, FlextLdapEntry, get_ldap_api
from flext_meltano.dbt import FlextMeltanoDbtManager

from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig

logger = get_logger(__name__)


class FlextDbtLdapClient:
    """DBT client for LDAP data transformations.

    Provides unified interface for LDAP data extraction, validation,
    and DBT transformation operations.
    """

    def __init__(
        self,
        config: FlextDbtLdapConfig | None = None,
    ) -> None:
        """Initialize DBT LDAP client.

        Args:
            config: Configuration for LDAP and DBT operations

        """
        self.config = config or FlextDbtLdapConfig()
        # Precisely type the LDAP API to enable method access
        self._ldap_api: FlextLdapApi = get_ldap_api()
        self._dbt_manager: FlextMeltanoDbtManager | None = None
        logger.info("Initialized DBT LDAP client with config: %s", self.config)

    @property
    def dbt_manager(self) -> FlextMeltanoDbtManager:
        """Get or create DBT manager instance."""
        if self._dbt_manager is None:
            project_dir = (
                Path(self.config.dbt_project_dir)
                if self.config.dbt_project_dir
                else None
            )
            self._dbt_manager = FlextMeltanoDbtManager(project_dir)
        return self._dbt_manager

    def extract_ldap_entries(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: list[str] | None = None,
    ) -> FlextResult[list[FlextLdapEntry]]:
        """Extract LDAP entries for DBT processing.

        Args:
            search_base: LDAP search base (defaults to config base_dn)
            search_filter: LDAP search filter
            attributes: Attributes to retrieve
        Returns:
            FlextResult containing list of LDAP entries

        """
        try:
            logger.info(
                "Extracting LDAP entries: base=%s, filter=%s",
                search_base or self.config.ldap_base_dn,
                search_filter,
            )
            # Use flext-ldap async API for extraction via a sync wrapper
            result = self._search_entries_sync(
                base_dn=search_base or self.config.ldap_base_dn,
                search_filter=search_filter,
                attributes=attributes,
            )
            if result.is_success:
                logger.info(
                    "Successfully extracted %d LDAP entries",
                    len(result.data) if result.data else 0,
                )
            else:
                logger.error("LDAP extraction failed: %s", result.error)
                return FlextResult.fail(
                    f"LDAP extraction failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during LDAP extraction")
            return FlextResult.fail(
                f"LDAP extraction error: {e}",
            )

    def validate_ldap_data(
        self,
        entries: list[FlextLdapEntry],
    ) -> FlextResult[dict[str, object]]:
        """Validate LDAP data quality for DBT processing.

        Args:
            entries: List of LDAP entries to validate
        Returns:
            FlextResult containing validation metrics

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
                attrs: dict[str, list[str]] = getattr(entry, "attributes", {})
                if all(attr in attrs and attrs[attr] for attr in required_attributes):
                    valid_entries += 1
            quality_score = (
                (valid_entries / total_entries) if total_entries > 0 else 0.0
            )
            metrics: dict[str, object] = {
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
                return FlextResult.fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )
            return FlextResult.ok(metrics)
        except Exception as e:
            logger.exception("Unexpected error during LDAP validation")
            return FlextResult.fail(
                f"LDAP validation error: {e}",
            )

    def transform_with_dbt(
        self,
        entries: list[FlextLdapEntry],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Transform LDAP data using DBT models.

        Args:
            entries: LDAP entries to transform
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

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
            manager = self.dbt_manager
            result = manager.run_models(model_names)
            if result.is_success:
                logger.info("DBT transformation completed successfully")
            else:
                logger.error("DBT transformation failed: %s", result.error)
                return FlextResult.fail(
                    f"DBT transformation failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return FlextResult.fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: list[str] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run complete LDAP to DBT transformation pipeline.

        Args:
            search_base: LDAP search base
            search_filter: LDAP search filter
            attributes: Attributes to retrieve
            model_names: DBT models to run
        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full LDAP-to-DBT pipeline")
        # Step 1: Extract LDAP data
        extract_result = self.extract_ldap_entries(
            search_base,
            search_filter,
            attributes,
        )
        if extract_result.is_failure:
            return FlextResult.fail(extract_result.error or "LDAP extraction failed")
        entries = extract_result.data or []
        # Step 2: Validate data quality
        validate_result = self.validate_ldap_data(entries)
        if validate_result.is_failure:
            return FlextResult.fail(validate_result.error or "LDAP validation failed")
        # Step 3: Transform with DBT
        transform_result = self.transform_with_dbt(entries, model_names)
        if transform_result.is_failure:
            return FlextResult.fail(
                transform_result.error or "DBT transformation failed",
            )
        # Combine results
        pipeline_results: dict[str, object] = {
            "extracted_entries": len(entries),
            "validation_metrics": validate_result.data,
            "transformation_results": transform_result.data,
        }
        logger.info("Full LDAP-to-DBT pipeline completed successfully")
        return FlextResult.ok(pipeline_results)

    def _prepare_ldap_data_for_dbt(
        self,
        entries: list[FlextLdapEntry],
    ) -> dict[str, list[dict[str, object]]]:
        """Prepare LDAP entries for DBT processing.

        Converts LDAP entries to format suitable for DBT models.

        Args:
            entries: List of LDAP entries
        Returns:
            Dictionary of prepared data for DBT

        """
        # Apply schema and attribute mapping from config
        prepared_data: dict[str, list[dict[str, object]]] = {}
        for schema_name, table_name in self.config.ldap_schema_mapping.items():
            # Filter entries by schema type and prepare for DBT
            schema_entries = [
                entry for entry in entries if self._matches_schema(entry, schema_name)
            ]
            # Convert to tabular format with attribute mapping
            table_data: list[dict[str, object]] = [
                self._map_entry_attributes(entry) for entry in schema_entries
            ]
            prepared_data[table_name] = table_data
        logger.debug(
            "Prepared LDAP data for DBT: %s",
            {k: len(v) for k, v in prepared_data.items()},
        )
        return prepared_data

    def _matches_schema(self, entry: FlextLdapEntry, schema_name: str) -> bool:
        """Check if LDAP entry matches schema type."""
        # Simple schema matching based on objectClass
        object_classes = entry.object_classes
        schema_mapping = {
            "users": ["person", "user", "inetOrgPerson"],
            "groups": ["group", "groupOfNames", "groupOfUniqueNames"],
            "org_units": ["organizationalUnit", "organization"],
        }
        expected_classes = schema_mapping.get(schema_name, [])
        return any(cls in object_classes for cls in expected_classes)

    def _map_entry_attributes(self, entry: FlextLdapEntry) -> dict[str, object]:
        """Map LDAP entry attributes using configuration mapping."""
        mapped_attrs: dict[str, object] = {"dn": entry.dn}
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
        attributes: list[str] | None,
    ) -> FlextResult[list[FlextLdapEntry]]:
        """Synchronously perform LDAP search using flext-ldap async API."""
        server_uri = (
            f"ldaps://{self.config.ldap_host}:{self.config.ldap_port}"
            if self.config.ldap_use_tls
            else f"ldap://{self.config.ldap_host}:{self.config.ldap_port}"
        )

        async def _run_search() -> FlextResult[list[FlextLdapEntry]]:
            api = get_ldap_api()
            async with api.connection(
                server_uri,
                self.config.ldap_bind_dn,
                self.config.ldap_bind_password,
            ) as session:
                return await api.search(
                    session_id=session,
                    base_dn=base_dn,
                    search_filter=search_filter,
                    scope="subtree",
                    attributes=attributes,
                )

        return asyncio.run(_run_search())


__all__: list[str] = [
    "FlextDbtLdapClient",
]
