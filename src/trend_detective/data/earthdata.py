"""Thin, credential-free helpers around NASA Earthdata access."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class EarthdataConnector:
    """Lazy Earthdata connector; authentication is delegated to earthaccess."""

    _authenticated: bool = False

    def authenticate(self, persist: bool = True) -> None:
        """Authenticate using earthaccess's configured interactive/token flow.

        No credentials are stored in this repository. The call is intentionally
        lazy so synthetic demo mode works without an Earthdata account.
        """

        import earthaccess

        earthaccess.login(strategy="interactive", persist=persist)
        self._authenticated = True

    def search(self, **kwargs: Any) -> list[Any]:
        """Search Earthdata granules after authentication."""

        if not self._authenticated:
            raise RuntimeError("Call authenticate() before searching Earthdata")
        import earthaccess

        return list(earthaccess.search_data(**kwargs))

    def open(self, results: list[Any]) -> Any:
        """Open remote results through earthaccess."""

        if not self._authenticated:
            raise RuntimeError("Call authenticate() before opening Earthdata results")
        import earthaccess

        return earthaccess.open(results)
