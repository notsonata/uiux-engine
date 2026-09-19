# Tabs

## Use when
- Users switch among peer views of the same object or scope.
- The alternatives are few and conceptually parallel.

## Avoid when
- Items form a process sequence rather than peer views.
- There are too many options to scan comfortably.

## Core anatomy
- Tab list.
- Selected tab.
- Panel content.
- Optional counts/status where decision-relevant.

## State and behavior
- Selected, unselected, disabled when truly unavailable, loading panel content.

## Accessibility
- Use tab semantics and expected arrow-key behavior when implementing actual tabs.
- Focus and selection behavior should be consistent.

## Responsive behavior
- Allow horizontal scrolling or transform when labels no longer fit.
- Do not truncate to ambiguous icons unless meaning remains clear.

## Decision rules
- Tabs switch context; they should not behave like unrelated navigation links without reason.
- Preserve selected tab in history/URL when deep linking matters.

## Related
- breadcrumbs.md
- sidebar-navigation.md
