# 🧪 DBT LDAP - Test Suite

> **Module**: Comprehensive test suite for DBT LDAP transformations with data quality validation | **Audience**: Data Engineers, Analytics Engineers, QA Specialists | **Status**: Production Ready

## 📋 **Overview**

Enterprise-grade test suite for the DBT LDAP transformation project, providing comprehensive testing coverage including unit tests for macros, data quality tests, end-to-end transformation validation, and DBT model testing. This test suite demonstrates best practices for testing DBT projects and LDAP data transformations.

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto Home](../../README.md) → **📂 Component**: [DBT LDAP](../README.md) → **📂 Current**: Test Suite

---

## 🎯 **Module Purpose**

This test module provides comprehensive validation for the DBT LDAP transformations, ensuring data quality, transformation correctness, and reliability of all LDAP data modeling operations within the DBT framework.

### **Key Testing Areas**

- **Unit Testing** - DBT macro and model logic validation
- **Data Quality Testing** - Data integrity and quality checks
- **End-to-End Testing** - Complete transformation pipeline validation
- **Generic Tests** - Reusable data quality tests
- **Schema Tests** - DBT schema validation
- **Snapshot Testing** - Historical data tracking validation

---

## 📁 **Test Structure**

```
tests/
├── e2e/
│   ├── conftest.py                       # E2E test configuration
│   ├── test_dbt_e2e.py                   # End-to-end transformation tests
│   ├── profiles/
│   │   └── profiles.yml                  # Test DBT profiles
│   └── sql/
│       ├── 01-create-raw-tables.sql      # Test table creation
│       └── 02-insert-test-data.sql       # Test data insertion
├── generic/
│   ├── test_data_quality.sql             # Generic data quality tests
│   ├── test_uniqueness.sql               # Uniqueness constraint tests
│   ├── test_relationships.sql            # Referential integrity tests
│   └── test_not_null.sql                 # Not null constraint tests
├── unit/
│   ├── test_ldap_macros.sql              # LDAP macro unit tests
│   ├── test_schema_mapping.sql           # Schema mapping tests
│   └── test_transformations.sql          # Transformation logic tests
├── integration/
│   ├── test_staging_models.sql           # Staging layer tests
│   ├── test_intermediate_models.sql      # Intermediate layer tests
│   └── test_marts_models.sql             # Marts layer tests
├── performance/
│   ├── test_query_performance.sql        # Query performance tests
│   └── test_model_build_time.py          # Model build time tests
├── fixtures/
│   ├── ldap_test_data.csv               # LDAP test data fixtures
│   ├── expected_results.csv              # Expected transformation results
│   └── edge_cases.csv                    # Edge case test data
└── test_macros.sql                       # Macro testing utilities
```

---

## 🔧 **Test Categories**

### **1. End-to-End Tests (e2e/)**

#### **DBT E2E Testing (test_dbt_e2e.py)**

