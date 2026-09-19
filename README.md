# UIUX Engine

A tool-agnostic UI/UX reasoning engine built around **four public commands**, **eight internal skills**, and **two internal agents**.

The commands are the product surface. Skills are implementation details and should not be exposed as a menu the user has to understand.

## Public interface

| Command | Purpose |
|---|---|
| `/ux-design [task]` | Wireframe + UX spec before implementation |
| `/ux-audit [target]` | Prioritized audit of a file, URL, screenshot, screen, or path |
| `/ux-review` | UX review of the current diff before merge |
| `/restyle [path]` | Visual diagnosis + DESIGN.md-driven restyle + before/after |

These are the only four user-facing entrypoints.

## Internal architecture

### 8 reasoning skills

1. `ux-intent-discovery`
2. `information-hierarchy`
3. `state-completeness`
4. `form-ux`
5. `feedback-and-affordance`
6. `ux-auditor`
7. `design-system`
8. `visual-character`

### 2 agents

- `ux-designer` orchestrates spec-first design work.
- `ux-auditor` orchestrates full audits and current-diff reviews.

```text
/ux-design ──> ux-designer
               ├─ ux-intent-discovery
               ├─ information-hierarchy
               ├─ state-completeness
               ├─ form-ux
               ├─ feedback-and-affordance
               ├─ design-system
               └─ visual-character

/ux-audit ──┐
/ux-review ─┴─> ux-auditor
                ├─ ux-auditor
                └─ relevant specialist skills

/restyle ──> design-system + visual-character
```

## Design principles

- User intent before schema shape.
- Wireframe and behavior before polish.
- Loading, empty, partial, error, success, and offline states are considered up front.
- Destructive actions receive protection proportional to consequence.
- Existing design systems are discovered before new values are invented.
- `DESIGN.md` is the product's visual source of truth.
- Accessibility and responsive behavior are embedded inside the relevant skills rather than split into extra user-facing modules.
- Visual character is deliberate, not an agent's default aesthetic.
- Audits use evidence and severity, not arbitrary UX scores.

## Portable command model

This repository defines canonical command contracts, not a Claude-specific plugin API.

An integration for Claude Code, Codex, Cursor, OpenCode, an IDE, or another agent should map its command mechanism to the four files in `commands/` and keep the internal skills/agents hidden from normal user interaction.

If a host cannot register literal slash commands, expose equivalent actions with the same four names. Do not turn all internal skills into separate public commands.

## Package layout

```text
commands/       # four public entrypoints
agents/         # internal orchestrators
skills/         # exactly eight internal reasoning skills
references/     # shared heuristics/checklists
templates/      # output contracts and DESIGN.md template
```

Keep the package intact when installing because commands and skills reference shared templates and references.

## DESIGN.md

The `design-system` skill first reads the product's existing tokens, theme files, recurring components, typography, spacing, iconography, and motion. It then consolidates what is already intentional into a root-level `DESIGN.md`.

New values must either:
1. use the existing system, or
2. be recorded as a deliberate extension.

Silent one-off styling is considered drift.

## License

MIT.
