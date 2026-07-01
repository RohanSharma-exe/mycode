"""
Provider capability models.
"""

from __future__ import annotations

from pydantic import BaseModel


class ProviderCapabilities(BaseModel):
    """Capabilities supported by a provider."""

    streaming: bool = True

    reasoning: bool = False

    vision: bool = False

    tool_calling: bool = False

    embeddings: bool = False

    json_mode: bool = False

    function_calling: bool = False
