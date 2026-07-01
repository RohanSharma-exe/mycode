"""
Configuration loader.
"""

from pathlib import Path

import yaml

from mycode.core.config.models import Settings

SETTINGS_FILE = Path("configs/settings.yaml")


class ConfigLoader:
    """Loads framework configuration."""

    def load(self) -> Settings:
        """Load settings.yaml."""

        with SETTINGS_FILE.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return Settings.model_validate(data)
