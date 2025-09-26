# =============================================================================
# FLEXT-DBT-LDAP - LDAP Directory Data Transformations Makefile
# =============================================================================
# DBT 1.7+ | Python 3.13 | LDAP Analytics - Clean Architecture + DDD + Zero Tolerance
# =============================================================================

# Project Configuration
PROJECT_NAME := flext-dbt-ldap
PYTHON_VERSION := 3.13
POETRY := poetry
SRC_DIR := src
TESTS_DIR := tests
COV_DIR := flext_dbt_ldap

# Quality Standards
MIN_COVERAGE := 100

# DBT Configuration
DBT_PROFILES_DIR := profiles
DBT_TARGET := dev
DBT_THREADS := 4

# Export Configuration
export PROJECT_NAME PYTHON_VERSION MIN_COVERAGE DBT_PROFILES_DIR DBT_TARGET DBT_THREADS

# =============================================================================
# HELP & INFORMATION
# =============================================================================

.PHONY: help
help: ## Show available commands
	@echo "FLEXT-DBT-LDAP - LDAP Directory Data Transformations"
	@echo "==================================================="
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \\\\033[36m%-20s\\\\033[0m %s\\\\n", $$1, $$2}'

.PHONY: info
info: ## Show project information
	@echo "Project: $(PROJECT_NAME)"
	@echo "Python: $(PYTHON_VERSION)+"
	@echo "Poetry: $(POETRY)"
	@echo "Coverage: $(MIN_COVERAGE)% minimum (MANDATORY)"
	@echo "DBT Profiles Dir: $(DBT_PROFILES_DIR)"
	@echo "DBT Target: $(DBT_TARGET)"
	@echo "DBT Threads: $(DBT_THREADS)"
	@echo "Architecture: Clean Architecture + DDD + DBT + LDAP Analytics"

# =============================================================================
# SETUP & INSTALLATION
# =============================================================================

.PHONY: install
install: ## Install dependencies
	$(POETRY) install

.PHONY: install-dev
install-dev: ## Install dev dependencies
	$(POETRY) install --with dev,test,docs

.PHONY: setup
setup: install-dev ## Complete development setup
	mkdir -p $(DBT_PROFILES_DIR) logs target dbt_packages
	$(POETRY) run pre-commit install

# =============================================================================
# QUALITY GATES (MANDATORY - ZERO TOLERANCE)
# =============================================================================

.PHONY: validate
validate: lint type-check security test dbt-test ## Run all quality gates

.PHONY: check
check: lint type-check dbt-compile ## Quick health check

.PHONY: lint
lint: ## Run linting (ZERO TOLERANCE)
	$(POETRY) run ruff check .

.PHONY: format
format: ## Format code
	$(POETRY) run ruff format .

.PHONY: type-check
type-check: ## Run type checking with Pyrefly (ZERO TOLERANCE)
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pyrefly check .

.PHONY: security
security: ## Run security scanning
	$(POETRY) run bandit -r $(SRC_DIR)
	$(POETRY) run pip-audit

.PHONY: fix
fix: ## Auto-fix code issues
	$(POETRY) run ruff check . --fix
	$(POETRY) run ruff format .

# =============================================================================
# TESTING (MANDATORY - 100% COVERAGE)
# =============================================================================

.PHONY: test
test: ## Run tests with 100% coverage (MANDATORY)
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -q --maxfail=10000 --cov=$(COV_DIR) --cov-report=term-missing:skip-covered --cov-fail-under=$(MIN_COVERAGE)

.PHONY: test-unit
test-unit: ## Run unit tests only
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -m "not integration" -v

.PHONY: test-integration
test-integration: ## Run integration tests with Docker only
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -m integration -v

.PHONY: test-dbt
test-dbt: ## Run dbt-specific tests
	$(POETRY) run pytest $(TESTS_DIR) -m dbt -v

.PHONY: test-ldap
test-ldap: ## Run LDAP integration tests
	$(POETRY) run pytest $(TESTS_DIR) -m ldap -v

.PHONY: test-e2e
test-e2e: ## Run end-to-end tests
	$(POETRY) run pytest $(TESTS_DIR) -m e2e -v

.PHONY: test-fast
test-fast: ## Run tests without coverage
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -v

.PHONY: coverage-html
coverage-html: ## Generate HTML coverage report
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest --cov=$(COV_DIR) --cov-report=html

# =============================================================================
# BUILD & DISTRIBUTION
# =============================================================================

.PHONY: build
build: dbt-compile ## Build package
	$(POETRY) build

.PHONY: build-clean
build-clean: clean build ## Clean and build

# =============================================================================
# DBT OPERATIONS
# =============================================================================

.PHONY: dbt-deps
dbt-deps: ## Install dbt dependencies
	$(POETRY) run dbt deps --profiles-dir $(DBT_PROFILES_DIR)

.PHONY: dbt-debug
dbt-debug: ## Debug dbt configuration
	$(POETRY) run dbt debug --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-compile
dbt-compile: dbt-deps ## Compile dbt models
	$(POETRY) run dbt compile --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-run
dbt-run: dbt-compile ## Run dbt models
	$(POETRY) run dbt run --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-test
dbt-test: dbt-compile ## Run dbt tests
	$(POETRY) run dbt test --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-docs
dbt-docs: dbt-compile ## Generate dbt documentation
	$(POETRY) run dbt docs generate --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-seed
dbt-seed: dbt-deps ## Load seed data
	$(POETRY) run dbt seed --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-snapshot
dbt-snapshot: dbt-deps ## Run snapshots
	$(POETRY) run dbt snapshot --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: dbt-clean
dbt-clean: ## Clean dbt artifacts
	$(POETRY) run dbt clean --profiles-dir $(DBT_PROFILES_DIR)
	rm -rf logs/dbt.log

# =============================================================================
# LDAP-SPECIFIC OPERATIONS
# =============================================================================

.PHONY: ldap-validate
ldap-validate: dbt-compile ## Validate LDAP schema mappings
	$(POETRY) run dbt test --models tag:schema_mapping --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: ldap-macros
ldap-macros: dbt-deps ## Test LDAP macros
	$(POETRY) run dbt test --models tag:ldap_macros --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

.PHONY: ldap-analytics
ldap-analytics: dbt-run ## Run LDAP analytics models
	$(POETRY) run dbt run --models tag:analytics --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

# =============================================================================
# DOCUMENTATION
# =============================================================================

.PHONY: docs
docs: dbt-docs ## Build all documentation
	$(POETRY) run mkdocs build

.PHONY: docs-serve
docs-serve: ## Serve documentation locally
	$(POETRY) run mkdocs serve

# =============================================================================
# DEPENDENCIES
# =============================================================================

.PHONY: deps-update
deps-update: ## Update all dependencies
	$(POETRY) update
	$(POETRY) run dbt deps --profiles-dir $(DBT_PROFILES_DIR)

.PHONY: deps-show
deps-show: ## Show dependency tree
	$(POETRY) show --tree

.PHONY: deps-audit
deps-audit: ## Security audit dependencies
	$(POETRY) run pip-audit

# =============================================================================
# DEVELOPMENT
# =============================================================================

.PHONY: shell
shell: ## Open Python shell
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python

.PHONY: pre-commit
pre-commit: ## Run pre-commit hooks
	$(POETRY) run pre-commit run --all-files

# =============================================================================
# MAINTENANCE
# =============================================================================

.PHONY: clean
clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ htmlcov/ .coverage .mypy_cache/ .pyrefly_cache/ .ruff_cache/
	rm -rf target/ dbt_packages/ logs/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

.PHONY: clean-all
clean-all: clean ## Deep clean including venv
	rm -rf .venv/

.PHONY: reset
reset: clean-all setup ## Complete project reset

# =============================================================================
# DIAGNOSTICS
# =============================================================================

.PHONY: diagnose
diagnose: ## Show environment diagnostics
	@echo "Python: $$(python --version)"
	@echo "Poetry: $$($(POETRY) --version)"
	@echo "DBT: $$($(POETRY) run dbt --version)"
	@echo "LDAP Processor: $$(PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c 'import flext_dbt_ldap; print(getattr(flext_dbt_ldap, \"__version__\", \"dev\"))' 2>/dev/null || echo 'Not available')"
	@$(POETRY) env info

.PHONY: doctor
doctor: diagnose check ## Full health check

# =============================================================================

# =============================================================================

.PHONY: t l f tc c i v dr dt dc la lv
t: test
l: lint
f: format
tc: type-check
c: clean
i: install
v: validate
dr: dbt-run
dt: dbt-test
dc: dbt-compile
la: ldap-analytics
lv: ldap-validate

# =============================================================================
# CONFIGURATION
# =============================================================================

.DEFAULT_GOAL := help

.PHONY: help install install-dev setup validate check lint format type-check security fix test test-unit test-integration test-dbt test-ldap test-e2e test-fast coverage-html build build-clean dbt-deps dbt-debug dbt-compile dbt-run dbt-test dbt-docs dbt-seed dbt-snapshot dbt-clean ldap-validate ldap-macros ldap-analytics docs docs-serve deps-update deps-show deps-audit shell pre-commit clean clean-all reset diagnose doctor t l f tc c i v dr dt dc la lv
