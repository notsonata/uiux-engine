---
name: restyle
description: Diagnose an existing UI by type, color, space, and finish, apply DESIGN.md, and return a before/after without changing product behavior. Invoke explicitly for visual-system restyling.
---

# Restyle

This is a visual-system task, not a product redesign.

Read:
- `.uiux/skills/design-system/SKILL.md`
- `.uiux/skills/visual-character/SKILL.md`
- `.uiux/skills/feedback-and-affordance/SKILL.md` only when visual affordance issues can be corrected without changing behavior.

Workflow:
1. Inspect the target and existing system.
2. Read DESIGN.md.
3. If DESIGN.md is missing, consolidate the system already present before styling.
4. Diagnose the UI on four axes: type, color, space, finish.
5. Identify deliberate, inconsistent, and default-looking decisions.
6. Apply DESIGN.md and resolve off-system values.
7. Re-check focus, contrast, status cues, target sizing, and reduced motion.
8. Return a before/after summary.

Preserve application logic, data flow, component responsibility, information meaning, copy meaning, and feature scope.

If structural UX changes are required, report them as out of scope and direct them to `$ux-design`.

Return:

| Axis | Before | After | Reason |
|---|---|---|---|
| Type | | | |
| Color | | | |
| Space | | | |
| Finish | | | |

Also list files changed and issues intentionally left untouched.
