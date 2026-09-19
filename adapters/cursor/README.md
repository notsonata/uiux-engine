# Cursor Adapter

This adapter maps UIUX Engine to Cursor while preserving the engine's public invariant: exactly four user-facing actions.

## Public actions

Cursor project skills can be manually invoked from the Agent `/` menu. This adapter exposes exactly:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

Each public skill sets `disable-model-invocation: true`, so Cursor does not automatically apply these workflows from an ordinary prompt.

## Layout

```text
.cursor/
└── skills/
    ├── ux-design/
    ├── ux-audit/
    ├── ux-review/
    └── restyle/

.uiux/
├── agents/       # two hidden orchestration contracts
├── skills/       # eight hidden reasoning modules
├── references/
└── templates/
```

## Why there are no .cursor/agents files

Cursor custom subagents under `.cursor/agents/` can also be invoked directly with `/name`.

Registering `ux-designer` and `ux-auditor` there would create two additional user-facing slash actions and violate UIUX Engine's four-action invariant.

Instead, the two canonical agent contracts are stored under `.uiux/agents/`. The public `/ux-design`, `/ux-audit`, and `/ux-review` skills instruct Cursor's parent Agent to spawn an isolated subagent internally using the relevant hidden contract.

This preserves both requirements:
- two internal orchestration roles;
- only four public UIUX Engine actions.

`/restyle` stays in the parent Agent because it is a current-context visual-system workflow and does not require isolated orchestration.

## Hidden reasoning core

The eight canonical reasoning modules live under `.uiux/skills/`, outside Cursor's discovered skill directories.

They are therefore project resources that the public workflows can read without becoming peer entries in the `/` menu.

## Install into a project

Merge these directories into the target repository root:

```text
.cursor/
.uiux/
```

Do not copy the canonical root `skills/` directory into `.cursor/skills/` or `.agents/skills/`. Doing so would expose the eight internal reasoning modules.

## Verify

Open Cursor Agent in the target repository and type `/`.

The UIUX Engine surface should contain exactly:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

Suggested smoke tests:

```text
/ux-design redesign the account settings page
/ux-audit src/components/Checkout.tsx
/ux-review
/restyle src/app/dashboard/page.tsx
```

Also verify that `ux-intent-discovery`, `state-completeness`, `visual-character`, `ux-designer`, and `ux-auditor` do not appear as peer UIUX Engine actions.

## Source of truth

The repository root `commands/`, `agents/`, and `skills/` remain the canonical cross-host definitions.

The Cursor adapter changes packaging and delegation mechanics only. It must preserve the same four-action user mental model.
