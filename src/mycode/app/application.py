"""
Application root.

Owns all framework services.
"""

from __future__ import annotations

from typing import Any

import httpx

from mycode.app.container import Container


class Application:
    """Main application instance."""

    def __init__(self) -> None:
        self.container = Container()

    def register(
        self,
        service_type: type[Any],
        instance: Any,
    ) -> None:
        """Register a shared service."""
        self.container.register(service_type, instance)

    def resolve(
        self,
        service_type: type[Any],
    ) -> Any:
        """Resolve a shared service."""
        return self.container.resolve(service_type)

    async def shutdown(self) -> None:
        """Release shared resources."""

        try:
            client: httpx.AsyncClient = self.resolve(httpx.AsyncClient)
            await client.aclose()
        except KeyError:
            pass
