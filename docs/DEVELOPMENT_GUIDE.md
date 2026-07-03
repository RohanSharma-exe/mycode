# MyCode Development Guide

> **Version:** v1.0
>
> This guide explains how to set up a development environment, work on MyCode, run tests, debug issues, and contribute changes.
>
> If you plan to actively develop MyCode, this document should be your primary reference.

---

# Table of Contents

1. Introduction
2. Development Philosophy
3. System Requirements
4. Development Environment
5. Installing the Project
6. Repository Layout
7. Daily Development Workflow
8. Running the Framework
9. Testing
10. Linting & Formatting
11. Debugging
12. Adding Features
13. Adding Providers
14. Adding CLI Commands
15. Git Workflow
16. Release Workflow
17. Troubleshooting
18. Best Practices

---

# Introduction

This guide is intended for developers working on MyCode itself.

It explains:

- how to build the project
- how to test changes
- how to maintain code quality
- how to add new features
- how to keep the architecture consistent

---

# Development Philosophy

Every feature should be developed as a **vertical slice**.

Instead of implementing every part of one subsystem before moving to the next, complete one end-to-end feature at a time.

Example:

```
CLI

↓

Runtime

↓

Provider

↓

Network

↓

Response
```

Advantages:

- Always working
- Easier debugging
- Smaller pull requests
- Faster feedback

---

# System Requirements

Recommended

- Windows 11 / Linux / macOS
- Python 3.14+
- Git
- VS Code
- uv

Optional

- Docker
- Ollama
- PostgreSQL
- Redis

---

# Development Environment

Clone the repository

```bash
git clone https://github.com/<username>/mycode.git

cd mycode
```

Install dependencies

```bash
uv sync
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

# Environment Variables

Create

```
.env
```

Example

```env
NVIDIA_API_KEY=your_api_key

NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1

OPENAI_API_KEY=

GROQ_API_KEY=

GEMINI_API_KEY=
```

Never commit this file.

---

# Repository Layout

```
configs/
docs/
scripts/
src/
tests/
```

See

```
PROJECT_STRUCTURE.md
```

for detailed explanations.

---

# Daily Development Workflow

Recommended workflow

```
Pull latest changes

↓

Create feature branch

↓

Implement feature

↓

Write tests

↓

Run Ruff

↓

Run Pytest

↓

Commit

↓

Push

↓

Open Pull Request
```

---

# Running the Framework

Verify installation

```bash
uv run mycode doctor
```

View configuration

```bash
uv run mycode config
```

Display version

```bash
uv run mycode version
```

Run an AI prompt

```bash
uv run mycode prompt "Hello!"
```

---

# Running Tests

Execute the full test suite

```bash
uv run pytest
```

Run a specific test

```bash
uv run pytest tests/runtime/test_router.py
```

Run a specific test function

```bash
uv run pytest -k default_provider
```

---

# Linting

Check formatting

```bash
uv run ruff check .
```

Automatically format

```bash
uv run ruff format .
```

Run before every commit.

---

# Pre-Commit Hooks

Install

```bash
pre-commit install
```

Run manually

```bash
pre-commit run --all-files
```

Hooks automatically check

- formatting
- trailing whitespace
- YAML
- large files

---

# Debugging

Recommended IDE

VS Code

Useful extensions

- Python
- Ruff
- GitLens
- Better TOML

Debug configuration

Run

```
main.py
```

or

```
uv run mycode ...
```

Avoid using print() for debugging.

Use LoggerManager.

---

# Adding a New Feature

Every feature should follow this order.

1. Design
2. Models
3. Runtime
4. Tests
5. CLI
6. Documentation

Avoid implementing CLI before the runtime exists.

---

# Adding a Provider

Steps

1. Create ProviderClient

```
runtime/providers/
```

2. Create Provider

```
BaseProvider
```

↓

```
OpenAIProvider
```

3. Register provider

```
bootstrap.py
```

4. Add tests

5. Update documentation

---

# Adding CLI Commands

Commands belong in

```
cli/commands.py
```

Business logic belongs in

```
RuntimeEngine
```

The CLI should never communicate directly with providers.

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

# Updating Configuration

Application configuration

```
settings.yaml
```

Secrets

```
.env
```

Never hardcode API keys.

---

# Git Workflow

Create a feature branch

```bash
git checkout -b feature/streaming
```

Commit

```bash
git add .

git commit -m "feat(runtime): implement streaming"
```

Push

```bash
git push
```

---

# Release Workflow

Before creating a release

Run

```bash
uv run ruff format .

uv run ruff check .

uv run pytest
```

Ensure

- documentation updated
- version updated
- changelog updated

Create tag

```bash
git tag v0.2.0

git push origin v0.2.0
```

---

# Troubleshooting

## Missing Environment Variables

Check

```
.env
```

---

## Provider Not Registered

Verify

```
bootstrap.py
```

---

## Tests Failing

Run

```bash
uv run pytest
```

Read the first failure carefully before fixing subsequent ones.

---

## Ruff Errors

Run

```bash
uv run ruff format .
```

Then

```bash
uv run ruff check .
```

---

## Git Push Blocked

Common causes

- committed secrets
- large files
- failed hooks

Resolve the issue before pushing again.

---

# Best Practices

Prefer

- small commits
- small pull requests
- complete features
- comprehensive tests
- updated documentation

Avoid

- large refactors mixed with feature work
- committing generated files
- skipping tests
- bypassing pre-commit hooks

---

# Definition of Ready

Before starting work

- Requirements are understood
- Architecture impact is known
- Design is discussed (if needed)

---

# Definition of Done

A task is complete when:

- Implementation finished
- Tests pass
- Ruff passes
- Documentation updated
- Pull Request approved
- CI passes

---

# Final Advice

Always leave the project in a better state than you found it.

Small, consistent improvements over time lead to a healthy and maintainable codebase.

The goal is not only to build features, but to build a framework that developers enjoy working on for years to come.
