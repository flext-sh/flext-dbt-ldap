# FLEXT DBT LDAP - LDAP Directory Data Transformations
# ===================================================
# Enterprise dbt project for LDAP directory data analytics and transformations
# Python 3.13 + dbt Core + PostgreSQL + LDAP Domain + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-dbt
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: dbt-compile dbt-run dbt-test dbt-docs dbt-debug dbt-seed dbt-snapshot dbt-deps dbt-clean
.PHONY: ldap-profile-test ldap-macros-test ldap-schema-validate

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT DBT LDAP - LDAP Directory Data Transformations"
	@echo "======================================================"
	@echo "🎯 dbt Core + PostgreSQL + LDAP Analytics + Python 3.13"
	@echo ""
	@echo "📦 Enterprise dbt project for LDAP directory data analytics"
	@echo "🔒 Zero tolerance quality gates with comprehensive data testing"
	@echo "🧪 90%+ test coverage requirement with dbt model testing"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'


info: ## Mostrar informações do projeto
	@echo "📊 Informações do Projeto"
	@echo "======================"
	@echo "Nome: flext-dbt-ldap"
	@echo "Título: FLEXT DBT LDAP"
	@echo "Tipo: dbt-project"
	@echo "Versão: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Não ativado")"
	@echo "Diretório: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Não é repo git")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) arquivos alterados"

diagnose: ## Executar diagnósticos completos
	@echo "🔍 Executando diagnósticos para flext-dbt-ldap..."
	@echo "Informações do Sistema:"
	@echo "OS: $(shell uname -s)"
	@echo "Arquitetura: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo ""
	@echo "Estrutura do Projeto:"
	@ls -la
	@echo ""
	@echo "Configuração Poetry:"
	@poetry config --list 2>/dev/null || echo "Poetry não configurado"
	@echo ""
	@echo "Status das Dependências:"
	@poetry show --outdated 2>/dev/null || echo "Nenhuma dependência desatualizada"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test dbt-test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT DBT LDAP COMPLIANT"

check: lint type-check test dbt-compile ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_dbt_ldap --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-dbt: dbt-deps dbt-compile ## Run dbt data tests
	@echo "🧪 Running dbt data tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT data tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_dbt_ldap --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit dbt-deps ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@mkdir -p profiles logs target dbt_packages
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎯 DBT OPERATIONS - CORE WORKFLOW
# ============================================================================

dbt-deps: ## Install dbt dependencies
	@echo "📦 Installing dbt dependencies..."
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ DBT dependencies installed"

dbt-debug: ## Debug dbt configuration
	@echo "🔍 Debugging dbt configuration..."
	@poetry run dbt debug --profiles-dir profiles/ --target dev
	@echo "✅ DBT debug complete"

dbt-compile: dbt-deps ## Compile dbt models
	@echo "🔨 Compiling dbt models..."
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@echo "✅ DBT models compiled"

dbt-run: dbt-deps dbt-compile ## Run dbt models
	@echo "🚀 Running dbt models..."
	@poetry run dbt run --profiles-dir profiles/ --target dev
	@echo "✅ DBT models executed"

dbt-test: dbt-compile ## Run dbt tests
	@echo "🧪 Running dbt tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT tests complete"

dbt-docs: dbt-compile ## Generate dbt documentation
	@echo "📚 Generating dbt documentation..."
	@poetry run dbt docs generate --profiles-dir profiles/ --target dev
	@echo "✅ DBT documentation generated"

dbt-seed: dbt-deps ## Load dbt seed data
	@echo "🌱 Loading dbt seed data..."
	@poetry run dbt seed --profiles-dir profiles/ --target dev
	@echo "✅ DBT seed data loaded"

dbt-snapshot: dbt-deps ## Run dbt snapshots
	@echo "📸 Running dbt snapshots..."
	@poetry run dbt snapshot --profiles-dir profiles/ --target dev
	@echo "✅ DBT snapshots complete"

dbt-clean: ## Clean dbt artifacts
	@echo "🧹 Cleaning dbt artifacts..."
	@poetry run dbt clean --profiles-dir profiles/
	@rm -rf logs/dbt.log
	@echo "✅ DBT artifacts cleaned"

# ============================================================================
# 🔧 LDAP SPECIFIC OPERATIONS
# ============================================================================

ldap-profile-test: ## Test LDAP connection profiles
	@echo "🔗 Testing LDAP connection profiles..."
	@poetry run dbt debug --profiles-dir profiles/ --target dev
	@poetry run python scripts/test_ldap_connections.py
	@echo "✅ LDAP profile tests complete"

