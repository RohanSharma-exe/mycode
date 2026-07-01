"""
Vendor client interface.

Only this layer should communicate directly with
SDKs or HTTP APIs.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from mycode.runtime.models import ChatRequest, ChatResponse


class BaseClient(ABC):
    """Base vendor client."""

    @abstractmethod
    async def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """Send a request to the vendor."""
