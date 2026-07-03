from pydantic import BaseModel


class ModelInfo(BaseModel):
    """Information about a model."""

    id: str

    provider: str

    context_window: int

    max_output_tokens: int

    reasoning: bool = False

    vision: bool = False

    tool_calling: bool = False
