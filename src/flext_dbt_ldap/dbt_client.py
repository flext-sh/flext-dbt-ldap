"""DBT client for LDAP data transformations with FLEXT ecosystem integration.

This module provides dbt functionality for LDAP directory data transformations
using FLEXT ecosystem patterns for data processing and analytics.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
from pathlib import Path

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig
from flext_ldap import FlextLdapClient, FlextLdapModels
from flext_meltano import FlextMeltanoService

logger = FlextLogger(__name__)


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
        self.config: dict[str, object] = config or FlextDbtLdapConfig()
        # Precisely type the LDAP API to enable method access
        self._ldap_api: FlextLdapClient = FlextLdapClient()
        self._dbt_manager: FlextMeltanoService | None = None
        logger.info("Initialized DBT LDAP client with config: %s", self.config)

    @property
    def dbt_manager(self: object) -> FlextMeltanoService:
        """Get or create DBT manager instance."""
        if self._dbt_manager is None:
            (Path(self.config.dbt_project_dir) if self.config.dbt_project_dir else None)
            self._dbt_manager = FlextMeltanoService()
        return self._dbt_manager

    def extract_ldap_entries(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[list[FlextLdapModels.Entry]]:
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
                    len(result.value) if result.value else 0,
                )
            else:
                logger.error("LDAP extraction failed: %s", result.error)
                return FlextResult[list[FlextLdapModels.Entry]].fail(
                    f"LDAP extraction failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during LDAP extraction")
            return FlextResult[list[FlextLdapModels.Entry]].fail(
                f"LDAP extraction error: {e}",
            )

    def validate_ldap_data(
        self,
        entries: list[FlextLdapModels.Entry],
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
                attrs: dict[str, FlextTypes.Core.StringList] = getattr(
                    entry,
                    "attributes",
                    {},
                )
                if all(attr in attrs and attrs[attr] for attr in required_attributes):
                    valid_entries += 1
            quality_score = (
                (valid_entries / total_entries) if total_entries > 0 else 0.0
            )
            metrics: FlextTypes.Core.Dict = {
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
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )
            return FlextResult[FlextTypes.Core.Dict].ok(metrics)
        except Exception as e:
            logger.exception("Unexpected error during LDAP validation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"LDAP validation error: {e}",
            )

    def transform_with_dbt(
        self,
        entries: list[FlextLdapModels.Entry],
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
            result: FlextResult[object] = manager.run_models(model_names)
            if result.is_success:
                logger.info("DBT transformation completed successfully")
            else:
                logger.error("DBT transformation failed: %s", result.error)
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"DBT transformation failed: {result.error}",
                )
            return result
        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        search_base: str | None = None,
        search_filter: str = "(objectClass=*)",
        attributes: FlextTypes.Core.StringList | None = None,
        model_names: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
            return FlextResult[FlextTypes.Core.Dict].fail(
                extract_result.error or "LDAP extraction failed",
            )
        entries = extract_result.value or []
        # Step 2: Validate data quality
        validate_result: FlextResult[object] = self.validate_ldap_data(entries)
        if validate_result.is_failure:
            return FlextResult[FlextTypes.Core.Dict].fail(
                validate_result.error or "LDAP validation failed",
            )
        # Step 3: Transform with DBT
        transform_result: FlextResult[object] = self.transform_with_dbt(
            entries, model_names
        )
        if transform_result.is_failure:
            return FlextResult[FlextTypes.Core.Dict].fail(
                transform_result.error or "DBT transformation failed",
            )
        # Combine results
        pipeline_results: FlextTypes.Core.Dict = {
            "extracted_entries": len(entries),
            "validation_metrics": validate_result.value,
            "transformation_results": transform_result.value,
        }
        logger.info("Full LDAP-to-DBT pipeline completed successfully")
        return FlextResult[FlextTypes.Core.Dict].ok(pipeline_results)

    def _prepare_ldap_data_for_dbt(
        self,
        entries: list[FlextLdapModels.Entry],
    ) -> dict[str, list[FlextTypes.Core.Dict]]:
        """Prepare LDAP entries for DBT processing.

        Converts LDAP entries to format suitable for DBT models.

        Args:
            entries: List of LDAP entries
        Returns:
            Dictionary of prepared data for DBT

        """
        # Apply schema and attribute mapping from config
        prepared_data: dict[str, list[FlextTypes.Core.Dict]] = {}
        for schema_name, table_name in self.config.ldap_schema_mapping.items():
            # Filter entries by schema type and prepare for DBT
            schema_entries = [
                entry for entry in entries if self._matches_schema(entry, schema_name)
            ]
            # Convert to tabular format with attribute mapping
            table_data: list[FlextTypes.Core.Dict] = [
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
        expected_classes: list[object] = schema_mapping.get(schema_name, [])
        return any(cls in object_classes for cls in expected_classes)

    def _map_entry_attributes(
        self,
        entry: FlextLdapModels.Entry,
    ) -> FlextTypes.Core.Dict:
        """Map LDAP entry attributes using configuration mapping."""
        mapped_attrs: FlextTypes.Core.Dict = {"dn": entry.dn}
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
        attributes: FlextTypes.Core.StringList | None,
    ) -> FlextResult[list[FlextLdapModels.Entry]]:
        """Synchronously perform LDAP search using flext-ldap API."""
        try:
            api = FlextLdapClient()

            # Create SearchRequest object as required by flext-ldap API
            search_request = FlextLdapModels.SearchRequest(
                base_dn=base_dn,
                filter_str=search_filter,
                attributes=attributes or [],
                scope="subtree",
            )

            # Use asyncio.run to handle async API in sync context (flext-ldap pattern)
            result: FlextResult[object] = asyncio.run(api.search(search_request))

            # Convert FlextLdapModels.Entry to FlextLdapModels.Entry
            if result.is_success and result.value:
                # Convert models to entities
                entities: list[FlextLdapModels.Entry] = []
                for model_entry in result.value:
                    entity = FlextLdapModels.Entry(
                        dn=model_entry.dn,
                        attributes=model_entry.attributes,
                        object_classes=getattr(model_entry, "object_classes", []),
                    )
                    entities.append(entity)
                return FlextResult[list[FlextLdapModels.Entry]].ok(entities)

            return FlextResult[list[FlextLdapModels.Entry]].fail(
                result.error or "Search returned no results",
            )
        except Exception as e:
            return FlextResult[list[FlextLdapModels.Entry]].fail(
                f"LDAP search failed: {e}",
            )


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdapClient",
]
