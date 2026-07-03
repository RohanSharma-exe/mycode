# MyCode

<p align="center">
  <strong>A Production-Grade AI Agent Framework for Python</strong>
</p>

<p align="center">
Build intelligent AI applications using a modular runtime, provider-independent architecture, memory, tools, workflows, and agents.
</p>

---

## Vision

MyCode is an open-source AI framework designed to make building AI applications simple, scalable, and maintainable.

Unlike frameworks tightly coupled to a single provider or orchestration library, MyCode provides a clean architecture where every component has a single responsibility.

The framework is built around the following principles:

- Provider Independence
- Clean Architecture
- Dependency Injection
- Async First
- Extensibility
- Testability
- Production Readiness

Whether you're building a chatbot, AI assistant, coding agent, research system, workflow automation platform, or enterprise AI application, MyCode provides the foundation.

---

# Features

## Runtime

- Provider-independent runtime
- Conversation management
- Request routing
- Shared models
- Streaming support (planned)

## Providers

Current

- NVIDIA AI

Planned

- OpenAI
- Google Gemini
- Groq
- Ollama
- OpenRouter
- Anthropic

## Architecture

- Dependency Injection
- Configuration Management
- Event Bus
- Logging
- Async HTTP Client
- Provider Registry
- Provider Router

## CLI

- doctor
- config
- version
- prompt

## Developer Experience

- Python 3.14+
- Ruff
- Pytest
- Pre-commit
- Type Hints
- Pydantic
- Typer CLI

---

# Architecture

```
                +----------------------+
                |        CLI           |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Application      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    Runtime Engine    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Provider Router    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Provider Registry   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      Provider        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Provider Client    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     HTTP Client      |
                +----------+-----------+
                           |
                           v
                  External AI Provider
```

---

# Project Structure

```
mycode/

├── configs/
├── docs/
├── scripts/
├── src/
│   └── mycode/
│       ├── agents/
│       ├── api/
│       ├── app/
│       ├── cli/
│       ├── core/
│       ├── memory/
│       ├── mcp/
│       ├── plugins/
│       ├── runtime/
│       ├── skills/
│       ├── tools/
│       ├── ui/
│       └── workflows/
│
├── tests/
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Installation

## Clone

```bash
git clone https://github.com/<your-username>/mycode.git

cd mycode
```

---

## Install Dependencies

```bash
uv sync
```

---

## Create Environment File

```bash
cp .env.example .env
```

Example:

```env
NVIDIA_API_KEY=your_api_key_here

NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

---

# Quick Start

Verify installation:

```bash
uv run mycode doctor
```

Display configuration:

```bash
uv run mycode config
```

Display version:

```bash
uv run mycode version
```

Run your first AI prompt:

```bash
uv run mycode prompt "Hello!"
```

Example output:

```
Hello! I am Nemotron 3 Ultra, a language model developed by NVIDIA.
```

---

# CLI Commands

| Command | Description |
|----------|-------------|
| doctor | Display framework diagnostics |
| version | Display version information |
| config | Display loaded configuration |
| prompt | Send a prompt to the configured provider |

---

# Configuration

Configuration is split into two parts.

## settings.yaml

Contains application configuration.

- default provider
- default model
- timeout
- logging
- security

## .env

Contains secrets.

Examples:

- NVIDIA_API_KEY
- OPENAI_API_KEY
- GEMINI_API_KEY
- GROQ_API_KEY

Secrets should **never** be committed to Git.

---

# Development

Format code

```bash
uv run ruff format .
```

Lint

```bash
uv run ruff check .
```

Run tests

```bash
uv run pytest
```

Run pre-commit

```bash
pre-commit run --all-files
```

---

# Design Goals

MyCode is designed around several architectural goals.

- Separation of Concerns
- Composition over Inheritance
- Dependency Injection
- Provider Independence
- Async First
- Explicit Configuration
- Testability
- Extensibility

---

# Roadmap

## Phase 1

- ✅ Runtime
- ✅ Dependency Injection
- ✅ Configuration
- ✅ CLI
- ✅ NVIDIA Provider

## Phase 2

- Conversation Memory
- Streaming
- Tool Calling

## Phase 3

- OpenAI
- Gemini
- Groq
- Ollama
- OpenRouter

## Phase 4

- MCP
- Agents
- Skills
- Workflows

## Phase 5

- Web API
- Dashboard
- Plugin Marketplace

---

# Documentation

Documentation is available in the `docs/` directory.

- Architecture
- Development Guide
- Coding Standards
- Runtime
- Providers
- Memory
- Tools
- Workflows
- MCP
- API Reference

---

# Contributing

Contributions are welcome.

Before opening a Pull Request:

- Follow the coding standards
- Write tests
- Ensure Ruff passes
- Ensure Pytest passes
- Update documentation

See:

```
docs/CONTRIBUTING.md
```

---

# License

MIT License

---

# Acknowledgements

Built with:

- Python
- Pydantic
- Typer
- HTTPX
- Ruff
- Pytest

---

# Project Status

Current Version

**v0.1.0-alpha**

The framework is under active development.

Core architecture is complete.

Current focus:

- Conversation Memory
- Streaming
- Multi-provider Runtime

---
