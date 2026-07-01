"""
LLM-specific exceptions.
"""

from __future__ import annotations


class LLMError(Exception):
    """Base exception for the LLM subsystem."""


class ProviderAlreadyRegisteredError(LLMError):
    """Raised when registering a provider twice."""


class ProviderNotFoundError(LLMError):
    """Raised when a requested provider does not exist."""
