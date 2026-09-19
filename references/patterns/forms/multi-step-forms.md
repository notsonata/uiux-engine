# Multi-Step Forms

## Use when
- The task has meaningful stages or dependencies.
- A single page would create excessive cognitive load or conditional complexity.

## Avoid when
- The form is short and could be completed faster in one view.
- Steps exist only to make the UI look sparse.

## Core anatomy
- Step title/purpose.
- Progress indication when sequence matters.
- Back/continue controls.
- Preserved data.
- Review step when consequence warrants it.

## State and behavior
- Support validation per step without losing prior work.
- Handle resume/re-entry if the workflow is long or consequential.

## Accessibility
- Progress must be textually understandable.
- Focus should move predictably when steps change.

## Responsive behavior
- A step model often adapts well to narrow screens; keep the current step and progress clear.

## Decision rules
- Split on user decisions or task stages, not arbitrary field counts.
- Do not force users to re-enter completed information.
- Allow backward correction without destructive reset.

## Related
- validation-and-errors.md
- autosave.md