```python
"""End-to-end tests for DBT LDAP transformations."""

import pytest
import subprocess
import os
from pathlib import Path
import pandas as pd
import sqlalchemy
from typing import Dict, List, Any

class TestDBTLDAPE2E:
    """Test complete DBT LDAP transformation pipeline."""

    @pytest.fixture
    def dbt_project_dir(self):
        """DBT project directory."""
        return Path(__file__).parent.parent.parent

    @pytest.fixture
    def test_database_url(self):
        """Test database connection URL."""
        return os.getenv('TEST_DATABASE_URL', 'postgresql://test:test@localhost/dbt_ldap_test')

    @pytest.fixture
    def db_engine(self, test_database_url):
        """SQLAlchemy database engine."""
        return sqlalchemy.create_engine(test_database_url)

    @pytest.fixture
    def setup_test_database(self, db_engine):
        """Set up test database with sample data."""
        # Execute SQL scripts to create tables and insert test data
        sql_dir = Path(__file__).parent / 'sql'

        with db_engine.connect() as conn:
            # Create raw tables
            with open(sql_dir / '01-create-raw-tables.sql', 'r') as f:
                conn.execute(sqlalchemy.text(f.read()))

            # Insert test data
            with open(sql_dir / '02-insert-test-data.sql', 'r') as f:
                conn.execute(sqlalchemy.text(f.read()))

            conn.commit()

        yield

        # Cleanup
        with db_engine.connect() as conn:
            conn.execute(sqlalchemy.text("DROP SCHEMA IF EXISTS raw CASCADE"))
            conn.execute(sqlalchemy.text("DROP SCHEMA IF EXISTS staging CASCADE"))
            conn.execute(sqlalchemy.text("DROP SCHEMA IF EXISTS intermediate CASCADE"))
            conn.execute(sqlalchemy.text("DROP SCHEMA IF EXISTS marts CASCADE"))
            conn.commit()

    def test_full_dbt_run(self, dbt_project_dir, setup_test_database):
        """Test complete DBT run from raw to marts."""
        # Run DBT
        result = subprocess.run(
            ['dbt', 'run', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=dbt_project_dir,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0, f"DBT run failed: {result.stderr}"

        # Verify all models were created
        output_lines = result.stdout.split('\n')
        completed_models = [
            line for line in output_lines
            if 'OK created' in line or 'OK found' in line
        ]

        expected_models = [
            'stg_users',
            'stg_groups',
            'stg_org_units',
            'int_user_groups',
            'int_org_hierarchy',
            'dim_users',
            'dim_groups',
            'fact_memberships'
        ]

        for model in expected_models:
            assert any(model in line for line in completed_models), \
                f"Model {model} was not created successfully"

    def test_staging_layer_transformations(self, db_engine, setup_test_database):
        """Test staging layer data transformations."""
        # Run only staging models
        subprocess.run(
            ['dbt', 'run', '--models', 'staging', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        # Verify staging data
        with db_engine.connect() as conn:
            # Check stg_users
            users_df = pd.read_sql(
                "SELECT * FROM staging.stg_users ORDER BY user_id",
                conn
            )

            assert len(users_df) > 0, "No users in staging"
            assert 'user_id' in users_df.columns
            assert 'username' in users_df.columns
            assert 'email' in users_df.columns
            assert users_df['user_id'].is_unique

            # Check for proper data cleaning
            assert users_df['email'].notna().all(), "Null emails found"
            assert users_df['username'].str.match(r'^[a-z0-9._]+$').all(), \
                "Invalid username format found"

    def test_intermediate_layer_logic(self, db_engine, setup_test_database):
        """Test intermediate layer business logic."""
        # Run up to intermediate layer
        subprocess.run(
            ['dbt', 'run', '--models', '+intermediate', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        with db_engine.connect() as conn:
            # Test user groups aggregation
            user_groups_df = pd.read_sql(
                """
                SELECT user_id, COUNT(*) as group_count
                FROM intermediate.int_user_groups
                GROUP BY user_id
                ORDER BY user_id
                """,
                conn
            )

            assert len(user_groups_df) > 0, "No user groups found"
            assert user_groups_df['group_count'].min() >= 0, \
                "Negative group counts found"

            # Test org hierarchy
            org_hierarchy_df = pd.read_sql(
                "SELECT * FROM intermediate.int_org_hierarchy",
                conn
            )

            # Verify hierarchy relationships
            for _, row in org_hierarchy_df.iterrows():
                if row['parent_ou_id'] is not None:
                    parent_exists = org_hierarchy_df[
                        org_hierarchy_df['ou_id'] == row['parent_ou_id']
                    ].shape[0] > 0
                    assert parent_exists, \
                        f"Parent OU {row['parent_ou_id']} not found for {row['ou_id']}"

    def test_marts_layer_dimensions(self, db_engine, setup_test_database):
        """Test marts layer dimension tables."""
        # Run full DBT pipeline
        subprocess.run(
            ['dbt', 'run', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        with db_engine.connect() as conn:
            # Test dim_users
            dim_users_df = pd.read_sql(
                "SELECT * FROM marts.dim_users",
                conn
            )

            required_columns = [
                'user_key', 'user_id', 'username', 'full_name',
                'email', 'department', 'is_active', 'created_at'
            ]

            for col in required_columns:
                assert col in dim_users_df.columns, f"Missing column: {col}"

            # Verify surrogate keys
            assert dim_users_df['user_key'].is_unique, \
                "Duplicate user keys found"

            # Test dim_groups
            dim_groups_df = pd.read_sql(
                "SELECT * FROM marts.dim_groups",
                conn
            )

            assert len(dim_groups_df) > 0, "No groups in dimension"
            assert dim_groups_df['group_key'].is_unique, \
                "Duplicate group keys found"

    def test_fact_table_integrity(self, db_engine, setup_test_database):
        """Test fact table referential integrity."""
        # Run full pipeline
        subprocess.run(
            ['dbt', 'run', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        with db_engine.connect() as conn:
            # Test fact_memberships
            fact_df = pd.read_sql(
                """
                SELECT
                    f.*,
                    u.user_key as u_check,
                    g.group_key as g_check
                FROM marts.fact_memberships f
                LEFT JOIN marts.dim_users u ON f.user_key = u.user_key
                LEFT JOIN marts.dim_groups g ON f.group_key = g.group_key
                """,
                conn
            )

            # All foreign keys should exist
            assert fact_df['u_check'].notna().all(), \
                "Orphaned user keys in fact table"
            assert fact_df['g_check'].notna().all(), \
                "Orphaned group keys in fact table"

            # No duplicate memberships
            duplicates = fact_df.groupby(['user_key', 'group_key']).size()
            assert (duplicates == 1).all(), "Duplicate memberships found"

    def test_incremental_model_behavior(self, db_engine, setup_test_database):
        """Test incremental model updates."""
        # Initial run
        subprocess.run(
            ['dbt', 'run', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        # Get initial row counts
        with db_engine.connect() as conn:
            initial_count = pd.read_sql(
                "SELECT COUNT(*) as cnt FROM marts.fact_memberships",
                conn
            ).iloc[0]['cnt']

            # Insert new test data
            conn.execute(sqlalchemy.text("""
                INSERT INTO raw.ldap_users (uid, cn, mail, created_at)
                VALUES ('newuser', 'New User', 'new@example.com', NOW())
            """))
            conn.commit()

        # Run incremental update
        subprocess.run(
            ['dbt', 'run', '--models', 'fact_memberships', '--full-refresh',
             '--profiles-dir', 'tests/e2e/profiles'],
            cwd=Path(__file__).parent.parent.parent,
            check=True
        )

        # Verify new data was processed
        with db_engine.connect() as conn:
            new_count = pd.read_sql(
                "SELECT COUNT(*) as cnt FROM marts.dim_users WHERE username = 'newuser'",
                conn
            ).iloc[0]['cnt']

            assert new_count == 1, "New user was not processed"

    def test_dbt_test_suite(self, dbt_project_dir, setup_test_database):
        """Run DBT's built-in test suite."""
        # Run models first
        subprocess.run(
            ['dbt', 'run', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=dbt_project_dir,
            check=True
        )

        # Run DBT tests
        result = subprocess.run(
            ['dbt', 'test', '--profiles-dir', 'tests/e2e/profiles'],
            cwd=dbt_project_dir,
            capture_output=True,
            text=True
        )

        assert result.returncode == 0, f"DBT tests failed: {result.stdout}"

        # Parse test results
        test_lines = [
            line for line in result.stdout.split('\n')
            if 'PASS' in line or 'FAIL' in line
        ]

        failed_tests = [line for line in test_lines if 'FAIL' in line]
        assert len(failed_tests) == 0, f"Failed tests: {failed_tests}"
```

