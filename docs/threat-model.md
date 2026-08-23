# Threat model

## Assets

- Personal and client confidentiality
- Business decisions and commitments
- Source integrity and provenance
- Agent instructions and approval policy
- Connector tokens and secrets
- Audit and transaction history
- Availability and recoverability
- User judgement and trust

## Threat actors and failure sources

- Malicious external content author
- Compromised source or dependency
- Over-permissioned or manipulated agent
- Accidental user action
- Faulty automation
- Model hallucination or misclassification
- Insider or stolen account
- Sync conflict or storage failure

## Principal threats

### Prompt injection

An imported document, email, webpage, issue, transcript, plugin, or tool result attempts to change instructions, obtain secrets, expand scope, or trigger an action.

Controls: treat retrieved content as data; isolate instructions; scope context; allowlist tools; validate output; require approval.

### Sensitive data disclosure

The wrong model, log, repository, retrieval scope, or output receives personal, client, financial, or confidential information.

Controls: classification before retrieval; separate security domains; least privilege; redaction; approved providers; log minimisation; egress controls.

### Knowledge poisoning and silent drift

A weak or malicious source causes the wiki to overwrite correct information, or generated summaries diverge from authoritative systems.

Controls: immutable evidence; authority rankings; claim ledger; freshness; contradiction visibility; verification; human canon; source-change triggers.

### Excessive agency

An agent sends communications, changes records, deletes data, modifies permissions, or makes financial/legal commitments without valid approval.

Controls: recommend/prepare defaults; explicit action classes; human approval; reversible operations; scoped credentials; audit.

### Cross-client retrieval

Content from one client appears in another client's context or output.

Controls: security boundary selection before search; separate indexes/storage where needed; negative tests; deny-by-default filters.

### Supply-chain compromise

An Obsidian plugin, agent skill, MCP server, package, container, installer, or model endpoint introduces malicious code or data access.

Controls: pin, review, scan, inventory, sandbox, minimise, test with synthetic data, and monitor updates.

### Secret leakage

Credentials enter Markdown, Git history, prompts, logs, generated outputs, or backups.

Controls: Vaultwarden/SOPS-age; secret scanning and push protection; placeholders; log redaction; rotation process.

### Concurrency and sync corruption

Multiple agents or sync services overwrite changes or produce inconsistent knowledge.

Controls: one writer; transaction locks; draft-return workers; no mixed bidirectional sync; Git snapshots; conflict alerts.

### Loss and ransomware

Vault, source snapshots, or history are deleted, encrypted, or corrupted.

Controls: 3-2-1 encrypted backups; immutable/offline copy; versioning; monitored jobs; restoration tests.

### Cognitive over-reliance

Users accept polished summaries, lose contact with original evidence, or delegate understanding.

Controls: citations; uncertainty; contradiction prompts; scheduled human review; challenge workflows; quality sampling.

## Required testing

- Direct and indirect prompt injection
- Secret and personal-data exfiltration
- Cross-client isolation
- Unsupported claim insertion
- Contradictory sources
- Stale and revoked source handling
- Concurrent writer prevention
- Approval bypass
- Rollback and restore
- Provider/connector failure
- Cost and resource bounds
