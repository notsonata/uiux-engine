---
name: ux-design
description: Design or redesign a UI with an intent brief, wireframe, state coverage, and UX specification before implementation.
argument-hint: "[task, screen, path, or feature]"
disable-model-invocation: true
context: fork
agent: ux-designer
background: false
---

# UX Design

Work on: $ARGUMENTS

Use the preloaded UIUX Engine reasoning skills to design before implementation.

Required sequence:
1. Inspect existing product, code, and design context when available.
2. Establish user intent, required information, constraints, and the worst plausible mistake.
3. Establish information and action hierarchy.
4. Cover loading, empty, partial, error, success, and offline states.
5. Apply form UX when meaningful input exists.
6. Define feedback, affordance, destructive-action protection, accessibility, and responsive behavior.
7. Read or establish DESIGN.md and preserve the existing design system.
8. Make deliberate type, color, space, and finish decisions.
9. Produce a low-fidelity structural wireframe.
10. Produce an implementation-ready UX specification.
11. If the user's request includes implementation, implement only after the design gate above is explicit.

Do not jump directly to polished components.
Do not invent user research.
If context is sufficient, do not ask redundant questions.
If a material unknown blocks a sound decision, ask only the minimum necessary question.
