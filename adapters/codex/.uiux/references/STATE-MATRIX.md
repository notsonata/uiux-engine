# State Matrix

The canonical state-completeness contract contains six states. Additional states are conditional.

## Six required states

| State | Question |
|---|---|
| Loading | What does the user see while required work is pending? |
| Empty | Is this first-use empty, zero results, or genuinely no data? |
| Partial | What remains usable when only some data or operations succeed? |
| Error | What failed, what is safe, and how can the user recover? |
| Success | How is completion or the resulting state made clear? |
| Offline | What remains usable, what is stale, and what retries later? |

A state may be not applicable, but it should be considered explicitly.

## Conditional states

Use when the product requires them:

| State | Question |
|---|---|
| Initial | What appears before the user acts? |
| Validation | Which field/action is invalid and how is it corrected? |
| Disabled | Why is this unavailable, if explanation is needed? |
| Permission denied | What access is missing and how can it be obtained? |
| Session expired | What work can be preserved? |
| Destructive pending | Is confirmation, undo, or recovery appropriate? |
| Stale/conflict | What changed elsewhere and how is the conflict resolved? |
| Queued/running/cancelled | How does long-running work progress and recover? |
