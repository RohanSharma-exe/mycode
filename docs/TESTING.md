# MyCode Testing Guide

> Version: v1.0
>
> Testing is a core part of MyCode's development process.
>
> Every feature should be designed with testability in mind.

**Current Status:** Implemented (Unit Testing)

---

# Table of Contents

1. Philosophy
2. Goals
3. Testing Pyramid
4. Project Structure
5. Running Tests
6. Writing Tests
7. Mocking
8. Providers
9. Runtime Testing
10. Coverage
11. Continuous Integration
12. Best Practices

---

# Philosophy

Testing is not an optional activity performed after development.

Testing is part of development.

Every feature should be accompanied by tests that verify its expected behavior.

The purpose of tests is to:

- Prevent regressions
- Enable refactoring
- Document expected behavior
- Increase confidence

---

# Goals

The testing strategy aims to ensure:

- Correctness
- Reliability
- Fast feedback
- Isolation
- Repeatability

Tests should be deterministic and should produce the same result every time they are run.

---

# Testing Pyramid

MyCode follows a testing pyramid.

```
                E2E Tests
                    ▲
            Integration Tests
                    ▲
              Unit Tests
```

### Unit Tests

Test individual classes and functions in isolation.

Examples:

- RuntimeEngine
- ProviderRouter
- ProviderRegistry
- ConversationStore

Unit tests should not perform network requests.

---

### Integration Tests

Verify that multiple components work together.

Examples:

- Runtime + Provider
- Runtime + Memory
- Runtime + Tool Registry

Integration tests may use local services or mocks.

---

### End-to-End Tests

Verify complete user workflows.

Examples:

- CLI prompt execution
- Multi-step workflow
- Agent task completion

These tests simulate real user interactions.

---

# Project Structure

Tests mirror the source tree.

Example:

```
src/mycode/runtime/router.py

↓

tests/runtime/test_router.py
```

Recommended structure:

```
tests/

runtime/

providers/

memory/

tools/

agents/

workflows/

cli/

integration/
```

---

# Running Tests

Run all tests:

```bash
uv run pytest
```

Run a specific file:

```bash
uv run pytest tests/runtime/test_router.py
```

Run a single test:

```bash
uv run pytest -k default_provider
```

Verbose output:

```bash
uv run pytest -v
```

---

# Writing Tests

Every test should follow the Arrange–Act–Assert pattern.

Example:

```python
def test_provider_registration():
    # Arrange
    registry = ProviderRegistry()

    # Act
    registry.register(provider)

    # Assert
    assert registry.exists(provider.name)
```

Avoid combining multiple unrelated assertions in a single test.

---

# Mocking

External dependencies should be mocked.

Examples:

- HTTP requests
- Provider APIs
- Databases
- File systems (where appropriate)

This keeps tests fast and deterministic.

---

# Provider Testing

Provider tests should verify:

- Request translation
- Response translation
- Error handling
- Configuration usage

Avoid using real API keys in automated tests.

---

# Runtime Testing

Runtime tests should focus on orchestration.

Examples:

- Provider selection
- Conversation updates
- Response handling

Use fake providers to isolate Runtime behavior.

---

# Coverage

High coverage is desirable, but meaningful tests are more important than percentages.

Prioritize:

- Core Runtime
- Providers
- Memory
- Tools
- Workflow execution

---

# Continuous Integration

Every pull request should run:

1. Ruff formatting
2. Ruff linting
3. Pytest

A pull request should not be merged if the test suite fails.

---

# Best Practices

- Keep tests small.
- Use descriptive names.
- Mock external systems.
- Test one behavior per test.
- Avoid hidden dependencies.
- Prefer readability over cleverness.

---

# Summary

Testing is an essential part of MyCode.

A strong test suite enables safe refactoring, reliable releases, and long-term maintainability.

Every contribution should leave the test suite stronger than before.

---

# Related Documents

- DEVELOPMENT_GUIDE.md
- CODING_STANDARDS.md
- CONTRIBUTING.md
- RUNTIME.md
