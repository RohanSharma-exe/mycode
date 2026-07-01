# Contributing to MyCode

First of all, thank you for your interest in contributing to MyCode!

MyCode is a production-grade, provider-agnostic AI Agent Framework designed to be modular, extensible, and maintainable. Whether you're fixing a bug, improving documentation, or adding a new feature, your contribution is appreciated.

---

# Before You Start

Please read the following documents before contributing:

* `README.md`
* `docs/ARCHITECTURE.md`
* `docs/CODING_STANDARDS.md`

These documents describe the project's architecture, coding conventions, and development philosophy.

---

# Development Setup

Clone the repository:

```bash
git clone <repository-url>
cd mycode
```

Install dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run mycode
```

---

# Development Workflow

1. Create a feature branch.
2. Implement the change.
3. Format the code.
4. Run lint checks.
5. Run tests.
6. Commit with a descriptive message.
7. Open a pull request.

---

# Commit Message Convention

Use Conventional Commits.

Examples:

```text
feat(llm): add NVIDIA provider
feat(runtime): implement conversation manager
fix(logging): resolve file rotation issue
refactor(core): simplify container
docs: update architecture guide
test(router): add provider selection tests
```

---

# Pull Requests

A pull request should:

* Solve one logical problem.
* Include tests when appropriate.
* Keep changes focused.
* Update documentation if behavior changes.

Avoid combining unrelated changes into a single pull request.

---

# Code Reviews

Reviewers may request changes to improve:

* Architecture
* Maintainability
* Performance
* Security
* Readability
* Test coverage

Code review feedback is intended to improve the project rather than criticize contributors.

---

# Testing

Before submitting changes, run:

```bash
uv run ruff format .
uv run ruff check .
uv run pytest
```

All checks should pass before opening a pull request.

---

# Architecture Rules

Do not bypass framework abstractions.

Examples:

✅ Agent → Runtime → Router → Provider

❌ Agent → Provider

---

Providers must never communicate directly with the CLI, UI, or Agent.

Tools must never access providers directly.

Every layer should communicate only with the layer immediately below it.

---

# Adding a New Provider

When adding a provider:

1. Implement `BaseClient`.
2. Implement `BaseProvider`.
3. Register the provider.
4. Add tests.
5. Update documentation if necessary.

Avoid introducing provider-specific logic into the runtime.

---

# Adding a Tool

Every tool should:

* Perform one responsibility.
* Return predictable results.
* Be reusable.
* Avoid side effects where possible.

Business logic belongs in Skills or Workflows, not individual tools.

---

# Reporting Bugs

When reporting bugs, include:

* Operating system
* Python version
* MyCode version
* Relevant logs
* Steps to reproduce
* Expected behavior
* Actual behavior

---

# Philosophy

MyCode values:

* Simplicity
* Modularity
* Explicit APIs
* Strong typing
* Provider independence
* Security by default
* Long-term maintainability

When in doubt, prefer clarity over cleverness.
