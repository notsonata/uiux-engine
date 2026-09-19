# Autosave

## Use when
- Users edit over time and explicit Save would create repeated friction.
- Draft preservation materially reduces loss risk.

## Avoid when
- Changes have immediate external consequences that require deliberate commit.
- The system cannot reliably communicate save state.

## Core anatomy
- Editable content.
- Saving/saved/error indicator.
- Retry or recovery.
- Conflict handling when concurrent edits are possible.

## State and behavior
- Unsaved, saving, saved, failed, offline, and conflict should be distinguishable when relevant.
- Do not show 'saved' before persistence actually succeeds.

## Accessibility
- Status changes should be perceivable without being excessively announced.

## Responsive behavior
- Keep save state visible but unobtrusive.

## Decision rules
- Autosave is not silent if failure can lose work.
- Explicit Save may still be needed for consequential publish/commit actions.
- Debounce writes without making status misleading.

## Related
- ../feedback/offline-and-sync.md
- ../feedback/long-running-jobs.md
