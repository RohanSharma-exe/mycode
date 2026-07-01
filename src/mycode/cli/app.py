"""
Command-line interface.
"""

import typer

from mycode.llm import ProviderCapabilities

cli = typer.Typer(
    help="Production-grade AI Agent Framework.",
)


class ExampleService:
    """Temporary service for testing."""


@cli.callback(invoke_without_command=True)
def main() -> None:
    """Start MyCode."""

    capabilities = ProviderCapabilities(
        streaming=True,
        reasoning=True,
        tool_calling=True,
    )

    typer.echo(capabilities.model_dump_json(indent=4))
