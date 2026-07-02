"""
Base provider interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from mycode.runtime.capabilities import ProviderCapabilities
from mycode.runtime.models import ChatRequest, ChatResponse, ModelInfo, StreamChunk
from mycode.runtime.provider_config import ProviderConfig


class BaseProvider(ABC):
    """Base class for every provider."""

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:
        """Initialize the provider."""

        self._config = config

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name."""

    @property
    @abstractmethod
    def default_model(self) -> str:
        """Default model."""

    @property
    @abstractmethod
    def capabilities(self) -> ProviderCapabilities:
        """Provider capabilities."""

    @property
    def config(self) -> ProviderConfig:
        """Return provider configuration."""
        return self._config

    @abstractmethod
    async def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """Generate a response."""

    @abstractmethod
    async def stream_generate(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[StreamChunk]:
        """Generate a streamed response."""

    @abstractmethod
    async def health(self) -> bool:
        """Health check."""

    @abstractmethod
    async def list_models(self) -> list[ModelInfo]:
        """Return supported models."""
