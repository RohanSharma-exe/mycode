"""
Logging formatter.
"""

from loguru import Record


def console_formatter(record: Record) -> str:
    """Pretty console logs."""

    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>\n"
    )
