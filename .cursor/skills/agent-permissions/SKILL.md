---
name: agent-permissions
description: >-
  Repo-specific permission policy: web search and read-only git without prior
  approval; git commit and git push only after explicit user confirmation in chat.
---

# Agent permissions (this repository)

## No prior approval required

- **Web search** — Use when you need current docs, URLs, or facts. Do not wait for a separate “permission to search” message unless the user has asked you to hold off.
- **Read-only git** — Examples: `git status`, `git log`, `git diff`, `git show`, `git branch -a`, `git remote -v`. Run as needed to understand state.

## Prior approval required (chat confirmation)

Before running any of these, **ask in the chat and wait for explicit confirmation** (e.g. “yes, commit and push”, “go ahead”):

- **`git commit`** (any flags)
- **`git push`** (any remote/branch)
- **Combined flows** that include the above (e.g. `git commit -am … && git push`)

Treat confirmation as **per batch**: if the user approves one commit, do not assume later commits are approved unless they say so.

## Still disallowed without explicit request

- Destructive or risky git: `git push --force`, hard reset, rewriting shared history, deleting remotes, etc. — only if the user **explicitly** asks for that operation by name.

## Rationale

Search and inspection are low-risk and keep the agent productive; commits and pushes change repository state and remote history, so the user should confirm in-thread before they run.
