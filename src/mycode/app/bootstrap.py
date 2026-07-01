"""
Framework bootstrap.
"""

from mycode.app.application import Application
from mycode.core.config import ConfigManager
from mycode.core.events import EventBus
from mycode.core.logging import LoggerManager
from mycode.llm.registry import ProviderRegistry
from mycode.llm.router import ProviderRouter
from mycode.llm.runtime import AIRuntime


def bootstrap() -> Application:
    """Initialize the application."""

    application = Application()

    config = ConfigManager()

    logger = LoggerManager(config)

    application.register(ConfigManager, config)
    application.register(LoggerManager, logger)
    events = EventBus()

    application.register(EventBus, events)

    registry = ProviderRegistry()

    router = ProviderRouter(
        registry=registry,
        config=config,
    )

    application.register(ProviderRegistry, registry)
    application.register(ProviderRouter, router)

    runtime = AIRuntime(router)

    application.register(AIRuntime, runtime)

    return application
