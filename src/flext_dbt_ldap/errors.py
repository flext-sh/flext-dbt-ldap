"""FLEXT DBT LDAP Exceptions.

Domain-specific exceptions — e.BaseError _params_cls hook; Pydantic validates kwargs.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar, override

from flext_dbt_ldap import e, m, t


class FlextDbtLdapError(e.BaseError):
    """FlextDbtLdapError - base DBT LDAP error."""


class FlextDbtLdapValidationError(e.ValidationError):
    """FlextDbtLdapValidationError - validation error."""


class FlextDbtLdapConfigurationError(e.ConfigurationError):
    """FlextDbtLdapConfigurationError - configuration error."""


class FlextDbtLdapConnectionError(FlextDbtLdapError):
    """FlextDbtLdapConnectionError - connection error."""


class FlextDbtLdapProcessingError(FlextDbtLdapError):
    """FlextDbtLdapProcessingError - processing error."""


class FlextDbtLdapAuthenticationError(FlextDbtLdapError):
    """FlextDbtLdapAuthenticationError - authentication error."""


class FlextDbtLdapTimeoutError(FlextDbtLdapError):
    """FlextDbtLdapTimeoutError - timeout error."""


class _ModelErrorParams(m.Value):
    model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")
    model_name: Annotated[
        str | None,
        m.Field(description="Optional dbt model name associated with the error"),
    ] = None
    model_type: Annotated[
        str | None,
        m.Field(description="Optional dbt model type associated with the error"),
    ] = None


class FlextDbtLdapModelError(e.BaseError):
    """LDAP DBT model-specific errors."""

    _params_cls = _ModelErrorParams
    _param_keys: ClassVar[frozenset[str]] = frozenset({"model_name", "model_type"})
    _default_error_code: ClassVar[str] = "DBT_LDAP_MODEL_ERROR"

    @override
    def __init__(
        self, message: str = "LDAP DBT model error", **kwargs: t.JsonValue
    ) -> None:
        super().__init__(f"LDAP DBT model: {message}", merged_kwargs=kwargs)


class _MacroErrorParams(m.Value):
    model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")
    macro_name: Annotated[
        str | None,
        m.Field(description="Optional dbt macro name associated with the error"),
    ] = None


class FlextDbtLdapMacroError(e.BaseError):
    """LDAP DBT macro errors."""

    _params_cls = _MacroErrorParams
    _param_keys: ClassVar[frozenset[str]] = frozenset({"macro_name"})
    _default_error_code: ClassVar[str] = "DBT_LDAP_MACRO_ERROR"

    @override
    def __init__(
        self, message: str = "LDAP DBT macro error", **kwargs: t.JsonValue
    ) -> None:
        super().__init__(f"LDAP DBT macro: {message}", merged_kwargs=kwargs)


class _TestErrorParams(m.Value):
    model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")
    test_name: Annotated[
        str | None,
        m.Field(description="Optional dbt test name associated with the error"),
    ] = None
    model_name: Annotated[
        str | None,
        m.Field(description="Optional dbt model name associated with the test error"),
    ] = None


class FlextDbtLdapTestError(e.BaseError):
    """LDAP DBT test errors."""

    _params_cls = _TestErrorParams
    _param_keys: ClassVar[frozenset[str]] = frozenset({"test_name", "model_name"})
    _default_error_code: ClassVar[str] = "DBT_LDAP_TEST_ERROR"

    @override
    def __init__(
        self, message: str = "LDAP DBT test failed", **kwargs: t.JsonValue
    ) -> None:
        super().__init__(f"LDAP DBT test: {message}", merged_kwargs=kwargs)


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
