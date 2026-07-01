"""
Provider registry.
"""

from __future__ import annotations

from mycode.runtime.exceptions import (
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)
from mycode.runtime.providers import BaseProvider


class ProviderRegistry:
    """Stores provider instances."""

    def __init__(self) -> None:
        self._providers: dict[str, BaseProvider] = {}

    def register(self, provider: BaseProvider) -> None:
        """
        Register a provider.

        Provider names must be unique.
        """

        name = provider.name.lower()

        if name in self._providers:
            raise ProviderAlreadyRegisteredError(f"Provider '{name}' is already registered.")

        self._providers[name] = provider

    def unregister(self, name: str) -> None:
        """Remove a provider if present."""

        self._providers.pop(name.lower(), None)

    def get(self, name: str) -> BaseProvider:
        """Retrieve a provider by name."""

        try:
            return self._providers[name.lower()]
        except KeyError as exc:
            raise ProviderNotFoundError(f"Provider '{name}' is not registered.") from exc

    def exists(self, name: str) -> bool:
        """Return True if the provider exists."""

        return name.lower() in self._providers

    def names(self) -> list[str]:
        """Return provider names."""

        return sorted(self._providers.keys())

    def clear(self) -> None:
        """Remove all providers."""

        self._providers.clear()

    def __len__(self) -> int:
        """Return the number of registered providers."""

        return len(self._providers)
