from mycode.core.config import config

print(config.settings.app.name)

print(config.settings.app.version)

print(config.settings.llm.default_provider)

print(config.environment.OLLAMA_BASE_URL)
