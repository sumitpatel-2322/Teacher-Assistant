"""
Layer 2: Rule-based Situation Detection
Consumes normalized text from Layer 1.
Outputs situation scores using canonical SITUATIONS.
"""

from decision_engine.constants import SITUATIONS


# Signal token → situation mapping with base weights
SIGNAL_RULES = {
    "low_attention_signal": {
        SITUATIONS["LOW_ATTENTION"]: 0.8,
    },
    "silent_class_signal": {
        SITUATIONS["LOW_ATTENTION"]: 0.6,
    },
    "unresponsive_class_signal": {
        SITUATIONS["LOW_ATTENTION"]: 0.7,
    },
    "confusion_signal": {
        SITUATIONS["STUDENTS_NOT_UNDERSTANDING"]: 0.85,
    },
    "noise_spike_signal": {
        SITUATIONS["ACTIVITY_FAILURE"]: 0.6,
    },
    "writing_block_signal": {
        SITUATIONS["LEARNING_DIFFICULTIES"]: 0.8,
    },
    "low_engagement_signal": {
        SITUATIONS["ACTIVITY_FAILURE"]: 0.7,
    },
    "fatigue_signal": {
        SITUATIONS["EMOTIONAL_INSTABILITY"]: 0.6,
    },
}


def detect_situations(normalized_text: str) -> dict:
    """
    Returns a dict of {situation_id: score}
    Deterministic, multi-situation allowed.
    """

    situation_scores = {}

    if not normalized_text:
        return situation_scores

    tokens = normalized_text.split()

    for token in tokens:
        if token in SIGNAL_RULES:
            for situation, weight in SIGNAL_RULES[token].items():
                situation_scores[situation] = max(
                    situation_scores.get(situation, 0.0),
                    weight
                )

    return situation_scores