#### **Test Database Setup SQL (sql/01-create-raw-tables.sql)**

```sql
-- Create test schemas
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS intermediate;
CREATE SCHEMA IF NOT EXISTS marts;

-- Create raw LDAP tables
CREATE TABLE IF NOT EXISTS raw.ldap_users (
    uid VARCHAR(255) PRIMARY KEY,
    cn VARCHAR(255),
    sn VARCHAR(255),
    givenName VARCHAR(255),
    mail VARCHAR(255),
    department VARCHAR(255),
    title VARCHAR(255),
    manager VARCHAR(255),
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    is_active BOOLEAN DEFAULT true
);

CREATE TABLE IF NOT EXISTS raw.ldap_groups (
    cn VARCHAR(255) PRIMARY KEY,
    description TEXT,
    owner VARCHAR(255),
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.ldap_group_members (
    group_cn VARCHAR(255),
    member_uid VARCHAR(255),
    added_at TIMESTAMP,
    PRIMARY KEY (group_cn, member_uid)
);

CREATE TABLE IF NOT EXISTS raw.ldap_org_units (
    ou VARCHAR(255) PRIMARY KEY,
    description TEXT,
    parent_ou VARCHAR(255),
    created_at TIMESTAMP
);
```

#### **Test Data Insertion SQL (sql/02-insert-test-data.sql)**

