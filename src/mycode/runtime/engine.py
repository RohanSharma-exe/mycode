"""
AI Runtime.

Coordinates conversations and providers.
"""

from __future__ import annotations

from mycode.runtime.conversation import Conversation
from mycode.runtime.conversation_store import ConversationStore
from mycode.runtime.models import ChatRequest, ChatResponse
from mycode.runtime.router import ProviderRouter


class RuntimeEngine:
    """Main AI runtime."""

    def __init__(
        self,
        router: ProviderRouter,
        conversation_store: ConversationStore,
    ) -> None:
        """Initialize the runtime."""

        self._router = router
        self._conversation_store = conversation_store

    @property
    def router(self) -> ProviderRouter:
        """Return the provider router."""
        return self._router

    @property
    def conversation_store(self) -> ConversationStore:
        """Return the conversation store."""
        return self._conversation_store

    @property
    def conversation(self) -> Conversation:
        """Return the active conversation."""
        return self._conversation

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Send a chat request using the default provider.
        """

        # Keep the runtime's conversation synchronized.
        for message in request.messages:
            self._conversation.add_message(message)

        provider = self._router.default_provider()

        response = await provider.generate(request)

        self._conversation.add_message(response.message)

        return response

    def clear(self) -> None:
        """Clear the current conversation."""
        self._conversation.clear()
