# Dashboards

## Use when
- Users need a quick operational or analytical overview.
- Multiple signals must support prioritization and drill-down.

## Avoid when
- The user has one dominant task that deserves a focused workflow.
- Metrics are decorative and do not support decisions.

## Core anatomy
- Scope/time context.
- Primary signals.
- Exceptions or changes needing attention.
- Drill-down paths.
- Freshness/status indicators when data is delayed.

## State and behavior
- Define loading and partial-data behavior per region.
- Distinguish stale, delayed, and failed data.
- Avoid blanking the whole dashboard for one failed widget.

## Accessibility
- Charts require textual equivalents for essential information.
- Status cannot depend on hue alone.

## Responsive behavior
- Reorder by decision priority rather than simple stacking.
- Preserve the most actionable signals near the top.

## Decision rules
- A dashboard should answer what changed, what matters, and what can I do next.
- Prefer fewer decision-relevant metrics over metric wallpaper.
- Use consistent time ranges and scopes.

## Related
- status-display.md
- ../feedback/loading-and-progress.md
- ../navigation/sidebar-navigation.md
