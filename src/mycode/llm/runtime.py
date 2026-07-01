"""
AI Runtime.

Coordinates conversations and providers.
"""

from __future__ import annotations

from mycode.llm.conversation import Conversation
from mycode.llm.models import ChatRequest, ChatResponse
from mycode.llm.router import ProviderRouter


class AIRuntime:
    """Main AI runtime."""

    def __init__(
        self,
        router: ProviderRouter,
    ) -> None:
        self._router = router
        self._conversation = Conversation()

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
