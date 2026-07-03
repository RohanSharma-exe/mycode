# MyCode Design Principles

> Version: v1.0
>
> This document defines the architectural philosophy of MyCode.
>
> These principles are more important than individual implementations.
>
> Code may change.
>
> Architecture may evolve.
>
> These principles should remain stable.

---

# Table of Contents

1. Introduction
2. Philosophy
3. Core Principles
4. Design Rules
5. Decision Framework
6. Long-Term Vision

---

# Introduction

Every software project eventually faces difficult architectural decisions.

Examples:

- Should this feature belong in Runtime?
- Should Providers execute tools?
- Should Memory know about Providers?
- Should Agents call HTTP directly?

Rather than making these decisions repeatedly, MyCode defines a set of architectural principles.

Whenever there is uncertainty, these principles take precedence.

---

# Philosophy

MyCode is designed around one idea:

> **Every component should have one responsibility and communicate through well-defined abstractions.**

The framework favors:

- Simplicity
- Modularity
- Testability
- Explicitness
- Long-term maintainability

Over:

- Clever abstractions
- Hidden behavior
- Tight coupling
- Convenience at the cost of architecture

---

# Principle 1 — Single Responsibility

Every module should have exactly one reason to change.

Examples

Runtime

Responsible for AI execution.

Provider

Responsible for model translation.

HTTPClient

Responsible for network transport.

Logger

Responsible for logging.

If a component has multiple unrelated responsibilities, split it.

---

# Principle 2 — Separation of Concerns

Different layers solve different problems.

CLI

↓

Runtime

↓

Provider

↓

HTTP

Each layer understands only its own domain.

---

# Principle 3 — Provider Independence

The framework should never depend on a specific AI provider.

Providers are plugins.

The Runtime should not know whether it is talking to:

- NVIDIA
- OpenAI
- Gemini
- Groq
- Ollama

Changing providers should not require Runtime changes.

---

# Principle 4 — Dependency Injection

Components should receive dependencies.

They should not create them.

Correct

```python
RuntimeEngine(router)
```

Incorrect

```python
RuntimeEngine()

↓

ProviderRouter()
```

Dependency Injection makes testing easier and reduces coupling.

---

# Principle 5 — Composition over Inheritance

Prefer assembling small components.

Avoid deep inheritance trees.

Correct

```
Runtime

↓

Router

↓

Registry

↓

Provider
```

Avoid inheritance chains that make behavior difficult to follow.

---

# Principle 6 — Async First

AI applications spend most of their time waiting for I/O.

Therefore:

- network operations
- database access
- file access
- streaming

should all be asynchronous.

Blocking operations should be avoided whenever practical.

---

# Principle 7 — Explicit Configuration

Configuration should be visible and typed.

Never hide configuration in source code.

Good

```
settings.yaml

.env
```

Bad

```python
DEFAULT_MODEL = "..."
```

inside business logic.

---

# Principle 8 — Runtime Owns AI Execution

Every AI request passes through Runtime.

No component should bypass Runtime to communicate directly with a provider.

Correct

```
CLI

↓

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

# Principle 9 — Providers Translate

Providers do not contain business logic.

They translate between:

MyCode Models

↓

Provider API

↓

MyCode Models

Nothing more.

---

# Principle 10 — Transport Is Generic

HTTPClient performs transport only.

It should never know:

- provider names
- endpoints beyond those passed to it
- AI concepts
- models

Networking remains reusable.

---

# Principle 11 — Testability

Every major component should be testable in isolation.

Example

```
Fake Provider

↓

Runtime

↓

Unit Test
```

Tests should not require:

- internet
- API keys
- external services

---

# Principle 12 — Extensibility

Adding a new capability should require adding code, not rewriting existing code.

Examples

Adding:

- Provider
- Tool
- Workflow
- Memory Backend

should not require Runtime modifications.

---

# Principle 13 — Secure by Default

Security should not rely on user discipline.

Examples

- never log secrets
- validate input
- restrict workspace access
- require confirmation for dangerous operations

Safe defaults are preferred.

---

# Principle 14 — Documentation Is Part of the Architecture

Documentation should evolve together with the code.

Every significant feature should include:

- implementation
- tests
- documentation

Documentation is not optional.

---

# Decision Framework

Before introducing a new feature, ask:

### Does it violate Single Responsibility?

If yes, redesign it.

---

### Does it increase coupling?

If yes, reconsider.

---

### Can it be tested independently?

If not, redesign.

---

### Can another provider reuse it?

If not, reconsider the abstraction.

---

### Is it explicit?

If behavior is hidden, redesign.

---

### Will a new contributor understand it?

If not, simplify it.

---

# Long-Term Vision

The goal of MyCode is not simply to support today's AI models.

The goal is to build a framework that remains understandable, maintainable, and adaptable as AI capabilities evolve.

Future features—including new providers, tools, memory systems, workflows, and agent architectures—should strengthen these principles rather than weaken them.

---

# Summary

These principles guide every architectural decision in MyCode.

When there is a conflict between implementing a feature quickly and preserving the long-term architecture, the architecture should take precedence.

A framework with consistent principles is easier to maintain, easier to extend, and easier for others to contribute to.
