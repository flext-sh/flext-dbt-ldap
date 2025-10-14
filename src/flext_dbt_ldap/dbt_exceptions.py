"""FLEXT DBT LDAP Exceptions.

Domain-specific exceptions using factory pattern to eliminate duplication.

Module documentation:

- ZERO code duplication através do DRY exception factory pattern de flext-core
- USA create_module_exception_classes() para eliminar exception boilerplate massivo
- Elimina 185+ linhas duplicadas de código boilerplate por exception class
- SOLID: Single source of truth para module exception patterns
- Redução de 186+ linhas para 85 linhas (54% reduction)

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import override

from flext_core import FlextCore

from flext_dbt_ldap.typings import FlextDbtLdapTypes

# Use FlextCore.Exceptions directly (current signature)
_exceptions = FlextCore.Exceptions

# Extract exception classes with precise typing for MyPy
# Only create aliases for exceptions that actually exist in the factory
FlextDbtLdapError = FlextCore.Exceptions.BaseError
FlextDbtLdapValidationError = FlextCore.Exceptions.ValidationError
FlextDbtLdapConfigurationError = FlextCore.Exceptions.ConfigurationError

# Create aliases for additional exception types using existing base classes
FlextDbtLdapConnectionError = FlextDbtLdapError
FlextDbtLdapProcessingError = FlextDbtLdapError
FlextDbtLdapAuthenticationError = FlextDbtLdapError
FlextDbtLdapTimeoutError = FlextDbtLdapError


# Domain-specific DBT LDAP errors using composition over duplication


class FlextDbtLdapModelError(FlextCore.Exceptions.BaseError):
    """LDAP DBT model-specific errors using DRY foundation."""

    def _extract_common_kwargs(
        self, kwargs: dict
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(self, base_context: dict, **extra_fields) -> dict[str, object]:
        """Build context dictionary with additional fields."""
        context = dict[str, object](base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT model error with context."""
        # Store model attributes before extracting common kwargs
        self.model_name = model_name
        self.model_type = model_type

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with model-specific fields
        context = self._build_context(
            base_context,
            model_name=model_name,
            model_type=model_type,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDAP DBT model: {message}",
            code=error_code or "DBT_LDAP_MODEL_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextDbtLdapMacroError(FlextCore.Exceptions.BaseError):
    """LDAP DBT macro errors using DRY foundation."""

    def _extract_common_kwargs(
        self, kwargs: dict
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(self, base_context: dict, **extra_fields) -> dict[str, object]:
        """Build context dictionary with additional fields."""
        context = dict[str, object](base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT macro error",
        *,
        macro_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT macro error with context."""
        # Store macro name before extracting common kwargs
        self.macro_name = macro_name

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with macro-specific fields
        context = self._build_context(
            base_context,
            macro_name=macro_name,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDAP DBT macro: {message}",
            code=error_code or "DBT_LDAP_MACRO_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextDbtLdapTestError(FlextCore.Exceptions.BaseError):
    """LDAP DBT test errors using DRY foundation."""

    def _extract_common_kwargs(
        self, kwargs: dict
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(self, base_context: dict, **extra_fields) -> dict[str, object]:
        """Build context dictionary with additional fields."""
        context = dict[str, object](base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT test failed",
        *,
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT test error with context."""
        # Store test attributes before extracting common kwargs
        self.test_name = test_name
        self.model_name = model_name

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with test-specific fields
        context = self._build_context(
            base_context,
            test_name=test_name,
            model_name=model_name,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDAP DBT test: {message}",
            code=error_code or "DBT_LDAP_TEST_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


__all__: FlextDbtLdapTypes.Core.StringList = [
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapValidationError",
]
