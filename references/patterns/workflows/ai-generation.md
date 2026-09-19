# AI Generation

## Use when
- The product generates, transforms, summarizes, or proposes content using an AI model.
- Users need to understand progress, editability, uncertainty, or provenance.

## Avoid when
- The AI behavior is incidental and ordinary system feedback is enough.

## Core anatomy
- User intent/input.
- Generation status.
- Generated result.
- Regenerate/retry.
- Edit/accept/reject controls.
- Provenance or source context when material.

## State and behavior
- Queued, streaming/generating, completed, failed, cancelled, partially generated, stale after input change.

## Accessibility
- Streaming updates should not spam assistive technology.
- Controls must remain usable without animation.

## Responsive behavior
- Keep result editing and primary controls reachable; collapse secondary generation settings.

## Decision rules
- Do not imply certainty the model does not have.
- Distinguish generated content from user-authored or verified content when that matters.
- Regenerate should not silently destroy edits.
- Preserve history when iteration is a core task.

## Related
- ../feedback/long-running-jobs.md
- ../feedback/loading-and-progress.md
- editors.md
