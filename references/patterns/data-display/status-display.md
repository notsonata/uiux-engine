# Status Display

## Use when
- Records move through meaningful lifecycle states.
- Users need to distinguish normal, warning, failed, pending, or completed conditions.

## Avoid when
- The label does not change behavior or decision-making.
- Colorful badges would only add visual noise.

## Core anatomy
- Plain-language status label.
- Optional icon or shape cue.
- Semantic color as reinforcement.
- Timestamp or reason when useful.

## State and behavior
- Represent unknown and stale states explicitly when needed.
- Do not collapse queued, running, failed, and completed if those distinctions matter.

## Accessibility
- Never use color alone.
- Keep labels understandable without icons.

## Responsive behavior
- Shorten secondary metadata before removing the status label itself.

## Decision rules
- Status vocabulary should be finite and consistent.
- Prefer user-facing lifecycle terms over backend enums.
- Use badges sparingly; not every piece of metadata is a status.

## Related
- ../feedback/long-running-jobs.md
- ../feedback/offline-and-sync.md
