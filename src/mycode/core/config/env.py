"""
Environment variable loader.
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

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


env = Environment()
