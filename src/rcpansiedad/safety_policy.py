"""Conservative explicit-answer routing for development tests.

This is not a crisis detector or a clinical risk assessment. It only prevents
the future flow from continuing when a direct safety answer is explicit danger
or cannot be understood as a clear no.
"""

from enum import Enum
import re


class SafetyRoute(str, Enum):
    CONTINUE = "continue"
    HUMAN_HELP = "human_help"
    CLARIFY = "clarify"


_DANGER = (
    "i am in immediate danger",
    "i'm in immediate danger",
    "i am in danger",
    "i'm in danger",
    "i want to hurt myself",
    "i want to hurt someone",
    "i cannot keep myself safe",
    "i can't keep myself safe",
    "estoy en peligro inmediato",
    "estoy en peligro",
    "quiero hacerme daño",
    "quiero hacerle daño a alguien",
    "no puedo mantenerme a salvo",
    "no puedo mantenerme seguro",
)

_CLEAR_NO = {
    "no",
    "no i am safe",
    "no i'm safe",
    "no, i am safe",
    "no, i'm safe",
    "no estoy en peligro",
    "no estoy en peligro inmediato",
    "no tengo pensamientos de hacerme daño",
    "no tengo pensamientos de hacerle daño a alguien",
    "i am safe",
    "i'm safe",
    "i am not in danger",
    "i'm not in danger",
    "i am not thinking about hurting myself",
    "i am not thinking about hurting anyone",
}


def _normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip().lower())
    return text.strip(" .!?¡¿")


def screen_explicit_response(text: str) -> SafetyRoute:
    """Route a direct answer without pretending to assess risk."""

    normalized = _normalize(text)
    if normalized in _CLEAR_NO:
        return SafetyRoute.CONTINUE
    if any(signal in normalized for signal in _DANGER):
        return SafetyRoute.HUMAN_HELP
    return SafetyRoute.CLARIFY
