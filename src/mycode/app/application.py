"""
Application root.

Owns all managers and services used by the framework.
"""

from __future__ import annotations

from mycode.app.container import Container


class Application:
    """Main application instance."""

    def __init__(self) -> None:
        # Dependency injection container.
        self.container = Container()

    def register(self, name: str, service: object) -> None:
        """Register a shared service."""
        self.container.register(name, service)

    def get(self, name: str) -> object:
        """Retrieve a shared service."""
        return self.container.resolve(name)
