from typing import Dict, List
# Situation keyword mapping
SITUATION_KEYWORDS: Dict[str, List[str]] = {
    "low_attention": [
        "not listening",
        "noise",
        "chaos",
        "not paying attention",
        "attention issue",
        "discipline",
        "restless",
        "disturbance"
    ],

    "students_not_understanding": [
        "not understanding",
        "confused",
        "concept not clear",
        "difficult",
        "clarify",
        "misunderstood",
        "not clear",
        "didn't get"
    ],

    "time_pressure": [
        "no time",
        "running out of time",
        "short period",
        "syllabus pressure",
        "time left",
        "less time"
    ],

    "activity_failure": [
        "activity failed",
        "didn't work",
        "group work failed",
        "students confused during activity",
        "activity not working"
    ],

    "behavior_edge_case": [
        "special needs",
        "aggressive",
        "withdrawn",
        "emotional",
        "isolated student",
        "behavior issue"
    ],

    "high_class_strength": [
        "many students",
        "class is big",
        "crowded class",
        "large class",
        "too many students",
        "high strength"
    ]
}
# Constraint keyword mapping

CONSTRAINT_KEYWORDS: Dict[str, List[str]] = {
    "projector_available": [
        "projector",
        "smart board",
        "interactive board"
    ],

    "low_internet": [
        "no internet",
        "network issue",
        "poor connection",
        "offline"
    ],

    "power_issue": [
        "power cut",
        "no electricity",
        "light gone"
    ],

    "no_mobile_in_class": [
        "mobile not allowed",
        "no mobile",
        "phones not allowed"
    ]
}
# Scoring helpers

def _score_matches(text: str, keywords: List[str]) -> float:
    """
    Returns a weak-signal confidence score based on keyword matches.
    """
    hits = sum(1 for kw in keywords if kw in text)

    if hits == 0:
        return 0.0
    if hits == 1:
        return 0.6
    if hits == 2:
        return 0.75

    return 0.9  # cap confidence, no fake certainty

# Public API

def extract_signals(raw_text: str) -> Dict[str, Dict[str, float]]:
    """
    Extracts situations and constraints as weak signals with confidence scores.

    Returns:
    {
        "situations": { <situation>: <confidence> },
        "constraints": { <constraint>: <confidence> }
    }
    """

    text = raw_text.lower()

    situations: Dict[str, float] = {}
    constraints: Dict[str, float] = {}

    # Extract situations
    for situation, keywords in SITUATION_KEYWORDS.items():
        score = _score_matches(text, keywords)
        if score > 0:
            situations[situation] = score

    # Extract constraints
    for constraint, keywords in CONSTRAINT_KEYWORDS.items():
        score = _score_matches(text, keywords)
        if score > 0:
            constraints[constraint] = score

    return {
        "situations": situations,
        "constraints": constraints
    }