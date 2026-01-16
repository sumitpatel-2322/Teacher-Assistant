"""
Theme 1 Constants
Merged: Master Situations + Backward Compatibility + Project Constraints
"""

# ======================================================
# 1. MASTER SITUATIONS (Normalized for Detection & Reporting)
# ======================================================
SITUATIONS = {
    # --- BEHAVIOR & DISCIPLINE ---
    "CLASSROOM_CHAOS": "classroom_chaos",
    "DISRESPECT_DEFIANCE": "disrespect_defiance",
    "BULLYING_CONFLICT": "bullying_conflict",

    # --- ENGAGEMENT & ENERGY ---
    "LOW_ENGAGEMENT": "low_engagement",
    "LOW_ATTENTION": "low_attention",
    "SHYNESS_LOW_CONFIDENCE": "shyness_low_confidence",

    # --- COGNITION & LEARNING ---
    "CONCEPT_CONFUSION": "concept_confusion",
    "MEMORY_RETENTION_ISSUE": "memory_retention_issue",
    "LACK_CRITICAL_THINKING": "lack_critical_thinking",

    # --- ACADEMIC SKILLS ---
    "WRITING_DIFFICULTY": "writing_difficulty",
    "READING_LANGUAGE_ISSUE": "reading_language_issue",
    "MATH_DIFFICULTY": "math_difficulty",

    # --- CLASSROOM MANAGEMENT ---
    "TIME_MANAGEMENT_ISSUE": "time_management_issue",
    "MIXED_LEVELS": "mixed_levels",
    "LARGE_CLASS_CROWD": "large_class_crowd",

    # --- EXTERNAL FACTORS ---
    "HOMEWORK_PARENT_ISSUE": "homework_parent_issue",
    "RESOURCE_CONSTRAINT": "resource_constraint",
    "EMOTIONAL_WELLBEING": "emotional_wellbeing",
    
    # --- BASELINE (MANDATORY) ---
    "GENERAL_CLASSROOM_SUPPORT": "general_classroom_support",

    # ======================================================
    # ⚠️ BACKWARD COMPATIBILITY ALIASES (Fixes KeyError)
    # Maps OLD keys (used in solutions.py) to NEW normalized values
    # ======================================================
    "MIXED_LEARNING_LEVELS": "mixed_levels",        # Maps to MIXED_LEVELS
    "STUDENTS_NOT_UNDERSTANDING": "concept_confusion", # Maps to CONCEPT_CONFUSION
    "HIGH_CLASS_STRENGTH": "large_class_crowd",     # Maps to LARGE_CLASS_CROWD
    "ACTIVITY_FAILURE": "concept_confusion",        # Maps to CONCEPT_CONFUSION
    "LEARNING_DIFFICULTIES": "low_engagement",      # Maps to LOW_ENGAGEMENT (or specific)
    "EMOTIONAL_INSTABILITY": "emotional_wellbeing", # Maps to EMOTIONAL_WELLBEING
}

# ======================================================
# 2. EXISTING PROJECT CONSTANTS (Preserved)
# ======================================================

# Subjects
SUBJECTS = {
    "MATH": "math",
    "SCIENCE": "science",
    "LANGUAGE": "language",
    "SOCIAL_SCIENCE": "social_science",
    "GENERAL": "general",
}

# Class ranges
CLASS_RANGES = {
    "PRIMARY": "1-5",
    "MIDDLE": "6-8",
    "SECONDARY": "9-10",
}

# Topic types
TOPIC_TYPES = {
    "CONCEPTUAL": "conceptual",
    "PROCEDURAL": "procedural",
    "MEMORIZATION": "memorization",
    "APPLICATION": "application",
}

# Learning modes
LEARNING_MODES = {
    "VERBAL": "verbal",
    "VISUAL": "visual",
    "KINESTHETIC": "kinesthetic",
    "MIXED": "mixed",
}

# Constraints
CONSTRAINTS = {
    "LOW_INTERNET": "low_internet",
    "PROJECTOR_AVAILABLE": "projector_available",
    "POWER_ISSUE": "power_issue",
    "NO_MOBILE": "no_mobile",
    "TIME_PRESSURE": "time_pressure",
    "BOARD_AVAILABLE": "board_available",
}

# Effort levels
EFFORT_LEVELS = {
    "LOW": "low",
    "MEDIUM": "medium",
    "HIGH": "high",
}

# Safety levels
SAFETY_LEVELS = {
    "HIGH": "high",
    "MEDIUM": "medium",
    "LOW": "low",  # Ensure LOW is here too if used
}

# Noise levels
NOISE_LEVELS = {
    "LOW": "low",
    "MEDIUM": "medium",
    "HIGH": "high",
}

# Student states
STUDENT_STATES = {
    "PASSIVE": "passive",
    "RESTLESS": "restless",
    "MIXED": "mixed",
}