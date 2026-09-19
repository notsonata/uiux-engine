# Pagination vs Infinite Scroll

## Use when
- A result set is large enough that loading everything is inefficient.
- The browsing model needs an explicit retrieval strategy.

## Avoid when
- The dataset is small.
- The interface needs precise position/reference and infinite scroll would make it harder.

## Core anatomy
- Current position or loaded range.
- Loading affordance.
- End condition.
- Recovery when fetching more fails.

## State and behavior
- Preserve loaded content when fetching additional results.
- Handle empty first page separately from later-page failure.

## Accessibility
- Provide reachable navigation controls and meaningful progress.
- Do not trap keyboard users in endless appended content.

## Responsive behavior
- Both approaches can work; choose based on task rather than viewport.

## Decision rules
- Prefer pagination for goal-oriented lookup, comparison, and return-to-position workflows.
- Prefer infinite scroll for exploratory consumption where exact position matters less.
- Use cursor-based loading internally without forcing infinite-scroll UX.

## Related
- filtering-and-sorting.md
- tables.md
- lists-vs-cards.md
