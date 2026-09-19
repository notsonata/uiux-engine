# Claude Code Adapter

This adapter maps UIUX Engine to Claude Code while preserving the engine's public invariant:

- `/ux-design`
- `/ux-audit`
- `/ux-review`
- `/restyle`

The eight reasoning skills remain internal and are hidden from the slash-command menu.

## Target

Claude Code v2.1.218 or newer is recommended because this adapter uses forked skills with `background: false`.

## Layout

```text
.claude/
├── skills/
│   ├── ux-design/                 # public
│   ├── ux-audit/                  # public
│   ├── ux-review/                 # public
│   ├── restyle/                   # public
│   ├── ux-intent-discovery/       # internal
│   ├── information-hierarchy/     # internal
│   ├── state-completeness/        # internal
│   ├── form-ux/                   # internal
│   ├── feedback-and-affordance/   # internal
│   ├── ux-auditor/                # internal
│   ├── design-system/             # internal
│   └── visual-character/          # internal
└── agents/
    ├── ux-designer.md
    └── ux-auditor.md
```

## Why this mapping works

Claude Code treats project skills at `.claude/skills/<name>/SKILL.md` as slash commands named from their directory.

The four public skills use `disable-model-invocation: true`, so they run only when the user explicitly invokes them.

The eight internal skills use `user-invocable: false`, so they remain available to Claude and the internal agents without appearing as user actions.

`/ux-design`, `/ux-audit`, and `/ux-review` use `context: fork` with one of the two canonical UIUX Engine subagents. `background: false` makes the invoking turn wait for the result and avoids turning the workflow into an asynchronous background task.

`/restyle` stays inline because it intentionally uses the current conversation context and does not justify a third custom subagent.

## Install manually into a project

Copy the adapter's `.claude` directory into the target project root:

```bash
cp -R adapters/claude-code/.claude /path/to/project/
```

If the project already has a `.claude` directory, merge the `skills/` and `agents/` directories instead of replacing existing configuration.

Restart Claude Code if the target project did not previously have those directories.

## Verify

Start Claude Code in the target project and type `/`.

The UIUX Engine surface should contain these four user actions:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

The eight internal reasoning skills should not appear as user-invocable commands.

Suggested smoke tests:

```text
/ux-design redesign the account settings page
/ux-audit src/components/Checkout.tsx
/ux-review
/restyle src/app/dashboard/page.tsx
```

## Source of truth

The root `commands/`, `agents/`, and `skills/` directories remain the canonical cross-host definitions.

Files in this adapter are Claude Code packaging of those contracts. Host-specific fields such as `user-invocable`, `disable-model-invocation`, `context`, `agent`, and `background` must not leak back into the canonical cross-host files.

When canonical behavior changes, update this adapter in the same change or mark it incompatible until regenerated.
