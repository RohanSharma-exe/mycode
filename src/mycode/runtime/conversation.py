"""
Conversation manager.

Maintains conversation history independently of any LLM provider.
"""

from __future__ import annotations

from mycode.runtime.models import ChatMessage, MessageRole


class Conversation:
    """Represents a conversation between a user and an AI model."""

    def __init__(self) -> None:
        """Create an empty conversation."""
        self._messages: list[ChatMessage] = []

    @property
    def messages(self) -> list[ChatMessage]:
        """
        Return a copy of the conversation history.

        Returning a copy prevents callers from modifying the internal state.
        """
        return list(self._messages)

    def add_message(self, message: ChatMessage) -> None:
        """Append a message to the conversation."""
        self._messages.append(message)

    def add_system(self, content: str) -> None:
        """Add a system message."""
        self.add_message(
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=content,
            )
        )

    def add_user(self, content: str) -> None:
        """Add a user message."""
        self.add_message(
            ChatMessage(
                role=MessageRole.USER,
                content=content,
            )
        )

    def add_assistant(self, content: str) -> None:
        """Add an assistant message."""
        self.add_message(
            ChatMessage(
                role=MessageRole.ASSISTANT,
                content=content,
            )
        )

    def add_tool(
        self,
        tool_name: str,
        content: str,
    ) -> None:
        """Add a tool response."""
        self.add_message(
            ChatMessage(
                role=MessageRole.TOOL,
                name=tool_name,
                content=content,
            )
        )

    def clear(self) -> None:
        """Remove all messages."""
        self._messages.clear()

    def __len__(self) -> int:
        """Return the number of messages."""
        return len(self._messages)

    def __iter__(self):
        """Iterate over messages."""
        return iter(self._messages)
