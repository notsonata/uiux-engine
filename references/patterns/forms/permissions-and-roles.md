# Permissions and Roles

## Use when
- Users assign access, capabilities, or responsibility.
- Mistakes can expose data or block work.

## Avoid when
- The product only has one simple access level.

## Core anatomy
- Subject/user or group.
- Role or permission set.
- Scope.
- Inherited vs direct access when relevant.
- Impact summary.

## State and behavior
- Handle pending invitations, revoked access, unavailable scopes, and conflicting inheritance.
- Confirm high-impact privilege removal when recovery is costly.

## Accessibility
- Permission differences must be textual, not color-coded only.

## Responsive behavior
- Prioritize identity, role, and scope; move secondary audit metadata into detail views.

## Decision rules
- Prefer role-level choices when users should not reason about dozens of granular permissions.
- Use granular permissions only when the domain requires it.
- Explain why an option is unavailable or inherited.

## Related
- ../actions/destructive-actions.md
- ../data-display/tables.md
