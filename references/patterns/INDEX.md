# UX Pattern Library

This library is internal reference material for UIUX Engine's eight reasoning skills. It does not create new public commands or skills.

Use patterns as decision support, not as mandatory templates. A pattern is appropriate only when its task model, risk, frequency, and information needs match the current product.

## Selection rule

Start from the user's task and failure risk, then consult the smallest set of relevant patterns. Do not pattern-match by visual resemblance alone.

## Categories

### Actions
- [Destructive actions](actions/destructive-actions.md)
- [Undo vs confirmation](actions/undo-vs-confirmation.md)
- [Bulk actions](actions/bulk-actions.md)
- [Row actions](actions/row-actions.md)
- [Disabled actions](actions/disabled-actions.md)

### Data display
- [Tables](data-display/tables.md)
- [Lists vs cards](data-display/lists-vs-cards.md)
- [Dashboards](data-display/dashboards.md)
- [Master-detail](data-display/master-detail.md)
- [Status display](data-display/status-display.md)
- [Pagination vs infinite scroll](data-display/pagination-vs-infinite-scroll.md)
- [Filtering and sorting](data-display/filtering-and-sorting.md)

### Forms
- [Validation and errors](forms/validation-and-errors.md)
- [Multi-step forms](forms/multi-step-forms.md)
- [Autosave](forms/autosave.md)
- [Search input](forms/search-input.md)
- [Settings forms](forms/settings-forms.md)
- [Permissions and roles](forms/permissions-and-roles.md)

### Navigation
- [Sidebar navigation](navigation/sidebar-navigation.md)
- [Tabs](navigation/tabs.md)
- [Breadcrumbs](navigation/breadcrumbs.md)
- [Command palette](navigation/command-palette.md)
- [Mobile navigation](navigation/mobile-navigation.md)

### Feedback
- [Loading and progress](feedback/loading-and-progress.md)
- [Empty states](feedback/empty-states.md)
- [Toasts and inline alerts](feedback/toasts-and-inline-alerts.md)
- [Long-running jobs](feedback/long-running-jobs.md)
- [Offline and sync](feedback/offline-and-sync.md)

### Overlays
- [Dialogs](overlays/dialogs.md)
- [Drawers](overlays/drawers.md)
- [Popovers and tooltips](overlays/popovers-and-tooltips.md)

### Workflows
- [Onboarding](workflows/onboarding.md)
- [Upload, import, and export](workflows/upload-import-export.md)
- [Editors](workflows/editors.md)
- [AI generation](workflows/ai-generation.md)

## Pattern priority

When several patterns apply, prioritize:
1. task completion and safety;
2. state/recovery behavior;
3. information hierarchy and comparison needs;
4. accessibility and responsive integrity;
5. efficiency for repeated work;
6. visual treatment.

Patterns should never override a product's established DESIGN.md without a deliberate system extension.
