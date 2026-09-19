# Settings Forms

## Use when
- Users configure persistent preferences or product behavior.
- Different settings have different save semantics.

## Avoid when
- The control is actually a one-time workflow rather than a persistent setting.

## Core anatomy
- Grouped settings by user concept.
- Clear labels and consequences.
- Immediate vs explicit-save semantics.
- Defaults/reset when meaningful.

## State and behavior
- Show saving/error state for immediate settings.
- Preserve unsaved edits for explicit-save forms.
- Separate destructive account/workspace actions from routine preferences.

## Accessibility
- Switches need clear labels and current state.
- Do not use a switch for a choice that only commits after Save unless that model is explicit.

## Responsive behavior
- Keep labels and descriptions readable; avoid dense multi-column settings on small screens.

## Decision rules
- Group by mental model, not backend module.
- Prefer immediate toggles only when changes are safe and reversible.
- Put dangerous account actions in a distinct danger zone.

## Related
- ../actions/destructive-actions.md
- validation-and-errors.md
