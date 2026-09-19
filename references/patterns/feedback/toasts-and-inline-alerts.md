# Toasts and Inline Alerts

## Use when
- The system needs to communicate transient success or non-blocking status.
- A local problem needs persistent context near the affected task.

## Avoid when
- A toast would be the only explanation for a blocking error.
- Critical information must remain available after the toast disappears.

## Core anatomy
- Message.
- Optional action such as Undo.
- Severity/status.
- Placement matched to scope.

## State and behavior
- Avoid duplicate stacked notifications for repeated background events.
- Persist errors that require user action.

## Accessibility
- Announcements should be timely but not noisy.
- Do not require users to hover a disappearing toast to understand what failed.

## Responsive behavior
- Avoid covering primary controls on small screens.
- Inline alerts often adapt better for task-local errors.

## Decision rules
- Use toasts for transient confirmation, not durable state.
- Use inline alerts for blocking/recoverable problems.
- Use persistent banners only for broad-scope conditions.

## Related
- ../actions/undo-vs-confirmation.md
- validation-and-errors.md
