from mycode.runtime.conversation import Conversation
from mycode.runtime.engine import AIRuntime


class DummyRouter:
    """Simple router used for testing."""

    def default_provider(self):
        raise NotImplementedError


def test_runtime_creation() -> None:
    runtime = AIRuntime(DummyRouter())

    assert isinstance(runtime.conversation, Conversation)
