"""
Situation alias mapping.
Maps detector-level situations to solution-library situations.
"""

from decision_engine.constants import SITUATIONS

SITUATION_ALIASES = {
    # Core activity failure expansion
    SITUATIONS["ACTIVITY_FAILURE"]: {
        "CLASS_NOISE_SPIKE",
        "LOSS_OF_FOCUS",
        "MESSY_ACTIVITY_END",
        "TRANSITION_CONFUSION",
        "END_OF_CLASS_DRIFT",
        "LOW_ENGAGEMENT",
        "PASSIVE_LEARNING",
        "BOREDOM",
    },

    # Low attention expansion
    SITUATIONS["LOW_ATTENTION"]: {
        "LOSS_OF_FOCUS",
        "CLASS_NOISE_SPIKE",
        "SILENT_CLASS",
        "LOW_PARTICIPATION",
    },

    # Students not understanding
    SITUATIONS["STUDENTS_NOT_UNDERSTANDING"]: {
        "UNCLEAR_UNDERSTANDING",
        "MISREAD_INSTRUCTIONS",
        "TASK_ERRORS",
        "CONFUSION",
    },
}