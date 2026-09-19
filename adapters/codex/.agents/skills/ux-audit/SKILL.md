---
name: ux-audit
description: Produce a prioritized, actionable UX audit of a file, URL, screen, screenshot, or path. Invoke explicitly when you want a full UX audit.
---

# UX Audit

Use the custom `ux_auditor` subagent in full-audit mode and wait for its result.

The subagent must read the relevant internal UIUX Engine reasoning modules under `.uiux/skills/`, including the internal `ux-auditor` protocol.

Requirements:
1. Inspect the target that is actually available.
2. Separate observed evidence from inference and unverified behavior.
3. Audit task fit, hierarchy, state completeness, forms, feedback and affordance, accessibility, responsive behavior, design-system consistency, and visual character as applicable.
4. Rank findings by user impact using blocker, high, medium, or low severity.
5. Give a concrete recommended change and verification method for every finding.
6. Start with the 3 to 5 most consequential findings.

Do not assign an arbitrary UX score.
Do not modify code unless the user explicitly asked for fixes.
