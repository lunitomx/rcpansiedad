#!/usr/bin/env python3
"""Dependency-free checks for the public alpha Skill package."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "rcpansiedad"


def test_required_skill_files_exist():
    required = {
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "safety-and-privacy.md",
        SKILL / "references" / "rcp-flow.md",
        SKILL / "references" / "response-style.md",
        SKILL / "references" / "official-links.md",
    }
    assert all(path.is_file() for path in required)


def test_skill_contains_non_negotiable_boundaries():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    for phrase in (
        "## Safety gate",
        "never diagnose",
        "never receive, synchronize, inspect or analyze",
        "local-only",
        "## Five-step flow",
        "## Privacy contract",
    ):
        assert phrase in text


def test_bilingual_content_has_five_steps():
    for locale in ("en", "es"):
        text = (ROOT / "content" / locale / "core-flow.md").read_text(encoding="utf-8")
        assert text.count("## ") == 5


def test_four_runtime_manifests_are_local_and_bilingual():
    import json

    manifests = sorted((ROOT / "adapters").glob("*/manifest.json"))
    assert {path.parent.name for path in manifests} == {"antigravity", "claude", "codex", "hermes"}
    for path in manifests:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        assert manifest["local_only"] is True
        assert set(manifest["languages"]) == {"en", "es"}
        assert manifest["text_complete"] is True


def test_public_package_has_no_private_source_material():
    forbidden_suffixes = {".pdf", ".docx", ".mp4", ".mov", ".m4a"}
    assert not any(path.suffix.lower() in forbidden_suffixes for path in ROOT.rglob("*"))
    assert not any("incoming" in path.parts for path in ROOT.rglob("*"))


def test_public_copy_does_not_repeat_rejected_claims():
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for directory in (ROOT / "skills", ROOT / "content")
        for path in directory.rglob("*.md")
    ).lower()
    for phrase in ("90%", "scientifically identified causes", "therapy savings"):
        assert phrase not in text


if __name__ == "__main__":
    tests = [
        test_required_skill_files_exist,
        test_skill_contains_non_negotiable_boundaries,
        test_bilingual_content_has_five_steps,
        test_four_runtime_manifests_are_local_and_bilingual,
        test_public_package_has_no_private_source_material,
        test_public_copy_does_not_repeat_rejected_claims,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
