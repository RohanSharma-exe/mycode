"""
Framework bootstrap.
"""

from __future__ import annotations

from mycode.app.application import Application
from mycode.core.config import ConfigManager


def bootstrap() -> Application:
    """Create and initialize the application."""

    application = Application()

    config = ConfigManager()

    application.register(ConfigManager, config)

    return application
