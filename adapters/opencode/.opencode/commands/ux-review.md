---
description: UX pass on the current diff before merge
agent: ux-auditor
subagent: true
---

Review the current git diff using UIUX Engine diff-review mode.

Focus only on changed user-facing behavior and likely regressions introduced by the diff.

Prioritize:
- state gaps;
- hierarchy regressions;
- affordance and feedback;
- copy clarity;
- destructive-action safety;
- form behavior;
- accessibility regressions;
- responsive regressions;
- DESIGN.md and design-system drift.

Distinguish pre-existing issues from regressions introduced by the diff.

For every finding include severity, changed file or surface, evidence, user impact, recommended patch direction, and verification.

End with a concise merge-readiness summary listing unresolved UX risks without a numeric score.
