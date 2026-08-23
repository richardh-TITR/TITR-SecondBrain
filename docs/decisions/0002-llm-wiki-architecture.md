# ADR-0002: Persistent Markdown wiki architecture

- Status: Accepted
- Date: 2026-08-22

## Context

Query-time RAG repeatedly reconstructs understanding from raw chunks and does not retain useful synthesis. The 2026 LLM Wiki pattern instead compiles selected sources into a persistent interlinked wiki.

## Decision

Use:

- immutable authoritative sources or snapshots;
- a persistent, interlinked Markdown wiki;
- a documented schema in AGENTS.md-compatible instructions;
- ingest, query, and lint operations;
- content and chronological indexes;
- Git history;
- simple scoped search before vector infrastructure.

Obsidian is the initial human interface, but Markdown remains the durable format and agents must not depend on proprietary hidden state.

## Consequences

- Knowledge can outlive Obsidian or a particular model provider.
- The wiki accumulates reusable synthesis.
- Provenance and maintenance become product features.
- Search infrastructure is deferred until evaluation proves a need.
