---
name: ux-review
usage: /ux-review
visibility: public
---

# /ux-review

Run a UX pass on the current diff before merge.

## Route

Delegate to the internal `ux-auditor` agent in diff-review mode.

## Scope

Review only changed UI behavior and likely regressions introduced by the current diff. Inspect surrounding code only when necessary to understand impact.

Prioritize:
- state gaps;
- hierarchy regressions;
- affordance and feedback;
- copy clarity;
- destructive-action safety;
- form behavior;
- accessibility regressions;
- responsive regressions;
- DESIGN.md/design-system drift.

## Contract

1. Inspect the current diff.
2. Identify changed user-facing surfaces.
3. Run only the internal skills relevant to those changes.
4. Report blockers/high-impact issues first.
5. Distinguish pre-existing problems from regressions introduced by the diff.

Do not rewrite unrelated UI. Do not broaden the review into a whole-product audit.

## Output

For each finding:
- severity;
- changed file/surface;
- evidence;
- user impact;
- recommended patch direction;
- verification.

End with a concise merge-readiness summary that lists unresolved UX risks without inventing a numeric score.
