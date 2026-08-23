# TITR-SecondBrain

TITR-SecondBrain is a secure, local-first AI knowledge system for THEITREVOLUTION LTD. It implements the compounding Markdown wiki pattern popularised by the 2026 AI second-brain workflow while adding business-grade provenance, approval, isolation, recovery, and audit controls.

## Status

Foundation and architecture phase. No production vault or private business data belongs in this repository.

## Design principles

- **Files over apps:** durable knowledge uses readable Markdown and open metadata.
- **Sources remain authoritative:** Microsoft 365, Git repositories, business systems, and original documents are not replaced by the wiki.
- **Immutable evidence:** ingested sources are never silently rewritten.
- **Provenance first:** important claims identify their supporting sources, confidence, freshness, and review state.
- **Generated wiki, approved canon:** AI may propose and maintain reversible synthesis; decisions, commitments, people facts, client facts, policies, and external actions require approval.
- **Least privilege:** agents receive only the files and tools required for the current operation.
- **One controlled writer:** parallel workers return drafts; one orchestrator validates and applies an approved transaction.
- **No premature RAG:** indexes, links, metadata, and full-text search come before vector infrastructure.
- **Recoverability:** Git history, independent encrypted backups, and tested restores are mandatory.
- **Internal and lean:** this is a single-consultancy internal system, not a multi-tenant SaaS product.

## Target architecture

1. Authoritative sources and immutable snapshots
2. Controlled ingestion
3. AI-generated draft changes
4. Deterministic and independent verification
5. Human-approved canon plus reversible generated wiki
6. Grounded briefs, answers, drafts, and approved actions
7. Scheduled review, linting, and measurement

See [Architecture](docs/architecture/overview.md), [Threat model](docs/threat-model.md), and [Roadmap](docs/roadmap.md).

## Repository boundary

This repository may contain source code, schemas, templates, tests, documentation, and synthetic fixtures.

It must never contain:

- a live Obsidian vault;
- personal journals or private notes;
- client names, client documents, transcripts, emails, or contact records;
- credentials, tokens, certificates, private keys, or environment files;
- production exports or backups;
- model-provider request/response logs containing business data.

The operational vault and source stores must use separate private storage with their own access, retention, backup, and recovery controls.

## Initial software direction

- Obsidian Desktop/Mobile as the human workspace
- Markdown and YAML-compatible properties as the durable format
- Claude Code as the initial file-maintenance agent, with AGENTS.md compatibility for Codex and other capable agents
- VS Code for review, configuration, Git, and implementation
- private Forgejo/Git for operational vault versioning
- n8n and Microsoft Graph for controlled integration
- existing Vaultwarden and SOPS/age for secrets
- restic for independent encrypted backups
- existing Prometheus, Grafana, Loki, and Alertmanager for operations
- local index/full-text search first; hybrid semantic search only after evaluation

## Development

Read [AGENTS.md](AGENTS.md) before making changes.

Run the repository checks with:

```bash
python3 scripts/validate_repository.py
```

## Research lineage

The design is informed by Karpathy's LLM Wiki pattern, Tiago Forte's CODE/PARA method, Ron Forbes' workflow, the provenance and transaction model demonstrated by claude-obsidian, verifier separation used by COG, official Obsidian agent skills, OWASP guidance, NIST AI RMF, ICO guidance, and Microsoft Graph integration practices.

See [research landscape](docs/research/2026-08-landscape.md) for links and adoption decisions.
