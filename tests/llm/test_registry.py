from __future__ import annotations

from collections.abc import AsyncIterator

from mycode.llm import (
    ChatRequest,
    ChatResponse,
    ModelInfo,
    ProviderCapabilities,
    StreamChunk,
)
from mycode.llm.providers import BaseProvider
from mycode.llm.registry import ProviderRegistry


class FakeProvider(BaseProvider):
    @property
    def name(self) -> str:
        return "fake"

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


def test_register_provider() -> None:
    registry = ProviderRegistry()

    registry.register(FakeProvider())

    assert registry.exists("fake")


def test_get_provider() -> None:
    registry = ProviderRegistry()

    provider = FakeProvider()

    registry.register(provider)

    assert registry.get("fake") is provider


def test_unregister_provider() -> None:
    registry = ProviderRegistry()

    registry.register(FakeProvider())

    registry.unregister("fake")

    assert not registry.exists("fake")
