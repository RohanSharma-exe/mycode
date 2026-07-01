"""
Provider factory.

Responsible for creating provider instances.
"""

from __future__ import annotations

from collections.abc import Callable

from mycode.llm.providers import BaseProvider

ProviderBuilder = Callable[[], BaseProvider]


class ProviderFactory:
    """Factory responsible for creating providers."""

    def __init__(self) -> None:
        self._builders: dict[str, ProviderBuilder] = {}

    def register(
        self,
        name: str,
        builder: ProviderBuilder,
    ) -> None:
        """Register a provider builder."""

        self._builders[name.lower()] = builder

    def create(self, name: str) -> BaseProvider:
        """Create a provider."""

        builder = self._builders[name.lower()]

        return builder()

    def names(self) -> list[str]:
        """Return registered provider builders."""

        return sorted(self._builders.keys())
