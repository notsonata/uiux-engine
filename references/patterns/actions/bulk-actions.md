# Bulk Actions

## Use when
- Users repeatedly act on multiple records.
- Selection materially reduces repetitive work.

## Avoid when
- Actions differ per item in ways that make group behavior ambiguous.
- Bulk operations would hide important per-item decisions.

## Core anatomy
- Selection mechanism.
- Selection count and scope.
- Bulk action bar or menu.
- Clear success/failure reporting, including partial success.

## State and behavior
- Support none, some, and all-selected states.
- Distinguish page selection from all-results selection.
- Handle partial failure item-by-item when needed.

## Accessibility
- Selection must be keyboard operable and programmatically associated with rows/items.
- Do not communicate selection by highlight color alone.

## Responsive behavior
- Use a sticky selection/action region when helpful.
- Do not hide the selection count on small screens.

## Decision rules
- Only offer actions valid for the whole selection or explain mixed eligibility.
- Make destructive bulk actions proportionally safer than single-item actions.
- Preserve selection after recoverable failure when practical.

## Related
- row-actions.md
- ../data-display/tables.md
- ../feedback/long-running-jobs.md
