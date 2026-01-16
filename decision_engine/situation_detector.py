"""
Layer 2: Rule-based Situation Detection
Maps signals (from normalized text) to Master Situations.
"""

from decision_engine.constants import SITUATIONS

# Signal -> Master Situation Mapping
SIGNAL_RULES = {
    "chaos_signal":      SITUATIONS["CLASSROOM_CHAOS"],
    "boredom_signal":    SITUATIONS["LOW_ENGAGEMENT"],
    "attention_signal":  SITUATIONS["LOW_ATTENTION"],
    "confusion_signal":  SITUATIONS["CONCEPT_CONFUSION"],
    "memory_signal":     SITUATIONS["MEMORY_RETENTION_ISSUE"],
    "writing_signal":    SITUATIONS["WRITING_DIFFICULTY"],
    "reading_signal":    SITUATIONS["READING_LANGUAGE_ISSUE"],
    "math_signal":       SITUATIONS["MATH_DIFFICULTY"],
    "shyness_signal":    SITUATIONS["SHYNESS_LOW_CONFIDENCE"],
    "time_signal":       SITUATIONS["TIME_MANAGEMENT_ISSUE"],
    "mixed_signal":      SITUATIONS["MIXED_LEVELS"],
    "disrespect_signal": SITUATIONS["DISRESPECT_DEFIANCE"],
    "home_signal":       SITUATIONS["HOMEWORK_PARENT_ISSUE"],
    "resource_signal":   SITUATIONS["RESOURCE_CONSTRAINT"],
    "emotion_signal":    SITUATIONS["EMOTIONAL_WELLBEING"],
}

def detect_situations(normalized_text: str) -> dict:
    """
    Returns {situation_id: score}
    Example: {'classroom_chaos': 0.95, 'low_attention': 0.95}
    """
    situation_scores = {}
    if not normalized_text:
        return situation_scores

    tokens = normalized_text.split()

    for token in tokens:
        if token in SIGNAL_RULES:
            situation = SIGNAL_RULES[token]
            # Accumulate score if found
            situation_scores[situation] = 0.95 

    return situation_scores