# Contributing

TITR-SecondBrain is currently an internal project with a public software repository.

## Before contributing

1. Read [AGENTS.md](AGENTS.md).
2. Review the architecture decisions under `docs/decisions/`.
3. Use synthetic data only.
4. Open an issue before introducing a new service, persistence layer, connector, agent runtime, Obsidian plugin, or security boundary.
5. Keep pull requests small enough to review meaningfully.

## Pull request requirements

- Explain the user outcome.
- Identify affected trust boundaries.
- Include tests or validation.
- Document new permissions, data flows, network egress, dependencies, and retention.
- Confirm no sensitive data or credentials are included.
- Run `python3 scripts/validate_repository.py`.

A worker agent must not approve or verify its own high-impact output.
