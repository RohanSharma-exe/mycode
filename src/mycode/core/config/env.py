"""
Environment variables.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(BaseSettings):
    """Environment variables loaded from .env."""

    NVIDIA_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    OPENROUTER_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    OLLAMA_BASE_URL: str = "http://localhost:11434"

    NVIDIA_BASE_URL: str = "https://integrate.api.nvidia.com/v1"

    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"

    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    OPENAI_BASE_URL: str = "https://api.openai.com/v1"

    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
