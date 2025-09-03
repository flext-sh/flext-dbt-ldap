# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

flext-dbt-ldap is an enterprise-grade dbt project for LDAP directory data transformations. It provides comprehensive data models, transformations, and analytics for LDAP/Active Directory environments using dbt Core with PostgreSQL/DuckDB backends.

## Architecture

### dbt Project Structure

- **Staging Models** (`models/staging/`): Raw LDAP data transformation and cleansing
- **Intermediate Models** (`models/intermediate/`): Business logic and data enrichment
- **Marts Models** (`models/marts/`): Final dimensional/fact tables for analytics
- **Macros** (`macros/`): LDAP-specific dbt macros and utility functions
- **Snapshots** (`snapshots/`): Historical tracking of LDAP entries
- **Tests** (`tests/`): Data quality and validation tests

### Python Components (`src/flext_dbt_ldap/`)

- **ldap_integration.py**: LDAP connectivity and data extraction
- **models.py**: Pydantic models for LDAP entities
- **macros.py**: Python-based macro helpers
- **simple_api.py**: Simple API for dbt model execution
- **infrastructure/**: Dependency injection and service configuration

## TODO: GAPS DE ARQUITETURA IDENTIFICADOS - PRIORIDADE ALTA

### 🚨 GAP 1: DBT-Python Integration Complexity

**Status**: ALTO - Hybrid dbt-Python architecture pode ser over-engineered
**Problema**:

- Python components em dbt project pode criar maintenance overhead
- LDAP integration logic duplicated com flext-ldap library
- DI container em dbt project pode be overkill

**TODO**:

- [ ] Simplify dbt-Python integration architecture
- [ ] Leverage flext-ldap library mais efficiently
- [ ] Review need para DI container em dbt context
- [ ] Document integration patterns clearly

### 🚨 GAP 2: LDAP Library Integration Optimization

**Status**: ALTO - Integration com flext-ldap pode não be optimal
**Problema**:

- ldap_integration.py pode duplicate flext-ldap functionality
- LDAP connectivity patterns podem divergir between projects
- DN parsing logic pode be duplicated

**TODO**:

- [ ] Optimize integration com flext-ldap library
- [ ] Eliminate duplication de LDAP functionality
- [ ] Align LDAP connectivity patterns
- [ ] Consolidate DN parsing logic

### 🚨 GAP 3: Meltano Integration Gap

**Status**: ALTO - Integration com flext-meltano não clearly defined
**Problema**:

- dbt project relationship com Singer ecosystem não clear
- Integration com flext-tap-ldap patterns podem be suboptimal
- Data flow from taps → dbt → targets não fully documented

**TODO**:

- [ ] Define clear integration patterns com flext-meltano
- [ ] Document data flow from Singer taps to dbt models
- [ ] Optimize integration com flext-tap-ldap e flext-tap-ldif
- [ ] Create integrated pipeline documentation

## Technology Stack

- **dbt Core**: Data transformation framework
- **Python 3.13**: Runtime with Poetry dependency management
- **PostgreSQL/DuckDB**: Data warehouse backends
- **FLEXT Libraries**: flext-core, flext-ldap, flext-observability
- **Testing**: pytest with 90%+ coverage requirement

## Essential Commands for Development

### Most Common Development Workflow

```bash
# Setup (first time only)
make setup            # Complete development setup
poetry install        # Install dependencies

# Daily development cycle
make check            # Essential checks (lint + type + test + dbt-compile)
make dbt-run          # Execute dbt models
make dbt-test         # Run dbt data quality tests

# Before committing (mandatory)
make validate         # Complete validation (lint + type + security + test + dbt-test)
```

### Essential Quality Gates (Must Pass)

```bash
make validate          # Complete validation (lint + type + security + test + dbt-test)
make check            # Essential checks (lint + type + test + dbt-compile)
make test             # Run pytest with 90% coverage minimum
make dbt-test         # Run dbt data quality tests
```

### dbt Operations

```bash
# Core dbt workflow
make dbt-deps         # Install dbt dependencies
make dbt-debug        # Debug dbt configuration and connections
make dbt-compile      # Compile dbt models without execution
make dbt-run          # Execute dbt models
make dbt-test         # Run dbt data tests
make dbt-docs         # Generate dbt documentation

# Data operations
make dbt-seed         # Load seed data
make dbt-snapshot     # Run snapshot models
make dbt-clean        # Clean dbt artifacts

# Full dbt workflow (deps -> compile -> run -> test)
make dbt-deps dbt-compile dbt-run dbt-test
```

### LDAP-Specific Operations

```bash
make ldap-profile-test       # Test LDAP connection profiles
make ldap-macros-test        # Test LDAP-specific macros
make ldap-schema-validate    # Validate LDAP schema mapping
make ldap-hierarchy-analysis # Analyze organizational hierarchy
make ldap-security-audit     # Run LDAP security audit
make ldap-compliance-check   # Check LDAP compliance
```

### Analytics Operations

```bash
make analytics-users         # Run user analytics models
make analytics-groups        # Run group analytics models
make analytics-memberships   # Run membership analytics
make analytics-activity      # Run activity analytics
make analytics-all          # Run all analytics models
```

### Development Setup

```bash
make setup              # Complete development setup
make install            # Install dependencies with Poetry
make dev-install        # Development environment setup
make pre-commit         # Setup pre-commit hooks

# Quality and formatting
make lint               # Ruff linting (ALL rules enabled)
make type-check         # MyPy strict type checking
make security           # Security scans (bandit + pip-audit)
make format             # Format code with ruff
make fix                # Auto-fix all issues
```

### Testing

```bash
# Python tests
make test-unit          # Unit tests only
make test-integration   # Integration tests only
make coverage           # Generate coverage report
make coverage-html      # Generate HTML coverage report

# Test with specific markers
poetry run pytest -m unit                    # Unit tests
poetry run pytest -m integration             # Integration tests
poetry run pytest -m e2e                     # End-to-end tests
poetry run pytest -m dbt                     # dbt-specific tests
poetry run pytest -m ldap                    # LDAP integration tests
poetry run pytest -m transformation          # Data transformation tests
poetry run pytest -m validation              # Data validation tests
poetry run pytest -m performance             # Performance tests
poetry run pytest -m slow                    # Slow tests
poetry run pytest -m "not slow"              # Exclude slow tests
```

## Project Configuration

### dbt Profiles

- **Dev Target**: DuckDB (`./target/ldap_transform.db`)
- **Prod Target**: PostgreSQL with environment variables
- **Profile Name**: `flext_ldap` (configured in `dbt_project.yml`)

### Environment Variables

```bash
# dbt Configuration
export DBT_PROFILES_DIR=$(PWD)/profiles
export DBT_TARGET=dev
export DBT_THREADS=4

# LDAP Analytics
export LDAP_SOURCE_SCHEMA=ldap_raw
export LDAP_TARGET_SCHEMA=ldap_analytics
export LDAP_ANALYTICS_TIMEZONE=UTC

# Data Warehouse (Prod)
export DW_HOST=localhost
export DW_PORT=5432
export DW_DATABASE=flext_analytics
export DW_USER=dbt_user
```

### dbt Variables

```yaml
# Configured in dbt_project.yml
ldap_base_dn: "dc=example,dc=com"
ldap_user_base: "ou=users"
ldap_group_base: "ou=groups"
ldap_ou_base: "ou=departments"
```

### Key Files and Their Purpose

- **dbt_project.yml**: dbt project configuration with LDAP-specific variables
- **profiles.yml**: Database connection profiles (dev: DuckDB, prod: PostgreSQL)
- **Makefile**: Development commands and quality gates
- **pyproject.toml**: Python dependencies and tool configuration
- **src/flext_dbt_ldap/**init**.py**: Main module exports and FLEXT ecosystem integration
- **macros/ldap_macros.sql**: LDAP-specific dbt macros for DN parsing and attribute handling
- **models/**: dbt models organized in staging → intermediate → marts layers
- **tests/**: Python unit/integration tests and dbt SQL tests

## Data Models Architecture

### Staging Layer (`models/staging/`)

- **stg_users**: User entries with basic transformations
- **stg_groups**: Group entries with member processing
- **stg_org_units**: Organizational unit hierarchy

### Intermediate Layer (`models/intermediate/`)

- **int_org_hierarchy**: Organizational hierarchy enrichment
- **int_user_groups**: User-group relationship processing

### Marts Layer (`models/marts/`)

- **dim_users**: User dimension table
- **dim_groups**: Group dimension table
- **fact_memberships**: Group membership facts

## LDAP-Specific Macros

### DN (Distinguished Name) Processing

```sql
{{ parse_dn('dn_column') }}                    -- Parse DN components
{{ extract_ou_from_dn('dn_column') }}          -- Extract OU from DN
{{ is_under_base('dn_column', 'base_dn') }}    -- Check if DN under base
```

### Attribute Processing

```sql
{{ normalize_array_field('field_name') }}      -- Normalize multi-valued fields
{{ count_group_members('member_field') }}      -- Count group members
{{ extract_email_domain('email_field') }}      -- Extract email domain
```

### Timestamp Conversion

```sql
{{ ldap_timestamp_to_timestamp('timestamp_field') }}  -- Convert LDAP timestamps
```

### Hierarchy Operations

```sql
{{ generate_hierarchy_path('dn_column') }}     -- Generate hierarchy path
```

## Testing Strategy

### Data Quality Tests

- **Source Tests**: Validate raw LDAP data integrity
- **Model Tests**: Ensure transformation accuracy
- **Generic Tests**: unique, not_null, accepted_values
- **Custom Tests**: LDAP-specific validation rules

### Test Categories

- **Unit**: Individual function/macro testing
- **Integration**: LDAP connection and data extraction
- **dbt**: Model compilation and execution
- **E2E**: Full pipeline testing
- **Performance**: Large dataset processing
- **Validation**: Business rule compliance

### Coverage Requirements

- **Python Code**: 90% minimum coverage
- **dbt Models**: All models must have tests
- **LDAP Macros**: Comprehensive test coverage

## Common Workflows

### Adding New LDAP Source

1. Update `models/staging/schema.yml` with source definition
2. Create staging model in `models/staging/stg_<source>.sql`
3. Add appropriate tests and documentation
4. Create corresponding intermediate/marts models
5. Run `make dbt-compile dbt-test` to validate

### Creating Custom LDAP Macro

1. Add macro to `macros/ldap_macros.sql`
2. Follow existing patterns for DN/attribute processing
3. Add tests in `tests/test_macros.sql`
4. Run `make ldap-macros-test` to validate

### Performance Optimization

1. Use appropriate materialization strategies
2. Implement incremental models for large datasets
3. Add indexes and partitioning in target warehouse
4. Monitor with `make analytics-all` performance

## Data Quality Standards

### LDAP Data Validation

- **DN Format**: Must follow RFC 4514 format
- **Email Validation**: RFC 5322 compliant addresses
- **Required Attributes**: cn, objectClass for all entries
- **Object Classes**: Validate against LDAP schema
- **Referential Integrity**: Member DNs must exist in users

### Business Rules

- **Unique Constraints**: DN, uid, email uniqueness
- **Account Types**: Employee, Service, Application, Standard
- **Group Categories**: Security vs Distribution groups
- **OU Hierarchy**: Valid organizational structure

## Integration Points

### FLEXT Ecosystem

- **flext-core**: Base patterns and ServiceResult handling
- **flext-ldap**: LDAP connectivity and DN parsing
- **flext-observability**: Monitoring and metrics
- **flext-meltano**: Integration with Singer taps/targets

### Data Sources

- **Raw LDAP**: Via flext-tap-ldap
- **LDIF Files**: Via flext-tap-ldif
- **Oracle WMS**: Via flext-tap-oracle-wms

### Output Targets

- **PostgreSQL**: Production data warehouse
- **DuckDB**: Development and testing
- **Analytics Tools**: BI dashboards and reporting

## Current Development Status & Limitations

### Known Issues & Workarounds

- **dbt Profile**: Currently uses `dbt_ldap` profile name (check profiles.yml vs dbt_project.yml)
- **Python Integration**: Hybrid dbt-Python architecture may need simplification
- **LDAP Macros**: Some macros reference undefined functions (ldap_timestamp_to_timestamp, validate_dn_format)
- **Test Coverage**: Python tests exist but may need DBT model integration tests

### Architecture Gaps Identified

1. **Integration with flext-ldap**: May have code duplication - leverage flext-ldap library more efficiently
2. **Meltano Integration**: Data flow from Singer taps → dbt → targets needs clearer documentation
3. **Python Components**: DI container in dbt project may be over-engineered for this use case

## Troubleshooting

### Common dbt Issues

```bash
# Connection problems
make dbt-debug                    # Check profiles and connections

# Compilation errors
make dbt-compile                  # Test model compilation
poetry run dbt compile --select model_name

# Test failures
make dbt-test                     # Run all dbt tests
poetry run dbt test --select model_name

# Performance issues
poetry run dbt run --select model_name --full-refresh
```

### Python Integration Issues

```bash
# Import errors
poetry run python -c "import flext_dbt_ldap"

# Dependency conflicts
poetry show --tree
poetry update

# LDAP connection issues
make ldap-profile-test
```

### Quality Gate Failures

```bash
# Fix linting automatically
make format

# Type checking issues
poetry run mypy src/ --show-error-codes

# Security vulnerabilities
poetry run pip-audit --fix

# Test coverage below 90%
make coverage-html  # View detailed coverage report
```

### dbt Model Development Workflow

```bash
# Develop new model
1. Create SQL file in appropriate layer (staging/intermediate/marts)
2. Add model documentation to schema.yml
3. Add tests (generic + custom) to schema.yml
4. Compile and test: make dbt-compile && make dbt-test
5. Run specific model: poetry run dbt run --select +model_name
6. Validate with: make validate
```

### Testing Individual Models

```bash
# Test specific model
poetry run dbt test --select model_name

# Test model with dependencies
poetry run dbt test --select +model_name

# Run model and test
poetry run dbt run --select model_name && poetry run dbt test --select model_name

# Test with fresh rebuild
poetry run dbt run --select model_name --full-refresh
```

## Best Practices

### dbt Model Development

- Use staging -> intermediate -> marts layering
- Implement incremental models for large datasets
- Add comprehensive tests and documentation
- Follow consistent naming conventions

### LDAP Data Handling

- Always validate DN formats
- Handle multi-valued attributes properly
- Implement proper error handling for missing data
- Use LDAP-specific macros consistently

### Performance Considerations

- Use appropriate materialization strategies
- Implement proper indexing in target warehouse
- Monitor transformation performance
- Use incremental strategies for large datasets

### Code Quality

- Maintain 90%+ test coverage
- Follow strict typing with MyPy
- Use comprehensive linting with Ruff
- Implement proper error handling patterns
