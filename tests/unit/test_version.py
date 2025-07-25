"""Unit tests for flext-dbt-ldap version module."""

from __future__ import annotations

import importlib.metadata

import flext_dbt_ldap


def test_version_is_string() -> None:
    """Test that __version__ is a string."""
    assert isinstance(flext_dbt_ldap.__version__, str)


def test_version_info_is_tuple() -> None:
    """Test that __version_info__ is a tuple of integers."""
    assert isinstance(flext_dbt_ldap.__version_info__, tuple)
    assert all(isinstance(x, int) for x in flext_dbt_ldap.__version_info__)


def test_version_all_exports() -> None:
    """Test that __all__ contains expected exports."""
    expected_exports = [
        "BaseModel",
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
    assert flext_dbt_ldap.__all__ == expected_exports


def test_version_parsing() -> None:
    """Test version string parsing to tuple."""
    # Test with a mock version
    version = "1.2.3"
    version_info = tuple(int(x) for x in version.split(".") if x.isdigit())
    assert version_info == (1, 2, 3)


def test_package_metadata_fallback() -> None:
    """Test that package metadata fallback works."""
    # The actual package may not be installed in dev mode
    # so we test the fallback behavior
    try:
        version = importlib.metadata.version("flext-dbt-ldap")
        assert isinstance(version, str)
    except importlib.metadata.PackageNotFoundError:
        # This is expected in dev environment
        assert flext_dbt_ldap.__version__ == "0.7.0"


def test_package_metadata_error_handling() -> None:
    """Test the exception path in __init__.py module loading."""
    # Import the module fresh to trigger the metadata lookup
    import sys
    from unittest.mock import patch

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
        import flext_dbt_ldap as test_module

        # Verify the fallback version is used
        assert test_module.__version__ == "0.7.0"
        assert test_module.__version_info__ == (0, 7, 0)  # Only digits are included
