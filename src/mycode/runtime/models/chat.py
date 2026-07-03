from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field

from mycode.runtime.models.tools import ToolCall
from mycode.runtime.models.usage import TokenUsage


class MessageRole(StrEnum):
    """Supported message roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class ChatMessage(BaseModel):
    """Single message."""

    role: MessageRole

    content: str

    name: str | None = None


class ChatRequest(BaseModel):
    """Provider request."""

    messages: list[ChatMessage]

    model: str | None = None

    temperature: float = 0.7

    max_tokens: int | None = None

    stream: bool = False


class ChatResponse(BaseModel):
    """Provider response."""

    message: ChatMessage

    model: str

    finish_reason: str = "stop"

    usage: TokenUsage = Field(default_factory=TokenUsage)

    tool_calls: list[ToolCall] = Field(default_factory=list)
