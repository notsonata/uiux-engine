# Drawers

## Use when
- Secondary controls or details should remain connected to the current page.
- Filters or lightweight detail benefit from preserving underlying context.

## Avoid when
- The content is a primary workflow deserving its own page.
- The drawer would become a cramped full application.

## Core anatomy
- Title/context.
- Scrollable content.
- Close control.
- Actions anchored appropriately.

## State and behavior
- Handle loading and unsaved changes inside the drawer.
- Preserve underlying page state.

## Accessibility
- Manage focus like a modal when blocking interaction.
- If non-modal, make focus/interaction relationship explicit.

## Responsive behavior
- Drawers may become full-screen sheets on narrow screens.

## Decision rules
- Good for filters, secondary detail, and short edits.
- Avoid nesting drawers.
- Do not hide critical primary workflows in side panels.

## Related
- dialogs.md
- ../data-display/filtering-and-sorting.md
- ../navigation/mobile-navigation.md
