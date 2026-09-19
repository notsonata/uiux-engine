---
name: uiux-design
description: Design or redesign a user interface or end-to-end product flow. Use for new screens, features, workflows, prototypes, product UI changes, or requests to improve overall UI/UX. Coordinates research, information architecture, interaction, states, accessibility, responsive behavior, visual design, and design-system consistency before implementation.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# UI/UX Design Orchestrator

Use this skill when the task is broader than a single specialist concern.

## Objective

Produce interfaces that are understandable, complete, recoverable, accessible, responsive, and visually coherent. Optimize for the user's task before optimizing for visual novelty.

## Non-negotiable rule

Do not begin by choosing colors, card styles, gradients, illustrations, or animation. First understand the user, task, content hierarchy, interaction model, and major states.

## Workflow

### 1. Establish the design problem
Identify:
- who is using the interface;
- what they are trying to accomplish;
- what triggers the task;
- what information they need to decide or act;
- what a costly mistake looks like;
- whether the interface already exists;
- technical, business, policy, device, or platform constraints.

When evidence is absent, explicitly label assumptions. Do not fabricate user research.

For ambiguous product problems, use `ux-research`.

### 2. Define success
State the observable user outcome. Prefer task outcomes such as "user can compare three plans and select one with confidence" over implementation outputs such as "create three pricing cards."

Identify one primary task per surface whenever possible.

### 3. Build the information hierarchy
Use `information-architecture` to determine:
- what must be visible immediately;
- what supports the primary decision;
- what can be secondary or progressive disclosure;
- navigation and grouping;
- labels and terminology.

Do not give every element equal visual weight.

### 4. Define the interaction model
Use `interaction-design` for:
- primary and secondary actions;
- selection and editing behavior;
- navigation transitions;
- confirmations, undo, and destructive actions;
- keyboard, pointer, touch, and focus behavior;
- feedback timing and affordances.

### 5. Complete the states
Use `states-and-feedback` before considering the flow complete. At minimum consider:
- initial;
- loading;
- empty;
- partial;
- success;
- error;
- validation;
- disabled/unavailable;
- permission/auth/session states when relevant;
- stale/conflict/offline states for networked or collaborative products.

### 6. Handle data entry deliberately
If the flow contains meaningful input, use `forms-and-inputs`.

Minimize requested data, group related fields, provide labels, and validate at useful moments. Never rely on placeholders as the only labels.

### 7. Apply accessibility requirements
Use `accessibility` before finalizing interaction or visual decisions.

Accessibility is a design constraint, not a post-build checklist.

### 8. Define responsive transformations
Use `responsive-design` for interfaces expected to work across sizes or input modes.

Do not merely stack desktop columns. Decide what gets prioritized, collapsed, moved, converted, or deferred.

### 9. Preserve or establish a design system
If an existing product is being changed, inspect its tokens and recurring components with `design-system` before introducing new visual language.

Prefer extension over gratuitous replacement.

### 10. Define visual character
Use `visual-design` only after the preceding structure is stable.

Specify hierarchy, type roles, spacing rhythm, density, color roles, surfaces, borders, imagery, and motion. Avoid generic aesthetic decoration that has no relationship to the product, audience, or content.

### 11. Produce an implementation-ready output
Unless the user asks for a different artifact, provide:
1. problem and user outcome;
2. assumptions and constraints;
3. primary flow;
4. screen/component inventory;
5. information hierarchy;
6. state behavior;
7. interaction rules;
8. accessibility requirements;
9. responsive behavior;
10. visual direction;
11. acceptance criteria.

Use `../../templates/UX-SPEC.md` as a structure when useful.

## Working with existing code or screenshots

Before proposing changes:
1. inspect the current information architecture and components;
2. identify patterns already used elsewhere;
3. distinguish functional problems from visual preference;
4. preserve behavior that already works unless there is evidence it should change;
5. avoid rebuilding components solely for stylistic consistency if tokens or variants can solve the problem.

## Quality gates

A design is not ready if any of these are unresolved:
- the primary user/task is unclear;
- the main action competes with several equivalent actions;
- error or empty states are unspecified;
- a destructive action lacks proportional recovery protection;
- keyboard/focus behavior is impossible or undefined for core interactions;
- mobile behavior is described only as "responsive";
- visual decisions contradict the established design system without a reason;
- success is defined only by visual polish.
