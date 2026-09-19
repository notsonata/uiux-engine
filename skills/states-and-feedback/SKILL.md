---
name: states-and-feedback
description: Specify loading, empty, partial, success, error, validation, disabled, offline, permission, stale, conflict, and other system states. Use whenever a UI depends on async data, network operations, permissions, user-created content, background jobs, or consequential actions.
license: MIT
metadata:
  version: "1.0.0"
  category: ui-ux
---

# States and Feedback

## Objective

Make the interface understandable outside the ideal happy path.

Use `../../references/STATE-MATRIX.md` when auditing state coverage.

## Loading

Choose feedback based on duration and layout stability:
- preserve known content during background refresh when possible;
- use local progress for local actions;
- use skeletons only when the eventual structure is sufficiently predictable;
- avoid replacing an entire stable screen with a spinner for a small update.

## Empty states

Distinguish:
- first-use empty state;
- zero search/filter results;
- no permission;
- no data yet from an external source;
- data removed or unavailable.

Each can require a different explanation and next action.

## Errors

Classify errors as:
- field/local;
- operation-level;
- page/resource-level;
- connectivity;
- permission/auth;
- conflict/stale data;
- destructive or data-loss risk.

Place errors near the affected object when possible. Do not use a generic toast as the only explanation for a blocking failure.

## Success

Use feedback proportional to uncertainty and consequence. If the result is already visible, additional success UI may be unnecessary. For consequential operations, state what changed and what happens next.

## Optimistic UI

Use optimistic updates only when failure is unlikely and reversal is safe. Provide rollback or clear correction on failure.

## Long-running work

For uploads, imports, generation, processing, synchronization, or jobs:
- show queued/running/completed/failed states;
- allow navigation away when technically possible;
- preserve job status somewhere persistent;
- distinguish cancellation from failure;
- explain retry behavior.

## Output

Create a state matrix for important surfaces and define trigger, display, available actions, persistence, and recovery for each applicable state.
