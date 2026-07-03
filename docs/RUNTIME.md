# MyCode Runtime

> Version: v1.0
>
> The Runtime is the heart of MyCode.
>
> Every AI request, regardless of the provider, enters and exits through the Runtime.

---

# Table of Contents

1. Overview
2. Responsibilities
3. Runtime Architecture
4. Execution Flow
5. RuntimeEngine
6. ChatRequest
7. ChatResponse
8. Conversations
9. Provider Routing
10. Provider Registry
11. Provider Lifecycle
12. Request Lifecycle
13. Error Handling
14. Future Runtime Features
15. Design Principles

---

# Overview

The Runtime is responsible for coordinating every AI interaction inside MyCode.

The Runtime never communicates directly with NVIDIA, OpenAI, Gemini, or any external API.

Instead, it coordinates providers through a common abstraction.

Every request follows the same execution path regardless of the selected provider.

---

# Responsibilities

The Runtime is responsible for:

- Receiving AI requests
- Selecting the correct provider
- Executing requests
- Returning responses
- Managing conversations
- Supporting streaming
- Supporting tools
- Supporting memory
- Supporting workflows

The Runtime is **not** responsible for:

- HTTP requests
- Provider-specific JSON
- Authentication
- CLI input
- Web API routing

---

# Runtime Architecture

```
                RuntimeEngine
                      │
                      ▼
              ProviderRouter
                      │
                      ▼
             ProviderRegistry
                      │
                      ▼
             Selected Provider
                      │
                      ▼
             Provider Client
                      │
                      ▼
                HTTPClient
                      │
                      ▼
               External AI API
```

---

# RuntimeEngine

RuntimeEngine is the public entry point for all AI execution.

Every interface (CLI, REST API, Web UI, MCP, Agent, Workflow) should call RuntimeEngine.

Example

```python
response = await runtime.chat(request)
```

The RuntimeEngine should never know:

- HTTP
- JSON payloads
- API endpoints
- Provider-specific response formats

Its job is orchestration.

---

# ChatRequest

ChatRequest is the provider-independent request model.

Example

```python
ChatRequest(
    messages=[
        ChatMessage(
            role=MessageRole.USER,
            content="Hello"
        )
    ]
)
```

Fields

| Field | Description |
|--------|-------------|
| messages | Conversation messages |
| model | Optional model override |
| temperature | Sampling temperature |
| max_tokens | Output token limit |
| stream | Enable streaming |

Every provider receives the same ChatRequest object.

---

# ChatResponse

Every provider returns a ChatResponse.

Example

```python
ChatResponse(
    message=...,
    model="...",
    usage=...
)
```

This guarantees a consistent interface across providers.

The Runtime never parses provider-specific JSON.

---

# Conversation Model

Current

```
ConversationStore
```

Future

```
Conversation

├── id
├── title
├── messages
├── metadata
├── created_at
└── updated_at
```

A Conversation is the source of truth for all chat history.

---

# Provider Routing

The Runtime does not choose providers directly.

Instead:

```
Runtime

↓

ProviderRouter

↓

ProviderRegistry
```

The router decides which provider should satisfy the request.

Today

```
Default Provider
```

Future

```
Provider by Model

Provider by Capability

Provider by User Preference

Provider by Cost

Provider by Availability
```

---

# Provider Registry

The registry stores provider instances.

Example

```
NVIDIA

Groq

Gemini

OpenAI

Ollama
```

Responsibilities

- Register providers
- Remove providers
- Resolve providers
- List providers

The registry never creates providers.

---

# Provider Lifecycle

```
Bootstrap

↓

ProviderConfig

↓

ProviderClient

↓

Provider

↓

Registry

↓

Runtime
```

Each provider is created exactly once during bootstrap.

---

# Request Lifecycle

```
User

↓

CLI

↓

Runtime.chat()

↓

Router

↓

Registry

↓

Provider

↓

ProviderClient

↓

HTTPClient

↓

AI Provider

↓

HTTPClient

↓

ProviderClient

↓

Provider

↓

Runtime

↓

ChatResponse

↓

CLI
```

Every provider follows the same lifecycle.

---

# Conversation Lifecycle

Current

```
User

↓

ChatRequest

↓

Provider

↓

ChatResponse
```

Future

```
Conversation

↓

Append User Message

↓

Provider

↓

Append Assistant Message

↓

Return Response
```

The Runtime will manage conversations automatically.

---

# Streaming Lifecycle

Current

```
Generate()

↓

Return Response
```

Future

```
Generate()

↓

StreamChunk

↓

StreamChunk

↓

StreamChunk

↓

Finished
```

Streaming will reuse the Runtime architecture.

---

# Tool Calling Lifecycle

Future

```
Runtime

↓

Provider

↓

Tool Call

↓

Tool Execution

↓

Tool Result

↓

Provider

↓

Final Response
```

The Runtime will coordinate tool execution.

---

# Memory Lifecycle

Future

```
Conversation

↓

Memory

↓

Relevant Context

↓

Provider

↓

Response

↓

Store Memory
```

Memory is an extension of the Runtime.

---

# Workflow Lifecycle

Future

```
Workflow

↓

Runtime

↓

Tool

↓

Memory

↓

Provider

↓

Result
```

The Runtime remains the execution engine.

---

# Error Handling

Errors should be translated at each layer.

Example

```
HTTP

↓

HTTPRequestError

↓

ProviderError

↓

RuntimeError

↓

CLI
```

Each layer understands only its own errors.

---

# Retry Strategy

Future providers may implement retries.

The Runtime should not perform retries directly.

Retries belong to provider clients.

---

# Timeouts

Timeouts are configured through ProviderConfig.

The Runtime should never hardcode timeout values.

---

# Thread Safety

The Runtime is designed for asynchronous execution.

Shared services:

- ProviderRegistry
- HTTPClient
- Configuration

must be safe for concurrent access.

---

# Extension Points

Future extensions include:

- Multiple providers
- Streaming
- Function calling
- Tool calling
- Long-term memory
- Vector memory
- Multi-agent execution
- Workflow orchestration
- MCP

The Runtime is intentionally provider-independent so these features can be added without redesign.

---

# Runtime Rules

The Runtime:

✔ Coordinates execution

✔ Chooses providers

✔ Returns responses

The Runtime never:

✘ Makes HTTP requests

✘ Parses provider JSON

✘ Reads environment variables

✘ Performs CLI operations

✘ Writes logs directly

---

# Design Principles

The Runtime follows these principles.

## Provider Independence

The Runtime should never know which provider is being used.

---

## Testability

The Runtime should be testable using fake providers.

No internet connection should be required.

---

## Extensibility

Adding a provider should not require modifying RuntimeEngine.

Only the bootstrap process and provider registration should change.

---

## Stability

The Runtime API should change rarely.

It is the foundation upon which the rest of MyCode is built.

---

# Summary

The Runtime is the execution engine of MyCode.

Every AI interaction flows through it.

By separating orchestration from provider implementation, the Runtime remains simple, testable, extensible, and independent of external AI services.

It is intended to remain one of the most stable parts of the framework as MyCode evolves.
