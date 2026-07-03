# MyCode Provider System

> Version: v1.0
>
> The Provider System allows MyCode to interact with different AI models through a common interface.
>
> The Runtime never communicates directly with external APIs. Instead, it delegates all model execution to Providers.

---

# Table of Contents

1. Overview
2. Design Goals
3. Provider Architecture
4. Provider Lifecycle
5. Provider Interface
6. Provider Client
7. Provider Registry
8. Provider Router
9. Provider Configuration
10. Request Flow
11. Response Flow
12. Error Handling
13. Streaming
14. Tool Calling
15. Model Discovery
16. Health Checks
17. Adding a New Provider
18. Best Practices
19. Future Enhancements

---

# Overview

A Provider is responsible for translating MyCode's internal request and response models into the format required by an external AI service.

Examples of supported providers include:

- NVIDIA
- OpenAI
- Google Gemini
- Anthropic
- Groq
- Ollama
- OpenRouter
- Azure OpenAI
- Local models

The Runtime should never need to know which provider is executing the request.

---

# Design Goals

The provider system is designed around five goals.

## Provider Independence

Every provider exposes the same interface.

## Consistent Models

All providers receive:

```
ChatRequest
```

All providers return:

```
ChatResponse
```

## Easy Extension

Adding a provider should require:

- Creating a client
- Creating a provider
- Registering it

Nothing else.

## Testability

Providers should be testable without changing the Runtime.

## Replaceability

A provider can be replaced without affecting other parts of the framework.

---

# Provider Architecture

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
                BaseProvider
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 NVIDIAProvider  OpenAIProvider  GeminiProvider
        │              │              │
        ▼              ▼              ▼
 NVIDIAClient   OpenAIClient   GeminiClient
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  HTTPClient
                       ▼
               External AI API
```

---

# Provider Lifecycle

Application startup follows this sequence:

```
Bootstrap

↓

ProviderConfig

↓

HTTPClient

↓

ProviderClient

↓

Provider

↓

ProviderRegistry

↓

ProviderRouter

↓

RuntimeEngine
```

Providers are created exactly once and reused for the lifetime of the application.

---

# BaseProvider

Every provider inherits from:

```
BaseProvider
```

Required methods:

```
generate()

stream_generate()

health()

list_models()
```

Required properties:

```
name

default_model

capabilities
```

Every provider should implement all abstract members.

---

# Provider Client

Each provider owns a dedicated client.

Example:

```
NVIDIAProvider

↓

NVIDIAClient
```

Responsibilities:

- HTTP requests
- Authentication
- Request serialization
- Response parsing
- Provider-specific endpoints

A Provider Client should never contain Runtime logic.

---

# Provider Registry

The registry stores initialized provider instances.

Responsibilities:

- Register providers
- Remove providers
- Retrieve providers
- Check provider existence
- List providers

The registry should never create providers.

---

# Provider Router

The Router decides which provider should handle a request.

Current strategy:

```
Default Provider
```

Future strategies:

- Provider by model
- Provider by capability
- Provider by latency
- Provider by cost
- Provider by user preference
- Provider failover

The Router should contain only routing logic.

---

# Provider Configuration

Each provider receives a ProviderConfig object.

Typical fields include:

```
name
api_key
base_url
model
temperature
timeout
max_tokens
max_retries
enable_streaming
```

Provider implementations should avoid hardcoding configuration values.

---

# Request Flow

```
ChatRequest

↓

Provider.generate()

↓

ProviderClient.chat()

↓

HTTPClient.post()

↓

External AI
```

Providers are responsible for converting ChatRequest into provider-specific payloads.

---

# Response Flow

```
External AI

↓

HTTP Response

↓

ProviderClient

↓

Provider

↓

ChatResponse
```

The Runtime should only receive ChatResponse.

---

# Error Handling

Errors should be translated into framework exceptions.

Example:

```
HTTP Error

↓

HTTPRequestError

↓

ProviderError

↓

RuntimeError
```

Provider-specific exceptions should not leak into higher layers.

---

# Streaming

Providers supporting streaming should implement:

```
stream_generate()
```

The method returns an asynchronous iterator of StreamChunk objects.

Example flow:

```
Provider

↓

StreamChunk

↓

StreamChunk

↓

Finished
```

---

# Tool Calling

Future providers may support tool calling.

Example flow:

```
Provider

↓

Tool Request

↓

Runtime

↓

Tool Execution

↓

Provider

↓

Final Response
```

Tool execution is coordinated by the Runtime, not by the provider.

---

# Model Discovery

Providers should expose supported models through:

```
list_models()
```

Each model should include:

- Identifier
- Context window
- Maximum output tokens
- Reasoning support
- Vision support
- Tool calling support

This enables future UI features and model selection.

---

# Health Checks

Providers should implement:

```
health()
```

Typical checks include:

- Authentication
- Endpoint availability
- API responsiveness

Health checks should be lightweight.

---

# Adding a New Provider

Adding a provider should follow this process.

1. Create a ProviderClient.

Example:

```
OpenAIClient
```

2. Create a Provider.

```
OpenAIProvider
```

3. Register the provider during bootstrap.

4. Add tests.

5. Update documentation.

No changes to RuntimeEngine should be necessary.

---

# Best Practices

Providers should:

- Use dependency injection.
- Keep API logic inside the client.
- Translate provider responses into ChatResponse.
- Avoid business logic.
- Reuse HTTPClient.
- Respect ProviderConfig.

Providers should not:

- Read environment variables directly.
- Create HTTP clients.
- Print to the console.
- Perform logging unrelated to provider behavior.

---

# Future Enhancements

The provider system is designed to support future capabilities without architectural changes.

Planned additions include:

- Multi-provider routing
- Automatic failover
- Cost-aware routing
- Latency-aware routing
- Provider load balancing
- Request retries
- Response caching
- Model benchmarking
- Provider plugins

---

# Design Principles

The provider system follows three key principles.

## Uniform Interface

Every provider behaves the same from the Runtime's perspective.

## Separation of Concerns

Runtime orchestrates.

Provider translates.

Client communicates.

HTTPClient transports.

## Extensibility

Adding a provider should require minimal changes outside the provider itself.

---

# Summary

The Provider System isolates external AI services behind a stable, provider-independent interface.

By keeping RuntimeEngine unaware of provider-specific APIs, MyCode remains flexible, testable, and easy to extend as new models and providers emerge.
