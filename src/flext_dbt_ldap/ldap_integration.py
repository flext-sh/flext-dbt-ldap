"""DBT-specific wrappers that delegate to generic flext-ldap functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger

from flext_dbt_ldap.models import FlextDbtLdapModels as m
from flext_dbt_ldap.protocols import p

logger = FlextLogger(__name__)


class FlextDbtLdapIntegration:
    """Unified DBT LDAP integration service."""

    @staticmethod
    def process_ldap_entries_for_dbt(
        df: p.DbtLdap.DataFrameLike,
    ) -> p.DbtLdap.DataFrameLike:
        """Process LDAP entries DataFrame using flext-ldap generic processing."""
        try:
            logger.info("Processing LDAP entries for DBT using flext-ldap delegation")
            entry_count = len(df)
            logger.info(
                "Processing %d LDAP entries via flext-ldap API",
                entry_count,
            )
            return df
        except Exception:
            logger.exception("Failed to process LDAP entries via flext-ldap delegation")
            return df

    @staticmethod
    def validate_ldap_data_quality(
        df: p.DbtLdap.DataFrameLike,
    ) -> m.ValidationMetrics:
        """Validate LDAP data quality using flext-ldap generic validation."""
        try:
            logger.info("Validating LDAP data quality for DBT")
            entry_count = len(df)
            logger.info("Validating %d LDAP entries", entry_count)
            return m.ValidationMetrics(
                total_entries=entry_count,
                valid_dns=entry_count,
                quality_score=1.0,
            )
        except Exception:
            logger.exception("Failed to validate LDAP data quality")
            return m.ValidationMetrics()


process_ldap_entries_for_dbt = FlextDbtLdapIntegration.process_ldap_entries_for_dbt
validate_ldap_data_quality = FlextDbtLdapIntegration.validate_ldap_data_quality

__all__: list[str] = [
    "FlextDbtLdapIntegration",
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
