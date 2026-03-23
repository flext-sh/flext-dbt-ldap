"""Test configuration and fixtures for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
import pathlib
import re
import tempfile
from collections.abc import Generator, Mapping, Sequence
from typing import TypeIs

import pytest
from flext_tests import td, tk
from pydantic import TypeAdapter, ValidationError

from tests import t


@pytest.fixture(scope="session")
def shared_ldap_container(flext_docker: tk) -> str:
    """Managed LDAP container using centralized tk with docker-compose."""
    compose_file = pathlib.Path(
        "~/flext/docker/docker-compose.openldap.yml"
    ).expanduser()
    start_result = flext_docker.start_compose_stack(str(compose_file))
    if start_result.is_failure:
        pytest.skip(f"OpenLDAP container failed to start: {start_result.error}")
    return "flext-openldap-test"


@pytest.fixture(scope="session")
def shared_ldap_config() -> Mapping[str, t.NormalizedValue]:
    """Shared LDAP configuration for tests."""
    return {
        "server_url": "ldap://localhost:3390",
        "bind_dn": "cn=REDACTED_LDAP_BIND_PASSWORD,dc=flext,dc=local",
        "password": "REDACTED_LDAP_BIND_PASSWORD123",
        "base_dn": "dc=flext,dc=local",
    }


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "DEBUG"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["LDAP_TEST_MODE"] = "true"
    yield
    _ = os.environ.pop("FLEXT_ENV", None)
    _ = os.environ.pop("FLEXT_LOG_LEVEL", None)
    _ = os.environ.pop("DBT_PROFILES_DIR", None)
    _ = os.environ.pop("LDAP_TEST_MODE", None)


@pytest.fixture
def dbt_ldap_profile() -> Mapping[str, t.NormalizedValue]:
    """Dbt LDAP profile configuration for testing."""
    return {
        "config": {
            "partial_parse": True,
            "printer_width": 120,
            "send_anonymous_usage_stats": False,
            "use_colors": True,
        },
        "test": {
            "outputs": {
                "default": {
                    "type": "postgres",
                    "host": "localhost",
                    "port": 5432,
                    "database": "ldap_warehouse",
                    "schema": "ldap_transformed",
                    "user": "dbt_ldap_user",
                    "password": "dbt_ldap_pass",
                    "threads": 4,
                    "keepalives_idle": 0,
                    "search_path": "ldap_transformed",
                }
            },
            "target": "default",
        },
    }


@pytest.fixture
def dbt_ldap_project_config() -> Mapping[str, t.NormalizedValue]:
    """Dbt LDAP project configuration for testing."""
    return td.build_dbt_project_config(
        name="flext_dbt_ldap_test",
        version="0.9.0",
        profile="test",
        model_config={
            "materialized": "table",
            "ldap": {
                "enable_ldap_functions": True,
                "ldap_server": "localhost:389",
                "base_dn": "dc=test,dc=com",
            },
        },
        variables={
            "ldap_base_dn": "dc=test,dc=com",
            "ldap_users_ou": "ou=users",
            "ldap_groups_ou": "ou=groups",
            "enable_ldap_validation": True,
        },
    )


@pytest.fixture
def ldap_source_config(
    shared_ldap_config: Mapping[str, t.NormalizedValue],
) -> Mapping[str, t.NormalizedValue]:
    """LDAP source configuration for testing using shared container."""
    _ = shared_ldap_config
    return {
        "server": "localhost",
        "port": 3390,
        "base_dn": "dc=flext,dc=local",
        "bind_dn": "cn=REDACTED_LDAP_BIND_PASSWORD,dc=flext,dc=local",
        "bind_password": "REDACTED_LDAP_BIND_PASSWORD123",
        "use_ssl": False,
        "use_tls": False,
        "timeout": 30,
        "search_scope": "SUBTREE",
    }


@pytest.fixture
def sample_ldap_entries() -> Sequence[Mapping[str, t.NormalizedValue]]:
    """Sample LDAP entries for testing using shared container domain."""
    return [
        {
            "dn": "cn=john.doe,ou=people,dc=flext,dc=local",
            "attributes": {
                "cn": ["john.doe"],
                "uid": ["jdoe"],
                "mail": ["john.doe@internal.invalid"],
                "givenName": ["John"],
                "sn": ["Doe"],
                "employeeNumber": ["12345"],
                "departmentNumber": ["IT"],
                "title": ["Software Engineer"],
                "telephoneNumber": ["+1-555-1234"],
                "objectClass": ["inetOrgPerson", "organizationalPerson", "person"],
            },
        },
        {
            "dn": "cn=jane.smith,ou=people,dc=flext,dc=local",
            "attributes": {
                "cn": ["jane.smith"],
                "uid": ["jsmith"],
                "mail": ["jane.smith@internal.invalid"],
                "givenName": ["Jane"],
                "sn": ["Smith"],
                "employeeNumber": ["12346"],
                "departmentNumber": ["HR"],
                "title": ["HR Manager"],
                "telephoneNumber": ["+1-555-5678"],
                "objectClass": ["inetOrgPerson", "organizationalPerson", "person"],
            },
        },
        {
            "dn": "cn=developers,ou=groups,dc=flext,dc=local",
            "attributes": {
                "cn": ["developers"],
                "description": ["Software Developers Group"],
                "member": [
                    "cn=john.doe,ou=people,dc=flext,dc=local",
                    "cn=bob.johnson,ou=people,dc=flext,dc=local",
                ],
                "objectClass": ["groupOfNames"],
            },
        },
    ]


@pytest.fixture
def dbt_ldap_models() -> Mapping[str, str]:
    """Dbt LDAP model SQL definitions for testing."""
    return {
        "staging_ldap_users": "\n\n          {{ config(materialized='view') }}\n          SELECT\n              {{ ldap_extract_attribute('dn') }} as user_dn,\n              {{ ldap_extract_attribute('cn', 0) }} as username,\n              {{ ldap_extract_attribute('uid', 0) }} as user_id,\n              {{ ldap_extract_attribute('mail', 0) }} as email,\n              {{ ldap_extract_attribute('givenName', 0) }} as first_name,\n              {{ ldap_extract_attribute('sn', 0) }} as last_name,\n              {{ ldap_extract_attribute('employeeNumber', 0) }} as employee_number,\n              {{ ldap_extract_attribute('departmentNumber', 0) }} as department,\n              {{ ldap_extract_attribute('title', 0) }} as job_title,\n              {{ ldap_extract_attribute('telephoneNumber', 0) }} as phone,\n              CURRENT_TIMESTAMP as extracted_at\n          FROM {{ source('ldap_raw', 'users') }}\n          WHERE {{ ldap_filter_object_class('inetOrgPerson') }}\n      ",
        "dim_users": "\n\n          {{ config(\n              materialized='table',\n              ldap={'validate_dn': true, 'normalize_attributes': true}\n          ) }}\n          SELECT\n              user_dn,\n              username,\n              user_id,\n              LOWER(email) as email_normalized,\n              TRIM(first_name || ' ' || last_name) as full_name,\n              first_name,\n              last_name,\n              employee_number,\n              department,\n              job_title,\n              phone,\n              {{ ldap_parse_dn_component('user_dn', 'ou') }} as organizational_unit,\n              {{ ldap_validate_email('email') }} as email_valid,\n              extracted_at,\n              CURRENT_TIMESTAMP as dbt_updated_at\n          FROM {{ ref('staging_ldap_users') }}\n          WHERE email IS NOT NULL\n      ",
        "staging_ldap_groups": "\n\n          {{ config(materialized='view') }}\n          SELECT\n              {{ ldap_extract_attribute('dn') }} as group_dn,\n              {{ ldap_extract_attribute('cn', 0) }} as group_name,\n              {{ ldap_extract_attribute('description', 0) }} as group_description,\n              {{ ldap_extract_multi_attribute('member') }} as members,\n              CURRENT_TIMESTAMP as extracted_at\n          FROM {{ source('ldap_raw', 'groups') }}\n          WHERE {{ ldap_filter_object_class('groupOfNames') }}\n      ",
        "dim_groups": "\n\n          {{ config(materialized='table') }}\n          SELECT\n              group_dn,\n              group_name,\n              group_description,\n              {{ ldap_count_members('members') }} as member_count,\n              extracted_at,\n              CURRENT_TIMESTAMP as dbt_updated_at\n          FROM {{ ref('staging_ldap_groups') }}\n      ",
        "fact_group_memberships": "\n\n          {{ config(\n              materialized='incremental',\n              unique_key=['group_dn', 'member_dn']\n          ) }}\n          SELECT\n              g.group_dn,\n              g.group_name,\n              {{ ldap_unnest_members('g.members') }} as member_dn,\n              u.user_id,\n              u.username,\n              g.extracted_at,\n              CURRENT_TIMESTAMP as dbt_updated_at\n          FROM {{ ref('staging_ldap_groups') }} g\n          CROSS JOIN LATERAL {{ ldap_split_members('g.members') }} AS member_dn\n          LEFT JOIN {{ ref('dim_users') }} u\n              ON u.user_dn = member_dn\n          {% if is_incremental() %}\n              WHERE g.extracted_at > (SELECT MAX(extracted_at) FROM {{ this }})\n          {% endif %}\n      ",
    }


@pytest.fixture
def dbt_ldap_macros() -> Mapping[str, str]:
    """Dbt LDAP macro definitions for testing."""
    return {
        "ldap_extract_attribute": "\n\n          {% macro ldap_extract_attribute(attribute_name, index=None) -%}\n              {% if index is not none %}\n                  JSON_EXTRACT_PATH_TEXT(\n                      attributes, '{{ attribute_name }}', '{{ index }}'\n                  )\n              {% else %}\n                  JSON_EXTRACT_PATH_TEXT(attributes, '{{ attribute_name }}')\n              {% endif %}\n          {%- endmacro %}\n      ",
        "ldap_filter_object_class": "\n\n          {% macro ldap_filter_object_class(object_class) -%}\n              JSON_EXTRACT_PATH_TEXT(attributes, 'objectClass')\n              LIKE '%{{ object_class }}%'\n          {%- endmacro %}\n      ",
        "ldap_parse_dn_component": "\n\n          {% macro ldap_parse_dn_component(dn_field, component) -%}\n              REGEXP_EXTRACT({{ dn_field }}, '{{ component }}=([^,]+)', 1)\n          {%- endmacro %}\n      ",
        "ldap_validate_email": "\n\n          {% macro ldap_validate_email(email_field) -%}\n              CASE\n                  WHEN {{ email_field }}\n                  ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'\n                  THEN true\n                  ELSE false\n              END\n          {%- endmacro %}\n      ",
        "ldap_extract_multi_attribute": "\n\n          {% macro ldap_extract_multi_attribute(attribute_name) -%}\n              JSON_EXTRACT_PATH_TEXT(attributes, '{{ attribute_name }}')\n          {%- endmacro %}\n      ",
        "ldap_count_members": "\n\n          {% macro ldap_count_members(members_field) -%}\n              CASE\n                  WHEN {{ members_field }} IS NULL THEN 0\n                  ELSE JSON_ARRAY_LENGTH({{ members_field }}::json)\n              END\n          {%- endmacro %}\n      ",
    }


@pytest.fixture
def dbt_ldap_sources() -> Mapping[str, t.NormalizedValue]:
    """Dbt LDAP source definitions for testing."""
    return {
        "version": 2,
        "sources": [
            {
                "name": "ldap_raw",
                "description": "Raw LDAP data extracted via flext-tap-ldap",
                "tables": [
                    {
                        "name": "users",
                        "description": "LDAP user entries",
                        "columns": [
                            {
                                "name": "dn",
                                "description": "Distinguished Name",
                                "tests": ["unique", "not_null"],
                            },
                            {
                                "name": "attributes",
                                "description": "LDAP attributes as JSON",
                                "tests": ["not_null"],
                            },
                            {
                                "name": "extracted_at",
                                "description": "Extraction timestamp",
                                "tests": ["not_null"],
                            },
                        ],
                        "tests": [
                            {
                                "name": "ldap_valid_user_dn",
                                "description": "Validate user DN format",
                            }
                        ],
                    },
                    {
                        "name": "groups",
                        "description": "LDAP group entries",
                        "columns": [
                            {
                                "name": "dn",
                                "description": "Group Distinguished Name",
                                "tests": ["unique", "not_null"],
                            },
                            {
                                "name": "attributes",
                                "description": "LDAP group attributes as JSON",
                                "tests": ["not_null"],
                            },
                        ],
                    },
                ],
            }
        ],
    }


@pytest.fixture
def dbt_ldap_tests() -> Mapping[str, str]:
    """Dbt LDAP test definitions for testing."""
    return {
        "test_ldap_valid_user_dn": "\n\n          SELECT dn\n          FROM {{ source('ldap_raw', 'users') }}\n          WHERE dn !~ '^cn=.+,ou=.+,dc=.+,dc=.+'\n      ",
        "test_unique_email_addresses": "\n\n          SELECT email_normalized, COUNT(*)\n          FROM {{ ref('dim_users') }}\n          WHERE email_normalized IS NOT NULL\n          GROUP BY email_normalized\n          HAVING COUNT(*) > 1\n      ",
        "test_valid_group_memberships": "\n\n          SELECT member_dn\n          FROM {{ ref('fact_group_memberships') }}\n          WHERE member_dn NOT IN (\n              SELECT user_dn FROM {{ ref('dim_users') }}\n          )\n      ",
        "test_ldap_attribute_consistency": "\n\n          SELECT dn\n          FROM {{ source('ldap_raw', 'users') }}\n          WHERE JSON_EXTRACT_PATH_TEXT(attributes, 'objectClass') IS NULL\n          OR JSON_EXTRACT_PATH_TEXT(attributes, 'cn') IS NULL\n      ",
    }


@pytest.fixture
def ldap_validation_rules() -> Mapping[str, t.NormalizedValue]:
    """LDAP validation rules for testing."""
    return {
        "dn_format": {
            "pattern": "^(Union[cn, uid])=.+,(Union[ou, dc])=.+",
            "description": "Valid Distinguished Name format",
        },
        "email_format": {
            "pattern": "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$",
            "description": "Valid email address format",
        },
        "required_attributes": {
            "user": ["cn", "objectClass"],
            "group": ["cn", "objectClass", "member"],
        },
        "object_classes": {
            "user": ["inetOrgPerson", "organizationalPerson", "person"],
            "group": ["groupOfNames", "groupOfUniqueNames"],
        },
    }


@pytest.fixture
def ldap_performance_config() -> Mapping[str, t.NormalizedValue]:
    """LDAP performance test configuration."""
    return {
        "large_directory_entries": 10000,
        "complex_group_memberships": 500,
        "nested_group_levels": 5,
        "concurrent_queries": 10,
        "memory_threshold": "1GB",
        "processing_time_threshold": 180,
    }


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "dbt: dbt-specific tests")
    config.addinivalue_line("markers", "ldap: LDAP integration tests")
    config.addinivalue_line("markers", "transformation: Data transformation tests")
    config.addinivalue_line("markers", "validation: Data validation tests")
    config.addinivalue_line("markers", "performance: Performance tests")
    config.addinivalue_line("markers", "slow: Slow tests")


class MockLdapDbtAdapter:
    """Mock LDAP dbt adapter."""

    def __init__(self, config: Mapping[str, t.NormalizedValue]) -> None:
        """Initialize the instance."""
        super().__init__()
        self.config = config
        self.ldap_entries: Mapping[str, t.NormalizedValue] = {}
        self.compiled_models: Mapping[str, t.NormalizedValue] = {}

    def extract_ldap_data(
        self, _base_dn: str, _search_filter: str
    ) -> Sequence[Mapping[str, t.NormalizedValue]]:
        """Extract LDAP data for dbt processing."""
        return [
            {
                "dn": "cn=john.doe,ou=people,dc=flext,dc=local",
                "attributes": {
                    "cn": "john.doe",
                    "mail": "john.doe@internal.invalid",
                    "objectClass": "inetOrgPerson",
                },
                "extracted_at": "2023-01-01T12:00:00Z",
            }
        ]

    @staticmethod
    def _is_ldap_attribute_map(
        value: t.NormalizedValue,
    ) -> TypeIs[Mapping[str, str | Sequence[str] | None]]:
        adapter = TypeAdapter(Mapping[str, str | Sequence[str] | None])
        try:
            _ = adapter.validate_python(value)
            return True
        except ValidationError:
            return False

    def split(self, dn: str) -> bool:
        """Validate DN format."""
        return bool(re.match(r"^(?:cn|uid)=.+(?:,(?:ou|dc)=.+)+", dn))

    def parse_ldap_attributes(
        self, attributes: Mapping[str, str | Sequence[str] | None]
    ) -> Mapping[str, str | None]:
        """Parse LDAP attributes for dbt models."""
        parsed: Mapping[str, str | None] = {}
        for key, value in attributes.items():
            if isinstance(value, list):
                parsed[key] = str(value[0]) if value else None
            else:
                parsed[key] = str(value) if value is not None else None
        return parsed

    def transform_ldap_to_relational(
        self, ldap_data: Sequence[Mapping[str, t.NormalizedValue]]
    ) -> Sequence[Mapping[str, t.NormalizedValue]]:
        """Transform LDAP data to relational format."""
        transformed: Sequence[Mapping[str, t.NormalizedValue]] = []
        for entry in ldap_data:
            flat_entry = {"dn": entry["dn"], "extracted_at": entry["extracted_at"]}
            attrs = entry.get("attributes")
            if self._is_ldap_attribute_map(attrs):
                flat_entry.update(self.parse_ldap_attributes(attrs))
            transformed.append(flat_entry)
        return transformed


@pytest.fixture
def mock_ldap_dbt_adapter() -> type[MockLdapDbtAdapter]:
    """Mock LDAP dbt adapter for testing."""
    return MockLdapDbtAdapter


class MockLdapConnection:
    """Mock LDAP connection."""

    def __init__(self, config: Mapping[str, t.NormalizedValue]) -> None:
        """Initialize the instance."""
        super().__init__()
        self.config = config
        self.connected = False
        self.entries: Sequence[Mapping[str, t.NormalizedValue]] = []

    def connect(self) -> bool:
        """Connect to LDAP server."""
        self.connected = True
        return True

    def disconnect(self) -> bool:
        """Disconnect from LDAP server."""
        self.connected = False
        return True

    def search(
        self,
        base_dn: str,
        _search_filter: str,
        _attributes: Sequence[str] | None = None,
    ) -> Sequence[Mapping[str, t.NormalizedValue]]:
        """Search LDAP directory."""
        if "people" in base_dn or "users" in base_dn:
            return [
                {
                    "dn": "cn=john.doe,ou=people,dc=flext,dc=local",
                    "attributes": {
                        "cn": ["john.doe"],
                        "mail": ["john.doe@internal.invalid"],
                        "objectClass": ["inetOrgPerson"],
                    },
                }
            ]
        if "groups" in base_dn:
            return [
                {
                    "dn": "cn=developers,ou=groups,dc=flext,dc=local",
                    "attributes": {
                        "cn": ["developers"],
                        "member": ["cn=john.doe,ou=people,dc=flext,dc=local"],
                        "objectClass": ["groupOfNames"],
                    },
                }
            ]
        return []

    def validate_entry(self, dn: str) -> bool:
        """Validate LDAP entry exists."""
        return dn in [entry["dn"] for entry in self.entries]


@pytest.fixture
def mock_ldap_connection() -> type[MockLdapConnection]:
    """Mock LDAP connection for testing."""
    return MockLdapConnection
