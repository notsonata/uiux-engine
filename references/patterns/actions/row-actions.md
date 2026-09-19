# Row Actions

## Use when
- A repeated list or table needs item-level operations.
- Users need fast access to a small set of predictable actions.

## Avoid when
- The entire row already has multiple conflicting click targets.
- Actions are rare enough that a detail view is clearer.

## Core anatomy
- Primary row destination if any.
- Visible frequent action when justified.
- Overflow for lower-frequency actions.
- Consistent placement across rows.

## State and behavior
- Clearly distinguish selection, navigation, and action invocation.
- Disable unavailable actions with a reason when important.
- Preserve row context after action completion.

## Accessibility
- Icon-only row actions need accessible names.
- Keyboard focus order should not become excessive in very dense tables.

## Responsive behavior
- Prioritize the highest-value action and move secondary actions into overflow if space collapses.
- Do not make hover the only way to discover an action.

## Decision rules
- A row click and a checkbox should never mean the same thing ambiguously.
- Keep destructive actions visually separated inside menus.
- Do not add an overflow menu when there is only one obvious action.

## Related
- bulk-actions.md
- ../data-display/tables.md
- ../overlays/popovers-and-tooltips.md
