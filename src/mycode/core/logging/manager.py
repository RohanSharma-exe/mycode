"""
Logger manager.

Provides a stable logging interface for the framework.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from loguru import logger

from mycode.core.config.manager import ConfigManager


class LoggerManager:
    """Application logger."""

    def __init__(self, config: ConfigManager) -> None:
        self._config = config
        self._configure()

    def _configure(self) -> None:
        """Configure Loguru."""

        # Remove Loguru's default logger.
        logger.remove()

        # Ensure the log directory exists.
        Path("logs").mkdir(exist_ok=True)

        # Console logging.
        logger.add(
            sys.stdout,
            level=self._config.settings.logging.level,
            colorize=True,
        )

        # File logging.
        logger.add(
            self._config.settings.logging.file,
            level=self._config.settings.logging.level,
            rotation="10 MB",
            retention="14 days",
            compression="zip",
            enqueue=True,
        )

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write a debug log."""
        logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write an info log."""
        logger.info(message, *args, **kwargs)

    def success(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write a success log."""
        logger.success(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write a warning log."""
        logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write an error log."""
        logger.error(message, *args, **kwargs)

    def exception(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write an exception log."""
        logger.exception(message, *args, **kwargs)

    def critical(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Write a critical log."""
        logger.critical(message, *args, **kwargs)
