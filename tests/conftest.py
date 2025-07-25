"""Test configuration for flext-dbt-ldap.

Provides pytest fixtures and configuration for testing dbt LDAP integration
functionality using real LDAP connections and dbt-core patterns.
"""

from __future__ import annotations

import os
import tempfile
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator


# Test environment setup
@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "debug"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["LDAP_TEST_MODE"] = "true"
    yield
    # Cleanup
    os.environ.pop("FLEXT_ENV", None)
    os.environ.pop("FLEXT_LOG_LEVEL", None)
    os.environ.pop("DBT_PROFILES_DIR", None)
    os.environ.pop("LDAP_TEST_MODE", None)


# dbt LDAP configuration fixtures
@pytest.fixture
def dbt_ldap_profile() -> dict[str, Any]:
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
                    "type": "postgres",  # Using postgres as target for
                    # transformed LDAP data
                    "host": "localhost",
                    "port": 5432,
                    "database": "ldap_warehouse",
                    "schema": "ldap_transformed",
                    "user": "dbt_ldap_user",
                    "password": "dbt_ldap_pass",
                    "threads": 4,
                    "keepalives_idle": 0,
                    "search_path": "ldap_transformed",
                },
            },
            "target": "default",
        },
    }


@pytest.fixture
def dbt_ldap_project_config() -> dict[str, Any]:
    """Dbt LDAP project configuration for testing."""
    return {
        "name": "flext_dbt_ldap_test",
        "version": "1.0.0",
        "profile": "test",
        "model-paths": ["models"],
        "analysis-paths": ["analyses"],
        "test-paths": ["tests"],
        "seed-paths": ["seeds"],
        "macro-paths": ["macros"],
        "snapshot-paths": ["snapshots"],
        "docs-paths": ["docs"],
        "asset-paths": ["assets"],
        "target-path": "target",
        "clean-targets": ["target", "dbt_packages"],
        "require-dbt-version": ">=1.8.0",
        "model_config": {
            "materialized": "table",
            "ldap": {
                "enable_ldap_functions": True,
                "ldap_server": "localhost:389",
                "base_dn": "dc=test,dc=com",
            },
        },
        "vars": {
            "ldap_base_dn": "dc=test,dc=com",
            "ldap_users_ou": "ou=users",
            "ldap_groups_ou": "ou=groups",
            "enable_ldap_validation": True,
        },
    }


# LDAP source fixtures
@pytest.fixture
def ldap_source_config() -> dict[str, Any]:
    """LDAP source configuration for testing."""
    return {
        "server": "localhost",
        "port": 389,
        "base_dn": "dc=test,dc=com",
        "bind_dn": "cn=admin,dc=test,dc=com",
        "bind_password": "admin_pass",
        "use_ssl": False,
        "use_tls": False,
        "timeout": 30,
        "search_scope": "SUBTREE",
    }


