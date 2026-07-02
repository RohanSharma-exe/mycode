"""
CLI commands.

All CLI commands live in this module.
"""

from __future__ import annotations

import asyncio

import typer

from mycode.app.bootstrap import bootstrap
from mycode.core.config import ConfigManager
from mycode.core.logging import LoggerManager
from mycode.runtime.engine import RuntimeEngine
from mycode.runtime.models import (
    ChatMessage,
    ChatRequest,
    MessageRole,
)

app = typer.Typer()


@app.command()
def doctor() -> None:
    """Display framework diagnostics."""

    application = bootstrap()

    config = application.resolve(ConfigManager)
    logger = application.resolve(LoggerManager)

    typer.echo("=== MyCode Doctor ===")
    typer.echo(f"Application : {config.settings.app.name}")
    typer.echo(f"Version     : {config.settings.app.version}")
    typer.echo(f"Environment : {config.settings.app.environment}")
    typer.echo(f"Provider    : {config.settings.llm.default_provider}")
    typer.echo(f"Model       : {config.settings.llm.default_model}")
    typer.echo(f"Ollama URL  : {config.environment.OLLAMA_BASE_URL}")

    logger.success("Doctor completed successfully.")


@app.command()
def version() -> None:
    """Display framework version."""

    application = bootstrap()

    config = application.resolve(ConfigManager)

    typer.echo(f"{config.settings.app.name} v{config.settings.app.version}")


@app.command()
def config() -> None:
    """Display the loaded configuration."""

    application = bootstrap()

    config_manager = application.resolve(ConfigManager)

    typer.echo(config_manager.settings.model_dump_json(indent=4))


async def _prompt_async(prompt: str) -> None:
    """Execute a prompt."""

    application = bootstrap()

    try:
        runtime = application.resolve(RuntimeEngine)

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=MessageRole.USER,
                    content=prompt,
                )
            ]
        )

        response = await runtime.chat(request)

        typer.echo()
        typer.echo(response.message.content)
        typer.echo()

    finally:
        await application.shutdown()


@app.command()
def prompt(prompt: str) -> None:
    """
    Send a prompt to the configured provider.
    """

    asyncio.run(_prompt_async(prompt))
