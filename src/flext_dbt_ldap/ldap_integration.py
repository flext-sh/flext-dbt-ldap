"""LDAP Integration for DBT using flext-ldap library.

This module provides Python functions that can be called from DBT Python models
to eliminate code duplication with flext-ldap library.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

from flext_core import get_logger
from flext_ldap import (
    FlextLdapClient,
    format_ldap_timestamp,
    parse_dn,
    validate_dn,
)

logger = get_logger(__name__)


def process_ldap_entries_for_dbt(df: Any) -> Any:
    """Process LDAP entries DataFrame using flext-ldap functions.

    This function can be called from DBT Python models to leverage
    flext-ldap functionality without duplicating code.

    Args:
        df: Pandas DataFrame with LDAP entries

    Returns:
        Processed DataFrame with flext-ldap enhancements

    """
    try:
        # Use flext-ldap functions for processing
        df["is_valid_dn"] = df["dn"].apply(validate_dn)
        df["parsed_dn"] = df["dn"].apply(
            lambda x: parse_dn(x) if validate_dn(x) else None
        )
        df["formatted_timestamp"] = df.get("createTimestamp", "").apply(
            lambda x: format_ldap_timestamp(x) if x else None
        )

        logger.info("Processed %d LDAP entries using flext-ldap", len(df))
        return df

    except Exception:
        logger.exception("Failed to process LDAP entries")
        return df


def validate_ldap_data_quality(df: Any) -> dict[str, Any]:
    """Validate LDAP data quality using flext-ldap standards.

    Args:
        df: DataFrame to validate

    Returns:
        Quality metrics dictionary

    """
    try:
        if df.empty:
            return {"total_entries": 0, "valid_dns": 0, "quality_score": 0.0}

        total_entries = len(df)
        valid_dns = df["dn"].apply(validate_dn).sum() if "dn" in df.columns else 0
        quality_score = (valid_dns / total_entries) * 100 if total_entries > 0 else 0.0

        return {
            "total_entries": total_entries,
            "valid_dns": valid_dns,
            "quality_score": quality_score,
        }

    except Exception as e:
        logger.exception("Failed to validate LDAP data quality: %s", e)
        return {"total_entries": 0, "valid_dns": 0, "quality_score": 0.0}


__all__ = [
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
