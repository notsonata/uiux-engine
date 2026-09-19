# Search Input

## Use when
- Users need direct retrieval by a known term or partial memory.
- Search is faster than navigating categories.

## Avoid when
- The collection is tiny.
- The system cannot provide useful matching behavior.

## Core anatomy
- Clear search label/placeholder.
- Submit or live-search behavior.
- Clear action.
- Result/zero-result feedback.
- Scope if search is constrained.

## State and behavior
- Loading, zero results, network failure, and partial suggestions should be explicit.
- Preserve the query while results update.

## Accessibility
- Label search meaningfully.
- Announce result-count changes judiciously for live search.

## Responsive behavior
- Search can expand into a focused surface on small screens, but scope and query must persist.

## Decision rules
- Do not overload placeholder text with all instructions.
- Use debounce for live search when needed.
- Make matching scope visible if it is not global.

## Related
- ../data-display/filtering-and-sorting.md
- ../feedback/empty-states.md
