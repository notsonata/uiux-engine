# Popovers and Tooltips

## Use when
- A compact contextual surface needs brief controls or explanation.
- The content is tied to a specific trigger.

## Avoid when
- The content is essential and should remain visible.
- Complex editing or long reading is required.

## Core anatomy
- Trigger.
- Contextual content.
- Dismiss behavior.
- Optional actions for popovers.

## State and behavior
- Open/closed, keyboard focus, unavailable trigger if relevant.

## Accessibility
- Tooltip content should be available to keyboard focus, not hover only.
- Popover focus behavior should match whether it contains interactive controls.

## Responsive behavior
- On touch screens, ensure invocation does not depend on hover; consider a sheet for complex content.

## Decision rules
- Tooltips explain; they should not contain required actions.
- Popovers may contain actions but should remain small and contextual.
- Do not use tooltips to compensate for unclear primary labels.

## Related
- ../actions/row-actions.md
- dialogs.md
- drawers.md
