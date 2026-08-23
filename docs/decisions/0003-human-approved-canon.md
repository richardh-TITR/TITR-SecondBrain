# ADR-0003: Separate generated wiki from human-approved canon

- Status: Accepted
- Date: 2026-08-22

## Context

AI systems can produce plausible but unsupported conclusions, collapse genuine disagreements, or overwrite important historical nuance. Fully self-rewriting vaults are unsuitable for client, legal, financial, people, policy, commitment, and architecture knowledge.

## Decision

Separate reversible AI-generated synthesis from human-approved canon.

Automatic writes are permitted only when they are:

- deterministic or re-derivable;
- explicitly allowlisted;
- scoped;
- validated;
- logged;
- recoverable.

Reversible synthesis changes are proposed as transactions. High-impact content always requires human approval. Contradictions are recorded and surfaced; the AI does not silently choose truth.

## Consequences

- The system may require more review than a personal experimental vault.
- Confidence and provenance remain visible.
- Historical decisions are superseded, not silently rewritten.
- Autonomy can increase later only with measured accuracy and accepted risk.
