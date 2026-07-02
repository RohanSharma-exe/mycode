"""
MyCode command-line interface.
"""

from __future__ import annotations

import typer

from mycode.cli.commands import app as commands

app = typer.Typer(
    name="mycode",
    help="Production-grade AI Agent Framework.",
    no_args_is_help=True,
)

app.add_typer(commands)


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
