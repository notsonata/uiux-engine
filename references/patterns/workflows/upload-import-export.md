# Upload, Import, and Export

## Use when
- Users move external data or files into/out of the product.
- Large or asynchronous transfers require status and recovery.

## Avoid when
- A simple file attachment has no transformation or background processing.

## Core anatomy
- Source/file selection.
- Requirements/limits.
- Progress.
- Validation/preview where useful.
- Completion destination.
- Failure/retry.

## State and behavior
- Selected, uploading, validating, processing, completed, partial, failed, cancelled.

## Accessibility
- File input and drag-drop must have equivalent keyboard-accessible paths.
- Progress/status should be textual.

## Responsive behavior
- Keep progress and actionable errors visible; large tables/previews may need dedicated screens.

## Decision rules
- Separate transfer progress from server processing.
- Explain rejected files before wasting upload time when possible.
- For partial imports, identify which records failed and why.

## Related
- ../feedback/long-running-jobs.md
- ../feedback/loading-and-progress.md
- ../actions/bulk-actions.md
