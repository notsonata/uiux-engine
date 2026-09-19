---
name: ux-audit
description: Produce a prioritized, actionable UX audit of a file, URL, screen, screenshot, or path.
disable-model-invocation: true
---

# UX Audit

Treat the user's current message as the audit target.

Read `.uiux/agents/ux-auditor.md`, then delegate the audit to an isolated Cursor subagent using that contract in full-audit mode. The subagent should read the relevant hidden reasoning modules under `.uiux/skills/`.

Requirements:
1. Inspect the target that is actually available.
2. Separate observed evidence from inference and unverified behavior.
3. Audit task fit, hierarchy, state completeness, forms, feedback and affordance, accessibility, responsive behavior, design-system consistency, and visual character as applicable.
4. Rank findings by user impact using blocker, high, medium, or low severity.
5. Give a concrete recommended change and verification method for every finding.
6. Start with the 3 to 5 most consequential findings.

Do not assign an arbitrary UX score.
Do not modify code unless the user explicitly asked for fixes.
