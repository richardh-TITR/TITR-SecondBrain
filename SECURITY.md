# Security policy

## Scope

This repository contains public software and documentation. The live TITR-SecondBrain vault, authoritative documents, connector credentials, production configuration, logs, and backups must be stored separately in private controlled environments.

## Reporting a vulnerability

Do not disclose exploitable details, credentials, private data, or proof-of-concept payloads in a public issue. Report security concerns privately to the repository owner through an appropriate private channel.

## Security requirements

- No secrets or production data in Git history.
- Dependencies and external skills must be pinned and reviewed.
- Imported content is untrusted and may contain prompt injection.
- Model access and connector permissions follow least privilege.
- Source documents are read-only to AI workflows.
- Generated changes are staged, validated, diffed, and recoverable.
- High-impact mutations and external actions require human approval.
- Logs must not retain sensitive prompts or retrieved content by default.
- Backups must be encrypted and restoration tested.
- Client and security domains must be isolated before retrieval.

## Supported versions

Until the first release, only the latest commit on the default branch is supported.

## Public repository warning

Opening this repository to an AI agent does not authorise that agent to read adjacent directories, user profiles, credential stores, browser sessions, private repositories, or operational vaults.
