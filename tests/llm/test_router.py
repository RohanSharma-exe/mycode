from __future__ import annotations

from collections.abc import AsyncIterator

from mycode.core.config import ConfigManager
from mycode.llm import (
    ChatRequest,
    ChatResponse,
    ModelInfo,
    ProviderCapabilities,
    StreamChunk,
)
from mycode.llm.providers import BaseProvider
from mycode.llm.registry import ProviderRegistry
from mycode.llm.router import ProviderRouter


class FakeProvider(BaseProvider):
    @property
    def name(self) -> str:
        return "nvidia"

    @property
    def default_model(self) -> str:
        return "fake-model"

    @property
    def capabilities(self) -> ProviderCapabilities:
        return ProviderCapabilities()

    async def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        raise NotImplementedError

    async def stream_generate(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[StreamChunk]:
        if False:
            yield

    async def health(self) -> bool:
        return True

    async def list_models(self) -> list[ModelInfo]:
        return []


def test_default_provider() -> None:
    registry = ProviderRegistry()
    registry.register(FakeProvider())

    config = ConfigManager()

    router = ProviderRouter(
        registry=registry,
        config=config,
    )

    assert router.default_provider().name == "nvidia"
