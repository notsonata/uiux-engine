# Master-Detail

## Use when
- Users repeatedly move between a collection and one item's details.
- Maintaining list context improves efficiency.

## Avoid when
- Details are complex enough to deserve a full dedicated workflow.
- Small screens cannot sustain simultaneous panes without confusion.

## Core anatomy
- Master list.
- Current selection.
- Detail pane.
- Navigation/history behavior.

## State and behavior
- Handle no selection, loading detail, missing/deleted item, and list refresh.
- Keep selection stable when the list updates if the item still exists.

## Accessibility
- Selection and focus are separate concepts and should not be conflated.
- Pane headings should make context clear.

## Responsive behavior
- Collapse to list → detail navigation on narrow screens.
- Preserve a clear way back to the prior list state.

## Decision rules
- Do not make row click semantics ambiguous between selection and navigation.
- Keep list filters/sort when returning from detail.
- Use when repeated back-and-forth is core to the task.

## Related
- lists-vs-cards.md
- tables.md
