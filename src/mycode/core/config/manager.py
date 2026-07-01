"""
Configuration manager.
"""

from mycode.core.config.env import Environment
from mycode.core.config.loader import ConfigLoader
from mycode.core.config.models import Settings


class ConfigManager:
    """Application configuration."""

    def __init__(self) -> None:
        self.environment = Environment()

        self.settings: Settings = ConfigLoader().load()
