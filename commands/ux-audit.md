---
name: ux-audit
usage: /ux-audit [file, URL, screen, screenshot, or path]
visibility: public
---

# /ux-audit

Produce a prioritized, actionable audit of an existing interface.

## Route

Delegate to the internal `ux-auditor` agent in full-audit mode.

## Contract

1. Inspect the target that is actually available.
2. Separate observed evidence from inference and unverified behavior.
3. Audit intent fit, hierarchy, states, forms, feedback/affordance, design-system consistency, visual character, responsive behavior, and accessibility as applicable.
4. Rank findings by user impact.
5. Give a concrete fix and verification method for every finding.

Do not make code changes unless the user explicitly asks for fixes.

## Output

Start with the 3-5 most consequential issues, then the full severity-ranked findings.

Each finding includes:
- severity;
- evidence/location;
- user impact;
- recommended change;
- verification.

Do not assign an arbitrary UX score.
