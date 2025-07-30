"""LDAP DBT exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for LDAP DBT operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextConfigurationError,
    FlextConnectionError,
    FlextError,
    FlextProcessingError,
    FlextValidationError,
)


class FlextDbtLdapError(FlextError):
    """Base exception for LDAP DBT operations."""

    def __init__(
        self,
        message: str = "LDAP DBT error",
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(message, error_code="LDAP_DBT_ERROR", context=context)


class FlextDbtLdapConfigurationError(FlextConfigurationError):
    """LDAP DBT configuration errors."""

    def __init__(
        self,
        message: str = "LDAP DBT configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"LDAP DBT config: {message}", **context)


class FlextDbtLdapValidationError(FlextValidationError):
    """LDAP DBT validation errors."""

    def __init__(
        self,
        message: str = "LDAP DBT validation failed",
        field: str | None = None,
        value: object = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT validation error with context."""
        validation_details = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(
            f"LDAP DBT validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextDbtLdapConnectionError(FlextConnectionError):
    """LDAP DBT connection errors."""

    def __init__(
        self,
        message: str = "LDAP DBT connection failed",
        ldap_server: str | None = None,
        port: int | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT connection error with context."""
        context = kwargs.copy()
        if ldap_server is not None:
            context["ldap_server"] = ldap_server
        if port is not None:
            context["port"] = port

        super().__init__(f"LDAP DBT connection: {message}", **context)


class FlextDbtLdapProcessingError(FlextProcessingError):
    """LDAP DBT processing errors."""

    def __init__(
        self,
        message: str = "LDAP DBT processing failed",
        model_name: str | None = None,
        stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT processing error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name
        if stage is not None:
            context["stage"] = stage

        super().__init__(f"LDAP DBT processing: {message}", **context)


class FlextDbtLdapModelError(FlextDbtLdapError):
    """LDAP DBT model-specific errors."""

    def __init__(
        self,
        message: str = "LDAP DBT model error",
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDAP DBT model error with context."""
        context = kwargs.copy()
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(f"LDAP DBT model: {message}", model_name=model_name, **context)


class FlextDbtLdapMacroError(FlextDbtLdapError):
    """LDAP DBT macro errors."""

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

        super().__init__(f"LDAP DBT macro: {message}", **context)


class FlextDbtLdapTestError(FlextDbtLdapError):
    """LDAP DBT test errors."""

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

        super().__init__(f"LDAP DBT test: {message}", model_name=model_name, **context)


__all__ = [
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapTestError",
    "FlextDbtLdapValidationError",
]
