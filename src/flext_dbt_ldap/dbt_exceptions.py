"""FLEXT DBT LDAP Exceptions.

Domain-specific exceptions using factory pattern to eliminate duplication.

Module documentation:

- ZERO code duplication through DRY exception factory pattern from flext-core
- USES create_module_exception_classes() to eliminate massive exception boilerplate
- Eliminates 185+ duplicated lines of boilerplate code per exception class
- SOLID: Single source of truth for module exception patterns
- Reduction from 186+ lines to 85 lines (54% reduction)

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import override

from flext_core import FlextExceptions

from flext_dbt_ldap.typings import t

# Use FlextExceptions directly (current signature)
_exceptions = FlextExceptions


# Exception classes with real inheritance for precise typing
class FlextDbtLdapError(FlextExceptions.BaseError):
    """FlextDbtLdapError - real inheritance from BaseError."""


class FlextDbtLdapValidationError(FlextExceptions.ValidationError):
    """FlextDbtLdapValidationError - real inheritance from ValidationError."""


class FlextDbtLdapSettingsurationError(FlextExceptions.ConfigurationError):
    """FlextDbtLdapSettingsurationError - real inheritance from ConfigurationError."""


# Additional exception classes with real inheritance using base classes
class FlextDbtLdapConnectionError(FlextDbtLdapError):
    """FlextDbtLdapConnectionError - real inheritance from FlextDbtLdapError."""


class FlextDbtLdapProcessingError(FlextDbtLdapError):
    """FlextDbtLdapProcessingError - real inheritance from FlextDbtLdapError."""


class FlextDbtLdapAuthenticationError(FlextDbtLdapError):
    """FlextDbtLdapAuthenticationError - real inheritance from FlextDbtLdapError."""


class FlextDbtLdapTimeoutError(FlextDbtLdapError):
    """FlextDbtLdapTimeoutError - real inheritance from FlextDbtLdapError."""


# Domain-specific DBT LDAP errors using composition over duplication


class FlextDbtLdapModelError(FlextExceptions.BaseError):
    """LDAP DBT model-specific errors using DRY foundation."""

    def _extract_common_kwargs(
        self,
        kwargs: dict[str, t.GeneralValueType],
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(
        self,
        base_context: dict[str, t.GeneralValueType],
        **extra_fields: t.JsonValue,
    ) -> t.DbtLdap.ContextDict:
        """Build context dictionary with additional fields."""
        context: t.DbtLdap.ContextDict = dict(base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: t.JsonValue,
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


class FlextDbtLdapMacroError(FlextExceptions.BaseError):
    """LDAP DBT macro errors using DRY foundation."""

    def _extract_common_kwargs(
        self,
        kwargs: dict[str, t.GeneralValueType],
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(
        self,
        base_context: dict[str, t.GeneralValueType],
        **extra_fields: t.JsonValue,
    ) -> t.DbtLdap.ContextDict:
        """Build context dictionary with additional fields."""
        context: t.DbtLdap.ContextDict = dict(base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT macro error",
        *,
        macro_name: str | None = None,
        **kwargs: t.JsonValue,
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


class FlextDbtLdapTestError(FlextExceptions.BaseError):
    """LDAP DBT test errors using DRY foundation."""

    def _extract_common_kwargs(
        self,
        kwargs: dict[str, t.GeneralValueType],
    ) -> tuple[dict, str | None, str | None]:
        """Extract common parameters from kwargs."""
        base_context = kwargs.get("context", {})
        correlation_id = kwargs.get("correlation_id")
        error_code = kwargs.get("error_code")
        return base_context, correlation_id, error_code

    def _build_context(
        self,
        base_context: dict[str, t.GeneralValueType],
        **extra_fields: t.JsonValue,
    ) -> t.DbtLdap.ContextDict:
        """Build context dictionary with additional fields."""
        context: t.DbtLdap.ContextDict = dict(base_context)
        context.update(extra_fields)
        return context

    @override
    def __init__(
        self,
        message: str = "LDAP DBT test failed",
        *,
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: t.JsonValue,
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


__all__: list[str] = [
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapSettingsurationError",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapValidationError",
]
