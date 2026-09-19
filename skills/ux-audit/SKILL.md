---
name: ux-audit
description: Audit an existing UI, screenshot, prototype, product flow, or implemented interface for usability, information architecture, interaction, states, forms, accessibility, responsive behavior, and visual consistency. Use when asked to review, critique, improve, diagnose, or assess an existing interface.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# UX Audit

## Objective

Find concrete usability risks and improvement opportunities. Do not turn subjective visual preference into a usability finding.

Use `../../templates/AUDIT.md` for output structure when useful.

## Evidence first

Inspect the actual interface, flow, screenshots, code, or behavior available. State limitations when only one state or viewport is visible.

Do not assume missing behavior is broken if it cannot be observed. Mark it as unverified.

## Audit lenses

### Task and comprehension
- Is the purpose clear?
- Is the primary action obvious?
- Does terminology match the user's model?
- Is essential context present at decision time?

### Information architecture
- Are content and actions grouped logically?
- Is hierarchy visible?
- Can users find frequent destinations and actions?
- Is advanced complexity disclosed appropriately?

### Interaction
- Are controls recognizable and consistent?
- Is system feedback timely?
- Are destructive operations protected proportionally?
- Are selection, navigation, and editing meanings distinct?

### State completeness
Check applicable states in `../../references/STATE-MATRIX.md`.

### Forms
- Is every requested field necessary now?
- Are labels persistent and clear?
- Are validation and errors actionable?
- Is entered data preserved after recoverable failures?

### Accessibility
Use the `accessibility` skill. Distinguish observed violations from items requiring testing.

### Responsive behavior
Use the `responsive-design` skill when multiple sizes are available or responsive implementation can be inspected.

### Visual consistency
- Does visual weight match task priority?
- Are typography, spacing, color roles, and components consistent?
- Are decorative treatments increasing noise?
- Does the UI conform to its own design system?

## Severity

Use four levels:
- **Blocker:** prevents a core task or creates severe safety/data-loss/access barrier.
- **High:** causes likely failure, serious misunderstanding, or repeated major friction.
- **Medium:** noticeable friction or inconsistency with a practical workaround.
- **Low:** refinement with limited task impact.

Severity reflects user impact and frequency, not how difficult a fix is.

## Finding format

For every finding include:
- specific surface/evidence;
- affected user behavior;
- why it matters;
- recommended change;
- verification method.

Avoid vague findings such as "make it modern," "improve UX," or "add more whitespace."

## Prioritization

Order fixes by:
1. task blockers, data loss, safety, severe accessibility barriers;
2. core-task comprehension and completion;
3. repeated friction and recovery failures;
4. consistency and efficiency;
5. cosmetic refinement.

Do not use arbitrary 1-100 UX scores unless the user explicitly requires a scoring framework and the rubric is defined.
