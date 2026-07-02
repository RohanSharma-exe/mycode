"""
Framework bootstrap.
"""

from __future__ import annotations

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
from mycode.runtime.providers.nvidia_client import NVIDIAClient
from mycode.runtime.providers.nvidia_provider import NVIDIAProvider
from mycode.runtime.registry import ProviderRegistry
from mycode.runtime.router import ProviderRouter


def bootstrap() -> Application:
    """Build the application and register all shared services."""

    application = Application()

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    config = ConfigManager()

    provider_config = ProviderConfig(
        name="nvidia",
        api_key=config.environment.NVIDIA_API_KEY,
        base_url=config.environment.NVIDIA_BASE_URL,
        model=config.settings.llm.default_model,
        timeout=config.settings.llm.timeout,
        temperature=config.settings.llm.temperature,
        max_tokens=config.settings.llm.max_tokens,
    )

    # ------------------------------------------------------------------
    # Core Services
    # ------------------------------------------------------------------

    logger = LoggerManager(config)

    events = EventBus()

    registry = ProviderRegistry()

    factory = ProviderFactory()

    router = ProviderRouter(
        registry=registry,
        config=config,
    )

    conversation_store = ConversationStore()

    # ------------------------------------------------------------------
    # Networking
    # ------------------------------------------------------------------

    async_client = httpx.AsyncClient(
        timeout=config.settings.llm.timeout,
    )

    http_client = HTTPClient(async_client)

    # ------------------------------------------------------------------
    # Providers
    # ------------------------------------------------------------------

    nvidia_client = NVIDIAClient(
        http_client=http_client,
        config=provider_config,
    )

    nvidia_provider = NVIDIAProvider(
        config=provider_config,
        client=nvidia_client,
    )

    registry.register(nvidia_provider)

    # ------------------------------------------------------------------
    # Runtime
    # ------------------------------------------------------------------

    runtime = RuntimeEngine(
        router=router,
        conversation_store=conversation_store,
    )

    # ------------------------------------------------------------------
    # Dependency Injection
    # ------------------------------------------------------------------

    application.register(ConfigManager, config)

    application.register(LoggerManager, logger)

    application.register(EventBus, events)

    application.register(ProviderConfig, provider_config)

    application.register(ProviderRegistry, registry)

    application.register(ProviderFactory, factory)

    application.register(ProviderRouter, router)

    application.register(ConversationStore, conversation_store)

    application.register(httpx.AsyncClient, async_client)

    application.register(HTTPClient, http_client)

    application.register(RuntimeEngine, runtime)

    return application
