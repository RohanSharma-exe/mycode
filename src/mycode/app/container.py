"""
Simple dependency injection container.
"""

from __future__ import annotations

from typing import Any


class Container:
    """Stores shared singleton services."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """Register a singleton service."""
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        """Resolve a registered service."""
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(f"Service '{name}' is not registered.") from exc

    def exists(self, name: str) -> bool:
        """Check whether a service exists."""
        return name in self._services
