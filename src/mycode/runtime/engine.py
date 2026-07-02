"""
AI Runtime.

Coordinates conversations and providers.
"""

from __future__ import annotations

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

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Generate a chat response using the configured provider.
        """

        provider = self._router.default_provider()

        return await provider.generate(request)
