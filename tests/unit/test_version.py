"""Version metadata tests for flext-dbt-ldap."""

from __future__ import annotations

from unittest.mock import Mock

from flext_dbt_ldap import __version__, __version_info__
from flext_dbt_ldap.dbt_services import FlextDbtLdapService
from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion


def test_dunder_alignment() -> None:
    """Ensure dunder exports come from VERSION."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_version_metadata_integrity() -> None:
    """VERSION should expose normalized metadata."""
    assert isinstance(VERSION, FlextDbtLdapVersion)
    assert VERSION.version_tuple == VERSION.version_info


def test_version_properties() -> None:
    """Version properties should be accessible."""
    assert isinstance(VERSION.version, str)
    assert isinstance(VERSION.version_info, tuple)
    assert isinstance(VERSION.version_tuple, tuple)
    assert VERSION.author_name is None or isinstance(VERSION.author_name, str)
    assert VERSION.maintainer_name is None or isinstance(VERSION.maintainer_name, str)
    assert VERSION.description is None or isinstance(VERSION.description, str)
    assert VERSION.license is None or isinstance(VERSION.license, str)
    assert VERSION.url is None or isinstance(VERSION.url, str)


def test_incremental_users_sync_applies_bookmark_filter() -> None:
    client = Mock()
    client.run_full_pipeline.return_value = Mock(is_success=True, error=None)
    service = object.__new__(FlextDbtLdapService)
    service.client = client
    service.config = Mock(ldap_base_dn="dc=example,dc=com")
    service._sync_bookmarks = {"users": "20250101000000Z"}
    service._sync_state_file = Mock()

    result = service.sync_users_to_warehouse(incremental=True)

    assert result.is_success
    called_filter = client.run_full_pipeline.call_args.kwargs["search_filter"]
    assert "modifyTimestamp>=20250101000000Z" in called_filter
    assert service._sync_bookmarks["users"] != "20250101000000Z"


def test_incremental_groups_sync_applies_bookmark_filter() -> None:
    client = Mock()
    client.run_full_pipeline.return_value = Mock(is_success=True, error=None)
    service = object.__new__(FlextDbtLdapService)
    service.client = client
    service.config = Mock(ldap_base_dn="dc=example,dc=com")
    service._sync_bookmarks = {"groups": "20250101000000Z"}
    service._sync_state_file = Mock()

    result = service.sync_groups_to_warehouse(incremental=True)

    assert result.is_success
    called_filter = client.run_full_pipeline.call_args.kwargs["search_filter"]
    assert "modifyTimestamp>=20250101000000Z" in called_filter
    assert service._sync_bookmarks["groups"] != "20250101000000Z"
