"""Test utilities for flext-dbt-ldap.

Provides TestsFlextDbtLdapUtilities, combining TestsFlextUtilities with
FlextDbtLdapUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from pydantic import PrivateAttr

from flext_dbt_ldap import (
    FlextDbtLdap,
    FlextDbtLdapSettings,
    FlextDbtLdapUtilities,
    m,
    p,
    r,
    t,
)
from flext_ldap import FlextLdap
from flext_tests import FlextTestsUtilities


class TestsFlextDbtLdapUtilities(FlextTestsUtilities, FlextDbtLdapUtilities):
    """Test utilities combining TestsFlextUtilities with flext-dbt-ldap utilities."""

    class DbtLdap(FlextDbtLdapUtilities.DbtLdap):
        """DbtLdap test utilities namespace."""

        class Tests:
            """Internal tests declarations."""

            class InMemoryLdapDirectory(FlextLdap):
                """Real LDAP client backed by a test-owned in-memory directory.

                The facade runs its genuine extraction path against this client;
                every incoming search request is recorded verbatim so tests can
                observe the exact outgoing query the facade produced, and the
                directory answers with real ``m.Ldif.Entry`` models.
                """

                _directory_entries: list[m.Ldif.Entry] = PrivateAttr(
                    default_factory=list
                )
                _directory_requests: list[m.Ldap.SearchOptions] = PrivateAttr(
                    default_factory=list
                )
                _directory_reachable: bool = PrivateAttr(default=True)

                def serve(self, entries: t.SequenceOf[m.Ldif.Entry]) -> None:
                    """Replace the directory contents with ``entries``."""
                    self._directory_entries = list(entries)

                def mark_unreachable(self) -> None:
                    """Model a directory server that is unreachable."""
                    self._directory_reachable = False

                def last_search_request(self) -> m.Ldap.SearchOptions:
                    """Return the most recent search request sent by the facade."""
                    if not self._directory_requests:
                        msg = "No search request reached the directory"
                        raise RuntimeError(msg)
                    return self._directory_requests[-1]

                @override
                def search(
                    self, search_options: p.Ldap.SearchOptions, server_type: str = "rfc"
                ) -> p.Result[m.Ldap.SearchResult]:
                    """Serve the directory contents for the recorded request."""
                    concrete_options = (
                        search_options
                        if isinstance(search_options, m.Ldap.SearchOptions)
                        else m.Ldap.SearchOptions.model_validate(search_options)
                    )
                    self._directory_requests.append(concrete_options)
                    if not self._directory_reachable:
                        return r[m.Ldap.SearchResult].fail("directory unreachable")
                    return r[m.Ldap.SearchResult].ok(
                        m.Ldap.SearchResult(
                            entries=list(self._directory_entries),
                            search_options=concrete_options,
                        )
                    )

            class InMemoryDbtRunnerLdap(FlextDbtLdap):
                """FlextDbtLdap with test-owned in-memory external boundaries.

                The LDAP client is the in-memory directory produced by the
                facade's own ``create_ldap_api`` hook; the dbt runner executes
                in memory, records every requested model list, and answers with
                real ``m.Meltano.CommandExecutionResult`` models.
                """

                _dbt_runner_failure: str | None = PrivateAttr(default=None)
                _dbt_runner_requests: list[tuple[str, ...]] = PrivateAttr(
                    default_factory=list
                )

                def __init__(
                    self, settings: FlextDbtLdapSettings | None = None
                ) -> None:
                    """Wire the facade state with the canonical settings kwarg."""
                    super().__init__(settings=settings)

                @staticmethod
                @override
                def create_ldap_api(
                    settings: FlextDbtLdapSettings,
                ) -> u.DbtLdap.Tests.InMemoryLdapDirectory:
                    """Create the in-memory directory wired as the LDAP client."""
                    return u.DbtLdap.Tests.InMemoryLdapDirectory.with_settings(settings)

                def directory(self) -> u.DbtLdap.Tests.InMemoryLdapDirectory:
                    """Return the in-memory directory serving this facade."""
                    client = self._ldap_api
                    if not isinstance(client, u.DbtLdap.Tests.InMemoryLdapDirectory):
                        msg = "LDAP client is not the in-memory directory"
                        raise TypeError(msg)
                    return client

                def mark_dbt_failure(self, message: str) -> None:
                    """Make subsequent dbt runs fail with ``message``."""
                    self._dbt_runner_failure = message

                def dbt_requests(self) -> tuple[tuple[str, ...], ...]:
                    """Return every model list requested from the dbt runner."""
                    return tuple(self._dbt_runner_requests)

                @override
                def run_models(
                    self, models: t.StrSequence | None = None
                ) -> p.Result[m.Meltano.CommandExecutionResult]:
                    """Serve the dbt boundary from the recorded runner state."""
                    requested = tuple(models) if models else ()
                    self._dbt_runner_requests.append(requested)
                    if self._dbt_runner_failure is not None:
                        return r[m.Meltano.CommandExecutionResult].fail(
                            self._dbt_runner_failure
                        )
                    return r[m.Meltano.CommandExecutionResult].ok(
                        m.Meltano.CommandExecutionResult(
                            command=requested,
                            success=True,
                            exit_code=0,
                            output="",
                            error="",
                            execution_time=0.0,
                        )
                    )


u = TestsFlextDbtLdapUtilities
__all__: list[str] = ["TestsFlextDbtLdapUtilities", "u"]
