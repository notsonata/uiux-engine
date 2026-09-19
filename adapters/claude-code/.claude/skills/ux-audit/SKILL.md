---
name: ux-audit
description: Produce a prioritized, actionable UX audit of a file, URL, screen, screenshot, or path.
argument-hint: "[file, URL, screen, screenshot, or path]"
disable-model-invocation: true
context: fork
agent: ux-auditor
background: false
---

# UX Audit

Audit: $ARGUMENTS

Run a full UX audit using the preloaded UIUX Engine reasoning skills.

Requirements:
1. Inspect the target that is actually available.
2. Separate observed evidence from inference and unverified behavior.
3. Audit task fit, hierarchy, state completeness, forms, feedback and affordance, accessibility, responsive behavior, design-system consistency, and visual character as applicable.
4. Rank findings by user impact using blocker, high, medium, or low severity.
5. Give a concrete recommended change and verification method for every finding.
6. Start with the 3 to 5 most consequential findings.

Do not assign an arbitrary UX score.
Do not modify code unless the user explicitly asked for fixes.
