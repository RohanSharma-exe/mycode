# MyCode Project Structure

> **Version:** v1.0
>
> This document describes the organization of the MyCode source code and the responsibilities of every directory.
>
> Every contributor should read this document before adding new files.

---

# Table of Contents

1. Philosophy
2. Repository Layout
3. Source Tree
4. Package Responsibilities
5. Dependency Rules
6. File Naming
7. Folder Guidelines
8. Tests
9. Documentation
10. Assets
11. Future Expansion

---

# Philosophy

A predictable project structure is one of the most important characteristics of a maintainable framework.

Every folder in MyCode has **one clear responsibility**.

If you're unsure where something belongs, ask:

> **"What is this module's primary responsibility?"**

The answer determines its location.

---

# Repository Layout

```
mycode/

├── configs/
├── docs/
├── logs/
├── plugins/
├── scripts/
├── src/
├── tests/
│
├── .env
├── .gitignore
├── pyproject.toml
├── pytest.ini
├── README.md
├── ruff.toml
└── uv.lock
```

---

# Root Directory

The root directory should contain only project-level files.

Allowed:

- README
- pyproject.toml
- uv.lock
- LICENSE
- CHANGELOG
- .gitignore

Avoid placing application code here.

---

# configs/

Purpose:

Store application configuration files.

Examples:

```
settings.yaml

logging.yaml

providers.yaml
```

Rules:

- No secrets.
- No Python code.
- Environment-independent configuration only.

---

# docs/

Purpose:

Project documentation.

Examples:

```
ARCHITECTURE.md

CODING_STANDARDS.md

RUNTIME.md

PROVIDERS.md
```

Rules:

Documentation should evolve alongside the code.

---

# logs/

Purpose:

Application log files.

Rules:

- Never commit log files.
- Automatically generated.
- Can be safely deleted.

---

# plugins/

Purpose:

External plugins.

Future examples:

```
WeatherPlugin

SlackPlugin

GitHubPlugin
```

Core framework should never depend on plugins.

---

# scripts/

Purpose:

Developer utilities.

Examples:

```
build.py

release.py

generate_docs.py
```

Scripts should never contain runtime logic.

---

# src/

Purpose:

Application source code.

Everything inside this directory is importable.

```
src/

└── mycode/
```

---

# src/mycode/

Main package.

```
mycode/

app/

cli/

core/

runtime/

memory/

mcp/

tools/

agents/

workflows/

plugins/

api/

ui/

skills/
```

Each package has one responsibility.

---

# app/

Purpose:

Application bootstrap and dependency injection.

Contains:

- bootstrap.py
- application.py
- container.py
- lifecycle.py

Responsibilities:

- Service registration
- Application startup
- Shutdown

Should NOT contain:

- AI logic
- HTTP requests
- Provider implementations

---

# cli/

Purpose:

Command-line interface.

Responsibilities:

- Parse user input
- Display output
- Call RuntimeEngine

Should NOT contain:

- Provider logic
- HTTP logic
- Business logic

Think of CLI as a presentation layer.

---

# core/

Purpose:

Shared framework infrastructure.

Contains:

- configuration
- logging
- events
- utilities
- security

Everything here should be reusable.

---

# runtime/

Purpose:

Heart of the framework.

Contains:

- RuntimeEngine
- Conversation
- Models
- Provider system
- Routing
- Registry
- Networking

Everything related to AI execution belongs here.

---

# runtime/providers/

Purpose:

Provider implementations.

Examples:

```
NVIDIAProvider

OpenAIProvider

GeminiProvider

GroqProvider
```

Each provider consists of:

```
Provider

↓

Provider Client
```

---

# runtime/network/

Purpose:

Shared networking layer.

Contains:

- HTTPClient
- Network Exceptions

Rules:

Networking code must never know about specific AI providers.

---

# memory/

Purpose:

Conversation and long-term memory.

Future examples:

```
SQLiteMemory

RedisMemory

VectorMemory
```

Memory implementations should follow common interfaces.

---

# tools/

Purpose:

Tool calling.

Examples:

```
Calculator

Python

Shell

Web Search

Filesystem

GitHub
```

Each tool should be independent.

---

# agents/

Purpose:

Agent implementations.

Examples:

```
CodingAgent

ResearchAgent

PlanningAgent
```

Agents coordinate tools, memory, and workflows.

---

# workflows/

Purpose:

Task orchestration.

Examples:

```
Sequential Workflow

Parallel Workflow

Conditional Workflow
```

Workflows define execution order.

---

# api/

Purpose:

REST API.

Future:

FastAPI server.

Rules:

API should call RuntimeEngine.

Never call providers directly.

---

# ui/

Purpose:

Graphical user interfaces.

Examples:

```
Desktop

Web Dashboard

Electron
```

UI should remain independent from runtime implementation.

---

# skills/

Purpose:

Reusable AI capabilities.

Examples:

```
Summarization

Translation

Classification

Extraction
```

Skills should be provider-independent.

---

# Dependency Rules

Allowed:

```
CLI

↓

Runtime

↓

Provider

↓

HTTP
```

Not Allowed:

```
HTTP

↓

Runtime
```

or

```
Provider

↓

CLI
```

Dependencies must always point downward.

---

# File Naming

Good

```
runtime_engine.py

provider_router.py

conversation_store.py
```

Avoid

```
helpers.py

utils.py

misc.py

common.py
```

File names should describe exactly one concept.

---

# Folder Guidelines

One primary concept per file.

One responsibility per package.

Avoid giant modules.

If a file exceeds approximately 500 lines, consider splitting it.

---

# Tests

Mirror the source structure.

Example:

```
src/runtime/router.py

↓

tests/runtime/test_router.py
```

Every source package should have corresponding tests.

---

# Documentation

Every major package should eventually have its own documentation.

Examples:

```
RUNTIME.md

PROVIDERS.md

MEMORY.md

TOOLS.md
```

---

# Assets

Static assets should live outside source code.

Examples:

```
templates/

images/

examples/
```

Avoid embedding large assets in Python modules.

---

# Future Expansion

The project structure is designed to support future growth without major reorganization.

Planned additions include:

- Multiple provider backends
- Plugin marketplace
- Workflow editor
- Web dashboard
- Distributed execution
- Remote agents
- MCP server/client
- Enterprise integrations

These additions should fit naturally into the existing structure.

---

# Summary

The project structure is designed around one simple principle:

> **Every folder has one responsibility, and every dependency flows in one direction.**

Maintaining this discipline ensures that MyCode remains understandable, scalable, and easy to extend as it evolves.
