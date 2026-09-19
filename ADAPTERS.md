# Adapter Specification

UIUX Engine has one stable public interface:

- `ux-design`
- `ux-audit`
- `ux-review`
- `restyle`

These four actions are the product surface. Everything else in the repository is internal implementation.

## Architectural invariant

An adapter MUST expose exactly four user-facing actions corresponding to the four canonical commands.

An adapter MUST NOT expose the eight reasoning skills as peer user-facing commands, menu items, presets, tools, or actions.

An adapter MUST NOT require users to understand which internal skill should be invoked.

Internal routing may differ by host, but the public mental model must remain stable.

## Canonical action mapping

| Canonical action | Purpose | Internal route |
|---|---|---|
| `ux-design` | Wireframe and UX specification before implementation | `ux-designer` agent |
| `ux-audit` | Prioritized audit of a file, URL, screen, screenshot, or path | `ux-auditor` agent, full-audit mode |
| `ux-review` | UX pass on the current diff before merge | `ux-auditor` agent, diff-review mode |
| `restyle` | Diagnose visual character, apply DESIGN.md, return before/after | `design-system` + `visual-character` |

## Host integration rules

### Hosts with slash commands

Expose exactly:

```text
/ux-design
/ux-audit
/ux-review
/restyle
```

Command descriptions and argument syntax may follow host conventions, but semantics should remain aligned with the canonical files in `commands/`.

### Hosts without slash commands

Expose exactly four equivalent actions using the host's normal interaction model, for example:

- command palette entries;
- named actions;
- task presets;
- buttons;
- tool shortcuts;
- agent actions.

The labels should stay as close as practical to:

```text
UX Design
UX Audit
UX Review
Restyle
```

Do not replace the four-action surface with a flat list of skills.

### Hosts with skill discovery

The eight skill definitions may be installed or indexed internally if required by the host.

If the host automatically surfaces installed skills to users, the adapter should use whatever hiding, scoping, namespacing, or internal-only mechanism the host provides.

If the host has no way to hide installed skills, prefer an adapter layer that embeds or routes to their instructions internally rather than installing them as eight visible peer actions.

## Internal skills

The canonical internal skills are:

1. `ux-intent-discovery`
2. `information-hierarchy`
3. `state-completeness`
4. `form-ux`
5. `feedback-and-affordance`
6. `ux-auditor`
7. `design-system`
8. `visual-character`

These are reasoning modules, not user workflows.

Users should not need to decide whether a task requires `state-completeness`, `feedback-and-affordance`, or `information-hierarchy`. The command or internal agent makes that decision.

## Internal agents

Two canonical orchestration roles exist:

### `ux-designer`

Used by `ux-design`.

Responsible for routing through relevant design skills and producing the pre-implementation design gate:

- intent brief;
- wireframe;
- hierarchy;
- state coverage;
- interaction rules;
- design-system constraints;
- visual-character decisions;
- acceptance criteria.

### `ux-auditor`

Used by `ux-audit` and `ux-review`.

Supports:
- full-audit mode;
- diff-review mode.

It routes to relevant internal skills and converts findings into evidence-based severity-ranked output.

## Restyle exception

`restyle` does not require a separate public or internal orchestration agent.

Its scope is intentionally narrower:

1. inspect the current UI;
2. read or establish `DESIGN.md`;
3. diagnose type, color, space, and finish;
4. apply the design system;
5. preserve application logic and information meaning;
6. return a before/after.

If structural UX changes are required, report them as out of scope for `restyle` and direct the work through `ux-design` instead.

## Semantic compatibility

An adapter may translate file layout, metadata, command syntax, or agent configuration to fit a host.

It must preserve these semantics:

### `ux-design`
- design before implementation;
- wireframe before polished UI;
- UX specification before code changes;
- implementation may follow in the same invocation when requested.

### `ux-audit`
- evidence before judgment;
- findings ranked by user impact;
- no arbitrary UX score;
- no silent code edits unless requested.

### `ux-review`
- current diff is the primary scope;
- distinguish regressions from pre-existing issues;
- focus on merge-relevant UX risk.

### `restyle`
- visual-system work only;
- apply `DESIGN.md`;
- preserve behavior, feature scope, and copy meaning;
- return a before/after account.

## Adapter conformance checklist

An adapter is conformant when all are true:

- [ ] Exactly four user-facing UIUX Engine actions are exposed.
- [ ] The four actions map to the canonical command semantics.
- [ ] Internal skills are not presented as peer workflows.
- [ ] `ux-design` uses the design-before-implementation gate.
- [ ] `ux-audit` uses evidence and severity.
- [ ] `ux-review` is diff-scoped.
- [ ] `restyle` preserves functional behavior.
- [ ] `DESIGN.md` remains the visual-system source of truth.
- [ ] Host-specific implementation details do not alter the user's mental model.

## Non-conformant examples

The following adapter designs are intentionally invalid:

```text
/ux-intent-discovery
/information-hierarchy
/state-completeness
/form-ux
...
```

because they expose the internal engine.

This is also invalid:

```text
/design
/audit
/accessibility
/responsive
/colors
/forms
```

because it creates a different public product surface.

The invariant is simple:

> Four public actions. Internal complexity stays internal.