@pytest.fixture
def sample_ldap_entries() -> list[dict[str, Any]]:
    """Sample LDAP entries for testing."""
    return [
        {
            "dn": "cn=john.doe,ou=users,dc=test,dc=com",
            "attributes": {
                "cn": ["john.doe"],
                "uid": ["jdoe"],
                "mail": ["john.doe@test.com"],
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
            "dn": "cn=jane.smith,ou=users,dc=test,dc=com",
            "attributes": {
                "cn": ["jane.smith"],
                "uid": ["jsmith"],
                "mail": ["jane.smith@test.com"],
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
            "dn": "cn=developers,ou=groups,dc=test,dc=com",
            "attributes": {
                "cn": ["developers"],
                "description": ["Software Developers Group"],
                "member": [
                    "cn=john.doe,ou=users,dc=test,dc=com",
                    "cn=bob.johnson,ou=users,dc=test,dc=com",
                ],
                "objectClass": ["groupOfNames"],
            },
        },
    ]


# dbt LDAP model definitions
@pytest.fixture
def dbt_ldap_models() -> dict[str, str]:
    """Dbt LDAP model SQL definitions for testing."""
    return {
        "staging_ldap_users": """
            {{ config(materialized='view') }}
            SELECT
                {{ ldap_extract_attribute('dn') }} as user_dn,
                {{ ldap_extract_attribute('cn', 0) }} as username,
                {{ ldap_extract_attribute('uid', 0) }} as user_id,
                {{ ldap_extract_attribute('mail', 0) }} as email,
                {{ ldap_extract_attribute('givenName', 0) }} as first_name,
                {{ ldap_extract_attribute('sn', 0) }} as last_name,
                {{ ldap_extract_attribute('employeeNumber', 0) }} as employee_number,
                {{ ldap_extract_attribute('departmentNumber', 0) }} as department,
                {{ ldap_extract_attribute('title', 0) }} as job_title,
                {{ ldap_extract_attribute('telephoneNumber', 0) }} as phone,
                CURRENT_TIMESTAMP as extracted_at
            FROM {{ source('ldap_raw', 'users') }}
            WHERE {{ ldap_filter_object_class('inetOrgPerson') }}
        """,
        "dim_users": """
            {{ config(
                materialized='table',
                ldap={'validate_dn': true, 'normalize_attributes': true}
            ) }}
            SELECT
                user_dn,
                username,
                user_id,
                LOWER(email) as email_normalized,
                TRIM(first_name || ' ' || last_name) as full_name,
                first_name,
                last_name,
                employee_number,
                department,
                job_title,
                phone,
                {{ ldap_parse_dn_component('user_dn', 'ou') }} as organizational_unit,
                {{ ldap_validate_email('email') }} as email_valid,
                extracted_at,
                CURRENT_TIMESTAMP as dbt_updated_at
            FROM {{ ref('staging_ldap_users') }}
            WHERE email IS NOT NULL
        """,
        "staging_ldap_groups": """
            {{ config(materialized='view') }}
            SELECT
                {{ ldap_extract_attribute('dn') }} as group_dn,
                {{ ldap_extract_attribute('cn', 0) }} as group_name,
                {{ ldap_extract_attribute('description', 0) }} as group_description,
                {{ ldap_extract_multi_attribute('member') }} as members,
                CURRENT_TIMESTAMP as extracted_at
            FROM {{ source('ldap_raw', 'groups') }}
            WHERE {{ ldap_filter_object_class('groupOfNames') }}
        """,
        "dim_groups": """
            {{ config(materialized='table') }}
            SELECT
                group_dn,
                group_name,
                group_description,
                {{ ldap_count_members('members') }} as member_count,
                extracted_at,
                CURRENT_TIMESTAMP as dbt_updated_at
            FROM {{ ref('staging_ldap_groups') }}
        """,
        "fact_group_memberships": """
            {{ config(
                materialized='incremental',
                unique_key=['group_dn', 'member_dn']
            ) }}
            SELECT
                g.group_dn,
                g.group_name,
                {{ ldap_unnest_members('g.members') }} as member_dn,
                u.user_id,
                u.username,
                g.extracted_at,
                CURRENT_TIMESTAMP as dbt_updated_at
            FROM {{ ref('staging_ldap_groups') }} g
            CROSS JOIN LATERAL {{ ldap_split_members('g.members') }} AS member_dn
            LEFT JOIN {{ ref('dim_users') }} u
                ON u.user_dn = member_dn
            {% if is_incremental() %}
                WHERE g.extracted_at > (SELECT MAX(extracted_at) FROM {{ this }})
            {% endif %}
        """,
    }


# dbt LDAP macro definitions
@pytest.fixture
def dbt_ldap_macros() -> dict[str, str]:
    """Dbt LDAP macro definitions for testing."""
    return {
        "ldap_extract_attribute": """
            {% macro ldap_extract_attribute(attribute_name, index=None) -%}
                {% if index is not none %}
                    JSON_EXTRACT_PATH_TEXT(
                        attributes, '{{ attribute_name }}', '{{ index }}'
                    )
                {% else %}
                    JSON_EXTRACT_PATH_TEXT(attributes, '{{ attribute_name }}')
                {% endif %}
            {%- endmacro %}
        """,
        "ldap_filter_object_class": """
            {% macro ldap_filter_object_class(object_class) -%}
                JSON_EXTRACT_PATH_TEXT(attributes, 'objectClass')
                LIKE '%{{ object_class }}%'
            {%- endmacro %}
        """,
        "ldap_parse_dn_component": """
            {% macro ldap_parse_dn_component(dn_field, component) -%}
                REGEXP_EXTRACT({{ dn_field }}, '{{ component }}=([^,]+)', 1)
            {%- endmacro %}
        """,
        "ldap_validate_email": r"""
            {% macro ldap_validate_email(email_field) -%}
                CASE
                    WHEN {{ email_field }}
                    ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
                    THEN true
                    ELSE false
                END
            {%- endmacro %}
        """,
        "ldap_extract_multi_attribute": """
            {% macro ldap_extract_multi_attribute(attribute_name) -%}
                JSON_EXTRACT_PATH_TEXT(attributes, '{{ attribute_name }}')
            {%- endmacro %}
        """,
        "ldap_count_members": """
            {% macro ldap_count_members(members_field) -%}
                CASE
                    WHEN {{ members_field }} IS NULL THEN 0
                    ELSE JSON_ARRAY_LENGTH({{ members_field }}::json)
                END
            {%- endmacro %}
        """,
    }


# dbt LDAP source definitions
@pytest.fixture
def dbt_ldap_sources() -> dict[str, Any]:
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
                            },
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
            },
        ],
    }


