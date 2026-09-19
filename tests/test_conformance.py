import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_ACTIONS = {"ux-design", "ux-audit", "ux-review", "restyle"}
INTERNAL_SKILLS = {
    "ux-intent-discovery",
    "information-hierarchy",
    "state-completeness",
    "form-ux",
    "feedback-and-affordance",
    "ux-auditor",
    "design-system",
    "visual-character",
}
INTERNAL_AGENTS = {"ux-designer", "ux-auditor"}


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def child_dirs(path: str) -> set[str]:
    root = ROOT / path
    if not root.exists():
        return set()
    return {p.name for p in root.iterdir() if p.is_dir()}


def markdown_stems(path: str) -> set[str]:
    root = ROOT / path
    if not root.exists():
        return set()
    return {p.stem for p in root.glob("*.md")}


class CanonicalArchitectureTests(unittest.TestCase):
    def test_exactly_four_public_commands(self):
        self.assertEqual(markdown_stems("commands"), PUBLIC_ACTIONS)

    def test_exactly_eight_internal_skills(self):
        self.assertEqual(child_dirs("skills"), INTERNAL_SKILLS)
        for name in INTERNAL_SKILLS:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())

    def test_exactly_two_internal_agents(self):
        self.assertEqual(markdown_stems("agents"), INTERNAL_AGENTS)

    def test_design_contract_is_spec_first(self):
        body = text("commands/ux-design.md").lower()
        for phrase in ("wireframe", "ux spec", "before implementation"):
            self.assertIn(phrase, body)

    def test_audit_contract_is_evidence_based(self):
        body = text("commands/ux-audit.md").lower()
        for phrase in ("evidence", "severity", "verification"):
            self.assertIn(phrase, body)
        self.assertNotIn("ux score:", body)

    def test_review_contract_is_diff_scoped(self):
        body = text("commands/ux-review.md").lower()
        for phrase in ("current diff", "regress", "pre-existing"):
            self.assertIn(phrase, body)
        self.assertIn("do not rewrite unrelated ui", body)

    def test_restyle_contract_preserves_behavior(self):
        body = text("commands/restyle.md").lower()
        for phrase in ("design.md", "visual-only boundary", "before/after"):
            self.assertIn(phrase, body)
        for phrase in ("application logic", "data flow", "copy meaning", "feature scope"):
            self.assertIn(phrase, body)


class ClaudeCodeAdapterTests(unittest.TestCase):
    base = "adapters/claude-code/.claude"

    def test_public_and_internal_skill_counts(self):
        self.assertEqual(
            child_dirs(f"{self.base}/skills"),
            PUBLIC_ACTIONS | INTERNAL_SKILLS,
        )

    def test_public_actions_are_explicit_only(self):
        for name in PUBLIC_ACTIONS:
            body = text(f"{self.base}/skills/{name}/SKILL.md")
            self.assertIn("disable-model-invocation: true", body)

    def test_internal_skills_are_hidden(self):
        for name in INTERNAL_SKILLS:
            body = text(f"{self.base}/skills/{name}/SKILL.md")
            self.assertIn("user-invocable: false", body)

    def test_agent_routing(self):
        self.assertIn("agent: ux-designer", text(f"{self.base}/skills/ux-design/SKILL.md"))
        for name in ("ux-audit", "ux-review"):
            self.assertIn("agent: ux-auditor", text(f"{self.base}/skills/{name}/SKILL.md"))
        self.assertNotIn("\nagent:", text(f"{self.base}/skills/restyle/SKILL.md"))

    def test_exactly_two_agents(self):
        self.assertEqual(markdown_stems(f"{self.base}/agents"), INTERNAL_AGENTS)


class CodexAdapterTests(unittest.TestCase):
    base = "adapters/codex"

    def test_exactly_four_discovered_skills(self):
        self.assertEqual(child_dirs(f"{self.base}/.agents/skills"), PUBLIC_ACTIONS)

    def test_hidden_reasoning_core(self):
        self.assertEqual(child_dirs(f"{self.base}/.uiux/skills"), INTERNAL_SKILLS)

    def test_explicit_invocation_policy(self):
        for name in PUBLIC_ACTIONS:
            body = text(f"{self.base}/.agents/skills/{name}/agents/openai.yaml")
            self.assertRegex(
                body,
                r"allow_implicit_invocation:\s*false",
            )

    def test_exactly_two_custom_agents(self):
        self.assertEqual(
            {p.stem for p in (ROOT / self.base / ".codex" / "agents").glob("*.toml")},
            INTERNAL_AGENTS,
        )

    def test_internal_skills_are_not_discovered(self):
        discovered = child_dirs(f"{self.base}/.agents/skills")
        self.assertTrue(INTERNAL_SKILLS.isdisjoint(discovered))


