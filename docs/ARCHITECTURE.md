# MyCode Architecture

> **Version:** v0.1.0-alpha
> **Status:** Active Development

---

# Table of Contents

1. Introduction
2. Design Philosophy
3. Architectural Goals
4. High-Level Architecture
5. Layered Architecture
6. Application Lifecycle
7. Dependency Injection
8. Runtime
9. Provider System
10. Networking
11. Configuration
12. Logging
13. Events
14. Conversation Management
15. Future Components
16. Data Flow
17. Error Handling
18. Threading & Async Model
19. Extension Points
20. Design Decisions

---

# Introduction

MyCode is a modular AI framework designed around **clean architecture** and **provider independence**.

The framework separates responsibilities into well-defined layers so that new providers, memory systems, tools, workflows, and user interfaces can be added without modifying the core runtime.

The architecture prioritizes:

- Simplicity
- Maintainability
- Extensibility
- Testability
- Performance

---

# Design Philosophy

The framework follows several core principles.

## 1. Separation of Concerns

Every module should have exactly one responsibility.

Examples:

Runtime

- Coordinates AI execution.

Provider

- Implements provider-specific behavior.

Provider Client

- Talks to external APIs.

HTTP Client

- Sends HTTP requests.

CLI

- Handles user interaction only.

---

## 2. Dependency Injection

Objects never construct their own dependencies.

Instead:

```
Bootstrap

↓

Container

↓

Application

↓

Services
```

Benefits:

- Easier testing
- Easier mocking
- Replaceable implementations
- Lower coupling

---

## 3. Provider Independence

The runtime never communicates directly with NVIDIA, OpenAI, or Gemini.

Instead:

```
Runtime

↓

Provider Interface

↓

Provider Implementation
```

The runtime only understands:

- ChatRequest
- ChatResponse

Everything else is provider-specific.

---

## 4. Async First

All I/O is asynchronous.

This includes:

- HTTP
- File storage
- Memory
- Streaming
- Tool execution

This allows thousands of concurrent requests.

---

# High-Level Architecture

```
                   User
                     │
                     ▼
              Typer CLI
                     │
                     ▼
             Application
                     │
                     ▼
            Runtime Engine
                     │
                     ▼
            Provider Router
                     │
                     ▼
           Provider Registry
                     │
                     ▼
          Selected Provider
                     │
                     ▼
          Provider Client
                     │
                     ▼
             HTTP Client
                     │
                     ▼
            External AI API
```

---

# Layered Architecture

```
Presentation Layer

CLI
REST API
Future Web UI

────────────────────────────

Application Layer

Bootstrap
Container
Application

────────────────────────────

Core Layer

Config
Logging
Events
Security

────────────────────────────

Runtime Layer

Runtime Engine
Conversation
Provider Router
Provider Registry

────────────────────────────

Provider Layer

NVIDIA
OpenAI
Gemini
Groq
Ollama

────────────────────────────

Infrastructure Layer

HTTP
Filesystem
Databases
Caches
```

Each layer depends only on layers below it.

Never upwards.

---

# Application Lifecycle

```
bootstrap()

↓

Configuration

↓

Logger

↓

Events

↓

Provider Registry

↓

HTTP Client

↓

Providers

↓

Runtime Engine

↓

Application Ready
```

Shutdown:

```
Application

↓

Close HTTP Client

↓

Release Resources

↓

Exit
```

---

# Dependency Injection

All shared services are created once during bootstrap.

```
Application

├── ConfigManager
├── LoggerManager
├── EventBus
├── ProviderRegistry
├── ProviderRouter
├── RuntimeEngine
├── HTTPClient
└── ConversationStore
```

Services are resolved using type-based registration.

Example:

```python
runtime = application.resolve(RuntimeEngine)
```

---

# Runtime

The Runtime Engine is the heart of the framework.

Responsibilities:

- Receive requests
- Select provider
- Execute request
- Return response

The runtime never:

- Performs HTTP requests
- Knows provider APIs
- Parses provider JSON

Those belong elsewhere.

---

# Provider System

Providers implement a shared interface.

```
BaseProvider

↓

NVIDIAProvider

↓

Future Providers

OpenAIProvider

GeminiProvider

GroqProvider
```

Every provider exposes:

- generate()
- stream_generate()
- health()
- list_models()

---

# Provider Client

Each provider owns a client.

Example:

```
NVIDIAProvider

↓

NVIDIAClient

↓

HTTPClient
```

Responsibilities:

- Serialize requests
- Parse responses
- Handle provider-specific endpoints

---

# Networking

HTTPClient is intentionally generic.

Responsibilities:

- GET
- POST
- Error handling
- Timeouts

HTTPClient never knows:

- NVIDIA
- OpenAI
- JSON formats

---

# Configuration

Configuration is divided into two categories.

## settings.yaml

Application behavior.

Examples:

- default provider
- default model
- timeout
- logging

## .env

Secrets.

Examples:

- API keys
- Base URLs
- Tokens

This separation allows the same application configuration to be deployed in multiple environments without code changes.

---

# Logging

The LoggerManager provides centralized logging.

Goals:

- Consistent formatting
- Multiple outputs
- Future structured logging

---

# Events

The Event Bus allows components to communicate without direct dependencies.

Future events:

- RequestStarted
- RequestFinished
- ToolExecuted
- MemoryUpdated
- ProviderChanged

---

# Conversation Management

Current:

ConversationStore

Future:

```
Conversation

├── id
├── messages
├── metadata
├── created_at
└── updated_at
```

Multiple conversations will be supported.

---

# Future Components

Planned modules:

Memory

- Long-term memory
- Vector memory
- Summarization

Tools

- Python
- Shell
- Web
- Database

Agents

- Planning
- Reflection
- Multi-agent

MCP

- Client
- Server
- Tools

Workflows

- Sequential
- Parallel
- Conditional

---

# Data Flow

```
Prompt

↓

ChatRequest

↓

Runtime

↓

Provider

↓

Provider Client

↓

HTTP Client

↓

External AI

↓

HTTP Response

↓

Provider Client

↓

ChatResponse

↓

Runtime

↓

CLI
```

---

# Error Handling

Each layer handles only its own errors.

Example:

HTTP

↓

HTTPRequestError

↓

Provider

↓

ProviderError

↓

Runtime

↓

RuntimeError

↓

CLI

↓

User-friendly message

Errors should never leak implementation details to end users.

---

# Threading & Async Model

MyCode is async-first.

Blocking operations should be avoided.

Network operations must use asynchronous clients.

Future:

- Streaming
- Parallel tools
- Concurrent workflows

---

# Extension Points

The framework is designed to be extended.

Examples:

- New providers
- New tools
- New memory backends
- New workflows
- New UI layers

Core architecture should rarely change.

---

# Design Decisions

## Why Dependency Injection?

To reduce coupling.

---

## Why Provider Registry?

To support multiple providers simultaneously.

---

## Why Router?

To separate provider selection from execution.

---

## Why Provider Client?

To isolate API serialization from business logic.

---

## Why Generic HTTP Client?

To reuse transport across providers.

---

## Why Async?

Because AI applications spend most of their time waiting for I/O.

---

# Stability Policy

Core architecture is considered stable after v0.1.0-alpha.

Future development should extend the framework rather than redesign it.

Major architectural changes should be avoided unless they solve a demonstrable problem.

---

# Conclusion

The architecture of MyCode is designed to provide a stable foundation for:

- AI Assistants
- Chatbots
- Coding Agents
- Research Systems
- Workflow Automation
- Enterprise AI Platforms

By separating responsibilities into clear layers, the framework remains maintainable as new capabilities are added.
