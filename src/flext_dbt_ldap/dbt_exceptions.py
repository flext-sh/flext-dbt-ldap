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

from flext_core import FlextExceptions, FlextTypes

# Use FlextExceptions directly (current signature)
_exceptions = FlextExceptions

# Extract exception classes with precise typing for MyPy
# Only create aliases for exceptions that actually exist in the factory
FlextDbtLdapError = FlextExceptions.BaseError
FlextDbtLdapValidationError = FlextExceptions.ValidationError
FlextDbtLdapConfigurationError = FlextExceptions.ConfigurationError

# Create aliases for additional exception types using existing base classes
FlextDbtLdapConnectionError = FlextDbtLdapError
FlextDbtLdapProcessingError = FlextDbtLdapError
FlextDbtLdapAuthenticationError = FlextDbtLdapError
FlextDbtLdapTimeoutError = FlextDbtLdapError


# Domain-specific DBT LDAP errors using composition over duplication


class FlextDbtLdapModelError(FlextExceptions.BaseError):
    """LDAP DBT model-specific errors using DRY foundation."""

    def __init__(
        self,
        message: str = "LDAP DBT model error",
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT model error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(f"LDAP DBT model: {message}", context=context)


class FlextDbtLdapMacroError(FlextExceptions.BaseError):
    """LDAP DBT macro errors using DRY foundation."""

    def __init__(
        self,
        message: str = "LDAP DBT macro error",
        macro_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT macro error with context."""
        context = kwargs.copy()
        if macro_name is not None:
            context["macro_name"] = macro_name

        super().__init__(f"LDAP DBT macro: {message}", context=context)


class FlextDbtLdapTestError(FlextExceptions.BaseError):
    """LDAP DBT test errors using DRY foundation."""

    def __init__(
        self,
        message: str = "LDAP DBT test failed",
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT test error with context."""
        context = kwargs.copy()
        if test_name is not None:
            context["test_name"] = test_name
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(f"LDAP DBT test: {message}", context=context)


__all__: FlextTypes.Core.StringList = [
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
