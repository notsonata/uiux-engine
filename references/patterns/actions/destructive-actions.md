# Destructive Actions

## Use when
- An action deletes, revokes, publishes, overwrites, transfers, or otherwise creates high-cost consequences.
- The user needs a clear distinction between routine and dangerous actions.

## Avoid when
- The action is low-risk and trivially reversible.
- A confirmation would only add friction without protecting anything meaningful.

## Core anatomy
- Clear destructive label using a concrete verb.
- Visual treatment distinct from the primary action.
- Consequence explanation when impact is not obvious.
- Recovery, undo, confirmation, or delay proportional to risk.

## State and behavior
- Disable while the destructive request is already in flight.
- On failure, preserve the prior safe state and explain recovery.
- On success, make the resulting state explicit if it is not immediately visible.

## Accessibility
- Do not rely on red alone to communicate danger.
- Confirmation dialogs need clear focus management and named actions.

## Responsive behavior
- Keep destructive actions discoverable but separated from routine primary actions.
- Do not move a dangerous action closer to the primary CTA merely because space is constrained.

## Decision rules
- Prefer undo for fast reversible actions.
- Use confirmation for irreversible or expensive mistakes.
- Typed confirmation is exceptional and should match truly high consequence.
- Never make the destructive choice the visually dominant default without a strong task reason.

## Related
- undo-vs-confirmation.md
- ../overlays/dialogs.md
- ../feedback/toasts-and-inline-alerts.md
