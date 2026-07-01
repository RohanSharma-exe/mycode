from mycode.runtime.conversation import Conversation
from mycode.runtime.engine import RuntimeEngine


class DummyRouter:
    """Simple router used for testing."""

    def default_provider(self):
        raise NotImplementedError


def test_runtime_creation() -> None:
    runtime = RuntimeEngine(DummyRouter())

    assert isinstance(runtime.conversation, Conversation)
