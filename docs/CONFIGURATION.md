# MyCode Configuration

> Version: v1.0
>
> Configuration controls the behavior of MyCode without requiring code changes.
>
> **Current Status:** Partially Implemented

---

# Table of Contents

1. Overview
2. Design Goals
3. Configuration Sources
4. Configuration Hierarchy
5. settings.yaml
6. Environment Variables
7. Provider Configuration
8. Validation
9. Secrets Management
10. Configuration Lifecycle
11. Best Practices
12. Future Roadmap

---

# Overview

Configuration allows MyCode to adapt to different environments without modifying source code.

Examples include:

- Default provider
- Default model
- Logging level
- API keys
- Timeouts
- Runtime behavior

Configuration should be explicit, validated, and easy to extend.

---

# Design Goals

The configuration system is designed to be:

- Predictable
- Type-safe
- Secure
- Environment-aware
- Easy to validate
- Easy to extend

---

# Configuration Sources

MyCode currently uses two primary configuration sources.

## settings.yaml

Contains application behavior.

Examples:

- application name
- runtime defaults
- logging
- security
- provider defaults

---

## .env

Contains secrets and environment-specific values.

Examples:

```
NVIDIA_API_KEY

OPENAI_API_KEY

GROQ_API_KEY

GEMINI_API_KEY
```

Secrets should never appear in source code.

---

# Configuration Hierarchy

Configuration values should be resolved using the following precedence.

```
Command Line

↓

Environment Variables

↓

settings.yaml

↓

Built-in Defaults
```

Higher levels override lower levels.

---

# ConfigManager

The ConfigManager is responsible for loading and exposing validated configuration.

Responsibilities:

- Load configuration files
- Load environment variables
- Validate configuration
- Provide typed access
- Cache loaded settings

Other components should obtain configuration through ConfigManager rather than reading files directly.

---

# Environment

Environment variables are loaded using the Environment class.

Typical variables include:

```
NVIDIA_API_KEY

OPENAI_API_KEY

GROQ_API_KEY

GEMINI_API_KEY

OLLAMA_BASE_URL
```

Environment variables should remain provider-specific.

---

# settings.yaml

The primary configuration file.

Typical structure:

```yaml
app:
  name: MyCode
  version: 0.1.0

logging:
  level: INFO

runtime:
  default_provider: nvidia
  default_model: nvidia/llama-3.3-nemotron-super-49b-v1
```

The exact schema may evolve over time.

---

# Provider Configuration

Each provider receives a ProviderConfig object.

Typical fields include:

- name
- model
- timeout
- temperature
- max_tokens
- enable_streaming
- max_retries

Provider implementations should not read `.env` directly.

---

# Validation

Configuration should be validated during application startup.

Examples:

- Required values present
- Numeric ranges valid
- Supported provider names
- Existing file paths

Startup should fail fast if configuration is invalid.

---

# Secrets Management

Secrets include:

- API keys
- Access tokens
- Client secrets

Rules:

- Never commit secrets.
- Never log secrets.
- Never hardcode secrets.
- Rotate compromised credentials immediately.

The `.env` file should always be listed in `.gitignore`.

---

# Configuration Lifecycle

```
Application Starts

↓

Load settings.yaml

↓

Load .env

↓

Validate

↓

Create ConfigManager

↓

Inject into Services
```

Configuration should be loaded only once during startup.

---

# Adding New Configuration

When introducing a new configuration option:

1. Add it to the appropriate Pydantic model.
2. Update `settings.yaml` (or `.env` if it is a secret).
3. Document the new option.
4. Add validation if needed.
5. Update tests.

---

# Best Practices

- Keep configuration explicit.
- Prefer typed models over dictionaries.
- Group related settings.
- Avoid deeply nested structures.
- Do not duplicate configuration values.

---

# Future Roadmap

Planned enhancements include:

- Environment-specific configuration files
- Dynamic configuration reload
- Secret manager integration
- Configuration profiles
- Provider-specific overrides
- CLI configuration overrides

---

# Summary

The configuration system provides a single, validated source of truth for application behavior.

By separating application settings from secrets and exposing them through typed models, MyCode remains secure, maintainable, and easy to configure across different environments.

---

# Related Documents

- ARCHITECTURE.md
- DEVELOPMENT_GUIDE.md
- RUNTIME.md
- PROVIDERS.md
