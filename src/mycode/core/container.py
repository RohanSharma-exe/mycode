"""
Dependency Injection Container.

Stores and provides shared services across the application.
"""

from typing import Any


class Container:
    """Simple dependency injection container."""

    def __init__(self) -> None:
        # Stores all registered services.
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """
        Register a service.

        Parameters
        ----------
        name : str
            Unique service name.

        service : Any
            Service instance.
        """
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        """
        Retrieve a registered service.

        Raises
        ------
        KeyError
            If the service does not exist.
        """
        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")

        return self._services[name]

    def exists(self, name: str) -> bool:
        """Check whether a service is registered."""
        return name in self._services

    def clear(self) -> None:
        """Remove all registered services."""
        self._services.clear()
