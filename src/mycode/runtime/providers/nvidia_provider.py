"""
NVIDIA provider implementation.
"""

from __future__ import annotations

from collections.abc import AsyncIterator

from mycode.runtime.capabilities import ProviderCapabilities
from mycode.runtime.models import (
    ChatMessage,
    ChatRequest,
    ChatResponse,
    MessageRole,
    ModelInfo,
    StreamChunk,
    TokenUsage,
)
from mycode.runtime.provider_config import ProviderConfig
from mycode.runtime.providers.base import BaseProvider
from mycode.runtime.providers.nvidia_client import NVIDIAClient


class NVIDIAProvider(BaseProvider):
    """NVIDIA provider."""

    def __init__(
        self,
        config: ProviderConfig,
        client: NVIDIAClient,
    ) -> None:
        super().__init__(config)
        self._client = client

    @property
    def name(self) -> str:
        return self.config.name

    @property
    def default_model(self) -> str:
        return self.config.model

    @property
    def capabilities(self) -> ProviderCapabilities:
        return ProviderCapabilities(
            streaming=True,
            reasoning=True,
        )

    async def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """Generate a response."""

        response = await self._client.chat(
            [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in request.messages
            ]
        )

        choice = response["choices"][0]
        message = choice["message"]

        usage = response.get("usage", {})

        return ChatResponse(
            model=response["model"],
            message=ChatMessage(
                role=MessageRole.ASSISTANT,
                content=message["content"],
            ),
            usage=TokenUsage(
                prompt_tokens=usage.get("prompt_tokens", 0),
                completion_tokens=usage.get("completion_tokens", 0),
                total_tokens=usage.get("total_tokens", 0),
            ),
        )

    async def stream_generate(
        self,
        request: ChatRequest,
    ) -> AsyncIterator[StreamChunk]:
        raise NotImplementedError("Streaming will be implemented next.")

    async def health(self) -> bool:
        return True

    async def list_models(self) -> list[ModelInfo]:
        return [
            ModelInfo(
                id=self.config.model,
                provider=self.name,
                context_window=128000,
                max_output_tokens=self.config.max_tokens,
                reasoning=True,
            )
        ]
