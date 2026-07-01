"""
Framework bootstrap.
"""

from mycode.app.application import Application
from mycode.core.config import ConfigManager
from mycode.core.events import EventBus
from mycode.core.logging import LoggerManager


def bootstrap() -> Application:
    """Initialize the application."""

    application = Application()

    config = ConfigManager()

    logger = LoggerManager(config)

    application.register(ConfigManager, config)
    application.register(LoggerManager, logger)
    events = EventBus()

    application.register(EventBus, events)

    return application