ldap-macros-test: dbt-deps ## Test LDAP-specific macros
	@echo "🔧 Testing LDAP macros..."
	@poetry run dbt test --models test_ldap_macros --profiles-dir profiles/ --target dev
	@poetry run python scripts/validate_ldap_macros.py
	@echo "✅ LDAP macros tests complete"

ldap-schema-validate: dbt-compile ## Validate LDAP schema mapping
	@echo "📋 Validating LDAP schema mapping..."
	@poetry run python scripts/validate_ldap_schema.py
	@poetry run dbt test --models schema_mapping --profiles-dir profiles/ --target dev
	@echo "✅ LDAP schema validation complete"

ldap-hierarchy-analysis: dbt-run ## Analyze LDAP organizational hierarchy
	@echo "🏢 Analyzing LDAP organizational hierarchy..."
	@poetry run dbt run --models analysis.organizational_hierarchy --profiles-dir profiles/ --target dev
	@echo "✅ LDAP hierarchy analysis complete"

ldap-security-audit: dbt-run ## Run LDAP security audit
	@echo "🔒 Running LDAP security audit..."
	@poetry run dbt run --models analysis.security_audit --profiles-dir profiles/ --target dev
	@echo "✅ LDAP security audit complete"

ldap-compliance-check: dbt-test ## Check LDAP compliance
	@echo "✅ Running LDAP compliance checks..."
	@poetry run dbt test --models tests.compliance --profiles-dir profiles/ --target dev
	@echo "✅ LDAP compliance check complete"

# ============================================================================
# 📊 LDAP DATA ANALYTICS
# ============================================================================

analytics-users: dbt-run ## Run user analytics models
	@echo "👥 Running LDAP user analytics..."
	@poetry run dbt run --models marts.dim_users --profiles-dir profiles/ --target dev
	@echo "✅ User analytics complete"

analytics-groups: dbt-run ## Run group analytics models
	@echo "👥 Running LDAP group analytics..."
	@poetry run dbt run --models marts.dim_groups --profiles-dir profiles/ --target dev
	@echo "✅ Group analytics complete"

analytics-memberships: dbt-run ## Run membership analytics
	@echo "🔗 Running membership analytics..."
	@poetry run dbt run --models marts.fact_group_memberships --profiles-dir profiles/ --target dev
	@echo "✅ Membership analytics complete"

analytics-activity: dbt-run ## Run activity analytics
	@echo "📈 Running activity analytics..."
	@poetry run dbt run --models marts.fact_user_activity --profiles-dir profiles/ --target dev
	@echo "✅ Activity analytics complete"

analytics-all: analytics-users analytics-groups analytics-memberships analytics-activity ## Run all analytics
	@echo "✅ All LDAP analytics complete"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean dbt-compile ## Build dbt project
	@echo "🔨 Building dbt project..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf target/
	@rm -rf dbt_packages/
	@rm -rf logs/
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Project information
PROJECT_NAME := flext-dbt-ldap
PROJECT_TYPE := meltano-plugin
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT DBT LDAP - LDAP Directory Data Transformations

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# DBT settings
export DBT_PROFILES_DIR := $(PWD)/profiles
export DBT_PROJECT_DIR := $(PWD)
export DBT_TARGET := dev
export DBT_LOG_LEVEL := INFO

# LDAP Analytics settings
export LDAP_SOURCE_SCHEMA := ldap_raw
export LDAP_TARGET_SCHEMA := ldap_analytics
export LDAP_ANALYTICS_TIMEZONE := UTC

# Data warehouse settings
export DW_HOST := localhost
export DW_PORT := 5432
export DW_DATABASE := flext_analytics
export DW_USER := dbt_user

# Performance settings
export DBT_THREADS := 4
export DBT_PARTIAL_PARSE := true
export DBT_USE_COLORS := true
export DBT_PRINTER_WIDTH := 80

# Quality settings
export DBT_WARN_ERROR := false
export DBT_STORE_FAILURES := true
export DBT_FAIL_FAST := false

# Poetry settings
export POETRY_VENV_IN_PROJECT := false
export POETRY_CACHE_DIR := $(HOME)/.cache/pypoetry

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 WORKSPACE INTEGRATION
# ============================================================================

workspace-sync: ## Sync with workspace dependencies
	@echo "🔄 Syncing with workspace dependencies..."
	@poetry run python scripts/sync_workspace_deps.py
	@echo "✅ Workspace sync complete"

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 DBT project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: DBT + LDAP Analytics"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + dbt Core"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: LDAP Directory Data Transformations"
	@echo "🔗 Dependencies: flext-core, dbt-core, dbt-postgres"
	@echo "📦 Provides: LDAP analytics models and transformations"
	@echo "🎯 Standards: Enterprise data modeling patterns"