# MyCode Coding Standards

> **Version:** v1.0
>
> These standards apply to every line of code written for MyCode.
>
> The goal is consistency, readability, maintainability, and production-quality software.

---

# Table of Contents

1. Philosophy
2. General Principles
3. Project Structure
4. Python Standards
5. Naming Conventions
6. File Organization
7. Imports
8. Type Hints
9. Documentation
10. Error Handling
11. Logging
12. Async Programming
13. Dependency Injection
14. Configuration
15. Providers
16. Runtime
17. Testing
18. Performance
19. Security
20. Git Standards
21. Code Review Checklist

---

# Philosophy

Code is read far more often than it is written.

Every line should optimize for:

- Readability
- Simplicity
- Correctness
- Maintainability

Avoid clever code.

Prefer boring, predictable code.

---

# General Principles

## Single Responsibility Principle

Every class should have one purpose.

Good

```
HTTPClient

ProviderRouter

ConversationStore
```

Bad

```
RuntimeManager

HelperUtils

CommonFunctions
```

---

## Explicit is Better Than Implicit

Avoid hidden behavior.

Good

```python
provider.generate(request)
```

Bad

```python
provider.run()
```

---

## Composition Over Inheritance

Prefer

```
Runtime

↓

Provider

↓

HTTP Client
```

instead of deep inheritance hierarchies.

---

## Dependency Injection

Never create dependencies inside classes.

Bad

```python
class Runtime:

    def __init__(self):
        self.client = HTTPClient()
```

Good

```python
class Runtime:

    def __init__(self, client: HTTPClient):
        self.client = client
```

---

# Project Structure

Each package should represent one responsibility.

```
core/
runtime/
memory/
providers/
tools/
agents/
workflows/
```

Never mix responsibilities.

---

# Python Standards

Python Version

```
Python 3.14+
```

Always use:

- type hints
- dataclasses or Pydantic models where appropriate
- pathlib instead of os.path
- context managers
- f-strings

Avoid

```
print()
```

except for CLI output.

---

# Naming Conventions

## Classes

PascalCase

```
RuntimeEngine

ProviderRouter

ConversationStore
```

---

## Functions

snake_case

```
generate_response()

register_provider()
```

---

## Variables

snake_case

```
provider_name

conversation_store
```

---

## Constants

UPPER_CASE

```
DEFAULT_TIMEOUT

DEFAULT_PROVIDER
```

---

## Private Members

Prefix with underscore.

```
_client

_router

_registry
```

---

# File Organization

Each file should contain one primary concept.

Good

```
http_client.py

provider_router.py

conversation_store.py
```

Avoid

```
utils.py

helpers.py

common.py
```

---

# Imports

Always group imports.

Standard Library

```python
from pathlib import Path
```

Third Party

```python
import httpx
import typer
```

Project

```python
from mycode.runtime import RuntimeEngine
```

Never use wildcard imports.

Bad

```python
from runtime import *
```

---

# Type Hints

Every public function must include type hints.

Good

```python
def generate(
    request: ChatRequest,
) -> ChatResponse:
```

Avoid

```python
def generate(request):
```

---

# Documentation

Every public class must include a docstring.

Example

```python
class RuntimeEngine:
    """Coordinates AI execution."""
```

Every public function should explain:

- Purpose
- Parameters
- Return value

Keep docstrings concise.

---

# Error Handling

Never swallow exceptions.

Bad

```python
except:
    pass
```

Good

```python
except HTTPRequestError as exc:
    logger.error(str(exc))
    raise
```

Create domain-specific exceptions.

Example

```
ProviderError

NetworkError

ConfigurationError
```

---

# Logging

Never use print() for debugging.

Use LoggerManager.

Good

```python
logger.info("Provider initialized.")
```

Avoid logging secrets.

Never log:

- API keys
- Tokens
- Passwords

---

# Async Programming

Network operations must be asynchronous.

Good

```python
await client.post(...)
```

Avoid blocking calls.

Bad

```python
requests.post(...)
```

Never call

```
time.sleep()
```

inside async code.

---

# Dependency Injection

Shared services belong in bootstrap.

Resolve services through Application.

Good

```python
runtime = application.resolve(RuntimeEngine)
```

Avoid

```python
RuntimeEngine()
```

inside feature code.

---

# Configuration

Application settings belong in

```
settings.yaml
```

Secrets belong in

```
.env
```

Never commit secrets.

---

# Providers

Each provider consists of:

```
Provider

↓

Provider Client
```

Provider

- Business logic

Client

- API communication

HTTPClient

- Transport

Never mix responsibilities.

---

# Runtime

RuntimeEngine is the only public AI execution entry point.

Other modules should never call providers directly.

Correct

```
Runtime

↓

Provider
```

Incorrect

```
CLI

↓

Provider
```

---

# Testing

Every feature requires tests.

Required

- Unit Tests

Recommended

- Integration Tests

Never require internet access for unit tests.

Mock external APIs.

---

# Performance

Reuse expensive objects.

Examples

- AsyncClient
- Logger
- Configuration

Avoid unnecessary allocations.

Prefer async operations.

---

# Security

Never commit:

- API Keys
- Tokens
- Passwords

Always include

```
.env
```

in

```
.gitignore
```

Rotate compromised keys immediately.

---

# Git Standards

Commit messages follow Conventional Commits.

Examples

```
feat(runtime): add conversation memory

fix(cli): improve prompt command

refactor(network): simplify HTTP client

docs(runtime): update architecture

test(router): improve provider tests
```

---

# Code Review Checklist

Before merging:

- Ruff passes
- Pytest passes
- Documentation updated
- Type hints complete
- Docstrings present
- No duplicated logic
- No dead code
- No secrets committed
- No debug prints
- Architecture respected

---

# Principles to Remember

Always prefer:

Simple over clever.

Explicit over implicit.

Composition over inheritance.

Interfaces over implementations.

Dependency injection over object creation.

Readable over short.

Maintainable over clever.

---

# Final Rule

Every pull request should leave the codebase in a better state than it was before.

Small, continuous improvements are preferred over large rewrites.
