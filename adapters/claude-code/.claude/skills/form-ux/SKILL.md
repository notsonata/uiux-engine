---
name: form-ux
description: Design data-entry flows through field grouping, labels, control choice, validation strategy, smart defaults, progressive disclosure, accessibility, and recovery. Internal reasoning skill used by the public UX commands.
user-invocable: false
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---
# Form UX

## Purpose

Minimize effort and ambiguity while preventing avoidable errors.

## Field necessity

For every field ask:
- Is it needed for the user's current goal?
- Can it be safely inferred or defaulted?
- Can it be requested later?
- Does the user know the answer at this point?

Do not expose fields merely because they exist in the data model.

## Grouping and disclosure

Group fields by user task or decision, not database ownership. Reveal advanced or conditional fields only when relevant. Do not turn a short form into a wizard just to make each screen sparse.

## Labels and controls

Use persistent labels. Place format constraints before failure when practical. Choose controls by behavior, not fashion:
- checkbox for independent booleans;
- radio/segmented choices for small exclusive sets;
- select/combobox for larger sets;
- switch only when the change is immediate;
- input types appropriate to the required data and device.

## Defaults

A default should reduce work without hiding a consequential choice. Never preselect consent, destructive behavior, or a risky option simply to speed completion.

## Validation

Validate at a useful moment. Avoid errors while the user is still forming a valid value. An error should identify:
- what is wrong;
- where it is;
- how to fix it;
- whether existing input was preserved.

Preserve entered data after recoverable failures.

## Accessibility

Maintain logical focus order, visible focus, programmatic labels, useful error associations, non-color validation cues, and sufficiently large touch targets.

## Handoff

Return field inventory, grouping, defaults, validation timing, error/recovery behavior, and progressive-disclosure rules.
