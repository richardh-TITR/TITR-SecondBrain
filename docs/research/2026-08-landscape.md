# AI second-brain landscape review

- Review date: 2026-08-22
- Purpose: record the external evidence behind the initial architecture

## Primary pattern

Andrej Karpathy's LLM Wiki proposal defines immutable raw sources, an AI-maintained Markdown wiki, and a schema/instruction layer. It introduces ingest, query, lint, index, and chronological log operations, and recommends delaying embedding infrastructure at moderate scale.

Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Workflow lineage

Tiago Forte's CODE/PARA approach supplies Capture, Organise, Distil, Express, and a later explicit Review step.

Sources:

- https://fortelabs.com/blog/basboverview/
- https://fortelabs.com/blog/the-book-ive-been-waiting-to-write-for-15-years/

Ron Forbes demonstrates the practical Obsidian, agent, voice capture, meeting intelligence, daily brief, and weekly review workflow. It is useful workflow evidence, but it is a personal prototype rather than a complete business security architecture.

Sources:

- https://www.ronforbes.com/blog/building-your-ai-second-brain
- https://www.ronforbes.com/tech

## Implementation evidence

### claude-obsidian

Strongest reference for immutable content-addressed sources, claim/source ledgers, provenance, transaction previews, guarded apply, and single-writer orchestration.

Source: https://github.com/AgriciDaniel/claude-obsidian

Adoption: use as a reviewed reference and potential upstream, not as an unaudited one-line installation.

### COG-second-brain

Useful independent-verifier and acceptance-harness patterns. Its complete multi-agent and skill surface is too large for the initial TITR implementation.

Source: https://github.com/huytieu/COG-second-brain

Adoption: borrow worker/verifier separation and evidence-based acceptance.

### obsidian-second-brain

Useful temporal-fact and supersession ideas. Automatic contradiction resolution and whole-vault rewriting exceed the initial TITR risk tolerance.

Source: https://github.com/eugeniughelbur/obsidian-second-brain

Adoption: borrow temporal metadata; reject silent autonomous canon changes.

### Obsidian agent skills

Portable skills for valid Obsidian Markdown, Bases, Canvas, and CLI operations.

Source: https://github.com/kepano/obsidian-skills

Adoption: pin and review only the required skills.

### qmd

Local CLI/MCP hybrid Markdown search.

Source: https://github.com/tobi/qmd

Adoption: defer until measured retrieval failures justify it.

## Security and governance

- OWASP prompt injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- OWASP GenAI risks: https://genai.owasp.org/llm-top-10/
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- ICO AI guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
- MCP security practices: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
- Microsoft Graph delta queries: https://learn.microsoft.com/en-us/graph/delta-query-overview

## Conclusions

The strongest convergent design is not a large RAG application. It is an open Markdown knowledge compiler with immutable evidence, provenance, explicit instructions, reversible transactions, independent verification, human-approved canon, and disciplined recurring review.

Popularity is not longitudinal proof. The initial implementation therefore requires a synthetic pilot and measurable acceptance criteria before broader ingestion or autonomy.
