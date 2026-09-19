# Validation and Errors

## Use when
- Users enter structured or constrained data.
- The system can help prevent or recover from invalid input.

## Avoid when
- A field has no meaningful validation rule.
- Immediate validation would punish incomplete typing.

## Core anatomy
- Persistent label.
- Requirement/constraint guidance.
- Field-level error.
- Summary or operation error when multiple fields fail.

## State and behavior
- Validate formatting after input/blur when useful.
- Validate cross-field/server rules at submission when necessary.
- Preserve entered data after recoverable failure.

## Accessibility
- Associate errors programmatically with fields.
- Use text plus non-color cues.
- Move or announce focus appropriately after failed submission.

## Responsive behavior
- Keep error text adjacent to the field.
- Avoid layouts where validation pushes key actions off-screen unexpectedly.

## Decision rules
- Say what is wrong and how to fix it.
- Do not use 'Invalid' as the entire message when a specific rule can be named.
- Do not clear user input because validation failed.

## Related
- multi-step-forms.md
- ../feedback/toasts-and-inline-alerts.md
