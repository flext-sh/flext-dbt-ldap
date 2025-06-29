# CLAUDE.local.md - DBT-LDAP PROJECT SPECIFICS

**Hierarquia**: **PROJECT-SPECIFIC**  
**Projeto**: dbt LDAP - Enterprise Directory Data Transformation  
**Status**: PRODUCTION READY - Active LDAP data transformation  
**Framework**: dbt Core + LDAP Models + Data Warehouse + Analytics  
**Última Atualização**: 2025-06-26

**Referência Global**: `/home/marlonsc/CLAUDE.md` → Universal principles  
**Referência Workspace**: `../CLAUDE.md` → PyAuto workspace patterns  
**Referência Cross-Workspace**: `/home/marlonsc/CLAUDE.local.md` → Cross-workspace issues

---

## 🎯 PROJECT-SPECIFIC CONFIGURATION

### Virtual Environment Usage

```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate
# NOT project-specific venv
```

### Agent Coordination

```bash
# Read workspace coordination first
cat /home/marlonsc/pyauto/.token | tail -5
# Use project .token only for project-specific coordination
```

### Project-Specific Environment Variables

```bash
# dbt LDAP specific configurations
export DBT_POSTGRES_HOST=ldap-warehouse.enterprise.com
export DBT_POSTGRES_PORT=5432
export DBT_POSTGRES_USER=dbt_ldap_user
export DBT_POSTGRES_PASS=secure_dbt_password
export DBT_POSTGRES_DB=ldap_warehouse
export DBT_PROFILES_DIR=.
export DBT_TARGET=dev
export DBT_THREADS=4
export DBT_LDAP_BASE_DN=dc=company,dc=com
export DBT_ENABLE_SNAPSHOTS=true
export DBT_LOG_LEVEL=DEBUG
```

---

## 🏗️ DBT LDAP ARCHITECTURE

### **Purpose & Role**

- **LDAP Data Transformation Engine**: Complete dbt project for transforming raw LDAP data
- **Identity Analytics Platform**: Business intelligence models for directory analytics
- **Data Warehouse Builder**: Builds dimensional models for LDAP reporting
- **Historical Tracking System**: Snapshots and change tracking for directory evolution
- **Enterprise Reporting Foundation**: Analytics-ready tables for identity governance

### **Core dbt Components**

```sql
-- dbt LDAP project structure
dbt-ldap/
├── models/
│   ├── staging/         -- Raw LDAP data transformation
│   │   ├── stg_users.sql       -- User staging model
│   │   ├── stg_groups.sql      -- Group staging model
│   │   └── stg_org_units.sql   -- Organizational unit staging
│   ├── intermediate/    -- Business logic transformations
│   │   ├── int_user_groups.sql -- User-group relationships
│   │   └── int_org_hierarchy.sql -- Organizational hierarchy
│   └── marts/          -- Final analytics tables
│       ├── dim_users.sql       -- User dimension
│       ├── dim_groups.sql      -- Group dimension
│       └── fact_memberships.sql -- Membership facts
├── snapshots/          -- Historical tracking
│   └── ldap_entries_snapshot.sql -- LDAP entry snapshots
└── macros/            -- Reusable SQL functions
    ├── ldap_macros.sql         -- LDAP utility macros
    └── schema_mapping.sql      -- Schema transformation macros
```

### **LDAP Analytics Models**

- **Staging Models**: Raw LDAP data cleaning and standardization
- **Intermediate Models**: Business logic for relationships and hierarchies
- **Mart Models**: Dimensional models for analytics and reporting
- **Snapshot Models**: Historical tracking of LDAP entry changes
- **Macro Library**: Reusable transformations for LDAP-specific operations

---

## 🔧 PROJECT-SPECIFIC TECHNICAL DETAILS

### **Development Commands**

```bash
# MANDATORY: Always from workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate

# Core dbt development workflow
make install-dev       # Install dbt and development dependencies
make test              # Run dbt tests and data quality checks
make docs              # Generate and serve dbt documentation
make snapshot          # Create historical snapshots
make run               # Run all dbt models
make lint              # SQL linting and formatting

# dbt specific operations
dbt run                # Run all models
dbt test               # Run all tests
dbt docs generate && dbt docs serve  # Generate and serve documentation
dbt snapshot           # Create snapshots
```

