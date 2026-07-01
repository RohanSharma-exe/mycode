# MyCode Architecture

## Overview

MyCode is a modular, provider-agnostic AI Agent Framework designed to support multiple user interfaces (CLI, REST API, VS Code Extension, Web UI) while sharing a single application core.

The framework follows a layered architecture with strict dependency direction and constructor dependency injection.

---

# Architecture Principles

## 1. Single Responsibility Principle

Every module should have one responsibility.

Examples:

* `LLMRouter` → Routes LLM requests.
* `ToolManager` → Manages tool execution.
* `MemoryManager` → Manages memory.
* `Application` → Owns framework services.

Avoid large classes that perform multiple unrelated tasks.

---

## 2. Dependency Direction

Dependencies must always flow downward.

```text
CLI / API / UI
        │
Application
        │
Managers
        │
Services
        │
Providers
        │
Infrastructure
```

Higher layers may depend on lower layers.

Lower layers must never depend on higher layers.

---

## 3. Dependency Injection

Dependencies are injected through constructors.

Good:

```python
class LLMRouter:

    def __init__(
        self,
        logger: Logger,
        config: ConfigManager,
    ) -> None:
        ...
```

Avoid:

```python
logger = Logger()

config = ConfigManager()
```

or

```python
global logger
```

---

## 4. Provider Independence

The framework never communicates directly with a provider.

Instead:

```text
Agent
    │
LLM Router
    │
Base Provider
    │
NVIDIA
Gemini
Groq
OpenRouter
Ollama
```

Every provider implements the same interface.

Changing providers should never require changing agent code.

---

## 5. Tool Independence

The agent never accesses the operating system directly.

Instead:

```text
Agent
    │
Tool Manager
    │
Filesystem Tool
Shell Tool
Git Tool
Python Tool
```

Every tool inherits from the same base interface.

---

## 6. Security

Every dangerous action passes through the security layer.

Examples:

* Shell execution
* File deletion
* Git push
* Network requests

Security is never bypassed.

---

## 7. Event-Driven Design

Components communicate through events whenever appropriate.

Example:

```text
Tool Started

↓

Logger

↓

Metrics

↓

Plugins

↓

UI
```

This reduces coupling between modules.

---

## 8. Plugin-First Design

Plugins may register:

* Providers
* Tools
* Skills
* Workflows
* CLI Commands
* Event Listeners

Core framework code should not require modification to support plugins.

---

# Layer Responsibilities

## CLI

Responsibilities:

* Parse commands.
* Display output.
* Forward requests to the application.

The CLI contains no business logic.

---

## Application

Responsibilities:

* Create shared services.
* Initialize managers.
* Handle startup.
* Handle shutdown.

Everything starts here.

---

## Core

Contains shared framework infrastructure.

Examples:

* Configuration
* Logging
* Registry
* Security
* Events
* Utilities

---

## LLM

Responsible only for model communication.

Contains:

* Provider interfaces
* Provider implementations
* Router
* Registry

No business logic belongs here.

---

## Tools

Atomic operations.

Examples:

* Read file
* Write file
* Execute shell
* Run Python
* Git
* Browser

Tools should be reusable.

---

## Skills

Reusable combinations of tools.

Example:

Fix Python Errors

↓

Filesystem

↓

LLM

↓

Pytest

↓

Patch

Skills should not directly communicate with providers.

---

## Workflows

High-level orchestration.

Example:

Review Repository

↓

Read Files

↓

Analyze

↓

Generate Report

↓

Commit

↓

Open Pull Request

Workflows coordinate multiple skills.

---

## Agent

Responsible for reasoning.

Components include:

* Planner
* Executor
* Reflection
* Reasoning

The agent decides *what* to do.

Tools perform the actual work.

---

## Memory

Three levels:

* Conversation Memory
* Session Memory
* Long-Term Memory

Memory implementation should be replaceable.

---

## MCP

Responsible for communication with Model Context Protocol servers.

MCP servers are treated as external tool providers.

---

## Plugins

Loads third-party extensions dynamically.

Plugins may extend the framework without modifying core code.

---

# Coding Standards

## Naming

| Item            | Convention          |
| --------------- | ------------------- |
| Classes         | PascalCase          |
| Functions       | snake_case          |
| Variables       | snake_case          |
| Constants       | UPPER_CASE          |
| Private Members | _leading_underscore |

---

## File Size

Preferred:

200–300 lines

Maximum:

500 lines

Split large files into multiple modules.

---

## Comments

Comments should explain intent.

Avoid obvious comments.

Good:

```python
# Cache provider instances to avoid recreating clients.
```

Avoid:

```python
# Increment counter.
counter += 1
```

---

## Type Hints

All public functions and methods must include type hints.

---

## Docstrings

All public classes and methods require docstrings.

---

## Async

Use asynchronous programming for:

* HTTP requests
* LLM providers
* MCP
* Database access
* Long-running I/O

Avoid async where it provides no benefit.

---

# External Libraries

External libraries are adapters, not the architecture.

Current stack:

* uv
* Ruff
* Typer
* Rich
* Loguru
* Pydantic
* HTTPX
* orjson
* PyYAML

Official provider SDKs are preferred over third-party wrappers when appropriate.

---

# Future Components

Planned additions:

* REST API
* VS Code Extension
* Web Dashboard
* Multi-Agent Collaboration
* Voice Interface
* Docker Integration
* Kubernetes Support

These should integrate without requiring architectural changes.

---

# Development Workflow

For every completed feature:

1. Format code.
2. Run lint checks.
3. Execute tests.
4. Commit changes.

Recommended commands:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest
```

---

# Design Philosophy

MyCode is an AI Agent Framework.

The LLM is a replaceable component.

The framework owns:

* Application lifecycle
* Architecture
* Tool execution
* Memory
* Security
* Skills
* Workflows
* Plugins

AI providers are implementation details behind stable interfaces.
