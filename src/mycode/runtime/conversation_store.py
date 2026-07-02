"""
Conversation store.

Stores and manages multiple conversations.
"""

from __future__ import annotations

from uuid import uuid4

from mycode.runtime.conversation import Conversation


class ConversationStore:
    """Stores multiple conversations."""

    def __init__(self) -> None:
        """Initialize the conversation store."""
        self._conversations: dict[str, Conversation] = {}

    def create(self) -> str:
        """
        Create a new conversation.

        Returns:
            The generated conversation ID.
        """
        conversation_id = str(uuid4())
        self._conversations[conversation_id] = Conversation()
        return conversation_id

    def get(self, conversation_id: str) -> Conversation:
        """
        Retrieve a conversation.

        Raises:
            KeyError: If the conversation does not exist.
        """
        return self._conversations[conversation_id]

    def delete(self, conversation_id: str) -> None:
        """Delete a conversation if it exists."""
        self._conversations.pop(conversation_id, None)

    def exists(self, conversation_id: str) -> bool:
        """Return True if the conversation exists."""
        return conversation_id in self._conversations

    def ids(self) -> list[str]:
        """Return all conversation IDs."""
        return list(self._conversations.keys())

    def clear(self) -> None:
        """Remove every conversation."""
        self._conversations.clear()

    def __len__(self) -> int:
        """Return the number of stored conversations."""
        return len(self._conversations)