```sql
-- Insert test users
INSERT INTO raw.ldap_users (uid, cn, sn, givenName, mail, department, title, manager, created_at, modified_at, is_active)
VALUES
    ('john.doe', 'John Doe', 'Doe', 'John', 'john.doe@example.com', 'Engineering', 'Senior Engineer', 'jane.smith', '2023-01-15', '2024-06-01', true),
    ('jane.smith', 'Jane Smith', 'Smith', 'Jane', 'jane.smith@example.com', 'Engineering', 'Engineering Manager', 'bob.wilson', '2022-06-01', '2024-05-15', true),
    ('bob.wilson', 'Bob Wilson', 'Wilson', 'Bob', 'bob.wilson@example.com', 'Management', 'Director', NULL, '2020-01-01', '2024-06-10', true),
    ('alice.brown', 'Alice Brown', 'Brown', 'Alice', 'alice.brown@example.com', 'HR', 'HR Specialist', 'carol.white', '2023-03-20', '2024-04-25', true),
    ('carol.white', 'Carol White', 'White', 'Carol', 'carol.white@example.com', 'HR', 'HR Manager', 'bob.wilson', '2021-11-10', '2024-05-30', true),
    ('inactive.user', 'Inactive User', 'User', 'Inactive', 'inactive@example.com', 'Engineering', 'Engineer', 'jane.smith', '2022-01-01', '2023-12-31', false);

-- Insert test groups
INSERT INTO raw.ldap_groups (cn, description, owner, created_at, modified_at)
VALUES
    ('engineering', 'Engineering Team', 'jane.smith', '2020-01-01', '2024-06-01'),
    ('management', 'Management Team', 'bob.wilson', '2020-01-01', '2024-05-15'),
    ('hr', 'Human Resources', 'carol.white', '2020-01-01', '2024-04-20'),
    ('all-staff', 'All Staff Members', 'bob.wilson', '2020-01-01', '2024-06-10'),
    ('senior-engineers', 'Senior Engineering Staff', 'jane.smith', '2022-06-15', '2024-05-01');

-- Insert group memberships
INSERT INTO raw.ldap_group_members (group_cn, member_uid, added_at)
VALUES
    ('engineering', 'john.doe', '2023-01-15'),
    ('engineering', 'jane.smith', '2022-06-01'),
    ('engineering', 'inactive.user', '2022-01-01'),
    ('senior-engineers', 'john.doe', '2024-01-01'),
    ('management', 'jane.smith', '2023-01-01'),
    ('management', 'bob.wilson', '2020-01-01'),
    ('management', 'carol.white', '2021-11-10'),
    ('hr', 'alice.brown', '2023-03-20'),
    ('hr', 'carol.white', '2021-11-10'),
    ('all-staff', 'john.doe', '2023-01-15'),
    ('all-staff', 'jane.smith', '2022-06-01'),
    ('all-staff', 'bob.wilson', '2020-01-01'),
    ('all-staff', 'alice.brown', '2023-03-20'),
    ('all-staff', 'carol.white', '2021-11-10');

-- Insert organizational units
INSERT INTO raw.ldap_org_units (ou, description, parent_ou, created_at)
VALUES
    ('company', 'Example Company', NULL, '2020-01-01'),
    ('engineering', 'Engineering Department', 'company', '2020-01-01'),
    ('management', 'Management', 'company', '2020-01-01'),
    ('hr', 'Human Resources', 'company', '2020-01-01'),
    ('frontend', 'Frontend Team', 'engineering', '2021-06-01'),
    ('backend', 'Backend Team', 'engineering', '2021-06-01');
```

