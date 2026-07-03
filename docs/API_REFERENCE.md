# MyCode API Reference

> Version: v0.1.0-alpha
>
> This document provides a reference for the public Python API exposed by MyCode.
>
> **Current Status:** Partial (Core Runtime)

---

# Table of Contents

1. Introduction
2. Public API Policy
3. Application
4. Configuration
5. Runtime
6. Providers
7. Models
8. CLI
9. Exceptions
10. Stability

---

# Introduction

The public API consists of modules intended for application developers.

Internal modules may change without notice.

Only documented APIs should be considered stable.

---

# Public API Policy

Public modules include:

```
mycode.app

mycode.runtime

mycode.core.config

mycode.cli
```

Internal implementation details should not be imported directly.

Example

Good

```python
from mycode.runtime import RuntimeEngine
```

Avoid

```python
from mycode.runtime.providers.nvidia_client import NVIDIAClient
```

unless implementing a provider.

---

# Application

## bootstrap()

Creates and initializes the framework.

Example

```python
from mycode.app.bootstrap import bootstrap

app = bootstrap()
```

Returns

```
Application
```

---

## Application

Primary service container.

Methods

### register()

Registers a shared service.

```python
application.register(
    RuntimeEngine,
    runtime,
)
```

---

### resolve()

Retrieves a registered service.

```python
runtime = application.resolve(RuntimeEngine)
```

---

### shutdown()

Gracefully releases shared resources.

```python
await application.shutdown()
```

---

# Configuration

## ConfigManager

Loads application configuration.

Properties

```
settings

environment
```

---

# Runtime

## RuntimeEngine

Primary AI execution entry point.

Methods

### chat()

```python
response = await runtime.chat(request)
```

Returns

```
ChatResponse
```

---

### clear()

Clears the active conversation.

---

# ProviderRouter

Methods

```
default_provider()

get(name)
```

---

# ProviderRegistry

Methods

```
register()

unregister()

get()

exists()

names()

clear()
```

---

# ConversationStore

Responsible for managing conversations.

Current implementation provides in-memory storage.

Future versions may support persistent backends.

---

# Models

## ChatRequest

Represents an AI request.

Fields

```
messages

model

temperature

max_tokens

stream
```

---

## ChatResponse

Represents an AI response.

Fields

```
message

model

usage

finish_reason

tool_calls
```

---

## ChatMessage

Represents one conversation message.

Fields

```
role

content

name
```

---

## TokenUsage

Tracks token statistics.

Fields

```
prompt_tokens

completion_tokens

total_tokens
```

---

# Providers

Current provider

```
NVIDIA
```

Future providers

```
OpenAI

Groq

Gemini

Ollama

OpenRouter
```

All providers implement the BaseProvider interface.

---

# CLI

Current commands

```
doctor

version

config
```

See:

```
CLI_REFERENCE.md
```

for complete usage.

---

# Exceptions

Public exceptions include:

```
ProviderNotFoundError

ProviderAlreadyRegisteredError
```

Additional exceptions may be added in future releases.

---

# Stability

Current API status

| Component | Stability |
|-----------|-----------|
| Configuration | Stable |
| Runtime | Stable |
| Registry | Stable |
| Router | Stable |
| Models | Stable |
| Providers | Experimental |
| CLI | Stable |

---

# Version Compatibility

Public APIs follow Semantic Versioning.

Breaking changes will only occur in major releases.

Experimental APIs may change before version 1.0.

---

# Related Documents

- RUNTIME.md
- PROVIDERS.md
- CONFIGURATION.md
- CLI_REFERENCE.md

---

# Summary

The API Reference documents the stable public interfaces of MyCode.

Developers should rely on these APIs when building applications or extensions, while avoiding dependencies on internal implementation details.
