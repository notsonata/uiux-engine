# Editors

## Use when
- Users create or revise substantial content over time.
- The task benefits from persistent tools, preview, history, or autosave.

## Avoid when
- The input is short enough for a normal form.

## Core anatomy
- Editing canvas.
- Tool controls.
- Save/status.
- Preview or result context.
- Undo/history when meaningful.

## State and behavior
- Unsaved, saving, saved, conflict, invalid, preview/loading, offline.

## Accessibility
- Keyboard shortcuts require discoverable alternatives.
- Focus should not be trapped by custom editor chrome.

## Responsive behavior
- Prioritize the editing surface; collapse secondary inspectors/toolbars appropriately.

## Decision rules
- Protect work from loss.
- Keep editing and preview semantics clear.
- Do not overload the canvas with persistent controls that are rarely used.

## Related
- ../forms/autosave.md
- ../feedback/offline-and-sync.md
- ../navigation/command-palette.md