### **2. Generic Data Quality Tests (generic/)**

#### **Data Quality Tests (test_data_quality.sql)**

```sql
-- Generic data quality tests for LDAP transformations

-- Test: All users should have valid email addresses
{% test valid_email_format(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} IS NOT NULL
    AND {{ column_name }} NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
{% endtest %}

-- Test: Usernames should follow LDAP naming conventions
{% test valid_ldap_username(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} NOT REGEXP '^[a-z][a-z0-9._-]*$'
    OR LENGTH({{ column_name }}) < 3
    OR LENGTH({{ column_name }}) > 32
{% endtest %}

-- Test: No orphaned records in hierarchy
{% test no_orphaned_hierarchy(model, child_column, parent_column) %}
    SELECT child.*
    FROM {{ model }} child
    LEFT JOIN {{ model }} parent ON child.{{ parent_column }} = parent.{{ child_column }}
    WHERE child.{{ parent_column }} IS NOT NULL
    AND parent.{{ child_column }} IS NULL
{% endtest %}

-- Test: Group membership consistency
{% test valid_group_membership(membership_model, user_model, group_model) %}
    SELECT m.*
    FROM {{ membership_model }} m
    LEFT JOIN {{ user_model }} u ON m.user_id = u.user_id
    LEFT JOIN {{ group_model }} g ON m.group_id = g.group_id
    WHERE u.user_id IS NULL OR g.group_id IS NULL
{% endtest %}

-- Test: No future dates
{% test no_future_dates(model, date_column) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ date_column }} > CURRENT_TIMESTAMP
{% endtest %}

-- Test: Referential integrity for manager relationships
{% test valid_manager_reference(model, manager_column, employee_id_column) %}
    SELECT emp.*
    FROM {{ model }} emp
    LEFT JOIN {{ model }} mgr ON emp.{{ manager_column }} = mgr.{{ employee_id_column }}
    WHERE emp.{{ manager_column }} IS NOT NULL
    AND mgr.{{ employee_id_column }} IS NULL
{% endtest %}

-- Test: Data freshness check
{% test data_freshness(model, timestamp_column, max_days_old=7) %}
    SELECT
        MAX({{ timestamp_column }}) as latest_record,
        CURRENT_TIMESTAMP as current_time,
        DATEDIFF('day', MAX({{ timestamp_column }}), CURRENT_TIMESTAMP) as days_old
    FROM {{ model }}
    HAVING days_old > {{ max_days_old }}
{% endtest %}

-- Test: Duplicate detection
{% test no_duplicate_combinations(model, column_list) %}
    SELECT
        {{ column_list | join(', ') }},
        COUNT(*) as record_count
    FROM {{ model }}
    GROUP BY {{ column_list | join(', ') }}
    HAVING COUNT(*) > 1
{% endtest %}

-- Test: Required fields completeness
{% test required_fields_complete(model, required_columns) %}
    SELECT *
    FROM {{ model }}
    WHERE
    {% for column in required_columns %}
        {{ column }} IS NULL
        {%- if not loop.last %} OR {% endif %}
    {% endfor %}
{% endtest %}
```

