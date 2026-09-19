---
name: forms-and-inputs
description: Design forms, field layouts, validation, input controls, errors, defaults, multi-step entry, and data-entry workflows. Use for sign-up, settings, checkout, onboarding, CRUD interfaces, search/filter forms, or any workflow requiring significant user input.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# Forms and Inputs

## Objective

Reduce effort, ambiguity, and error while preserving enough context for confident data entry.

## Field necessity

For every field ask:
- Is this required to complete the user's current goal?
- Can it be inferred or prefilled safely?
- Can it be requested later?
- Does the user know the answer at this point?

Do not collect data merely because the backend model contains the field.

## Labels and help

Use persistent labels. Place format requirements and constraints near the field before failure when possible. Use examples only when they add clarity.

Placeholder text is not a substitute for a label.

## Control choice

Choose controls by behavior:
- checkbox for independent boolean choices;
- radio group for a small mutually exclusive set;
- select/combobox for larger option sets;
- segmented control for a very small, frequently switched peer set;
- switch for an immediate on/off setting, not a form answer awaiting Save;
- date/time controls appropriate to the required precision.

## Validation

Validate at a moment that helps the user:
- obvious formatting can validate after input/blur;
- cross-field or server rules may require submission;
- avoid aggressive errors before the user has had a chance to finish typing.

Errors should say:
- which field/action failed;
- what is wrong;
- how to fix it;
- whether entered data is preserved.

## Long forms

Use sections or steps only when they create meaningful cognitive boundaries. Keep dependencies visible. Show progress when the number or structure of steps matters.

Do not split a short form into a wizard simply to make each screen look sparse.

## Submission

Prevent duplicate submission where consequential. During saving, clarify whether the user can continue editing. Preserve user-entered data on recoverable failure.

## Output

Provide field inventory, required/optional rationale, control choice, defaults, validation timing, error copy intent, submission behavior, and recovery behavior.
