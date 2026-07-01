"""
Base provider interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from mycode.runtime.capabilities import ProviderCapabilities
from mycode.runtime.models import ChatRequest, ChatResponse, ModelInfo, StreamChunk


class BaseProvider(ABC):
    """Base class for every provider."""

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