# LDAP test fixtures
@pytest.fixture
def dbt_ldap_tests() -> dict[str, str]:
    """Dbt LDAP test definitions for testing."""
    return {
        "test_ldap_valid_user_dn": """
            SELECT dn
            FROM {{ source('ldap_raw', 'users') }}
            WHERE dn !~ '^cn=.+,ou=.+,dc=.+,dc=.+'
        """,
        "test_unique_email_addresses": """
            SELECT email_normalized, COUNT(*)
            FROM {{ ref('dim_users') }}
            WHERE email_normalized IS NOT NULL
            GROUP BY email_normalized
            HAVING COUNT(*) > 1
        """,
        "test_valid_group_memberships": """
            SELECT member_dn
            FROM {{ ref('fact_group_memberships') }}
            WHERE member_dn NOT IN (
                SELECT user_dn FROM {{ ref('dim_users') }}
            )
        """,
        "test_ldap_attribute_consistency": """
            SELECT dn
            FROM {{ source('ldap_raw', 'users') }}
            WHERE JSON_EXTRACT_PATH_TEXT(attributes, 'objectClass') IS NULL
            OR JSON_EXTRACT_PATH_TEXT(attributes, 'cn') IS NULL
        """,
    }


# LDAP validation fixtures
@pytest.fixture
def ldap_validation_rules() -> dict[str, Any]:
    """LDAP validation rules for testing."""
    return {
        "dn_format": {
            "pattern": r"^(cn|uid)=.+,(ou|dc)=.+",
            "description": "Valid Distinguished Name format",
        },
        "email_format": {
            "pattern": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
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


# Performance test fixtures
@pytest.fixture
def ldap_performance_config() -> dict[str, Any]:
    """LDAP performance test configuration."""
    return {
        "large_directory_entries": 10000,
        "complex_group_memberships": 500,
        "nested_group_levels": 5,
        "concurrent_queries": 10,
        "memory_threshold": "1GB",
        "processing_time_threshold": 180,  # 3 minutes
    }


# Pytest markers for test categorization
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


# Mock services
@pytest.fixture
def mock_ldap_dbt_adapter() -> Any:
    """Mock LDAP dbt adapter for testing."""

    class MockLdapDbtAdapter:
        def __init__(self, config: dict[str, Any]) -> None:
            self.config = config
            self.ldap_entries: dict[str, Any] = {}
            self.compiled_models: dict[str, Any] = {}

        def extract_ldap_data(
            self,
            base_dn: str,
            search_filter: str,
        ) -> list[dict[str, Any]]:
            """Extract LDAP data for dbt processing."""
            # Mock LDAP extraction
            return [
                {
                    "dn": "cn=john.doe,ou=users,dc=test,dc=com",
                    "attributes": {
                        "cn": "john.doe",
                        "mail": "john.doe@test.com",
                        "objectClass": "inetOrgPerson",
                    },
                    "extracted_at": "2023-01-01T12:00:00Z",
                },
            ]

        def validate_dn_format(self, dn: str) -> bool:
            """Validate DN format."""
            import re

            pattern = r"^(cn|uid)=.+,(ou|dc)=.+"
            return bool(re.match(pattern, dn))

        def parse_ldap_attributes(
            self,
            attributes: dict[str, Any],
        ) -> dict[str, str | None]:
            """Parse LDAP attributes for dbt models."""
            parsed: dict[str, str | None] = {}
            for key, value in attributes.items():
                if isinstance(value, list):
                    parsed[key] = value[0] if value else None
                else:
                    parsed[key] = str(value) if value is not None else None
            return parsed

        def transform_ldap_to_relational(
            self,
            ldap_data: list[dict[str, Any]],
        ) -> list[dict[str, Any]]:
            """Transform LDAP data to relational format."""
            transformed = []
            for entry in ldap_data:
                flat_entry = {
                    "dn": entry["dn"],
                    "extracted_at": entry["extracted_at"],
                }
                flat_entry.update(self.parse_ldap_attributes(entry["attributes"]))
                transformed.append(flat_entry)
            return transformed

    return MockLdapDbtAdapter


@pytest.fixture
def mock_ldap_connection() -> Any:
    """Mock LDAP connection for testing."""

    class MockLdapConnection:
        def __init__(self, config: dict[str, Any]) -> None:
            self.config = config
            self.connected = False
            self.entries: list[Any] = []

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
            search_filter: str,
            attributes: list[str] | None = None,
        ) -> list[dict[str, Any]]:
            """Search LDAP directory."""
            # Mock search results
            if "users" in base_dn:
                return [
                    {
                        "dn": "cn=john.doe,ou=users,dc=test,dc=com",
                        "attributes": {
                            "cn": ["john.doe"],
                            "mail": ["john.doe@test.com"],
                            "objectClass": ["inetOrgPerson"],
                        },
                    },
                ]
            if "groups" in base_dn:
                return [
                    {
                        "dn": "cn=developers,ou=groups,dc=test,dc=com",
                        "attributes": {
                            "cn": ["developers"],
                            "member": ["cn=john.doe,ou=users,dc=test,dc=com"],
                            "objectClass": ["groupOfNames"],
                        },
                    },
                ]
            return []

        def validate_entry(self, dn: str) -> bool:
            """Validate LDAP entry exists."""
            return dn in [entry["dn"] for entry in self.entries]

    return MockLdapConnection
