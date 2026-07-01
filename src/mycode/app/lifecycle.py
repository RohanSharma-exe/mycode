"""
Application lifecycle.
"""

from __future__ import annotations


class Lifecycle:
    """Framework startup and shutdown."""

    async def startup(self) -> None:
        """Called during framework startup."""

    async def shutdown(self) -> None:
        """Called during framework shutdown."""
