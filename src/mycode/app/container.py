"""
Dependency Injection Container.

Stores and resolves shared singleton services.
"""

from __future__ import annotations

from typing import Any


class Container:
    """Simple type-based dependency injection container."""

    def __init__(self) -> None:
        self._services: dict[type[Any], Any] = {}

    def register(self, service_type: type[Any], instance: Any) -> None:
        """
        Register a singleton instance.

        Parameters
        ----------
        service_type:
            Type used as the lookup key.

        instance:
            Singleton instance.
        """
        self._services[service_type] = instance

    def resolve(self, service_type: type[Any]) -> Any:
        """
        Resolve a registered service.

        Raises
        ------
        KeyError
            If the service has not been registered.
        """
        if service_type not in self._services:
            raise KeyError(f"Service '{service_type.__name__}' has not been registered.")

        return self._services[service_type]

    def exists(self, service_type: type[Any]) -> bool:
        """Return True if the service exists."""
        return service_type in self._services

    def remove(self, service_type: type[Any]) -> None:
        """Remove a registered service."""
        self._services.pop(service_type, None)

    def clear(self) -> None:
        """Remove all registered services."""
        self._services.clear()
