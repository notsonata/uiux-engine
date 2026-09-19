---
name: ux-design
usage: /ux-design [task, screen, path, or feature]
visibility: public
---

# /ux-design

Design a new UI or redesign an existing flow with a wireframe and UX specification before implementation.

## Route

Delegate the reasoning pass to the internal `ux-designer` agent.

The agent may use:
- `ux-intent-discovery`
- `information-hierarchy`
- `state-completeness`
- `form-ux` when input is meaningful
- `feedback-and-affordance`
- `design-system`
- `visual-character`

## Contract

1. Inspect the existing product/code/design context when available.
2. Resolve user intent and the highest-cost mistake.
3. Produce an intent brief.
4. Produce a low-fidelity wireframe or structural screen map.
5. Produce an implementation-ready UX spec.
6. Only then implement if the user's request includes implementation.

Do not skip directly to polished components.

If the user supplied enough context, do not ask redundant questions. If they ask to skip questions, state assumptions and continue.

## Required pre-implementation output

- user + primary job;
- risk/worst mistake;
- hierarchy;
- wireframe;
- six-state coverage;
- interaction/affordance rules;
- form behavior when relevant;
- design-system constraints;
- visual-character decisions;
- responsive/accessibility requirements embedded in those decisions.

Use `templates/UX-SPEC.md` when useful.
