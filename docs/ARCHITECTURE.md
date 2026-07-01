# MyCode Architecture

## Philosophy

MyCode is a provider-agnostic AI Runtime.

Models are plugins.

Tools are plugins.

Agents are plugins.

The Runtime is the core.

---

# Layered Architecture

                    User
                      │
                      ▼
            CLI / API / VSCode
                      │
                      ▼
                 Application
                      │
                      ▼
                 AI Runtime
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Conversation      Router         Middleware
                      │
                      ▼
              Provider Registry
                      │
                      ▼
                  Providers
                      │
                      ▼
                    Clients
                      │
                      ▼
                  SDK / HTTP API

---

# Core

Application

Container

Bootstrap

ConfigManager

LoggerManager

EventBus

SecurityManager

---

# Runtime

RuntimeEngine

Conversation

ConversationStore

ProviderRouter

ProviderRegistry

ProviderFactory

---

# Providers

BaseProvider

BaseClient

NVIDIAProvider

GeminiProvider

GroqProvider

OpenRouterProvider

OllamaProvider

---

# Future

Memory

Planner

Reasoner

Reflection

Skills

Tools

Plugins

MCP

REST API

VS Code Extension

---

# Dependency Rules

Every layer only depends on the layer below it.

Good

CLI

↓

Runtime

↓

Router

↓

Provider

↓

Client

Bad

CLI

↓

Provider

Providers must never know about:

- CLI

- Runtime

- Agents

- Memory

---

# Public API

The following classes are considered stable.

Application

RuntimeEngine

Conversation

ConversationStore

ProviderRouter

ProviderRegistry

ProviderFactory

BaseProvider

BaseClient

Breaking changes to these APIs should be avoided.
