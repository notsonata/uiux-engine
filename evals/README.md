# Behavioral Evals

These fixtures test the behavioral contract of UIUX Engine's four public workflows.

They are deliberately host-neutral. Claude Code, Codex, Cursor, and OpenCode should all be evaluated against the same cases even though their invocation syntax differs.

## What the fixtures contain

Each case in `cases.json` includes:

- `command`: canonical UIUX Engine action
- `prompt`: user request
- `setup`: context the evaluator should provide
- `must_demonstrate`: behaviors expected in a conformant response
- `must_not`: scope or reasoning failures that invalidate the response
- `rationale`: why the case exists

The fixtures are behavioral rubrics, not golden-response snapshots. UX work admits multiple valid outputs, so tests should judge whether the workflow respected its contract rather than whether wording matches a reference answer.

## Initial suite

The first suite contains two cases for each public action:

- `ux-design`: destructive settings and existing-design-system preservation
- `ux-audit`: screenshot evidence limits and async state-heavy flows
- `ux-review`: diff scoping and copy/affordance regressions
- `restyle`: visual-only preservation and structural-problem escalation

## Running an eval manually

For each host:

1. Install that host's adapter into a clean fixture repository.
2. Start a new session so prior conversation does not influence the result.
3. Provide the case `setup`.
4. Invoke the public action using the host-native syntax.
5. Provide the case `prompt`.
6. Record the output.
7. Check every `must_demonstrate` and `must_not` item.
8. Record failures as engine or adapter defects, not as wording differences.

## Host invocation mapping

| Canonical | Claude Code | Codex | Cursor | OpenCode |
|---|---|---|---|---|
| ux-design | `/ux-design` | `$ux-design` | `/ux-design` | `/ux-design` |
| ux-audit | `/ux-audit` | `$ux-audit` | `/ux-audit` | `/ux-audit` |
| ux-review | `/ux-review` | `$ux-review` | `/ux-review` | `/ux-review` |
| restyle | `/restyle` | `$restyle` | `/restyle` | `/restyle` |

## What is automated today

`tests/test_conformance.py` automatically verifies:

- exactly four canonical public commands
- exactly eight canonical reasoning skills
- exactly two canonical internal agents
- each adapter preserves the four-action surface
- hidden/internal modules do not leak into discovered skill locations
- host-specific explicit-invocation and hidden-agent settings remain present
- the canonical command contracts retain their key scope boundaries
- the behavioral fixture suite covers every public command with multiple cases

The actual LLM behavior still needs to be executed on each host. Those runs should come next, after this structural foundation is stable.


## Claude Code runner

Claude Code is the first executable host runner.

Prerequisites:

    claude --version
    git --version

Claude Code must already be authenticated.

Run all cases:

    python evals/runners/claude_code.py

Run selected cases:

    python evals/runners/claude_code.py --case design-destructive-settings --case review-regression-scope

Optionally select a model:

    python evals/runners/claude_code.py --model sonnet

The runner creates a disposable fixture repository, installs the Claude Code adapter, commits the fixture baseline, applies any intended uncommitted diff, invokes the explicit slash command with Claude Code print mode, captures JSON output, and records the resulting git diff.

For non-restyle cases, Edit and Write are explicitly disallowed. Restyle may edit only the disposable fixture repository.

Results are written beneath evals/results/claude-code/. Generate a human grading sheet with:

    python evals/grade.py evals/results/claude-code/<run-id>

Raw transcripts should not be committed by default.
