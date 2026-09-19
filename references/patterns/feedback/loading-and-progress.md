# Loading and Progress

## Use when
- Work takes long enough that the user needs status.
- Data or actions are asynchronous.

## Avoid when
- The operation is effectively instantaneous.
- Loading chrome would create more flicker than clarity.

## Core anatomy
- Affected region.
- Progress or activity indicator.
- Optional message/estimate.
- Cancel/retry where relevant.

## State and behavior
- Differentiate initial load, background refresh, incremental fetch, and long-running job.
- Keep known content during background refresh when possible.

## Accessibility
- Loading state should be perceivable without overwhelming assistive tech with repeated announcements.

## Responsive behavior
- Keep the indicator near the affected region rather than defaulting to full-screen blocking.

## Decision rules
- Skeletons are useful when final structure is predictable.
- Use determinate progress when meaningful measurement exists.
- Do not replace a whole page with a spinner for a local update.

## Related
- long-running-jobs.md
- ../data-display/dashboards.md
