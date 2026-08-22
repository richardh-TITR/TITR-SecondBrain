# Synthetic vault template

This directory documents the portable structure expected from a private operational vault. It contains templates only and must not be used as the live vault.

Recommended private vault layout:

```text
_system/        schemas, instructions, indexes, policy
inbox/          untrusted captures awaiting processing
sources/        immutable evidence or stable source manifests
drafts/         untrusted AI-proposed transactions
wiki/           reversible source-grounded synthesis
canon/          human-approved decisions and facts
daily/          working daily notes
meetings/       reviewed meeting knowledge
projects/       project context and Maps of Content
reviews/        daily, weekly and monthly reviews
outputs/        briefs, reports and prepared actions
audit/          append-only operation and approval records
archive/        inactive knowledge
```

A production deployment must place the live vault in separate private storage. Do not copy private content back into this public template repository.