### **3. Unit Tests for Macros (unit/)**

#### **LDAP Macro Tests (test_ldap_macros.sql)**

```sql
-- Unit tests for LDAP-specific DBT macros

-- Test: parse_ldap_dn macro
{% test test_parse_ldap_dn() %}
    WITH test_cases AS (
        SELECT
            'uid=john.doe,ou=users,dc=example,dc=com' as input_dn,
            'john.doe' as expected_uid,
            'users' as expected_ou,
            'example.com' as expected_domain
        UNION ALL
        SELECT
            'cn=admin,dc=company,dc=org' as input_dn,
            NULL as expected_uid,
            NULL as expected_ou,
            'company.org' as expected_domain
    )
    SELECT
        input_dn,
        {{ parse_ldap_dn(input_dn, 'uid') }} as parsed_uid,
        {{ parse_ldap_dn(input_dn, 'ou') }} as parsed_ou,
        {{ parse_ldap_dn(input_dn, 'dc') }} as parsed_domain
    FROM test_cases
    WHERE
        parsed_uid != expected_uid
        OR parsed_ou != expected_ou
        OR parsed_domain != expected_domain
{% endtest %}

-- Test: normalize_ldap_timestamp macro
{% test test_normalize_ldap_timestamp() %}
    WITH test_cases AS (
        SELECT
            '20240619120000Z' as ldap_timestamp,
            '2024-06-19 12:00:00'::timestamp as expected_timestamp
        UNION ALL
        SELECT
            '20231225000000Z' as ldap_timestamp,
            '2023-12-25 00:00:00'::timestamp as expected_timestamp
    )
    SELECT
        ldap_timestamp,
        {{ normalize_ldap_timestamp('ldap_timestamp') }} as parsed_timestamp,
        expected_timestamp
    FROM test_cases
    WHERE parsed_timestamp != expected_timestamp
{% endtest %}

-- Test: build_hierarchy_path macro
{% test test_build_hierarchy_path() %}
    WITH test_hierarchy AS (
        SELECT 'company' as node_id, NULL as parent_id, 1 as level
        UNION ALL
        SELECT 'engineering' as node_id, 'company' as parent_id, 2 as level
        UNION ALL
        SELECT 'frontend' as node_id, 'engineering' as parent_id, 3 as level
    )
    SELECT
        node_id,
        {{ build_hierarchy_path('node_id', 'parent_id') }} as path
    FROM test_hierarchy
    WHERE
        (node_id = 'frontend' AND path != '/company/engineering/frontend')
        OR (node_id = 'engineering' AND path != '/company/engineering')
        OR (node_id = 'company' AND path != '/company')
{% endtest %}

-- Test: calculate_group_permissions macro
{% test test_calculate_group_permissions() %}
    WITH test_permissions AS (
        SELECT
            'admin' as group_name,
            'read,write,delete' as expected_permissions
        UNION ALL
        SELECT
            'users' as group_name,
            'read' as expected_permissions
    )
    SELECT
        group_name,
        {{ calculate_group_permissions('group_name') }} as calculated_permissions,
        expected_permissions
    FROM test_permissions
    WHERE calculated_permissions != expected_permissions
{% endtest %}
```

---

## 🔧 **Test Configuration**

### **Pytest Configuration (conftest.py)**

