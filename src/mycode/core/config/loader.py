"""
Loads YAML configuration files.
"""

from pathlib import Path

import yaml

from mycode.core.config.models import Settings

CONFIG_FILE = Path("configs/settings.yaml")


def load_settings() -> Settings:
    """Load and validate the application settings."""

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Settings.model_validate(data)
