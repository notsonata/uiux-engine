# Codex Adapter

This adapter maps UIUX Engine to Codex while preserving the engine's public invariant: exactly four user-facing actions.

## Public actions

Codex explicitly invokes skills with the `$skill-name` syntax, so the four UIUX Engine actions are:

```text
$ux-design
$ux-audit
$ux-review
$restyle
```

These are the only UIUX Engine skills installed in Codex's repository skill-discovery path.

## Layout

```text
.agents/
└── skills/
    ├── ux-design/
    ├── ux-audit/
    ├── ux-review/
    └── restyle/

.codex/
└── agents/
    ├── ux-designer.toml
    └── ux-auditor.toml

.uiux/
├── skills/       # eight hidden reasoning modules
├── references/
└── templates/
```

## Why the internal skills are outside .agents/skills

Codex discovers repository skills under `.agents/skills`. If the eight internal reasoning modules were installed there, they could appear as peer skills in the user's skill picker.

This adapter therefore installs only the four public actions under `.agents/skills`. The eight reasoning modules live under `.uiux/skills`, where the public skills and custom subagents can read them as internal project resources without exposing them as user-selectable workflows.

## Invocation policy

Each public skill includes `agents/openai.yaml` with:

```yaml
policy:
  allow_implicit_invocation: false
```

That means Codex does not select these workflows automatically from an ordinary prompt. The user deliberately starts them with `$ux-design`, `$ux-audit`, `$ux-review`, or `$restyle`.

## Subagents

Codex project-specific custom agents live in `.codex/agents/*.toml`.

UIUX Engine maps its two canonical internal agents to:

- `ux_designer`: workspace-write design orchestrator for `$ux-design`
- `ux_auditor`: read-only audit orchestrator for `$ux-audit` and `$ux-review`

The underscore names are host identifiers. They correspond to the canonical `ux-designer` and `ux-auditor` roles.

`$restyle` stays in the parent agent because it is intentionally a current-context visual-system workflow and does not justify a third internal agent.

## Install into a project

Merge these three directories into the target repository root:

```text
.agents/
.codex/
.uiux/
```

Do not copy the repository's canonical root `skills/` directory into `.agents/skills`; doing so would expose the eight internal reasoning modules.

Codex automatically detects skill changes. If the new skills do not appear, restart Codex.

## Verify

Open Codex in the target repository and inspect the available project skills.

The UIUX Engine surface should contain exactly:

```text
$ux-design
$ux-audit
$ux-review
$restyle
```

Suggested smoke tests:

```text
$ux-design redesign the account settings page
$ux-audit src/components/Checkout.tsx
$ux-review
$restyle src/app/dashboard/page.tsx
```

Also verify that names such as `ux-intent-discovery`, `state-completeness`, and `visual-character` are not offered as peer user skills.

## Source of truth

The root `commands/`, `agents/`, and `skills/` directories remain the canonical cross-host definitions.

The Codex adapter changes packaging and invocation syntax only. It must not change the public four-action mental model.
