# Undo vs Confirmation

## Use when
- A user action has a meaningful chance of accidental activation.
- You need to choose whether to interrupt before an action or recover after it.

## Avoid when
- The action is both low-risk and obvious.
- The system cannot actually reverse the operation and a fake undo would mislead.

## Core anatomy
- Action consequence.
- Protection mechanism.
- Recovery window or confirmation details.
- Final state feedback.

## State and behavior
- Undo needs a stable reversal window and clear expiry.
- Confirmation should not silently disappear while the consequence is pending.
- If recovery fails, explain what remains changed.

## Accessibility
- Undo must be reachable without precise pointer interaction.
- Confirmation must not depend on color or icon recognition alone.

## Responsive behavior
- Keep recovery controls reachable on small screens.
- Avoid full-screen interruption for minor reversible actions.

## Decision rules
- Prefer undo when reversal is technically reliable and fast.
- Prefer confirmation when consequences are irreversible or difficult to restore.
- Do not stack confirmation plus undo unless the risk genuinely warrants both.

## Related
- destructive-actions.md
- ../feedback/toasts-and-inline-alerts.md
