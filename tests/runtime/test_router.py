from __future__ import annotations

from collections.abc import AsyncIterator

from mycode.core.config import ConfigManager
from mycode.runtime import (
    ChatRequest,
    ChatResponse,
    ModelInfo,
    ProviderCapabilities,
    ProviderConfig,
    StreamChunk,
)
from mycode.runtime.providers import BaseProvider
from mycode.runtime.registry import ProviderRegistry
from mycode.runtime.router import ProviderRouter


class FakeProvider(BaseProvider):
    def __init__(self) -> None:
        super().__init__(
            ProviderConfig(
                name="nvidia",
                model="fake-model",
            )
        )

    @property
    def name(self) -> str:
        return self.config.name

    @property
    def default_model(self) -> str:
        return self.config.model

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
