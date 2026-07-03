from pydantic import BaseModel


class TokenUsage(BaseModel):
    """Token usage."""

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0
