# Offline and Sync

## Use when
- The product can lose connectivity or queue local changes.
- Users need confidence about what is current and what will sync later.

## Avoid when
- The product cannot function offline at all and only needs a simple connection error.

## Core anatomy
- Connectivity state.
- Local/remote save status.
- Pending changes.
- Retry/sync action when needed.
- Conflict handling.

## State and behavior
- Online, offline, reconnecting, pending sync, synced, conflict, failed sync.

## Accessibility
- Connectivity and sync state must be textual, not icon/color-only.

## Responsive behavior
- Keep the state visible without permanently consuming large space.

## Decision rules
- Never claim synced before remote persistence succeeds.
- Preserve local work whenever feasible.
- Explain what features are unavailable offline.

## Related
- ../forms/autosave.md
- long-running-jobs.md
