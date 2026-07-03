from typing import Any

from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    """Tool call."""

    id: str

    name: str

    arguments: dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """Tool result."""

    tool_call_id: str

    content: str
