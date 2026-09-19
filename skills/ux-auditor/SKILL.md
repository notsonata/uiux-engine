---
name: ux-auditor
description: Produce evidence-based, severity-ranked UX findings for a file, URL, screen, screenshot, implementation, or current code diff. Internal reasoning skill used by ux-audit and ux-review.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# UX Auditor

## Purpose

Turn observable UI problems into prioritized, shippable fixes rather than vague taste-based advice.

## Evidence rule

Inspect the actual target available. Distinguish:
- **observed:** directly visible or inspectable;
- **inferred:** strongly implied but not directly verified;
- **unverified:** requires runtime, viewport, assistive-tech, or user testing.

Do not call unobserved behavior broken.

## Audit lenses

Run the relevant internal skills:
- intent and task fit;
- information hierarchy and density;
- state completeness;
- form UX;
- feedback and affordance;
- design-system consistency;
- visual character.

Also inspect embedded accessibility and responsive requirements within those skills.

For `ux-review`, constrain findings to the current diff and likely regressions introduced by it.

## Severity

- **Blocker:** prevents a core task or creates severe safety, data-loss, or accessibility failure.
- **High:** likely task failure, serious misunderstanding, or repeated major friction.
- **Medium:** meaningful friction with a practical workaround.
- **Low:** refinement with limited task impact.

Do not assign an arbitrary 1-100 UX score.

## Finding format

Each finding must contain:
- title;
- severity;
- evidence/surface;
- user impact;
- recommended change;
- verification method.

Prefer "Publish state is indistinguishable in the table" over "Improve visual hierarchy."

## Prioritization

Order by user impact and frequency:
1. blockers, safety, data loss, severe accessibility barriers;
2. core-task comprehension and completion;
3. recovery/state failures;
4. repeated friction and design-system drift;
5. cosmetic refinement.

## Pattern references

Use `../../references/patterns/INDEX.md` only when a concrete pattern is relevant to an observed finding. Do not generate findings merely because an interface differs from a library pattern.
