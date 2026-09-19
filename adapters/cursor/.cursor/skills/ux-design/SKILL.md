---
name: ux-design
description: Design or redesign a UI with an intent brief, wireframe, state coverage, and UX specification before implementation.
disable-model-invocation: true
---

# UX Design

Treat the user's current message as the design task.

Read `.uiux/agents/ux-designer.md`, then delegate the design pass to an isolated Cursor subagent using that contract. The subagent should read the relevant hidden reasoning modules under `.uiux/skills/` and return its result before implementation continues.

Required workflow:
1. Inspect the existing product, code, and design context when available.
2. Establish user intent, required information, constraints, and the worst plausible mistake.
3. Establish information and action hierarchy.
4. Cover loading, empty, partial, error, success, and offline states.
5. Apply form UX when meaningful input exists.
6. Define feedback, affordance, destructive-action protection, accessibility, and responsive behavior.
7. Read or establish DESIGN.md and preserve the existing design system.
8. Make deliberate type, color, space, and finish decisions.
9. Produce a low-fidelity structural wireframe.
10. Produce an implementation-ready UX specification.
11. If implementation was requested, implement only after the design gate is explicit.

Do not jump directly to polished components.
Do not invent user research.
Do not ask redundant questions when the context already answers them.
