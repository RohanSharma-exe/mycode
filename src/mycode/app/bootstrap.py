"""
Framework bootstrap.
"""

import httpx

from mycode.app.application import Application
from mycode.core.config import ConfigManager
from mycode.core.events import EventBus
from mycode.core.logging import LoggerManager
from mycode.runtime import ProviderConfig
from mycode.runtime.conversation_store import ConversationStore
from mycode.runtime.engine import RuntimeEngine
from mycode.runtime.factory import ProviderFactory
from mycode.runtime.network import HTTPClient
from mycode.runtime.registry import ProviderRegistry
from mycode.runtime.router import ProviderRouter


def bootstrap() -> Application:
    """Initialize the application."""

    application = Application()

    config = ConfigManager()

    nvidia_config = ProviderConfig(
        name="nvidia",
        api_key=config.env.nvidia_api_key,
        model=config.settings.llm.default_model,
        base_url=config.settings.providers.nvidia.base_url,
        timeout=config.settings.llm.timeout,
        temperature=config.settings.llm.temperature,
        max_tokens=config.settings.llm.max_tokens,
    )

    logger = LoggerManager(config)

    events = EventBus()

    registry = ProviderRegistry()

    factory = ProviderFactory()

    router = ProviderRouter(
        registry=registry,
        config=config,
    )

    conversation_store = ConversationStore()

    async_client = httpx.AsyncClient(
        timeout=config.settings.llm.timeout,
    )

    http_client = HTTPClient(async_client)

    runtime = RuntimeEngine(
        router=router,
        conversation_store=conversation_store,
    )

    application.register(ConfigManager, config)
    application.register(LoggerManager, logger)
    events = EventBus()

    application.register(EventBus, events)

    registry = ProviderRegistry()

    router = ProviderRouter(
        registry=registry,
        config=config,
    )

    application.register(ConfigManager, config)

    application.register(ProviderConfig, nvidia_config)

    application.register(LoggerManager, logger)

    application.register(EventBus, events)

    application.register(ProviderRegistry, registry)

    application.register(ProviderFactory, factory)

    application.register(ProviderRouter, router)

    application.register(ConversationStore, conversation_store)

    application.register(httpx.AsyncClient, async_client)

    application.register(HTTPClient, http_client)

    application.register(RuntimeEngine, runtime)

    return application
