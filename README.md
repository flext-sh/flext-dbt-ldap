# FLEXT-DBT-LDAP

[![dbt 1.6+](https://img.shields.io/badge/dbt-1.6+-orange.svg)](https://getdbt.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-DBT-LDAP** provides production-ready dbt models and transformations for LDAP directory data. It standardizes raw LDAP entries from Singer taps into business-ready dimensional models for user, group, and organizational analytics.

Part of the [FLEXT](https://github.com/flext-sh/flext) ecosystem.

## 🚀 Key Features

- **Dimensional Modeling**: Pre-built star schema for Users (`dim_users`), Groups (`dim_groups`), and Organizational Units (`dim_org_units`).
- **Security Analytics**: Dedicated fact tables for analyzing group memberships, password expiry risks, and account status.
- **Historical Tracking**: Built-in dbt snapshots for SCD Type 2 tracking of directory changes over time.
- **LDAP Macros**: Custom Jinja macros for parsing DNs (`distinguishedName`), handling bitmask attributes (UserAccountControl), and specialized timestamp conversions.
- **Hierarchy Handling**: Recursive CTE models to flatten nested Organizational Unit structures.
- **Quality Controls**: Integrated `dbt test` suites for referential integrity, schema validation, and orphan detection.

## 📦 Installation

To use in your dbt project, add to your `packages.yml`:

```yaml
packages:
  - git: "https://github.com/organization/flext.git"
    subdirectory: "flext-dbt-ldap"
    revision: "main" 
```

Run dependencies:

```bash
dbt deps
```

## 🛠️ Usage

### Core Models

Easily reference standardized models in your own analysis:

```sql
-- Analyze Active User Distribution by Department
SELECT 
    department,
    COUNT(*) as user_count
FROM {{ ref('dim_users') }}
WHERE is_active = true
GROUP BY department
ORDER BY user_count DESC
```

### Parsing Distinguished Names (DN)

Use the provided macros to handle complex LDAP attributes:

```sql
SELECT
    dn,
    -- Extract specific components
    {{ flext_dbt_ldap.extract_rdn('dn') }} as common_name,
    {{ flext_dbt_ldap.extract_parent_dn('dn') }} as parent_ou
FROM {{ ref('stg_ldap_entries') }}
```

### Analyzing Group Membership

Resolve nested group memberships effectively.

```sql
SELECT
    u.common_name as user_name,
    g.common_name as group_name,
    m.membership_type -- 'DIRECT' or 'NESTED'
FROM {{ ref('fact_group_memberships') }} m
JOIN {{ ref('dim_users') }} u ON m.user_key = u.user_key
JOIN {{ ref('dim_groups') }} g ON m.group_key = g.group_key
```

## 🏗️ Architecture

The project follows a standard dbt layer structure:

- **Staging**: Cleans raw JSON data from Singer taps (`stg_ldap_*`).
- **Intermediate**: Handles heavy transformations like DN parsing and hierarchy flattening (`int_ldap_*`).
- **Marts**: Business-facing dimensional models exposed to BI tools (`dim_*`, `fact_*`).

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new models, improving macros, and running the test suite.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
