# Lists vs Cards

## Use when
- Choosing between compact repeated rows and richer grouped records.
- The content needs a consistent repeated representation.

## Avoid when
- A table is better for cross-record comparison.
- The content is a single detail view.

## Core anatomy
- Stable item identity.
- Primary label.
- Supporting metadata.
- Clear destination or action.

## State and behavior
- Define selected, unread/changed, loading, and unavailable states as relevant.

## Accessibility
- Reading order should match visual order.
- Do not make the entire card clickable if nested interactive controls create conflict.

## Responsive behavior
- Lists generally compress well.
- Cards may stack but should not become deeply nested containers.

## Decision rules
- Choose lists for scan speed and repeated operations.
- Choose cards when grouping, imagery, or multi-line context materially helps.
- Do not use cards merely because they look modern.

## Related
- tables.md
- master-detail.md
