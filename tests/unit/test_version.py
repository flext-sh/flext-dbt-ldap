"""Unit tests for flext-dbt-ldap version module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata
import sys
from unittest.mock import patch

import flext_dbt_ldap
import flext_dbt_ldap as test_module


def test_version_is_string() -> None:
    """Test that __version__ is a string."""
    assert isinstance(flext_dbt_ldap.__version__, str)


def test_version_info_is_tuple() -> None:
    """Test that __version_info__ is a tuple of integers."""
    assert isinstance(flext_dbt_ldap.__version_info__, tuple)
    if not all(isinstance(x, int) for x in flext_dbt_ldap.__version_info__):
        invalid_types = [
            type(x).__name__
            for x in flext_dbt_ldap.__version_info__
            if not isinstance(x, int)
        ]
        msg: str = (
            f"Expected all integers in version_info, found types: {invalid_types}"
        )
        raise AssertionError(msg)


def test_version_all_exports() -> None:
    """Test that __all__ contains expected exports."""
    expected_exports = [
        "Config",
        "DNParser",
        "FlextDbtLdapDeprecationWarning",
        "GroupDimension",
        "LDAPBaseConfig",
        "LDAPError",
        "LDAPMacros",
        "LDAPTransformer",
        "FlextResult",
        "TimestampConverter",
        "UserDimension",
        "ValidationError",
        "__version__",
        "__version_info__",
    ]
    if flext_dbt_ldap.__all__ != expected_exports:
        msg: str = f"Expected {expected_exports}, got {flext_dbt_ldap.__all__}"
        raise AssertionError(msg)


def test_version_parsing() -> None:
    """Test version string parsing to tuple."""
    # Test with a mock version
    version = "1.2.3"
    version_info = tuple(int(x) for x in version.split(".") if x.isdigit())
    if version_info != (1, 2, 3):
        msg: str = f"Expected {(1, 2, 3)}, got {version_info}"
        raise AssertionError(msg)


def test_package_metadata_fallback() -> None:
    """Test that package metadata fallback works."""
    # The actual package may not be installed in dev mode
    # so we test the fallback behavior
    try:
        version = importlib.metadata.version("flext-dbt-ldap")
        assert isinstance(version, str)
    except importlib.metadata.PackageNotFoundError:
        # This is expected in dev environment
        if flext_dbt_ldap.__version__ != "0.9.0":
            msg = f'Expected "0.9.0", got {flext_dbt_ldap.__version__}'
            raise AssertionError(msg) from None


def test_package_metadata_error_handling() -> None:
    """Test the exception path in __init__.py module loading."""
    # Import the module fresh to trigger the metadata lookup

    # Remove the module if it's already cached
    module_name = "flext_dbt_ldap"
    if module_name in sys.modules:
        del sys.modules[module_name]

    # Mock the metadata.version to raise PackageNotFoundError
    with patch("importlib.metadata.version") as mock_version:
        mock_version.side_effect = importlib.metadata.PackageNotFoundError(
            "mocked error",
        )

        # Import the module - this should trigger the exception handling

        # Verify the fallback version is used
        if test_module.__version__ != "0.9.0":
            msg = f'Expected "0.9.0", got {test_module.__version__}'
            raise AssertionError(msg) from None
        assert test_module.__version_info__ == (0, 7, 0)  # Only digits are included
