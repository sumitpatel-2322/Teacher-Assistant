from typing import Dict

from preprocessing.normalizer import normalize_text
from decision_engine.situation_detector import detect_situations
from decision_engine.constants import CONSTRAINTS


# ------------------------------------------------------
# Constraint keyword mapping (kept rule-based)
# ------------------------------------------------------

CONSTRAINT_KEYWORDS = {
    CONSTRAINTS["PROJECTOR_AVAILABLE"]: [
        "projector",
        "smart board",
        "interactive board",
    ],
    CONSTRAINTS["LOW_INTERNET"]: [
        "no internet",
        "network issue",
        "poor connection",
        "offline",
    ],
    CONSTRAINTS["POWER_ISSUE"]: [
        "power cut",
        "no electricity",
        "light gone",
    ],
    CONSTRAINTS["NO_MOBILE"]: [
        "mobile not allowed",
        "no mobile",
        "phones not allowed",
    ],
    CONSTRAINTS["TIME_PRESSURE"]: [
        "no time",
        "running out of time",
        "short period",
        "syllabus pressure",
        "less time",
    ],
}


def _score_matches(text: str, keywords: list[str]) -> float:
    hits = sum(1 for kw in keywords if kw in text)
    if hits == 0:
        return 0.0
    if hits == 1:
        return 0.6
    if hits == 2:
        return 0.75
    return 0.9


def extract_signals(raw_text: str) -> Dict[str, Dict[str, float]]:
    """
    Orchestrates Layer 1 + Layer 2.
    No situation logic lives here.
    """

    normalized_text = normalize_text(raw_text)

    situations = detect_situations(normalized_text)
    constraints: Dict[str, float] = {}

    for constraint, keywords in CONSTRAINT_KEYWORDS.items():
        score = _score_matches(normalized_text, keywords)
        if score > 0:
            constraints[constraint] = score

    return {
        "situations": situations,
        "constraints": constraints,
    }