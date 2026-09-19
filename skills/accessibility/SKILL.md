---
name: accessibility
description: Review or specify accessible UI semantics, keyboard and focus behavior, contrast, labels, target sizes, motion, errors, media alternatives, and assistive-technology support. Use during design, implementation review, or UX audits for web, mobile, or desktop interfaces.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Accessibility

## Objective

Ensure core tasks do not require a specific sensory, motor, or input capability when a reasonable alternative can be provided.

Treat applicable platform accessibility guidance and WCAG as requirements, not aesthetic preferences.

## Structure and semantics

Prefer native semantic controls and structures before custom equivalents. Ensure headings, landmarks, lists, tables, labels, and form relationships reflect the visual structure.

## Keyboard

Core functionality must be operable without a pointer where the platform expects keyboard interaction. Check:
- logical focus order;
- visible focus;
- no keyboard trap;
- dialogs and menus manage focus correctly;
- custom controls expose equivalent keyboard behavior;
- skipped or hidden content is not unexpectedly focusable.

## Names and instructions

Interactive controls need meaningful accessible names. Icon-only controls require labels. Errors and required states must be programmatically associated with fields where applicable.

## Color and contrast

Do not use color alone to communicate status, selection, validation, or category. Verify text and meaningful graphical contrast against the applicable accessibility standard.

## Motion

Avoid unnecessary motion and provide reduced-motion behavior for nonessential animation. Never make essential understanding depend on animation alone.

## Targets and gestures

Provide adequately sized interaction targets and spacing. Avoid requiring precise gestures where a simpler alternative is feasible. Provide non-gesture alternatives for critical actions.

## Content changes

For dynamic interfaces, make important asynchronous changes perceivable to assistive technology without announcing excessive noise.

## Testing mindset

Do not claim an interface is "accessible" based only on code inspection. Distinguish design review, automated checks, keyboard testing, screen-reader testing, and user testing.

## Output

Provide concrete requirements or findings, the affected user/task, the remediation, and how to verify it.
