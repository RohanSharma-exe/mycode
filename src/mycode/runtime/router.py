"""
Provider router.

Responsible for selecting the provider used to satisfy a request.
"""

from __future__ import annotations

from mycode.core.config import ConfigManager
from mycode.runtime.providers import BaseProvider
from mycode.runtime.registry import ProviderRegistry


class ProviderRouter:
    """Selects providers for requests."""

    def __init__(
        self,
        registry: ProviderRegistry,
        config: ConfigManager,
    ) -> None:
        self._registry = registry
        self._config = config

    def default_provider(self) -> BaseProvider:
        """Return the configured default provider."""

        provider_name = self._config.settings.llm.default_provider

        return self._registry.get(provider_name)

    def get(self, name: str) -> BaseProvider:
        """Return a provider by name."""

        return self._registry.get(name)
