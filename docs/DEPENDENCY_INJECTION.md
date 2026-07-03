# MyCode Dependency Injection

> Version: v1.0
>
> Dependency Injection (DI) is one of the core architectural principles of MyCode.
>
> Every shared service in the framework is created once during application startup and accessed through the Application container.
>
> **Current Status:** Implemented

---

# Table of Contents

1. Overview
2. Why Dependency Injection?
3. Core Components
4. Application
5. Container
6. Bootstrap
7. Service Registration
8. Service Resolution
9. Service Lifetime
10. Dependency Graph
11. Best Practices
12. Anti-Patterns
13. Future Roadmap

---

# Overview

Dependency Injection is the mechanism used to manage shared services within MyCode.

Instead of each class creating its own dependencies, they are provided externally.

Example:

Bad

```python
class RuntimeEngine:

    def __init__(self):
        self.router = ProviderRouter()
```

Good

```python
class RuntimeEngine:

    def __init__(
        self,
        router: ProviderRouter,
    ):
        self._router = router
```

This makes every component easier to test and replace.

---

# Why Dependency Injection?

Without Dependency Injection:

- tight coupling
- duplicated objects
- difficult testing
- hidden dependencies

With Dependency Injection:

- explicit dependencies
- reusable services
- simpler testing
- replaceable implementations

---

# Core Components

The DI system consists of three parts.

```
bootstrap.py

↓

Application

↓

Container
```

---

# Bootstrap

Bootstrap is responsible for constructing the application.

Responsibilities include:

- loading configuration
- creating shared services
- wiring dependencies
- registering services
- returning a ready Application

Bootstrap should contain object construction only.

Business logic does not belong here.

---

# Application

Application is the root object of the framework.

Responsibilities:

- expose shared services
- coordinate startup
- coordinate shutdown
- own the service container

Example

```python
runtime = application.resolve(RuntimeEngine)
```

The Application should never contain business logic.

---

# Container

The Container stores shared service instances.

Example:

```
Container

├── ConfigManager

├── LoggerManager

├── EventBus

├── ProviderRegistry

├── ProviderRouter

├── RuntimeEngine

└── HTTPClient
```

The Container owns instances.

It does not construct them.

---

# Service Registration

Services are registered during bootstrap.

Example:

```python
application.register(
    RuntimeEngine,
    runtime,
)
```

Registration should occur only once during startup.

---

# Service Resolution

Components request services by type.

Example:

```python
runtime = application.resolve(RuntimeEngine)
```

Avoid passing the Application object throughout the codebase.

Instead, inject only the required dependency.

---

# Service Lifetime

Current lifetime:

```
Singleton
```

Every shared service exists once.

Examples:

- ConfigManager
- LoggerManager
- EventBus
- RuntimeEngine
- HTTPClient

Future versions may introduce scoped or transient services if required.

---

# Dependency Graph

```
Application

↓

RuntimeEngine

↓

ProviderRouter

↓

ProviderRegistry

↓

Provider

↓

ProviderClient

↓

HTTPClient
```

Dependencies always flow downward.

Circular dependencies are not allowed.

---

# Best Practices

- Register services in bootstrap only.
- Keep constructors explicit.
- Inject interfaces where possible.
- Resolve services through Application.
- Keep services stateless unless shared state is intentional.

---

# Anti-Patterns

Avoid constructing dependencies inside feature code.

Bad

```python
router = ProviderRouter(...)
```

inside RuntimeEngine.

Avoid global variables.

Avoid service locators throughout the application.

Avoid circular dependencies.

---

# Testing

Dependency Injection simplifies testing.

Example:

```python
runtime = RuntimeEngine(
    router=FakeRouter(),
    conversation_store=ConversationStore(),
)
```

No real providers or HTTP requests are required.

---

# Future Roadmap

Potential future enhancements include:

- Scoped lifetimes
- Lazy service initialization
- Automatic dependency graph validation
- Plugin-based service registration

---

# Summary

Dependency Injection keeps MyCode modular, testable, and maintainable.

Every shared service is created during bootstrap, registered once, and resolved through the Application container.

This approach minimizes coupling and makes it easy to replace implementations, add new services, and test components in isolation.

---

# Related Documents

- ARCHITECTURE.md
- DEVELOPMENT_GUIDE.md
- PROJECT_STRUCTURE.md
- RUNTIME.md