### **LDAP Data Transformation Testing**

```bash
# Test staging models
dbt run --select staging.*
dbt test --select staging.*

# Test specific mart models
dbt run --select +dim_users
dbt test --select dim_users

# Test data lineage and dependencies
dbt run --select +fact_memberships
dbt test --select fact_memberships

# Test snapshots
dbt snapshot
dbt test --select snapshots.*
```

### **Analytics Model Validation**

```bash
# Test user dimension completeness
dbt test --select dim_users --vars '{"min_user_count": 1000}'

# Test group hierarchy integrity
dbt test --select dim_groups --vars '{"validate_hierarchy": true}'

# Test membership fact accuracy
dbt test --select fact_memberships --vars '{"validate_referential_integrity": true}'

# Test historical snapshots
dbt snapshot --select ldap_entries_snapshot
```

---

## 🚨 PROJECT-SPECIFIC KNOWN ISSUES

### **LDAP Data Transformation Challenges**

- **Schema Variability**: Different LDAP schemas requiring flexible transformation logic
- **Hierarchical Data Complexity**: Organizational hierarchy modeling in relational structures
- **Large Dataset Processing**: Millions of LDAP entries requiring efficient transformations
- **Change Detection**: Identifying and tracking changes in LDAP directory structure
- **Performance Optimization**: dbt model performance for large LDAP datasets

### **dbt LDAP Specific Considerations**

```sql
-- LDAP-specific dbt patterns
-- Macro for handling LDAP DN hierarchy
{% macro parse_ldap_dn(dn_column) %}
  case
    when {{ dn_column }} like 'cn=%,ou=users,%' then 'user'
    when {{ dn_column }} like 'cn=%,ou=groups,%' then 'group'
    when {{ dn_column }} like 'ou=%' then 'organizational_unit'
    else 'unknown'
  end as entry_type,

  regexp_extract({{ dn_column }}, r'cn=([^,]+)', 1) as common_name,
  regexp_extract({{ dn_column }}, r'ou=([^,]+)', 1) as organizational_unit,
  regexp_extract({{ dn_column }}, r'dc=([^,]+)', 1) as domain_component
{% endmacro %}

-- Macro for LDAP group membership flattening
{% macro flatten_ldap_memberships(member_column) %}
  select
    dn,
    trim(member_dn) as member_dn
  from {{ ref('stg_groups') }}
  cross join unnest(split({{ member_column }}, ';')) as t(member_dn)
  where {{ member_column }} is not null
    and trim(member_dn) != ''
{% endmacro %}

-- Incremental strategy for large LDAP datasets
{% macro ldap_incremental_strategy() %}
  {% if is_incremental() %}
    where modify_timestamp > (select max(modify_timestamp) from {{ this }})
  {% endif %}
{% endmacro %}
```

### **Production dbt LDAP Edge Cases**

```bash
# Common dbt LDAP transformation issues
1. Memory Issues: Large LDAP datasets causing dbt memory exhaustion
2. Schema Evolution: LDAP schema changes breaking existing models
3. Circular References: Group membership circular references in hierarchy
4. Performance Degradation: Slow transformations for millions of entries
5. Snapshot Conflicts: Snapshot merge conflicts with high-frequency changes
```

---

## 🎯 PROJECT-SPECIFIC SUCCESS METRICS

### **dbt Transformation Performance**

- **Model Execution Time**: <30 minutes for complete LDAP transformation
- **Data Quality Score**: 99.9% passing dbt tests for all models
- **Documentation Coverage**: 100% model and column documentation
- **Test Coverage**: 95% test coverage for all critical business logic
- **Incremental Performance**: <5 minutes for incremental model updates

### **LDAP Analytics Quality Goals**

- **Data Completeness**: 100% LDAP source data captured in marts
- **Referential Integrity**: 99.99% referential integrity across all models
- **Historical Accuracy**: Complete change tracking via snapshots
- **Performance Scalability**: Linear scaling with LDAP directory size
- **Business Logic Accuracy**: 100% accurate identity analytics calculations

