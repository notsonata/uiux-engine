# Breadcrumbs

## Use when
- Users navigate a real hierarchy and need location context.
- Deep pages benefit from predictable ancestor access.

## Avoid when
- The product structure is flat.
- Breadcrumbs would simply duplicate a short top nav.

## Core anatomy
- Ancestor sequence.
- Current page label, usually non-link.
- Clear hierarchy separator.

## State and behavior
- Handle very deep paths without losing the nearest useful ancestors.

## Accessibility
- Use breadcrumb navigation semantics and a current-page marker.

## Responsive behavior
- Collapse middle ancestors first while preserving root and nearest parent when useful.

## Decision rules
- Breadcrumbs represent hierarchy, not history.
- Do not use them as the only primary navigation.
- Labels should match actual locations.

## Related
- sidebar-navigation.md
- tabs.md
