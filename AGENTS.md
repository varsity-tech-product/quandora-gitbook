# quandora-gitbook Agent Rules

## Living Map

This repository owns Quandora's public, user-facing GitBook in English and
Simplified Chinese. Organize content by user journey and keep public language
independent of internal deployment topology.

Canonical navigation lives in `SUMMARY.md` and follows this order:

1. Start here
2. Factor Mining
3. Factor Analysis
4. Strategy Building
5. Strategy Analysis
6. Portfolio Building
7. Portfolio Analysis
8. Portfolio Trading Analysis
9. Concepts and reference
10. Availability and support

The first six workflows use historical backtests. Portfolio Trading Analysis
covers forward evidence, Simulation account/run management, and read-only Live
analysis. Each task guide provides web steps and an Agent example where the
product supports them; do not invent web controls to make the paths symmetric.
Keep existing source paths stable when titles or navigation placement change.
GitBook page groups also affect published URLs. Preserve moved public routes in
each language's `.gitbook.yaml` redirects and check them in the PR preview.

Page responsibilities:

- `en/` is the authoritative English GitBook source.
- `zh/` is the repository-owned Simplified Chinese GitBook source.
- Root public Markdown is a temporary compatibility mirror of `en/` until the
  existing GitBook Space is repointed and validated.
- Within each language, `README.md` is the introduction and audience router;
  `getting-started/` owns activation; `guides/` owns task-oriented journeys;
  `understanding-quandora/` owns durable concepts; and `trust/` owns public
  availability, limitations, security, privacy, and support.
- `localization/glossary.json` owns approved bilingual product terminology.
- `LOCALIZATION.md` owns the GitBook migration and rollback runbook.
- `docs-policy.json` is the machine-readable documentation policy.
- `scripts/verify_docs.py` enforces the policy locally and in CI.

Internal engineering scenario guides may be used as product-fact inputs, but
must be translated before appearing here:

- start from the user's goal, choice, and visible outcome;
- preserve meaningful distinctions such as revise, fork, and rerun;
- explain pending, failed, stopped, and archived states in user language;
- hide RPC ordering, service identities, cursors, idempotency mechanics,
  provider topology, internal identifiers, and rollout controls.

## Public Language

- Document Factor, Strategy, and Portfolio research separately from Simulation
  and real Live execution. Use the seven workflow names consistently.
- Simulation may appear as Paper in interface labels. Explain that alias once
  in relevant guides without presenting it as a different product.
- Live access remains invite-only; access and actions depend on account
  eligibility. The plugin analyzes existing Live evidence read-only. Live
  setup and execution controls belong to the web interface.
- Do not describe a capability as generally available before the matching
  public product and plugin support it.
- Preserve existing authorization across workflow handoffs. Analysis alone is
  read-only; an explicit build-and-backtest request covers both steps.
- Do not expose internal environment names, rollout mechanics, private
  endpoints, credentials, or infrastructure in public pages.
- Do not invent security, privacy, retention, pricing, support, or operational
  claims. Leave owner-marked handoff pages until the responsible team supplies
  approved content.
- Cost viability is diagnostic evidence, not a factor Success/Fail gate.
- Do not duplicate executable grading logic in CI. Runtime-owned semantics may
  be explained in prose, but computation remains owned by the product runtime.

## Content Handoffs

Incomplete owner-supplied pages use frontmatter:

```yaml
content_status: handoff
content_owner: plugin-and-product-backend
```

Allowed handoff owners and expected pages are declared in `docs-policy.json`.
Remove the handoff status only when the owning team supplies and approves the
complete user procedure or policy.

Chinese pages declare one translation state:

- `draft`: translated in Git but awaiting final language-owner approval;
- `reviewed`: approved Chinese copy;
- `pending`: Chinese copy is not ready and the page temporarily shows the
  English source with a visible notice.

Keep corresponding `en/` and `zh/` relative paths identical. During migration,
apply every English content change to both root compatibility Markdown and
`en/`; CI rejects drift.

## Verify

Run:

```bash
make verify
```

The verifier checks navigation order and coverage, local links and assets,
handoff ownership, public-language restrictions, deprecated gate claims, and
the canonical registration URL.
