# Disabled Actions

## Use when
- An action truly cannot succeed in the current state.
- Preventing invocation is clearer than accepting and failing.

## Avoid when
- The user needs to understand an unavailable option but disabling would hide the explanation.
- The action could be attempted safely and return useful guidance.

## Core anatomy
- Unavailable control.
- Reason when non-obvious.
- Path to eligibility where one exists.

## State and behavior
- Distinguish disabled from loading.
- Re-enable immediately when eligibility changes.
- Do not leave stale disabled controls after state updates.

## Accessibility
- Disabled state must be perceivable beyond reduced opacity.
- If explanation matters, ensure it is available to keyboard and assistive-tech users.

## Responsive behavior
- Keep reasons available on touch devices, not only hover tooltips.

## Decision rules
- Do not disable the primary action without explaining why when the requirement is non-obvious.
- Prefer validation feedback over unexplained disabled submit buttons.
- Do not use disabled styling as a generic 'not recommended' state.

## Related
- ../forms/validation-and-errors.md
- ../feedback/toasts-and-inline-alerts.md
