# OpenCode Adapter

This adapter maps UIUX Engine to OpenCode while preserving exactly four public actions.

## Public actions

OpenCode custom commands live under `.opencode/commands/` and appear as slash commands in the TUI.

This adapter exposes exactly:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

## Layout

```text
.opencode/
├── commands/
│   ├── ux-design.md
│   ├── ux-audit.md
│   ├── ux-review.md
│   └── restyle.md
└── agents/
    ├── ux-designer.md
    └── ux-auditor.md

.uiux/
├── skills/       # eight internal reasoning modules
├── references/
└── templates/
```

## Why this mapping is native

OpenCode custom commands can select an agent and run as a subagent. Therefore:

- `/ux-design` targets `ux-designer` with `subagent: true`.
- `/ux-audit` targets `ux-auditor` with `subagent: true`.
- `/ux-review` targets `ux-auditor` with `subagent: true`.
- `/restyle` remains in the current agent with `subagent: false`.

The two internal agents use `mode: subagent` and `hidden: true`. OpenCode's hidden subagent option removes them from the `@` autocomplete menu while keeping them programmatically invocable.

This gives UIUX Engine its intended architecture without leaking extra user actions.

## Why the eight reasoning modules are under .uiux

OpenCode discovers skills from locations such as `.opencode/skills/`, `.claude/skills/`, and `.agents/skills/`.

Putting UIUX Engine's eight internal reasoning modules in those directories would advertise them to the model as independently loadable skills.

This adapter instead keeps them under `.uiux/skills/`. The two internal agents read those files directly. They remain internal reasoning modules rather than public workflows.

## Permissions

### ux-designer

The design agent can read and edit the workspace because `/ux-design` may continue into implementation after the design gate.

Shell commands require approval.

### ux-auditor

The audit agent is read-only:
- edit is denied;
- ordinary shell commands require approval;
- common read-only Git inspection commands are allowed;
- nested subagents and the OpenCode skill tool are disabled.

## Install into a project

Merge these directories into the target repository root:

```text
.opencode/
.uiux/
```

Do not copy the canonical root `skills/` directory into `.opencode/skills/`, `.claude/skills/`, or `.agents/skills/`.

## Verify

Open OpenCode in the target repository and type `/`.

The UIUX Engine command surface should contain exactly:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

The internal `ux-designer` and `ux-auditor` agents should not appear in normal `@` autocomplete.

Suggested smoke tests:

```text
/ux-design redesign the account settings page
/ux-audit src/components/Checkout.tsx
/ux-review
/restyle src/app/dashboard/page.tsx
```

## Source of truth

The repository root `commands/`, `agents/`, and `skills/` remain the canonical cross-host definitions.

This adapter changes only OpenCode packaging, permissions, and invocation mechanics.
