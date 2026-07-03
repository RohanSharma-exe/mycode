# Contributing to MyCode

First of all, thank you for considering contributing to **MyCode**.

Whether you're fixing a typo, improving documentation, reporting a bug, or implementing a new feature, every contribution is appreciated.

Our goal is to build a production-grade AI framework with a clean architecture, excellent developer experience, and long-term maintainability.

---

# Table of Contents

1. Before You Start
2. Ways to Contribute
3. Development Environment
4. Project Structure
5. Development Workflow
6. Branch Strategy
7. Coding Standards
8. Testing Requirements
9. Documentation Requirements
10. Commit Message Convention
11. Pull Request Process
12. Review Guidelines
13. Reporting Bugs
14. Requesting Features
15. Security Issues
16. Community Guidelines

---

# Before You Start

Please read the following documents before contributing.

- README.md
- ARCHITECTURE.md
- CODING_STANDARDS.md

Understanding the architecture before writing code will save both you and the reviewers time.

---

# Ways to Contribute

Contributions are welcome in many forms.

Examples include:

- Bug fixes
- New providers
- Runtime improvements
- Documentation
- Tests
- Performance optimizations
- Tool integrations
- Memory backends
- Workflow components
- MCP integrations
- Examples and tutorials

Not every contribution has to involve writing code.

---

# Development Environment

## Requirements

- Python 3.14+
- Git
- uv
- Ruff
- Pytest

Clone the repository:

```bash
git clone https://github.com/<username>/mycode.git

cd mycode
```

Install dependencies:

```bash
uv sync
```

Verify installation:

```bash
uv run mycode doctor
```

---

# Project Structure

```
src/mycode/

app/
cli/
core/
runtime/
memory/
providers/
tools/
agents/
workflows/
```

Each package has a clearly defined responsibility.

Please avoid mixing unrelated functionality.

---

# Development Workflow

The preferred workflow is:

```
Issue

↓

Discussion

↓

Branch

↓

Implementation

↓

Tests

↓

Documentation

↓

Pull Request

↓

Review

↓

Merge
```

Every change should include:

- Code
- Tests
- Documentation updates (if applicable)

---

# Branch Strategy

Never work directly on `main`.

Create a feature branch.

Examples:

```
feature/conversation-memory

feature/groq-provider

feature/tool-calling
```

Bug fixes:

```
fix/http-timeout

fix/provider-router
```

Documentation:

```
docs/runtime

docs/readme
```

---

# Coding Standards

All code must follow:

```
docs/CODING_STANDARDS.md
```

Highlights:

- Type hints
- Async I/O
- Dependency Injection
- Single Responsibility Principle
- Google-style docstrings

---

# Testing Requirements

Every feature should include tests.

Required:

- Unit tests

Recommended:

- Integration tests

Run before every commit:

```bash
uv run ruff format .

uv run ruff check .

uv run pytest
```

No Pull Request will be accepted if tests fail.

---

# Documentation Requirements

Documentation is considered part of the feature.

Examples:

New provider?

Update:

```
PROVIDERS.md
```

New runtime feature?

Update:

```
RUNTIME.md
```

New CLI command?

Update:

```
README.md
```

Documentation should evolve together with the code.

---

# Commit Message Convention

We follow the Conventional Commits specification.

Examples:

```
feat(runtime): add streaming support

feat(provider): implement Groq provider

fix(cli): improve prompt handling

refactor(runtime): simplify provider routing

docs(readme): update installation guide

test(runtime): improve conversation tests
```

Avoid messages like:

```
Update

Changes

Fix

Done

Final
```

Every commit should describe exactly what changed.

---

# Pull Request Process

A Pull Request should focus on **one logical change**.

Good examples:

- Add OpenAI provider
- Improve HTTP retry logic
- Add streaming support

Avoid combining unrelated work.

Example of a bad PR:

```
- Added provider
- Fixed logger
- Updated README
- Improved tests
- Refactored runtime
```

Break unrelated changes into separate Pull Requests.

---

# Pull Request Checklist

Before opening a Pull Request:

- Code compiles
- Ruff passes
- Tests pass
- Documentation updated
- No secrets committed
- No debug code
- No unused imports
- No commented-out code

---

# Code Review Guidelines

Reviewers will primarily look for:

## Correctness

Does the feature work?

---

## Architecture

Does it respect the project architecture?

---

## Readability

Is the code easy to understand?

---

## Testing

Are there enough tests?

---

## Documentation

Does the documentation explain the feature?

---

# Reporting Bugs

When reporting a bug, include:

- Operating System
- Python version
- MyCode version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error logs

The more information provided, the easier it is to reproduce the issue.

---

# Requesting Features

Feature requests should explain:

- The problem being solved
- Why the current implementation is insufficient
- The proposed solution
- Possible alternatives

Design discussions are encouraged before implementation.

---

# Security Issues

Do **not** open a public issue for security vulnerabilities.

Examples:

- API key exposure
- Authentication bypass
- Remote code execution
- Secret leakage

Instead, contact the maintainers privately.

---

# Community Guidelines

Please be respectful.

Constructive criticism is welcome.

Personal attacks are not.

We want MyCode to be a friendly place for developers of all experience levels.

---

# Design Philosophy

Every contribution should improve one or more of the following:

- Simplicity
- Maintainability
- Performance
- Reliability
- Developer Experience

Avoid unnecessary complexity.

---

# Definition of Done

A feature is considered complete when:

- Implementation is finished
- Tests pass
- Documentation is updated
- Code review is approved
- CI passes
- The feature is merged

---

# Thank You

Thank you for helping improve MyCode.

Every contribution, no matter how small, helps make the framework better for everyone.
