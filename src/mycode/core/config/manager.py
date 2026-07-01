"""
Central configuration manager.
"""

from mycode.core.config.env import env
from mycode.core.config.loader import load_settings


class ConfigManager:
    """Provides access to all application configuration."""

    def __init__(self) -> None:
        self.settings = load_settings()
        self.environment = env


config = ConfigManager()
