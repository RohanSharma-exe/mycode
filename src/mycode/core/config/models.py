"""
Configuration models.

This module contains all Pydantic models used by the
configuration system.
"""

from pydantic import BaseModel


class AppConfig(BaseModel):
    """Application configuration."""

    name: str
    version: str
    environment: str


class LoggingConfig(BaseModel):
    """Logging configuration."""

    level: str
    file: str


class LLMConfig(BaseModel):
    """Default LLM configuration."""

    default_provider: str
    default_model: str
    timeout: int


class SecurityConfig(BaseModel):
    """Security configuration."""

    workspace_only: bool
    confirm_dangerous_commands: bool


class Settings(BaseModel):
    """Complete application settings."""

    app: AppConfig
    logging: LoggingConfig
    llm: LLMConfig
    security: SecurityConfig
