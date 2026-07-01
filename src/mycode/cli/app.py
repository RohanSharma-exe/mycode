"""
Command-line interface.
"""

import typer

from mycode.app.bootstrap import bootstrap
from mycode.core.config.manager import ConfigManager

cli = typer.Typer(
    help="Production-grade AI Agent Framework.",
)


class ExampleService:
    """Temporary service for testing."""


@cli.callback(invoke_without_command=True)
def main() -> None:
    """Start MyCode."""

    application = bootstrap()

    config = application.resolve(ConfigManager)

    typer.echo("🚀 MyCode Started")
    typer.echo(f"App: {config.settings.app.name}")
    typer.echo(f"Version: {config.settings.app.version}")
    typer.echo(f"Provider: {config.settings.llm.default_provider}")
    typer.echo(f"Ollama: {config.environment.OLLAMA_BASE_URL}")
