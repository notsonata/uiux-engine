# Mobile Navigation

## Use when
- A product must preserve navigation on constrained screens.
- Desktop navigation does not fit without transformation.

## Avoid when
- There is only one simple flow and persistent navigation is unnecessary.

## Core anatomy
- Primary destinations.
- Current location.
- Overflow/secondary destinations.
- Back behavior.

## State and behavior
- Open/closed drawer or selected destination state.
- Permission-specific visibility when relevant.

## Accessibility
- Touch targets must be comfortably sized.
- Drawer navigation needs focus containment and restoration.

## Responsive behavior
- Choose bottom nav for a small set of high-frequency destinations; drawer/menu for larger sets.
- Preserve labels for ambiguous icons.

## Decision rules
- Do not mechanically shrink desktop sidebars.
- Keep the primary task reachable without excessive nesting.
- Respect platform back conventions.

## Related
- sidebar-navigation.md
- ../overlays/drawers.md
