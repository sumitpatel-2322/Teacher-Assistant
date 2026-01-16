"""
Theme 1 Preprocessing
Massive Phrase Map for 18 Master Situations
Maps raw phrases to intermediate signal tokens.
"""

PHRASE_MAP = {
    # 1. CLASSROOM CHAOS (chaos_signal)
    "too loud": "chaos_signal", "making noise": "chaos_signal", "fish market": "chaos_signal",
    "screaming": "chaos_signal", "shouting": "chaos_signal", "yelling": "chaos_signal",
    "running around": "chaos_signal", "out of control": "chaos_signal", "chaos": "chaos_signal",
    "unruly": "chaos_signal", "messy class": "chaos_signal", "disturbing": "chaos_signal",
    "talking constantly": "chaos_signal", "chatter": "chaos_signal", "noisy": "chaos_signal",
    "fighting": "chaos_signal", "hitting": "chaos_signal", "throwing things": "chaos_signal",

    # 2. LOW ENGAGEMENT (boredom_signal)
    "sleeping": "boredom_signal", "bored": "boredom_signal", "head down": "boredom_signal",
    "yawning": "boredom_signal", "not interested": "boredom_signal", "dull": "boredom_signal",
    "passive": "boredom_signal", "no energy": "boredom_signal", "lifeless": "boredom_signal",
    "zombie": "boredom_signal", "blank faces": "boredom_signal", "watching clock": "boredom_signal",

    # 3. LOW ATTENTION (attention_signal)
    "not listening": "attention_signal", "distracted": "attention_signal", "fidgeting": "attention_signal",
    "looking away": "attention_signal", "playing": "attention_signal", "drawing": "attention_signal",
    "daydreaming": "attention_signal", "zoning out": "attention_signal", "lost": "attention_signal",
    "ignoring me": "attention_signal", "short span": "attention_signal", "can't focus": "attention_signal",

    # 4. CONCEPT CONFUSION (confusion_signal)
    "don't understand": "confusion_signal", "confused": "confusion_signal", "hard to explain": "confusion_signal",
    "difficult topic": "confusion_signal", "struggling": "confusion_signal", "doubt": "confusion_signal",
    "not getting it": "confusion_signal", "fail": "confusion_signal", "complicated": "confusion_signal",
    "tricky": "confusion_signal", "abstract": "confusion_signal", "can't grasp": "confusion_signal",
    "misunderstanding": "confusion_signal", "wrong answers": "confusion_signal", "concept unclear": "confusion_signal",

    # 5. MEMORY ISSUES (memory_signal)
    "forgetting": "memory_signal", "forgot": "memory_signal", "can't remember": "memory_signal",
    "retention": "memory_signal", "recall": "memory_signal", "blanking out": "memory_signal",
    "short term memory": "memory_signal", "rote learning": "memory_signal", "memorizing": "memory_signal",

    # 6. WRITING ISSUES (writing_signal)
    "slow writing": "writing_signal", "bad handwriting": "writing_signal", "won't write": "writing_signal",
    "illegible": "writing_signal", "incomplete notes": "writing_signal", "writing speed": "writing_signal",
    "can't hold pen": "writing_signal", "spelling mistakes": "writing_signal", "scribbling": "writing_signal",

    # 7. READING / LANGUAGE (reading_signal)
    "can't read": "reading_signal", "stuttering": "reading_signal", "vocabulary": "reading_signal",
    "grammar": "reading_signal", "pronunciation": "reading_signal", "mother tongue": "reading_signal",
    "english problem": "reading_signal", "fluency": "reading_signal", "reading slow": "reading_signal",

    # 8. MATH ISSUES (math_signal)
    "calculation error": "math_signal", "scared of math": "math_signal", "numbers": "math_signal",
    "tables": "math_signal", "geometry": "math_signal", "algebra": "math_signal", "formula": "math_signal",
    "math phobia": "math_signal", "counting": "math_signal", "logic": "math_signal", "sums": "math_signal",

    # 9. SHYNESS / CONFIDENCE (shyness_signal)
    "shy": "shyness_signal", "quiet": "shyness_signal", "afraid to speak": "shyness_signal",
    "scared": "shyness_signal", "low confidence": "shyness_signal", "won't answer": "shyness_signal",
    "whispering answer": "shyness_signal", "hiding": "shyness_signal", "nervous": "shyness_signal",
    "fear of speaking": "shyness_signal", "introvert": "shyness_signal",

    # 10. TIME / TRANSITIONS (time_signal)
    "late": "time_signal", "slow start": "time_signal", "transition": "time_signal",
    "wasting time": "time_signal", "syllabus incomplete": "time_signal", "rushing": "time_signal",
    "bell rang": "time_signal", "settling down": "time_signal", "taking long": "time_signal",

    # 11. MIXED LEVELS (mixed_signal)
    "fast learners": "mixed_signal", "slow learners": "mixed_signal", "mixed group": "mixed_signal",
    "levels": "mixed_signal", "waiting": "mixed_signal", "finishing early": "mixed_signal",
    "different pace": "mixed_signal", "multi grade": "mixed_signal", "advanced": "mixed_signal",

    # 12. DISRESPECT / DEFIANCE (disrespect_signal)
    "rude": "disrespect_signal", "arguing": "disrespect_signal", "refusing": "disrespect_signal",
    "saying no": "disrespect_signal", "talking back": "disrespect_signal", "insulting": "disrespect_signal",
    "arrogant": "disrespect_signal", "defiant": "disrespect_signal", "attitude": "disrespect_signal",

    # 13. HOMEWORK / PARENTS (home_signal)
    "no homework": "home_signal", "parents": "home_signal", "support": "home_signal",
    "incomplete work": "home_signal", "notebook": "home_signal", "guardian": "home_signal",
    "home environment": "home_signal", "practice at home": "home_signal",

    # 14. RESOURCES (resource_signal)
    "no electricity": "resource_signal", "power cut": "resource_signal", "dark": "resource_signal",
    "no internet": "resource_signal", "offline": "resource_signal", "no projector": "resource_signal",
    "blackboard": "resource_signal", "chalk": "resource_signal", "hot": "resource_signal",
    "crowded": "resource_signal", "space": "resource_signal",

    # 15. EMOTIONAL / WELLBEING (emotion_signal)
    "hungry": "emotion_signal", "tired": "emotion_signal", "sad": "emotion_signal",
    "crying": "emotion_signal", "anxious": "emotion_signal", "stressed": "emotion_signal",
    "sick": "emotion_signal", "headache": "emotion_signal", "family issue": "emotion_signal",
    "upset": "emotion_signal", "depressed": "emotion_signal",
}