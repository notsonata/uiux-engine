# Filtering and Sorting

## Use when
- Users need to narrow or reorder a collection to find or compare items.
- Dataset size or heterogeneity makes manual scanning expensive.

## Avoid when
- There are too few items for controls to pay for themselves.
- Filters duplicate an existing navigation model.

## Core anatomy
- Filter controls.
- Active-filter summary.
- Clear/reset.
- Result count when useful.
- Sort control with understandable direction.

## State and behavior
- Zero-results state should distinguish filtering from truly empty data.
- Persist filters when returning from a detail view when appropriate.

## Accessibility
- Labels and selected states must be explicit.
- Do not rely on chip color to show activation.

## Responsive behavior
- Collapse secondary filters into a drawer/sheet if needed, while keeping active filters visible.
- Keep the most common filter directly accessible.

## Decision rules
- Default sort should match the dominant task.
- Do not combine filter and sort terminology ambiguously.
- Expose system-applied filters or scopes.

## Related
- tables.md
- ../overlays/drawers.md
- ../feedback/empty-states.md
