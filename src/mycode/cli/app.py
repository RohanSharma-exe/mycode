"""
Command-line interface.
"""

import typer

from mycode.llm import ChatMessage, ChatRequest, MessageRole

cli = typer.Typer(
    help="Production-grade AI Agent Framework.",
)


class ExampleService:
    """Temporary service for testing."""


@cli.callback(invoke_without_command=True)
def main() -> None:
    """Start MyCode."""

    request = ChatRequest(
        messages=[
            ChatMessage(
                role=MessageRole.USER,
                content="Hello MyCode!",
            )
        ]
    )

    typer.echo(request.model_dump_json(indent=4))
