"""
Shared provider configuration models.
"""

from __future__ import annotations

from pydantic import BaseModel


class ProviderConfig(BaseModel):
    """Configuration shared by every provider."""

    name: str

    api_key: str | None = None

    model: str

    base_url: str | None = None

    timeout: float = 120.0

    temperature: float = 0.7

    max_tokens: int = 4096

    max_retries: int = 3

    enable_streaming: bool = True
