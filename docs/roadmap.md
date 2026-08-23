# Roadmap

## Phase 0: Governance and safety foundation

- Confirm repository visibility and licence.
- Accept architecture and security ADRs.
- Define data classification, retention, and approval policy.
- Create threat model and DPIA decision record.
- Define model-provider and connector data handling.
- Establish dependency, plugin, skill, and MCP review process.
- Configure protected branches, secret scanning, and dependency updates.

Exit: no unresolved critical data-boundary or ownership questions.

## Phase 1: Synthetic vault prototype

- Build the portable Markdown vault scaffold.
- Implement source, claim, decision, daily, meeting, and review templates.
- Implement ingest, query, lint, preview, approve, apply, and rollback operations.
- Add stable IDs, source hashing, ledgers, transaction logs, and schema validation.
- Use synthetic fixtures only.
- Test Claude Code and AGENTS.md-compatible Codex operation.

Exit: a synthetic source can produce a cited draft, verified transaction, approved wiki update, and successful rollback.

## Phase 2: Private pilot

- Deploy a separate private operational vault.
- Configure encrypted sync and independent backups.
- Integrate one allowlisted low-risk source domain.
- Run daily brief and weekly review in recommendation-only mode.
- Measure citation accuracy, unsupported claims, maintenance effort, and usefulness.

Exit: 30-day pilot meets the acceptance metrics without privacy, integrity, or isolation incidents.

## Phase 3: Microsoft 365 integration

- Register a least-privilege Entra application.
- Use Graph delta queries and allowlisted SharePoint/OneDrive locations.
- Add selected calendar and Teams transcript workflows.
- Implement retention, deletion, and source revocation.
- Complete DPIA where required.

Exit: incremental ingestion is observable, scoped, reversible, and compliant with approved policy.

## Phase 4: Controlled operational workflows

- Meeting preparation and post-meeting extraction.
- Project context packs.
- Commitment and decision tracking.
- ConsultancyOS approval queue and briefs.
- Prepared CRM/task/calendar actions with human approval.

Exit: operational workflows save more time than they cost and retain human accountability.

## Phase 5: Retrieval optimisation

- Establish a retrieval evaluation set.
- Measure exact/full-text/index retrieval.
- Pilot qmd or another local hybrid index only if required.
- Test cross-domain isolation, prompt injection, stale claims, and leakage.

Exit: any added search service demonstrates measurable benefit and passes security evaluation.

## Success measures

- 100% of important claims linked to evidence.
- Zero high-impact changes applied without required approval.
- Zero cross-client retrieval incidents.
- Unsupported factual assertions below the approved tolerance.
- Meeting action extraction above the approved accuracy target.
- Daily and weekly workflows are consistently useful.
- Maintenance time remains below time saved.
- Backup restoration tests succeed.
