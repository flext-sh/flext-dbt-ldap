"""Version metadata tests for flext-dbt-ldap."""

from __future__ import annotations

from unittest.mock import Mock

from flext_dbt_ldap import __version__, __version_info__
from flext_dbt_ldap.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
)
from flext_dbt_ldap.dbt_services import FlextDbtLdapService


def test_dunder_alignment() -> None:
    """Ensure version exports are consistent."""
    assert isinstance(__version__, str)
    assert isinstance(__version_info__, tuple)
    assert (
        tuple(int(part) if part.isdigit() else part for part in __version__.split("."))
        == __version_info__
    )


def test_version_metadata_integrity() -> None:
    """Metadata exports should be strings."""
    assert isinstance(__title__, str)
    assert isinstance(__description__, str)
    assert isinstance(__author__, str)
    assert isinstance(__author_email__, str)
    assert isinstance(__license__, str)
    assert isinstance(__url__, str)


def test_version_properties() -> None:
    """Version fields should not be empty when package metadata is available."""
    assert __version__.strip() != ""
    assert len(__version_info__) >= 1


def test_incremental_users_sync_applies_bookmark_filter() -> None:
    service = object.__new__(FlextDbtLdapService)
    mock_pipeline = Mock(return_value=Mock(is_success=True, error=None))
    object.__setattr__(service, "run_full_pipeline", mock_pipeline)
    service._dbt_ldap_config = Mock(ldap_base_dn="dc=example,dc=com")
    service._sync_bookmarks = {"users": "20250101000000Z"}
    service._sync_state_file = Mock()
    result = service.sync_users_to_warehouse(incremental=True)
    assert result.is_success
    called_filter = mock_pipeline.call_args.kwargs["search_filter"]
    assert "modifyTimestamp>=20250101000000Z" in called_filter
    assert service._sync_bookmarks["users"] != "20250101000000Z"


def test_incremental_groups_sync_applies_bookmark_filter() -> None:
    service = object.__new__(FlextDbtLdapService)
    mock_pipeline = Mock(return_value=Mock(is_success=True, error=None))
    object.__setattr__(service, "run_full_pipeline", mock_pipeline)
    service._dbt_ldap_config = Mock(ldap_base_dn="dc=example,dc=com")
    service._sync_bookmarks = {"groups": "20250101000000Z"}
    service._sync_state_file = Mock()
    result = service.sync_groups_to_warehouse(incremental=True)
    assert result.is_success
    called_filter = mock_pipeline.call_args.kwargs["search_filter"]
    assert "modifyTimestamp>=20250101000000Z" in called_filter
    assert service._sync_bookmarks["groups"] != "20250101000000Z"
