# Sidebar Navigation

## Use when
- A product has several persistent top-level areas.
- Users benefit from always-visible location and switching.

## Avoid when
- The product has very few destinations.
- A mobile-only experience cannot justify persistent lateral space.

## Core anatomy
- Primary destinations.
- Current location.
- Optional grouped secondary destinations.
- Account/help/settings placement.

## State and behavior
- Current, hovered/focused, expanded/collapsed, and permission-hidden states.

## Accessibility
- Use semantic navigation and clear current-page indication.
- Collapsed icons still need names.

## Responsive behavior
- Collapse to drawer or compact navigation on narrow screens.
- Preserve destination labels where icon meaning is weak.

## Decision rules
- Order by frequency and product model, not implementation structure.
- Avoid deeply nested sidebars when a local page nav would be clearer.
- Keep current location obvious.

## Related
- mobile-navigation.md
- tabs.md
