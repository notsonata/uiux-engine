# Tables

## Use when
- Users compare values across records or columns.
- Dense repeated data benefits from aligned scanning.

## Avoid when
- Records are heterogeneous or primarily visual.
- The task is reading one item at a time rather than comparing many.

## Core anatomy
- Clear column labels.
- Stable row identity.
- Sortable/filterable columns only where useful.
- Predictable row actions and selection.

## State and behavior
- Define loading, empty, partial, error, and selected-row states.
- Preserve stable rows during background refresh when possible.

## Accessibility
- Use semantic table structure when the content is tabular.
- Header relationships and keyboard access must remain clear.
- Do not encode status only by cell color.

## Responsive behavior
- Prefer horizontal scroll when cross-column comparison matters.
- Prioritize columns when only a subset is essential.
- Convert to cards only when row-level scanning matters more than column comparison.

## Decision rules
- Do not hide critical comparison data just to avoid horizontal scroll.
- Avoid excessive action columns.
- Use sticky headers for long datasets when helpful.

## Related
- filtering-and-sorting.md
- pagination-vs-infinite-scroll.md
- ../actions/row-actions.md
- ../actions/bulk-actions.md
