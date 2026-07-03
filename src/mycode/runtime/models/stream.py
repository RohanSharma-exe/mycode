from pydantic import BaseModel, Field

from mycode.runtime.models.tools import ToolCall


class StreamChunk(BaseModel):
    """Streaming chunk."""

    content: str = ""

    reasoning: str = ""

    tool_calls: list[ToolCall] = Field(default_factory=list)

    finished: bool = False
