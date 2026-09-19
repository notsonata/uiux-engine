---
name: ux-review
description: Review the current diff for UX regressions before merge, including state gaps, hierarchy, affordance, copy, accessibility, responsiveness, and design-system drift. Invoke explicitly before merging UI changes.
---

# UX Review

Use the custom `ux_auditor` subagent in diff-review mode and wait for its result.

Requirements:
1. Inspect the current git diff and identify changed user-facing surfaces.
2. Review only changed behavior and likely regressions introduced by the diff.
3. Prioritize state gaps, hierarchy regressions, feedback and affordance, copy clarity, destructive-action safety, form behavior, accessibility, responsive behavior, and DESIGN.md drift.
4. Distinguish pre-existing issues from regressions introduced by this diff.
5. Report blockers and high-impact issues first.
6. For each finding include severity, changed file or surface, evidence, user impact, recommended patch direction, and verification.

Do not broaden this into a whole-product audit.
Do not rewrite unrelated UI.
End with a concise merge-readiness summary listing unresolved UX risks without a numeric score.