```python
"""Pytest configuration for DBT LDAP tests."""

import pytest
import os
from pathlib import Path
import subprocess
import tempfile
import shutil

@pytest.fixture(scope="session")
def dbt_project_root():
    """DBT project root directory."""
    return Path(__file__).parent.parent

@pytest.fixture(scope="session")
def test_profiles_dir():
    """Test profiles directory."""
    return Path(__file__).parent / "e2e" / "profiles"

@pytest.fixture
def temp_dbt_project():
    """Create temporary DBT project for isolated testing."""
    temp_dir = tempfile.mkdtemp()
    project_root = Path(__file__).parent.parent

    # Copy DBT project files
    for item in ['dbt_project.yml', 'models', 'macros', 'snapshots']:
        src = project_root / item
        dst = Path(temp_dir) / item
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    yield Path(temp_dir)

    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture
def dbt_runner(dbt_project_root, test_profiles_dir):
    """DBT command runner."""
    def run_dbt(*args, **kwargs):
        cmd = ['dbt'] + list(args) + ['--profiles-dir', str(test_profiles_dir)]

        result = subprocess.run(
            cmd,
            cwd=dbt_project_root,
            capture_output=True,
            text=True,
            **kwargs
        )

        return result

    return run_dbt

@pytest.fixture
def mock_ldap_data():
    """Mock LDAP data for testing."""
    return {
        'users': [
            {
                'uid': 'test.user1',
                'cn': 'Test User 1',
                'mail': 'test1@example.com',
                'department': 'Testing'
            },
            {
                'uid': 'test.user2',
                'cn': 'Test User 2',
                'mail': 'test2@example.com',
                'department': 'Testing'
            }
        ],
        'groups': [
            {
                'cn': 'test-group',
                'description': 'Test Group',
                'members': ['test.user1', 'test.user2']
            }
        ]
    }

@pytest.fixture
def test_database_config():
    """Test database configuration."""
    return {
        'host': os.getenv('TEST_DB_HOST', 'localhost'),
        'port': os.getenv('TEST_DB_PORT', '5432'),
        'database': os.getenv('TEST_DB_NAME', 'dbt_ldap_test'),
        'username': os.getenv('TEST_DB_USER', 'test'),
        'password': os.getenv('TEST_DB_PASS', 'test')
    }
```

### **Test Profiles Configuration (profiles/profiles.yml)**

```yaml
dbt_ldap:
  target: test
  outputs:
    test:
      type: postgres
      host: "{{ env_var('TEST_DB_HOST', 'localhost') }}"
      port: "{{ env_var('TEST_DB_PORT', '5432') | int }}"
      user: "{{ env_var('TEST_DB_USER', 'test') }}"
      pass: "{{ env_var('TEST_DB_PASS', 'test') }}"
      dbname: "{{ env_var('TEST_DB_NAME', 'dbt_ldap_test') }}"
      schema: public
      threads: 4
      keepalives_idle: 0
```

---

## 🔗 **Cross-References**

### **Component Documentation**

- [Component Overview](../README.md) - Complete DBT LDAP documentation
- [Models Documentation](../models/) - DBT model definitions
- [Macros Documentation](../macros/) - Custom macro implementations

### **DBT Documentation**

- [DBT Testing](https://docs.getdbt.com/docs/building-a-dbt-project/tests) - DBT testing guide
- [DBT Best Practices](https://docs.getdbt.com/guides/best-practices) - DBT best practices
- [DBT Macros](https://docs.getdbt.com/docs/building-a-dbt-project/jinja-macros) - Macro development

### **Testing References**

- [Data Quality Testing](https://www.getdbt.com/blog/data-quality-tests-dbt/) - Data quality patterns
- [PyTest Documentation](https://docs.pytest.org/) - Python testing framework
- [SQL Testing Patterns](https://mode.com/sql-tutorial/sql-unit-testing/) - SQL testing strategies

---

**📂 Module**: Test Suite | **🏠 Component**: [DBT LDAP](../README.md) | **Framework**: DBT 1.0+, PyTest | **Updated**: 2025-06-19
