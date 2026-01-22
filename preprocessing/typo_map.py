"""
Token-level typo corrections.
Strictly single-word mappings only.
"""
print("\n>>> DEBUG: [Import] preprocessing/typo_map.py loaded")
TYPO_MAP = {
    # students
    "stutents": "students",
    "stutends": "students",
    "studens": "students",
    "studnts": "students",

    # listening / attention
    "listning": "listening",
    "listing": "listening",
    "lisning": "listening",
    "attension": "attention",
    "attentin": "attention",
    "attensioned": "attention",

    # behavior / behaviour
    "behavour": "behavior",
    "behaviour": "behavior",

    # confusion
    "confusd": "confused",
    "confution": "confusion",

    # noise
    "noice": "noise",

    # participation
    "partcipation": "participation",
    "participateing": "participating",
}
