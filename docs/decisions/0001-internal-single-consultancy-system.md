# ADR-0001: Internal single-consultancy system

- Status: Accepted
- Date: 2026-08-22

## Context

TITR-SecondBrain supports THEITREVOLUTION LTD and integrates with existing internal systems. Similar projects often drift toward a multi-tenant SaaS architecture, creating unnecessary identity, tenancy, SDK, billing, API, and operational complexity.

## Decision

Build a lean internal system for one consultancy. Preserve clear client security boundaries, but do not implement multi-tenancy as a product feature.

Existing applications remain authoritative. ConsultancyOS may surface SecondBrain capabilities as an internal aggregation interface.

## Consequences

- No tenant abstraction, subscription model, public API product, or client portal.
- Client isolation is a security control, not a SaaS tenancy feature.
- Integrations may remain direct and narrowly scoped.
- A future change requires a new ADR with demonstrated need.
