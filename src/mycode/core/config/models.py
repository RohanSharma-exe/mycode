"""
Configuration models.
"""

from pydantic import BaseModel


class AppConfig(BaseModel):
    """Application settings."""

    name: str
    version: str
    environment: str


class LoggingConfig(BaseModel):
    """Logging settings."""

    level: str
    file: str


class LLMConfig(BaseModel):
    """Default LLM settings."""

    default_provider: str

    default_model: str

    timeout: int

    temperature: float

    max_tokens: int


class SecurityConfig(BaseModel):
    """Security settings."""

    workspace_only: bool
    confirm_dangerous_commands: bool


class Settings(BaseModel):
    """Root application settings."""

    app: AppConfig
    logging: LoggingConfig
    llm: LLMConfig
    security: SecurityConfig
