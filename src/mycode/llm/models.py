"""
Core models used by the AI Runtime.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


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


class TokenUsage(BaseModel):
    """Token usage."""

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


class ToolCall(BaseModel):
    """Tool call."""

    id: str

    name: str

    arguments: dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """Tool result."""

    tool_call_id: str

    content: str


class ModelInfo(BaseModel):
    """Information about a model."""

    id: str

    provider: str

    context_window: int

    max_output_tokens: int

    reasoning: bool = False

    vision: bool = False

    tool_calling: bool = False


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


class StreamChunk(BaseModel):
    """Streaming chunk."""

    content: str = ""

    reasoning: str = ""

    tool_calls: list[ToolCall] = Field(default_factory=list)

    finished: bool = False
