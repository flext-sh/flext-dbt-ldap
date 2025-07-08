# =============================================================================
# FLEXT DBT LDAP - MAKEFILE
# PEP Strict Compliance with Poetry Build System - dbt Models
# =============================================================================

.DEFAULT_GOAL := help
SHELL := /bin/bash

# Project Configuration
PROJECT_NAME := flext-dbt-ldap
PYTHON_VERSION := 3.13
SOURCE_DIR := src
TESTS_DIR := tests
REPORTS_DIR := reports
MODULE_NAME := dbt_ldap
DBT_PROJECT_DIR := dbt_project

# Colors for output
CYAN := \\033[0;36m
GREEN := \\033[0;32m
YELLOW := \\033[1;33m
RED := \\033[0;31m
NC := \\033[0m # No Color

# =============================================================================
# HELP SYSTEM
# =============================================================================

.PHONY: help
help: ## Show this help message
	@echo -e "$(CYAN)$(PROJECT_NAME) - dbt LDAP Models Development Commands$(NC)"
	@echo -e "$(CYAN)====================================================$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(GREEN)%-20s$(NC) %s\\n", $$1, $$2}' $(MAKEFILE_LIST)

# =============================================================================
# ENVIRONMENT SETUP
# =============================================================================

.PHONY: install
install: ## Install project dependencies with Poetry
	@echo -e "$(CYAN)Installing project dependencies...$(NC)"
	poetry install --all-extras
	poetry run pre-commit install
	@echo -e "$(GREEN)✓ Installation complete$(NC)"

.PHONY: install-dev
install-dev: ## Install development dependencies
	@echo -e "$(CYAN)Installing development dependencies...$(NC)"
	poetry install --with dev,security,build,test
	poetry run pre-commit install
	@echo -e "$(GREEN)✓ Development installation complete$(NC)"

.PHONY: update
update: ## Update all dependencies
	@echo -e "$(CYAN)Updating dependencies...$(NC)"
	poetry update
	@echo -e "$(GREEN)✓ Dependencies updated$(NC)"

.PHONY: lock
lock: ## Generate poetry.lock file
	@echo -e "$(CYAN)Generating lock file...$(NC)"
	poetry lock --no-update
	@echo -e "$(GREEN)✓ Lock file generated$(NC)"

# =============================================================================
# CODE QUALITY - PEP STRICT COMPLIANCE
# =============================================================================

.PHONY: format
format: ## Format code with black and isort
	@echo -e "$(CYAN)Formatting code...$(NC)"
	poetry run black $(SOURCE_DIR) $(TESTS_DIR)
	poetry run isort $(SOURCE_DIR) $(TESTS_DIR)
	@echo -e "$(GREEN)✓ Code formatted$(NC)"

.PHONY: lint
lint: ## Run all linters (ruff, mypy, bandit)
	@echo -e "$(CYAN)Running linters...$(NC)"
	poetry run ruff check $(SOURCE_DIR) $(TESTS_DIR)
	poetry run mypy $(SOURCE_DIR)
	poetry run bandit -r $(SOURCE_DIR)
	@echo -e "$(GREEN)✓ Linting complete$(NC)"

.PHONY: lint-fix
lint-fix: ## Run linters with auto-fix
	@echo -e "$(CYAN)Running linters with auto-fix...$(NC)"
	poetry run ruff check --fix $(SOURCE_DIR) $(TESTS_DIR)
	poetry run black $(SOURCE_DIR) $(TESTS_DIR)
	poetry run isort $(SOURCE_DIR) $(TESTS_DIR)
	@echo -e "$(GREEN)✓ Linting and formatting complete$(NC)"

.PHONY: type-check
type-check: ## Run type checking with mypy
	@echo -e "$(CYAN)Running type checks...$(NC)"
	poetry run mypy $(SOURCE_DIR)
	@echo -e "$(GREEN)✓ Type checking complete$(NC)"

.PHONY: security
security: ## Run security checks
	@echo -e "$(CYAN)Running security checks...$(NC)"
	poetry run bandit -r $(SOURCE_DIR)
	poetry run safety check
	@echo -e "$(GREEN)✓ Security checks complete$(NC)"

# =============================================================================
# TESTING
# =============================================================================

.PHONY: test
test: ## Run all tests with coverage
	@echo -e "$(CYAN)Running tests...$(NC)"
	mkdir -p $(REPORTS_DIR)
	poetry run pytest
	@echo -e "$(GREEN)✓ Tests complete$(NC)"

.PHONY: test-unit
test-unit: ## Run unit tests only
	@echo -e "$(CYAN)Running unit tests...$(NC)"
	poetry run pytest -m "unit" -v
	@echo -e "$(GREEN)✓ Unit tests complete$(NC)"

.PHONY: test-integration
test-integration: ## Run integration tests only
	@echo -e "$(CYAN)Running integration tests...$(NC)"
	poetry run pytest -m "integration" -v
	@echo -e "$(GREEN)✓ Integration tests complete$(NC)"

.PHONY: test-dbt
test-dbt: ## Run dbt tests only
	@echo -e "$(CYAN)Running dbt tests...$(NC)"
	poetry run pytest -m "dbt" -v
	@echo -e "$(GREEN)✓ dbt tests complete$(NC)"

.PHONY: test-ldap
test-ldap: ## Run LDAP tests only
	@echo -e "$(CYAN)Running LDAP tests...$(NC)"
	poetry run pytest -m "ldap" -v
	@echo -e "$(GREEN)✓ LDAP tests complete$(NC)"

.PHONY: test-models
test-models: ## Run model tests only
	@echo -e "$(CYAN)Running model tests...$(NC)"
	poetry run pytest -m "models" -v
	@echo -e "$(GREEN)✓ Model tests complete$(NC)"

.PHONY: test-macros
test-macros: ## Run macro tests only
	@echo -e "$(CYAN)Running macro tests...$(NC)"
	poetry run pytest -m "macros" -v
	@echo -e "$(GREEN)✓ Macro tests complete$(NC)"

.PHONY: test-e2e
test-e2e: ## Run end-to-end tests only
	@echo -e "$(CYAN)Running E2E tests...$(NC)"
	poetry run pytest -m "e2e" -v
	@echo -e "$(GREEN)✓ E2E tests complete$(NC)"

.PHONY: test-watch
test-watch: ## Run tests in watch mode
	@echo -e "$(CYAN)Running tests in watch mode...$(NC)"
	poetry run pytest-watch

.PHONY: coverage
coverage: ## Generate coverage report
	@echo -e "$(CYAN)Generating coverage report...$(NC)"
	mkdir -p $(REPORTS_DIR)
	poetry run pytest --cov=$(SOURCE_DIR) --cov-report=html:$(REPORTS_DIR)/coverage --cov-report=term-missing
	@echo -e "$(GREEN)✓ Coverage report generated: $(REPORTS_DIR)/coverage/index.html$(NC)"

# =============================================================================
# DBT OPERATIONS
# =============================================================================

.PHONY: dbt-init
dbt-init: ## Initialize dbt project
	@echo -e "$(CYAN)Initializing dbt project...$(NC)"
	mkdir -p $(DBT_PROJECT_DIR)
	poetry run dbt init --project-dir $(DBT_PROJECT_DIR)
	@echo -e "$(GREEN)✓ dbt project initialized$(NC)"

.PHONY: dbt-debug
dbt-debug: ## Debug dbt configuration
	@echo -e "$(CYAN)Debugging dbt configuration...$(NC)"
	poetry run dbt debug --project-dir $(DBT_PROJECT_DIR)
	@echo -e "$(GREEN)✓ dbt debug complete$(NC)"

.PHONY: dbt-deps
dbt-deps: ## Install dbt dependencies
	@echo -e "$(CYAN)Installing dbt dependencies...$(NC)"
	poetry run dbt deps --project-dir $(DBT_PROJECT_DIR)
	@echo -e "$(GREEN)✓ dbt dependencies installed$(NC)"

dbt-compile: ## Compile dbt models
	@echo "$(BLUE)Compiling dbt models...$(RESET)"
	$(POETRY) run $(DBT) compile

dbt-run: ## Run dbt models
	@echo "$(BLUE)Running dbt models...$(RESET)"
	$(POETRY) run $(DBT) run

dbt-test: ## Run dbt tests
	@echo "$(BLUE)Running dbt tests...$(RESET)"
	$(POETRY) run $(DBT) test

dbt-test-data: ## Run dbt tests with data validation
	@echo "$(BLUE)Running dbt data tests...$(RESET)"
	$(POETRY) run $(DBT) test --data

dbt-docs: ## Generate and serve dbt documentation
	@echo "$(BLUE)Generating dbt documentation...$(RESET)"
	$(POETRY) run $(DBT) docs generate
	$(POETRY) run $(DBT) docs serve

dbt-clean: ## Clean dbt artifacts
	@echo "$(BLUE)Cleaning dbt artifacts...$(RESET)"
	$(POETRY) run $(DBT) clean

dbt-debug: ## Debug dbt configuration
	@echo "$(BLUE)Debugging dbt configuration...$(RESET)"
	$(POETRY) run $(DBT) debug

dbt-lint: ## Lint dbt models with sqlfluff
	@echo "$(BLUE)Linting dbt models...$(RESET)"
	$(POETRY) run sqlfluff lint $(SOURCE_DIR)/ --dialect postgres

dbt-format: ## Format dbt models with sqlfluff
	@echo "$(BLUE)Formatting dbt models...$(RESET)"
	$(POETRY) run sqlfluff fix $(SOURCE_DIR)/ --dialect postgres

# dbt workflow targets
dbt-build: dbt-deps dbt-compile dbt-run dbt-test ## Full dbt build workflow
	@echo "$(GREEN)dbt build completed!$(RESET)"

dbt-refresh: dbt-clean dbt-deps dbt-compile ## Refresh dbt environment
	@echo "$(GREEN)dbt environment refreshed!$(RESET)"

# Specific model targets
dbt-run-staging: ## Run only staging models
	@echo "$(BLUE)Running staging models...$(RESET)"
	$(POETRY) run $(DBT) run --select staging

dbt-run-marts: ## Run only marts models
	@echo "$(BLUE)Running marts models...$(RESET)"
	$(POETRY) run $(DBT) run --select marts

dbt-test-staging: ## Test only staging models
	@echo "$(BLUE)Testing staging models...$(RESET)"
	$(POETRY) run $(DBT) test --select staging

dbt-test-marts: ## Test only marts models
	@echo "$(BLUE)Testing marts models...$(RESET)"
	$(POETRY) run $(DBT) test --select marts

# Testing targets (Python tests if applicable)
test: test-unit test-integration ## Run all Python tests
	@echo "$(GREEN)All tests completed!$(RESET)"

test-unit: ## Run unit tests
	@echo "$(BLUE)Running unit tests...$(RESET)"
	@if [ -d "$(TEST_DIR)/unit" ]; then \
		$(POETRY) run pytest $(TEST_DIR)/unit -v --cov=$(SOURCE_DIR) --cov-report=term-missing --cov-report=html --cov-report=xml; \
	else \
		echo "$(YELLOW)No unit tests found$(RESET)"; \
	fi

test-integration: ## Run integration tests
	@echo "$(BLUE)Running integration tests...$(RESET)"
	@if [ -d "$(TEST_DIR)/integration" ]; then \
		$(POETRY) run pytest $(TEST_DIR)/integration -v; \
	else \
		echo "$(YELLOW)No integration tests found$(RESET)"; \
	fi

test-e2e: ## Run E2E tests with Docker
	@echo "$(BLUE)Running E2E tests...$(RESET)"
	$(POETRY) run pytest $(TEST_DIR)/e2e -v --tb=short

test-coverage: ## Run tests with coverage report
	@echo "$(BLUE)Running tests with coverage...$(RESET)"
	@if [ -d "$(TEST_DIR)" ]; then \
		$(POETRY) run pytest $(TEST_DIR) -v --cov=$(SOURCE_DIR) --cov-report=term-missing --cov-report=html --cov-report=xml --cov-fail-under=90; \
	else \
		echo "$(YELLOW)No tests found$(RESET)"; \
	fi

# Code quality targets (for Python code if applicable)
lint: dbt-lint ## Run linting
	@echo "$(BLUE)Running Python linter...$(RESET)"
	@if [ -d "$(TEST_DIR)" ] || [ -d "macros" ]; then \
		$(POETRY) run ruff check . || true; \
	fi

format: dbt-format ## Format code
	@echo "$(BLUE)Formatting code...$(RESET)"
	@if [ -d "$(TEST_DIR)" ] || [ -d "macros" ]; then \
		$(POETRY) run ruff format . || true; \
		$(POETRY) run ruff check --fix . || true; \
	fi

format-check: ## Check code formatting
	@echo "$(BLUE)Checking code formatting...$(RESET)"
	@if [ -d "$(TEST_DIR)" ] || [ -d "macros" ]; then \
		$(POETRY) run ruff format --check . || true; \
	fi

type-check: ## Run type checking with mypy
	@echo "$(BLUE)Running type checker...$(RESET)"
	@if [ -d "$(TEST_DIR)" ] || [ -d "macros" ]; then \
		$(POETRY) run mypy . || true; \
	fi

security: ## Run security checks
	@echo "$(BLUE)Running security checks...$(RESET)"
	@if [ -d "$(TEST_DIR)" ] || [ -d "macros" ]; then \
		$(POETRY) run bandit -r . -f json -o bandit-report.json || true; \
		$(POETRY) run safety check; \
	fi

# Development targets
clean: dbt-clean ## Clean build artifacts and cache
	@echo "$(BLUE)Cleaning build artifacts...$(RESET)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -f coverage.xml
	rm -f bandit-report.json
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: dbt-build ## Build dbt project
	@echo "$(GREEN)dbt project built!$(RESET)"

# Docker targets
docker-test: ## Run tests in Docker environment
	@echo "$(BLUE)Starting Docker test environment...$(RESET)"
	docker-compose -f docker-compose.yml up -d
	@echo "$(YELLOW)Waiting for services to be ready...$(RESET)"
	sleep 10
	$(POETRY) run $(DBT) debug
	$(POETRY) run $(DBT) run
	$(POETRY) run $(DBT) test
	$(POETRY) run pytest $(TEST_DIR)/e2e -v
	docker-compose -f docker-compose.yml down -v

docker-clean: ## Clean Docker environment
	@echo "$(BLUE)Cleaning Docker environment...$(RESET)"
	docker-compose -f docker-compose.yml down -v --remove-orphans
	docker system prune -f

# Pre-commit and CI targets
pre-commit: format lint dbt-compile dbt-test ## Run pre-commit checks
	@echo "$(GREEN)Pre-commit checks completed!$(RESET)"

ci: install-dev pre-commit test ## Run CI pipeline
	@echo "$(GREEN)CI pipeline completed!$(RESET)"

# Convenience targets
all: clean install-dev dbt-deps pre-commit dbt-build ## Run complete development cycle
	@echo "$(GREEN)Complete development cycle finished!$(RESET)"

check: lint dbt-test ## Run all code quality checks
	@echo "$(GREEN)Code quality checks completed!$(RESET)"

dev-setup: install-dev dbt-deps ## Setup development environment
	@echo "$(BLUE)Setting up development environment...$(RESET)"
	$(POETRY) install --with dev,e2e
	$(POETRY) run $(DBT) deps
	@echo "$(GREEN)Development environment ready!$(RESET)"
	@echo "$(YELLOW)Next steps:$(RESET)"
	@echo "  1. Update profiles.yml with your database connection settings"
	@echo "  2. Run 'make dbt-debug' to test your configuration"
	@echo "  3. Run 'make dbt-run' to build your models"
	@echo "  4. Run 'make dbt-test' to validate your data"

# Poetry specific targets
poetry-lock: ## Update poetry.lock file
	@echo "$(BLUE)Updating poetry.lock...$(RESET)"
	$(POETRY) lock

poetry-update: ## Update dependencies
	@echo "$(BLUE)Updating dependencies...$(RESET)"
	$(POETRY) update

poetry-show: ## Show dependency tree
	@echo "$(BLUE)Dependency tree:$(RESET)"
	$(POETRY) show --tree

poetry-export: ## Export requirements.txt
	@echo "$(BLUE)Exporting requirements.txt...$(RESET)"
	$(POETRY) export -f requirements.txt --output requirements.txt --without-hashes

# Debug targets
debug-env: ## Show environment information
	@echo "$(BLUE)Environment Information:$(RESET)"
	@echo "Python: $$($(PYTHON) --version)"
	@echo "Poetry: $$($(POETRY) --version)"
	@echo "dbt: $$($(POETRY) run $(DBT) --version)"
	@echo "Package: $(PACKAGE_NAME)"
	@echo "Models: $(SOURCE_DIR)"
	@echo "Tests: $(TEST_DIR)"

# Data pipeline targets
pipeline-staging: dbt-run-staging dbt-test-staging ## Run staging pipeline
	@echo "$(GREEN)Staging pipeline completed!$(RESET)"

pipeline-marts: dbt-run-marts dbt-test-marts ## Run marts pipeline
	@echo "$(GREEN)Marts pipeline completed!$(RESET)"

pipeline-full: dbt-run dbt-test ## Run full data pipeline
	@echo "$(GREEN)Full pipeline completed!$(RESET)"

# Profile management
create-profile: ## Create example profiles.yml
	@echo "$(BLUE)Creating example profiles.yml...$(RESET)"
	@mkdir -p ~/.dbt
	@cat > ~/.dbt/profiles.yml << 'EOF'
dbt_ldap:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: dbt_user
      password: dbt_password
      port: 5432
      dbname: dbt_ldap_dev
      schema: dbt_ldap
      threads: 4
      keepalives_idle: 0
    test:
      type: postgres
      host: localhost
      user: dbt_user
      password: dbt_password
      port: 5432
      dbname: dbt_ldap_test
      schema: dbt_ldap_test
      threads: 4
      keepalives_idle: 0
EOF
	@echo "$(GREEN)Example profiles.yml created in ~/.dbt/$(RESET)"
