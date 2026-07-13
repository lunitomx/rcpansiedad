import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from rcpansiedad.safety_policy import SafetyRoute, screen_explicit_response


def test_clear_no_can_continue():
    assert screen_explicit_response("No, I am safe.") is SafetyRoute.CONTINUE
    assert screen_explicit_response("No estoy en peligro.") is SafetyRoute.CONTINUE


def test_explicit_danger_routes_to_human_help():
    assert screen_explicit_response("I want to hurt myself") is SafetyRoute.HUMAN_HELP
    assert screen_explicit_response("Estoy en peligro inmediato") is SafetyRoute.HUMAN_HELP


def test_ambiguous_answer_requires_clarification():
    assert screen_explicit_response("I am not sure") is SafetyRoute.CLARIFY
