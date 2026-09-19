# Dialogs

## Use when
- A focused decision or short task should interrupt the current context.
- Confirmation or contained editing benefits from temporary focus.

## Avoid when
- The task is long, multi-step, or requires broad context.
- A non-modal inline surface would be less disruptive.

## Core anatomy
- Title.
- Purpose/context.
- Content.
- Primary and secondary actions.
- Close/cancel behavior.

## State and behavior
- Loading within a dialog should stay local.
- Prevent duplicate submit for consequential actions.
- Define dismissal behavior for unsaved work.

## Accessibility
- Move focus into the dialog and restore it on close.
- Trap focus only while modal.
- Escape behavior should be predictable unless unsafe.

## Responsive behavior
- Convert to a full-screen sheet/dialog when narrow screens cannot support the content comfortably.

## Decision rules
- Do not stack modal dialogs.
- Do not use a dialog for information that users need while interacting with the underlying page.
- Confirmation copy should name the consequence.

## Related
- ../actions/destructive-actions.md
- drawers.md
