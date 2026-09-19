#!/usr/bin/env python3
"""Generate a human grading checklist for one behavioral eval run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = {c["id"]: c for c in json.loads((ROOT / "evals" / "cases.json").read_text())}


def extract_text(result: dict) -> str:
    parsed = result.get("parsed_output")
    if isinstance(parsed, dict):
        for key in ("result", "text", "response"):
            value = parsed.get(key)
            if isinstance(value, str):
                return value
    return result.get("stdout", "")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    run_dir = args.run_dir if args.run_dir.is_absolute() else ROOT / args.run_dir
    result_files = sorted(p for p in run_dir.glob("*.json") if p.name != "run.json")
    if not result_files:
        raise SystemExit("No case result files found in " + str(run_dir))

    lines = [
        "# Behavioral Eval Grade Sheet",
        "",
        "Run: " + str(run_dir),
        "",
        "Mark each item after inspecting the response and, for restyle cases, the captured git diff.",
        "",
    ]

    for path in result_files:
        result = json.loads(path.read_text(encoding="utf-8"))
        case = CASES[result["case_id"]]
        lines += [
            "## " + case["id"],
            "",
            "Command: " + case["command"],
            "CLI exit code: " + str(result["exit_code"]),
            "",
            "### Must demonstrate",
        ]
        lines += ["- [ ] " + item for item in case["must_demonstrate"]]
        lines += ["", "### Must not"]
        lines += ["- [ ] Did not: " + item for item in case["must_not"]]
        lines += [
            "",
            "### Notes",
            "",
            "- Outcome: PASS / FAIL / NEEDS REVIEW",
            "- Engine defect:",
            "- Adapter defect:",
            "- Model variance / unclear:",
            "",
            "<details>",
            "<summary>Captured response</summary>",
            "",
            "~~~text",
            extract_text(result).strip(),
            "~~~",
            "",
            "</details>",
            "",
        ]
        if result.get("git_diff"):
            lines += [
                "<details>",
                "<summary>Captured git diff</summary>",
                "",
                "~~~diff",
                result["git_diff"].rstrip(),
                "~~~",
                "",
                "</details>",
                "",
            ]

    output = args.output or run_dir / "GRADE.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
