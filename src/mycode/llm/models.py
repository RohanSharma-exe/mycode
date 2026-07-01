"""
Core models used by the AI Runtime.

These models are provider-independent and represent the
standard interface used throughout MyCode.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class MessageRole(StrEnum):
    """Supported chat message roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class ChatMessage(BaseModel):
    """Represents a single chat message."""

    role: MessageRole

    content: str

    name: str | None = None


class TokenUsage(BaseModel):
    """Token usage information."""

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


class ToolCall(BaseModel):
    """Represents a tool call requested by the model."""

    id: str

    name: str

    arguments: dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """Represents the result returned by a tool."""

    tool_call_id: str

    content: str


class ChatRequest(BaseModel):
    """Request sent to an LLM provider."""

    messages: list[ChatMessage]

    model: str | None = None

    temperature: float = 0.7

    max_tokens: int | None = None

    stream: bool = False


class ChatResponse(BaseModel):
    """Response returned by an LLM provider."""

    message: ChatMessage

    model: str

    finish_reason: str = "stop"

    usage: TokenUsage = Field(default_factory=TokenUsage)

    tool_calls: list[ToolCall] = Field(default_factory=list)


class StreamChunk(BaseModel):
    """Represents one streamed chunk."""

    content: str = ""

    reasoning: str = ""

    tool_calls: list[ToolCall] = Field(default_factory=list)

    finished: bool = False