---

## 🔗 PROJECT-SPECIFIC INTEGRATIONS

### **dbt Ecosystem Integration**

- **dbt Core**: Modern dbt patterns with latest features
- **Database Adapters**: Support for PostgreSQL, DuckDB, Snowflake
- **Documentation**: Complete dbt docs with lineage and testing
- **Testing Framework**: Comprehensive data quality testing

### **PyAuto Ecosystem Integration**

- **tap-ldap**: Primary data source for dbt LDAP transformations
- **target-ldap**: Output destination for transformed directory data
- **flext-ldap**: Integration with FLX LDAP migration workflows
- **ldap-core-shared**: Shared LDAP models and schema definitions

### **Enterprise Analytics Integration**

```sql
-- Production dbt LDAP configuration
-- dbt_project.yml
name: 'dbt_ldap'
version: '1.0.0'
profile: 'dbt_ldap'

model-paths: ["models"]
analysis-paths: ["analysis"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

target-path: "target"
clean-targets:
  - "target"
  - "dbt_packages"

models:
  dbt_ldap:
    staging:
      +materialized: table
      +schema: staging
    intermediate:
      +materialized: view
      +schema: intermediate
    marts:
      +materialized: table
      +schema: marts
      +post-hook: "grant select on {{ this }} to role reporting_role"

snapshots:
  dbt_ldap:
    +target_schema: snapshots
    +strategy: timestamp
    +updated_at: modify_timestamp

vars:
  ldap_base_dn: "dc=company,dc=com"
  user_object_class: "inetOrgPerson"
  group_object_class: "groupOfNames"
  enable_user_groups_flattening: true
  enable_org_hierarchy_validation: true
  snapshot_retention_days: 365
```

---

## 📊 PROJECT-SPECIFIC MONITORING

### **dbt LDAP Analytics Metrics**

```python
# Key metrics for dbt LDAP monitoring
DBT_LDAP_METRICS = {
    "model_execution_duration": "Time to execute all LDAP models",
    "test_success_rate": "Percentage of passing dbt tests",
    "data_freshness_score": "Freshness of LDAP source data",
    "transformation_accuracy": "Accuracy of LDAP transformations",
    "snapshot_size_growth": "Growth rate of historical snapshots",
    "documentation_coverage": "Percentage of documented models and columns",
}
```

### **LDAP Data Quality Monitoring**

```bash
# Comprehensive dbt LDAP monitoring
dbt test --store-failures --schema test_results
dbt run-operation test_data_quality --args '{"table": "dim_users"}'
dbt docs generate --target prod
```

---

## 📋 PROJECT-SPECIFIC MAINTENANCE

### **Regular Maintenance Tasks**

- **Daily**: Monitor dbt run performance and test results
- **Weekly**: Review data quality issues and optimize slow models
- **Monthly**: Update dbt version and refresh documentation
- **Quarterly**: Performance optimization and model architecture review

### **dbt Framework Updates**

```bash
# Keep dbt and adapters updated
pip install --upgrade dbt-core dbt-postgres dbt-duckdb

# Validate dbt project configuration
dbt debug
dbt parse
dbt compile
```

### **Emergency Procedures**

```bash
# dbt LDAP emergency troubleshooting
1. Test database connection: dbt debug --target prod
2. Validate model compilation: dbt compile --select failing_model
3. Check data freshness: dbt source freshness
4. Run specific model: dbt run --select +failing_model --full-refresh
5. Restore from snapshot: dbt snapshot --select ldap_entries_snapshot
```

---

**PROJECT SUMMARY**: Projeto dbt empresarial para transformação de dados LDAP com modelos dimensionais, análise de identidade, tracking histórico e analytics-ready tables para governança de diretório.

**CRITICAL SUCCESS FACTOR**: Manter transformações dbt eficientes e precisas para dados LDAP enterprise, garantindo qualidade de dados e performance para analytics de identidade corporativa.

---

_Última Atualização: 2025-06-26_  
_Próxima Revisão: Semanal durante transformações ativas_  
_Status: PRODUCTION READY - Transformações ativas de dados LDAP para analytics_
