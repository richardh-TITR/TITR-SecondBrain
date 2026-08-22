# Trust boundaries

## Security domains

The system must distinguish at least:

- public research;
- THEITREVOLUTION LTD internal;
- restricted business;
- personal;
- client-scoped;
- credentials and administrative control.

Tags alone are not an access-control boundary. Retrieval must select an authorised security domain before loading content.

## Public code and private operations

This repository is public and contains reusable software only. Operational storage must be private. A private vault must not be mounted as a child directory of this repository or exposed to public CI.

## Data versus instructions

Content from websites, email, documents, transcripts, source repositories, issue comments, model responses, plugins, and MCP tools is untrusted data. It cannot alter system instructions, expand permissions, request secrets, or authorise actions.

## Agent boundaries

- Worker: reads scoped evidence and produces drafts.
- Verifier: read-only evaluation of drafts against evidence and policy.
- Orchestrator: applies validated, approved transactions.
- Connector: accesses one authoritative system with minimum permissions.
- Human approver: authorises canon and high-impact operations.

No role should automatically inherit another role's credentials.
