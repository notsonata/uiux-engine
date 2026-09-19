---
name: ux-design
description: Design or redesign a UI with an intent brief, wireframe, state coverage, and UX specification before implementation. Invoke explicitly for UI/UX design work.
---

# UX Design

Use the custom `ux_designer` subagent for this workflow and wait for its result before continuing.

The subagent must read the internal UIUX Engine reasoning modules under:

- `.uiux/skills/ux-intent-discovery/SKILL.md`
- `.uiux/skills/information-hierarchy/SKILL.md`
- `.uiux/skills/state-completeness/SKILL.md`
- `.uiux/skills/form-ux/SKILL.md`
- `.uiux/skills/feedback-and-affordance/SKILL.md`
- `.uiux/skills/design-system/SKILL.md`
- `.uiux/skills/visual-character/SKILL.md`

Required sequence:
1. Inspect the existing product, code, and design context when available.
2. Establish the user, primary job, decision/information need, constraints, and worst plausible mistake.
3. Establish information and action hierarchy.
4. Cover loading, empty, partial, error, success, and offline states.
5. Apply form UX when meaningful input exists.
6. Define feedback, affordance, destructive-action protection, accessibility, and responsive behavior.
7. Read or establish DESIGN.md and preserve the existing design system.
8. Make deliberate type, color, space, and finish decisions.
9. Produce a low-fidelity structural wireframe.
10. Produce an implementation-ready UX specification.
11. If implementation is requested, implement only after the design gate above is explicit.

Do not jump directly to polished components.
Do not invent user research.
If context is sufficient, do not ask redundant questions.
