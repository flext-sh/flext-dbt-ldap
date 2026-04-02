"""FLEXT DBT LDAP Exceptions.

Domain-specific exceptions using DRY base mixin.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from flext_core import FlextExceptions
from flext_dbt_ldap import t


class FlextDbtLdapError(FlextExceptions.BaseError):
    """FlextDbtLdapError - base DBT LDAP error."""


class FlextDbtLdapValidationError(FlextExceptions.ValidationError):
    """FlextDbtLdapValidationError - validation error."""


class FlextDbtLdapConfigurationError(FlextExceptions.ConfigurationError):
    """FlextDbtLdapConfigurationError - configuration error."""


class FlextDbtLdapConnectionError(FlextDbtLdapError):
    """FlextDbtLdapConnectionError - connection error."""


class FlextDbtLdapProcessingError(FlextDbtLdapError):
    """FlextDbtLdapProcessingError - processing error."""


class FlextDbtLdapAuthenticationError(FlextDbtLdapError):
    """FlextDbtLdapAuthenticationError - authentication error."""


class FlextDbtLdapTimeoutError(FlextDbtLdapError):
    """FlextDbtLdapTimeoutError - timeout error."""


class _DbtLdapContextMixin:
    """DRY mixin for building MetadataAttributeValue-compatible context dicts."""

    @staticmethod
    def _build_context(
        **fields: t.Scalar | None,
    ) -> Mapping[str, t.MetadataValue]:
        """Build context dictionary from keyword arguments."""
        return {key: value for key, value in fields.items() if value is not None}


class FlextDbtLdapModelError(_DbtLdapContextMixin, FlextExceptions.BaseError):
    """LDAP DBT model-specific errors."""

    @override
    def __init__(
        self,
        message: str = "LDAP DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        error_code: str | None = None,
        correlation_id: str | None = None,
    ) -> None:
        """Initialize LDAP DBT model error with context."""
        self.model_name = model_name
        self.model_type = model_type
        context = self._build_context(model_name=model_name, model_type=model_type)
        super().__init__(
            f"LDAP DBT model: {message}",
            error_code=error_code or "DBT_LDAP_MODEL_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextDbtLdapMacroError(_DbtLdapContextMixin, FlextExceptions.BaseError):
    """LDAP DBT macro errors."""

    @override
    def __init__(
        self,
        message: str = "LDAP DBT macro error",
        *,
        macro_name: str | None = None,
        error_code: str | None = None,
        correlation_id: str | None = None,
    ) -> None:
        """Initialize LDAP DBT macro error with context."""
        self.macro_name = macro_name
        context = self._build_context(macro_name=macro_name)
        super().__init__(
            f"LDAP DBT macro: {message}",
            error_code=error_code or "DBT_LDAP_MACRO_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextDbtLdapTestError(_DbtLdapContextMixin, FlextExceptions.BaseError):
    """LDAP DBT test errors."""

    @override
    def __init__(
        self,
        message: str = "LDAP DBT test failed",
        *,
        test_name: str | None = None,
        model_name: str | None = None,
        error_code: str | None = None,
        correlation_id: str | None = None,
    ) -> None:
        """Initialize LDAP DBT test error with context."""
        self.test_name = test_name
        self.model_name = model_name
        context = self._build_context(test_name=test_name, model_name=model_name)
        super().__init__(
            f"LDAP DBT test: {message}",
            error_code=error_code or "DBT_LDAP_TEST_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


__all__: t.StrSequence = [
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
