# Long-Running Jobs

## Use when
- Work continues for seconds, minutes, or longer.
- Users may navigate away and return.

## Avoid when
- The operation is truly synchronous and brief.

## Core anatomy
- Job identity.
- Queued/running/completed/failed/cancelled state.
- Progress when meaningful.
- Persistent location/history.
- Retry/cancel actions where supported.

## State and behavior
- Represent queued, running, completed, failed, and cancelled distinctly.
- Handle stale status and reconnect after navigation.

## Accessibility
- Status changes should be available textually.
- Progress must not rely on animation alone.

## Responsive behavior
- Keep job status available outside the initiating screen when the user can leave.

## Decision rules
- Do not make a toast the only status for work that outlives the toast.
- Let users navigate away when technically possible.
- Separate cancel from failure.

## Related
- loading-and-progress.md
- ../data-display/status-display.md
- offline-and-sync.md
