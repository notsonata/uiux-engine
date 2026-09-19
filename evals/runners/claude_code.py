#!/usr/bin/env python3
"""Run UIUX Engine behavioral evals against Claude Code."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "evals" / "cases.json"
FIXTURES_PATH = ROOT / "evals" / "fixtures.json"
ADAPTER_PATH = ROOT / "adapters" / "claude-code" / ".claude"
RESULTS_ROOT = ROOT / "evals" / "results" / "claude-code"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def run(cmd: list[str], cwd: Path, check: bool = True):
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check)


def write_files(root: Path, mapping: dict[str, str]) -> None:
    for rel, content in mapping.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def build_project(fixture: dict, workdir: Path) -> None:
    write_files(workdir, fixture.get("files", {}))
    shutil.copytree(ADAPTER_PATH, workdir / ".claude", dirs_exist_ok=True)
    run(["git", "init", "-b", "main"], workdir)
    run(["git", "config", "user.email", "uiux-evals@example.invalid"], workdir)
    run(["git", "config", "user.name", "UIUX Evals"], workdir)
    run(["git", "add", "."], workdir)
    run(["git", "commit", "-m", "fixture: baseline"], workdir)
    write_files(workdir, fixture.get("changes", {}))


def invocation_prompt(case: dict, fixture: dict) -> str:
    if case["command"] == "ux-review":
        first = "/ux-review"
    else:
        first = "/" + case["command"] + " " + case["prompt"]

    parts = [
        first,
        "",
        "Evaluation context:",
        case["setup"],
    ]
    note = fixture.get("runner_note")
    if note:
        parts += ["", note]
    parts += [
        "",
        "Perform the workflow naturally. Do not discuss the evaluation rubric or try to optimize for a score.",
    ]
    return "\n".join(parts)


def claude_command(case: dict, prompt: str, args) -> list[str]:
    tools = [
        "Read",
        "Glob",
        "Grep",
        "Bash(git diff:*)",
        "Bash(git status:*)",
        "Bash(git log:*)",
    ]
    if case["command"] == "restyle":
        tools += ["Edit", "Write"]

    cmd = [
        args.claude_bin,
        "-p",
        prompt,
        "--output-format",
        "json",
        "--max-turns",
        str(args.max_turns),
        "--allowedTools",
        ",".join(tools),
    ]
    if case["command"] != "restyle":
        cmd += ["--disallowedTools", "Edit,Write"]
    if args.model:
        cmd += ["--model", args.model]
    return cmd


def parse_json_output(stdout: str):
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return None


def execute_case(case: dict, fixture: dict, run_dir: Path, args) -> dict:
    if args.keep_workdirs:
        project = run_dir / "workdirs" / case["id"]
        project.mkdir(parents=True, exist_ok=True)
        cleanup = None
    else:
        cleanup = tempfile.TemporaryDirectory(prefix="uiux-" + case["id"] + "-")
        project = Path(cleanup.name)

    try:
        build_project(fixture, project)
        prompt = invocation_prompt(case, fixture)
        cmd = claude_command(case, prompt, args)

        env = os.environ.copy()
        env.setdefault("DISABLE_AUTOUPDATER", "1")

        started = datetime.now(timezone.utc).isoformat()
        cp = subprocess.run(cmd, cwd=project, env=env, text=True, capture_output=True)
        finished = datetime.now(timezone.utc).isoformat()

        diff = run(["git", "diff", "--no-ext-diff"], project, check=False).stdout
        status = run(["git", "status", "--porcelain"], project, check=False).stdout

        result = {
            "host": "claude-code",
            "case_id": case["id"],
            "command": case["command"],
            "prompt": prompt,
            "started_at": started,
            "finished_at": finished,
            "exit_code": cp.returncode,
            "stdout": cp.stdout,
            "stderr": cp.stderr,
            "parsed_output": parse_json_output(cp.stdout),
            "git_diff": diff,
            "git_status": status,
            "model_requested": args.model,
            "max_turns": args.max_turns,
        }
        (run_dir / (case["id"] + ".json")).write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return result
    finally:
        if cleanup is not None:
            cleanup.cleanup()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", help="Case id. Repeat to run multiple.")
    parser.add_argument("--model", help="Claude Code model alias or full model name.")
    parser.add_argument("--max-turns", type=int, default=20)
    parser.add_argument("--claude-bin", default="claude")
    parser.add_argument("--keep-workdirs", action="store_true")
    parser.add_argument("--run-id")
    args = parser.parse_args()

    if shutil.which(args.claude_bin) is None:
        print("error: Claude Code CLI is not on PATH.", file=sys.stderr)
        return 2
    if shutil.which("git") is None:
        print("error: git is required.", file=sys.stderr)
        return 2
    if not ADAPTER_PATH.is_dir():
        print("error: Claude Code adapter is missing.", file=sys.stderr)
        return 2

    cases = load_json(CASES_PATH)
    fixtures = load_json(FIXTURES_PATH)
    by_id = {case["id"]: case for case in cases}
    selected = args.case or [case["id"] for case in cases]

    unknown = [case_id for case_id in selected if case_id not in by_id]
    if unknown:
        print("error: unknown cases: " + ", ".join(unknown), file=sys.stderr)
        return 2
    missing = [case_id for case_id in selected if case_id not in fixtures]
    if missing:
        print("error: missing fixtures: " + ", ".join(missing), file=sys.stderr)
        return 2

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = RESULTS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "run.json").write_text(
        json.dumps({
            "host": "claude-code",
            "run_id": run_id,
            "cases": selected,
            "model_requested": args.model,
            "max_turns": args.max_turns,
        }, indent=2) + "\n",
        encoding="utf-8",
    )

    failures = 0
    for case_id in selected:
        print("[claude-code] " + case_id + " ...", flush=True)
        result = execute_case(by_id[case_id], fixtures[case_id], run_dir, args)
        if result["exit_code"] != 0:
            failures += 1
            print("  failed: exit " + str(result["exit_code"]))
        else:
            print("  completed")

    print("\nResults: " + str(run_dir.relative_to(ROOT)))
    print("Grade: python evals/grade.py " + str(run_dir.relative_to(ROOT)))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
