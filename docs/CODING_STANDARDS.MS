# MyCode Coding Standards

This document defines the coding standards used throughout the MyCode project.

---

# General Principles

Code should be:

* Readable
* Predictable
* Testable
* Modular
* Well documented

Optimize for long-term maintainability rather than short-term convenience.

---

# Python Version

Target:

* Python 3.14+

Use modern language features whenever appropriate.

Examples:

* `StrEnum`
* `pathlib.Path`
* Built-in generic types
* Pattern matching where it improves readability

---

# Formatting

Formatting is handled automatically by Ruff.

Run before every commit:

```bash
uv run ruff format .
```

---

# Linting

Run:

```bash
uv run ruff check .
```

Warnings should be resolved instead of ignored whenever practical.

---

# Type Hints

Public APIs must include type hints.

Good:

```python
def register(provider: BaseProvider) -> None:
    ...
```

Avoid omitting annotations for public methods.

---

# Docstrings

Every public:

* Class
* Function
* Method
* Module

should include a concise docstring describing its purpose.

---

# Comments

Write comments that explain *why*, not *what*.

Good:

```python
# Cache provider instances to avoid repeated client creation.
```

Avoid:

```python
# Increment counter.
counter += 1
```

---

# Imports

Prefer explicit imports.

Good:

```python
from mycode.llm.runtime import RuntimeEngine
```

Avoid wildcard imports:

```python
from module import *
```

---

# Naming Conventions

| Item      | Convention |
| --------- | ---------- |
| Classes   | PascalCase |
| Functions | snake_case |
| Variables | snake_case |
| Constants | UPPER_CASE |
| Modules   | snake_case |
| Packages  | snake_case |

Names should clearly communicate intent.

---

# Project Structure

Each module should have one primary responsibility.

Avoid creating "utility" modules that collect unrelated functionality.

---

# Dependency Rules

Dependencies flow in one direction:

```text
CLI / API / UI
        ↓
Application
        ↓
Runtime
        ↓
Router
        ↓
Provider
        ↓
Client
```

Lower layers must not depend on higher layers.

---

# Dependency Injection

Shared services should be provided through the application's dependency injection container.

Avoid global state.

---

# Error Handling

Raise meaningful exceptions.

Never silently ignore errors.

Prefer explicit error handling over broad `except Exception` blocks.

---

# Logging

Use `LoggerManager`.

Do not instantiate logging libraries directly outside the logging subsystem.

---

# Configuration

Read configuration through `ConfigManager`.

Avoid hard-coded paths, secrets, or provider settings.

---

# Providers

Providers must:

* Implement `BaseProvider`.
* Remain provider-specific.
* Never contain framework business logic.

Vendor SDK usage belongs in client implementations.

---

# Runtime

The runtime owns:

* Conversations
* Routing
* Streaming
* Retry behavior
* Usage tracking
* Middleware (future)

Providers should focus only on generating model responses.

---

# Testing

Core framework components should include automated tests.

Recommended areas:

* Configuration
* Dependency Injection
* Runtime
* Router
* Registry
* Providers
* Tools

---

# Performance

Prefer efficient algorithms and avoid unnecessary object creation.

Profile before optimizing.

---

# Security

Never:

* Execute unvalidated shell commands.
* Trust external input.
* Expose secrets in logs.

Security should be considered during feature design, not added afterward.

---

# Breaking Changes

Changes to public APIs should be minimized.

If a breaking change is necessary:

1. Document it.
2. Update architecture documentation.
3. Update examples.
4. Add migration guidance when appropriate.

---

# Definition of Done

A task is complete when:

* Code is implemented.
* Ruff formatting passes.
* Ruff linting passes.
* Tests pass.
* Documentation is updated if needed.
* The architecture remains consistent.

Every contribution should leave the project in a better state than it was found.
