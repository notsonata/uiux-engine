---
name: state-completeness
description: Ensure important screens and components define loading, empty, partial, error, success, and offline behavior before implementation, with additional states when the product requires them. Internal reasoning skill used by the public UX commands.
license: MIT
metadata:
  version: "2.0.0"
  category: ui-ux
  visibility: internal
---

# State Completeness

## Purpose

Design the product outside the ideal happy path.

## Six required states

For every meaningful data-dependent surface, explicitly consider:

1. **Loading**
2. **Empty**
3. **Partial**
4. **Error**
5. **Success**
6. **Offline**

A state may be "not applicable", but it must be considered rather than silently omitted.

## State rules

### Loading
Preserve stable content during refresh when possible. Use local feedback for local work. Skeletons should resemble the final layout rather than acting as decorative gray boxes.

### Empty
Distinguish first-use emptiness from "no results" after filtering. Give a relevant next action when one exists.

### Partial
Specify how the UI behaves when only some data or operations succeed. Do not hide usable content because one request failed.

### Error
Explain what failed, what remains safe, whether work was preserved, and the next recovery action. Put blocking errors near the affected task rather than relying only on transient toasts.

### Success
Make completion visible when the outcome is not already obvious. Persistent status is better than a toast when the state matters later.

### Offline
State what remains usable, what is stale, and what will retry or sync later.

## Conditional states

Also inspect when relevant:
- validation;
- permission denied;
- authentication/session expiry;
- disabled/unavailable;
- destructive pending;
- stale/conflict;
- queued/running/cancelled background jobs.

These do not increase the canonical six-state contract. They are conditional product states.

## Handoff

Return a compact state matrix with trigger, UI, available actions, persistence, and recovery.
