---
name: restyle
usage: /restyle [path or screen]
visibility: public
---

# /restyle

Diagnose an existing UI axis by axis, apply the project's DESIGN.md, and return a concise before/after.

## Route

Use:
- `design-system`
- `visual-character`
- `feedback-and-affordance` only for visual affordance issues that can be corrected without changing behavior

## Visual-only boundary

Preserve:
- application logic;
- data flow;
- component responsibility/architecture;
- information meaning;
- copy meaning;
- feature scope.

Do not turn a restyle into a product redesign.

## Workflow

1. Inspect the target and existing system.
2. Read `DESIGN.md`.
3. If DESIGN.md is missing, run `design-system` to consolidate the system already present before styling.
4. Diagnose the current UI on four axes:
   - type;
   - color;
   - space;
   - finish.
5. Identify which choices are deliberate, inconsistent, or default-looking.
6. Apply DESIGN.md and resolve off-system values.
7. Re-check accessibility-sensitive visual states such as focus, contrast, status cues, targets, and reduced motion.
8. Return a before/after summary.

## Output

Use a compact table:

| Axis | Before | After | Reason |
|---|---|---|---|
| Type | | | |
| Color | | | |
| Space | | | |
| Finish | | | |

Also list files changed and any issues intentionally left untouched because they require structural or product changes.
