# quandora-gitbook Agent Rules

## Living Map

This repository owns Quandora's public, user-facing GitBook. Organize content by
user journey and keep public language independent of internal deployment
topology.

Canonical navigation lives in `SUMMARY.md` and follows this order:

1. Start here
2. Test your first idea
3. Understand the result
4. Improve and rerun
5. Build and evaluate a strategy
6. Paper trade a strategy
7. Availability and limitations
8. Concepts and reference
9. Security, privacy and support

Page responsibilities:

- `README.md` is the public introduction and audience router.
- `getting-started/` owns installation and first-run activation.
- `guides/` owns task-oriented user journeys and content-owner handoffs.
- `understanding-quandora/` owns durable concepts and reference material.
- `trust/` owns public availability, limitations, security, privacy, and support.
- `docs-policy.json` is the machine-readable documentation policy.
- `scripts/verify_docs.py` enforces the policy locally and in CI.

## Public Language

- Factor Mining, strategy composition/backtesting, and strategy paper trading
  are available to public users.
- Live trading is invite-only and is not open to general public users.
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

## Verify

Run:

```bash
make verify
```

The verifier checks navigation order and coverage, local links and assets,
handoff ownership, public-language restrictions, deprecated gate claims, and
the canonical registration URL.

