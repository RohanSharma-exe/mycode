# MyCode CLI Reference

> Version: v1.0
>
> This document describes every command available in the MyCode Command Line Interface (CLI).
>
> **Current Status:** Basic Commands Implemented

---

# Table of Contents

1. Overview
2. Installation
3. Command Structure
4. Global Options
5. Available Commands
6. Future Commands
7. Exit Codes
8. Examples

---

# Overview

The MyCode CLI provides access to the framework without writing Python code.

Typical uses include:

- Running prompts
- Inspecting providers
- Managing configuration
- Running workflows
- Diagnosing the installation

---

# Installation

Run:

```bash
uv sync
```

Then execute:

```bash
uv run python -m mycode
```

or

```bash
mycode
```

if installed as a package.

---

# Command Structure

```
mycode <command> [options]
```

Example:

```bash
mycode doctor
```

---

# Global Options

Future versions may support:

```
--help

--version

--verbose

--debug

--config

--workspace
```

---

# doctor

Displays diagnostic information.

Example

```bash
mycode doctor
```

Output includes:

- application version
- environment
- default provider
- default model
- Ollama URL
- runtime status

---

# version

Displays framework version.

Example

```bash
mycode version
```

Example output

```
MyCode v0.1.0
```

---

# config

Displays the currently loaded configuration.

Example

```bash
mycode config
```

---

# help

Display available commands.

Example

```bash
mycode --help
```

---

# Future Commands

## prompt

Execute a single prompt.

Example

```bash
mycode prompt "Hello"
```

---

## chat

Start an interactive chat session.

Example

```bash
mycode chat
```

---

## providers

List installed providers.

Example

```bash
mycode providers
```

---

## models

Display available models.

Example

```bash
mycode models
```

---

## memory

Inspect memory.

Examples

```bash
mycode memory list

mycode memory clear
```

---

## tools

Display installed tools.

```
mycode tools
```

---

## workflows

Execute workflows.

```
mycode workflow run build_project
```

---

## plugins

List installed plugins.

```
mycode plugins
```

---

## events

Display event statistics.

```
mycode events
```

---

## benchmark

Compare providers.

```
mycode benchmark
```

---

## update

Check for updates.

```
mycode update
```

---

## init

Create a new project.

```
mycode init
```

---

# Exit Codes

| Code | Meaning |
|-------|----------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid configuration |
| 3 | Provider error |
| 4 | Runtime error |
| 5 | CLI argument error |

---

# Examples

Display diagnostics

```bash
mycode doctor
```

Show version

```bash
mycode version
```

Display configuration

```bash
mycode config
```

Future prompt

```bash
mycode prompt "Explain dependency injection."
```

Future interactive chat

```bash
mycode chat
```

---

# Best Practices

- Use `doctor` after installation.
- Check configuration before reporting issues.
- Use `--help` to discover available commands.
- Prefer configuration files over long command-line arguments for repeatable workflows.

---

# Related Documents

- README.md
- CONFIGURATION.md
- DEVELOPMENT_GUIDE.md
- RUNTIME.md

---

# Summary

The MyCode CLI provides a simple and consistent interface for interacting with the framework.

As MyCode evolves, the CLI will become the primary entry point for development, automation, debugging, and project management.
