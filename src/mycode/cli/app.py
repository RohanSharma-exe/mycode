"""
Command-line interface.
"""

import typer

from mycode.app.bootstrap import bootstrap

cli = typer.Typer(
    help="Production-grade AI Agent Framework.",
)


@cli.callback(invoke_without_command=True)
def main() -> None:
    """Start MyCode."""

    print(type(bootstrap))
    print(bootstrap)

    application = bootstrap()

    typer.echo("🚀 MyCode Started")
    typer.echo(f"Application: {application}")
