from mycode.runtime import (
    ConversationStore,
    RuntimeEngine,
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
