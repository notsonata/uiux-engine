# UIUX Engine

A tool-agnostic Agent Skills pack for designing, reviewing, and improving user interfaces and user experiences.

It is intentionally framework-neutral. Use it with web apps, mobile apps, desktop apps, dashboards, internal tools, consumer products, prototypes, or existing codebases.

## Philosophy

UIUX Engine separates product reasoning from visual styling. It asks the agent to understand users, tasks, risk, hierarchy, states, interaction, accessibility, responsiveness, and visual coherence before polishing screens.

The pack follows the open Agent Skills folder + `SKILL.md` convention.

## Skills

| Skill | Purpose |
|---|---|
| `uiux-design` | Main orchestrator for designing or redesigning a UI/UX flow |
| `ux-research` | Clarify users, jobs, context, assumptions, risks, and evidence |
| `information-architecture` | Structure content, navigation, hierarchy, and task flow |
| `interaction-design` | Define controls, behaviors, transitions, affordances, and safety |
| `forms-and-inputs` | Design usable forms, validation, errors, and data entry |
| `states-and-feedback` | Cover loading, empty, partial, error, success, disabled, offline, and permission states |
| `accessibility` | Apply accessibility checks and inclusive interaction requirements |
| `visual-design` | Establish visual hierarchy, typography, spacing, color, density, and character |
| `responsive-design` | Adapt interaction and information across screen sizes and input modes |
| `design-system` | Discover or define tokens, components, patterns, and consistency rules |
| `ux-audit` | Audit an existing interface and produce prioritized findings and fixes |

## Recommended use

For a new feature or redesign, activate `uiux-design`. It routes into the specialist skills as needed.

For an existing product, activate `ux-audit`. Use `design-system` first if the product already has a component library or visual language that must be preserved.

## Core operating rule

Do not jump directly from a feature request to polished UI. Establish the user's goal, primary task, hierarchy, key states, constraints, and failure risks first.

## Installation

Copy the folders inside `skills/` into the skills directory used by your agent or IDE. If your client supports only manually loaded instructions, point it at the relevant `SKILL.md` file.

No command names, model names, or framework-specific APIs are required.
