import pytest

from mycode.runtime import (
    ConversationStore,
    RuntimeEngine,
)
from mycode.runtime.models import (
    ChatMessage,
    ChatRequest,
    ChatResponse,
    MessageRole,
    TokenUsage,
)


class DummyRouter:
    """Simple router used for testing."""


def test_runtime_creation() -> None:
    runtime = RuntimeEngine(
        router=DummyRouter(),
        conversation_store=ConversationStore(),
    )

    assert runtime.router is not None

    assert runtime.conversation_store is not None


class FakeProvider:
    async def generate(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            model="fake",
            message=ChatMessage(
                role=MessageRole.ASSISTANT,
                content="Hello from test!",
            ),
            usage=TokenUsage(
                prompt_tokens=1,
                completion_tokens=1,
                total_tokens=2,
            ),
        )


class FakeRouter:
    def default_provider(self):
        return FakeProvider()


@pytest.mark.asyncio
async def test_runtime_chat():
    runtime = RuntimeEngine(
        router=FakeRouter(),
        conversation_store=ConversationStore(),
    )

    response = await runtime.chat(
        ChatRequest(
            messages=[
                ChatMessage(
                    role=MessageRole.USER,
                    content="Hello",
                )
            ]
        )
    )

    assert response.message.content == "Hello from test!"
