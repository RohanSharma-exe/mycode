# MyCode

> A production-grade, provider-agnostic AI Agent Framework built in Python.

MyCode is an open-source AI agent framework designed to power intelligent coding assistants, automation systems, and AI-driven workflows.

Unlike projects that are tightly coupled to a single LLM framework or provider, MyCode follows a **hybrid architecture**. The framework owns the core application, agent, memory, tool, and workflow systems while integrating external AI providers through adapter layers.

---

# Vision

Build an extensible AI platform capable of running as:

* CLI Assistant
* VS Code Extension
* REST API
* Web Dashboard
* Background Automation Server
* Multi-Agent System

The CLI is only one interface to the framework.

---

# Goals

* Provider-agnostic architecture
* Secure by default
* Plugin-based
* MCP compatible
* Async-first
* Modular design
* Easy to extend
* Production-ready codebase

---

# Planned Features

## AI Providers

* NVIDIA
* Gemini
* OpenAI
* Groq
* OpenRouter
* Ollama
* Together AI
* Custom OpenAI-compatible APIs

---

## Tool System

* Filesystem
* Shell
* Git
* Python
* Browser
* Database
* HTTP/API
* Terminal
* MCP Tools

---

## Memory

* Conversation Memory
* Session Memory
* Long-Term Memory
* Vector Memory

---

## Agent System

* Planner
* Executor
* Reasoning
* Reflection
* Multi-Agent Collaboration

---

## Skills

Reusable high-level capabilities built from multiple tools.

Examples:

* Fix Python errors
* Generate documentation
* Review repositories
* Build REST APIs
* Generate unit tests

---

## Workflows

Multi-step automation pipelines.

Examples:

* Review repository
* Build project
* Run tests
* Commit changes
* Create pull request

---

## Plugin System

Third-party plugins will be able to register:

* Providers
* Tools
* Skills
* Workflows
* CLI Commands
* Event Listeners

without modifying the framework.

---

## Security

Every potentially dangerous action passes through the security layer.

Examples:

* Shell execution
* File deletion
* Git push
* Network access

---

# Architecture

```text
                    User
                      │
          ┌───────────┴───────────┐
          │                       │
        CLI                  REST API
          │                       │
          └───────────┬───────────┘
                      │
                Application
                      │
      ┌───────────────┼────────────────┐
      │               │                │
   Managers        Event Bus      Security
      │
      ├──────────┬──────────┬──────────┐
      ▼          ▼          ▼          ▼
   LLM      Tools      Memory      Plugins
      │          │
      ▼          ▼
 Providers     Skills
                  │
                  ▼
              Workflows
```

---

# Project Structure

```text
mycode/
├── configs/
├── data/
├── docs/
├── logs/
├── plugins/
├── scripts/
├── tests/
└── src/
    └── mycode/
        ├── app/
        ├── cli/
        ├── core/
        ├── llm/
        ├── tools/
        ├── agent/
        ├── memory/
        ├── skills/
        ├── workflows/
        ├── mcp/
        ├── plugins/
        ├── api/
        └── ui/
```

---

# Design Principles

* Single responsibility per module
* Dependency Injection
* Layered architecture
* Provider independence
* Tool-first design
* Event-driven communication
* Strong typing
* Async where appropriate
* Minimal vendor lock-in

---

# Technology Stack

## Core

* Python 3.14+
* uv
* Ruff
* Typer
* Rich
* Loguru
* Pydantic v2
* HTTPX
* PyYAML
* orjson

## AI

* Official Provider SDKs
* LangChain (adapter only where beneficial)
* Model Context Protocol (MCP)

---

# Development Roadmap

## Phase 1

* [ ] Application
* [ ] Bootstrap
* [ ] Configuration
* [ ] Logging
* [ ] Event Bus
* [ ] Registry
* [ ] Security

## Phase 2

* [ ] Provider Interface
* [ ] LLM Router
* [ ] NVIDIA Provider
* [ ] Gemini Provider
* [ ] Groq Provider
* [ ] OpenRouter Provider
* [ ] Ollama Provider

## Phase 3

* [ ] Filesystem Tool
* [ ] Shell Tool
* [ ] Python Tool
* [ ] Git Tool
* [ ] Browser Tool
* [ ] Database Tool
* [ ] Tool Manager

## Phase 4

* [ ] Memory System

## Phase 5

* [ ] Agent Engine

## Phase 6

* [ ] Skills

## Phase 7

* [ ] Workflows

## Phase 8

* [ ] MCP Integration

## Phase 9

* [ ] Plugin System

## Phase 10

* [ ] REST API

## Phase 11

* [ ] VS Code Extension

---

# Current Status

**Version:** 0.1.0

Current milestone:

* ✅ Project initialized with `uv`
* ✅ Professional `src` layout
* ✅ Ruff configured
* ✅ Typer CLI
* ✅ Application bootstrap
* ✅ Dependency injection container

---

# Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

Before opening a pull request:

1. Run Ruff formatting.
2. Run Ruff lint checks.
3. Ensure all tests pass.
4. Follow the existing project architecture.

---

# License

This project is released under the MIT License.

---

# Author

**Rohan Sharma**

Building an extensible, production-grade AI Agent Framework focused on modularity, security, and provider independence.
"# mycode" 