class CursorAdapterTests(unittest.TestCase):
    base = "adapters/cursor"

    def test_exactly_four_cursor_skills(self):
        self.assertEqual(child_dirs(f"{self.base}/.cursor/skills"), PUBLIC_ACTIONS)

    def test_hidden_reasoning_core(self):
        self.assertEqual(child_dirs(f"{self.base}/.uiux/skills"), INTERNAL_SKILLS)

    def test_public_actions_are_explicit_only(self):
        for name in PUBLIC_ACTIONS:
            body = text(f"{self.base}/.cursor/skills/{name}/SKILL.md")
            self.assertIn("disable-model-invocation: true", body)

    def test_agents_are_hidden_resources_not_cursor_actions(self):
        self.assertFalse((ROOT / self.base / ".cursor" / "agents").exists())
        self.assertEqual(
            markdown_stems(f"{self.base}/.uiux/agents"),
            INTERNAL_AGENTS,
        )


class OpenCodeAdapterTests(unittest.TestCase):
    base = "adapters/opencode"

    def test_exactly_four_commands(self):
        self.assertEqual(
            markdown_stems(f"{self.base}/.opencode/commands"),
            PUBLIC_ACTIONS,
        )

    def test_hidden_reasoning_core(self):
        self.assertEqual(child_dirs(f"{self.base}/.uiux/skills"), INTERNAL_SKILLS)

    def test_exactly_two_hidden_agents(self):
        self.assertEqual(
            markdown_stems(f"{self.base}/.opencode/agents"),
            INTERNAL_AGENTS,
        )
        for name in INTERNAL_AGENTS:
            body = text(f"{self.base}/.opencode/agents/{name}.md")
            self.assertRegex(body, r"(?m)^mode:\s*subagent\s*$")
            self.assertRegex(body, r"(?m)^hidden:\s*true\s*$")

    def test_command_routing(self):
        design = text(f"{self.base}/.opencode/commands/ux-design.md")
        audit = text(f"{self.base}/.opencode/commands/ux-audit.md")
        review = text(f"{self.base}/.opencode/commands/ux-review.md")
        restyle = text(f"{self.base}/.opencode/commands/restyle.md")

        self.assertIn("agent: ux-designer", design)
        self.assertIn("subagent: true", design)
        self.assertIn("agent: ux-auditor", audit)
        self.assertIn("subagent: true", audit)
        self.assertIn("agent: ux-auditor", review)
        self.assertIn("subagent: true", review)
        self.assertNotIn("\nagent:", restyle)
        self.assertIn("subagent: false", restyle)


class BehavioralFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(text("evals/cases.json"))

    def test_each_public_action_has_multiple_cases(self):
        counts = {action: 0 for action in PUBLIC_ACTIONS}
        for case in self.cases:
            counts[case["command"]] += 1
        for action, count in counts.items():
            self.assertGreaterEqual(count, 2, f"{action} needs at least two eval cases")

    def test_fixture_schema(self):
        required = {
            "id",
            "command",
            "prompt",
            "setup",
            "must_demonstrate",
            "must_not",
            "rationale",
        }
        ids = set()
        for case in self.cases:
            self.assertTrue(required.issubset(case))
            self.assertIn(case["command"], PUBLIC_ACTIONS)
            self.assertTrue(case["must_demonstrate"])
            self.assertTrue(case["must_not"])
            self.assertNotIn(case["id"], ids)
            ids.add(case["id"])

    def test_fixture_ids_match_cases(self):
        fixtures = json.loads(text("evals/fixtures.json"))
        case_ids = {case["id"] for case in self.cases}
        self.assertEqual(set(fixtures), case_ids)

    def test_fixtures_have_file_maps(self):
        fixtures = json.loads(text("evals/fixtures.json"))
        for case_id, fixture in fixtures.items():
            self.assertIsInstance(fixture.get("files"), dict, case_id)
            self.assertIsInstance(fixture.get("changes", {}), dict, case_id)


if __name__ == "__main__":
    unittest.main()
