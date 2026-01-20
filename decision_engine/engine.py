import uuid
import re
from typing import Dict, List

from decision_engine.situations import extract_signals
from decision_engine.solution_loader import load_solutions
from decision_engine.logging import log_decision
from decision_engine.constants import (
    EFFORT_LEVELS,
    SAFETY_LEVELS,
    SITUATIONS,
)
from decision_engine.situation_aliases import SITUATION_ALIASES

# ======================================================
# Runtime constants
# ======================================================

EFFORT_SCORE = {
    EFFORT_LEVELS["LOW"]: 0.4,
    EFFORT_LEVELS["MEDIUM"]: 0.2,
    EFFORT_LEVELS["HIGH"]: 0.0,
}

SAFETY_BONUS = {
    SAFETY_LEVELS["HIGH"]: 0.3,
    SAFETY_LEVELS["MEDIUM"]: 0.1,
}

BASELINE_SITUATION = SITUATIONS.get(
    "GENERAL_CLASSROOM_SUPPORT",
    "GENERAL_CLASSROOM_SUPPORT"
)

MAX_THEORETICAL_SCORE = 1.8

# Load solution library once
SOLUTION_LIBRARY = load_solutions()

# <--- DEBUG START: Verify Library Load Count --->
print(f"\n>>> DEBUG: [Engine] Total Solutions Loaded from Library: {len(SOLUTION_LIBRARY)}")
# <--- DEBUG END --->

# ======================================================
# Public Engine Entry Point
# ======================================================

def process_teacher_query(raw_text: str) -> Dict[str, List[Dict]]:
    request_id = str(uuid.uuid4())
    print(f"\n>>> DEBUG: Engine received query: '{raw_text}'")

    # --------------------------------------------------
    # 1. Context extraction (Subject + optional Class)
    # --------------------------------------------------
    context = _extract_context(raw_text)
    user_subject = context.get("subject", "GENERAL")
    user_class_range = context.get("class_range", "ALL")

    print(f">>> DEBUG: Subject={user_subject}, Class={user_class_range}")

    # --------------------------------------------------
    # 2. Signal extraction (situations + constraints)
    # --------------------------------------------------
    signals = extract_signals(raw_text)
    situations = signals.get("situations", {})
    constraints = signals.get("constraints", {})

    print(f">>> DEBUG: Detected situations: {list(situations.keys())}")

    expanded_situations = _expand_situations(situations)

    scored: List[Dict] = []
    rejection_stats = {"subject": 0, "class": 0, "constraint": 0}

    # --------------------------------------------------
    # 3. Candidate Pool (STRICT FILTERING)
    # --------------------------------------------------
    for solution in SOLUTION_LIBRARY:

        # HARD FILTER 1: Subject
        if not _is_subject_relevant(solution, user_subject):
            rejection_stats["subject"] += 1
            continue

        # HARD FILTER 2: Class Range
        if not _is_class_relevant(solution, user_class_range):
            rejection_stats["class"] += 1
            continue

        # HARD FILTER 3: Constraints
        if not _passes_hard_constraints(solution, constraints):
            rejection_stats["constraint"] += 1
            continue

        # --------------------------------------------------
        # 4. Scoring (Situation is RANKING ONLY)
        # --------------------------------------------------
        score = _score_solution(solution, expanded_situations)

        if score <= 0:
            continue

        scored.append(_format_solution(solution, score))

    print(
        f">>> DEBUG: Rejections -> "
        f"Subject:{rejection_stats['subject']} | "
        f"Class:{rejection_stats['class']} | "
        f"Constraint:{rejection_stats['constraint']}"
    )

    # --------------------------------------------------
    # 5. STRICT FALLBACK (same subject + class only)
    # --------------------------------------------------
    is_fallback = False

    if not scored:
        print(">>> DEBUG: ⚠️ STRICT FALLBACK ACTIVATED")
        is_fallback = True

        for solution in SOLUTION_LIBRARY:
            if not _is_subject_relevant(solution, user_subject):
                continue
            if not _is_class_relevant(solution, user_class_range):
                continue

            if BASELINE_SITUATION in solution.get("situations", []):
                score = 0.6 * MAX_THEORETICAL_SCORE
                scored.append(_format_solution(solution, score))

    # Emergency safety net (should almost never happen)
    if not scored:
        print(">>> DEBUG: 🚨 EMERGENCY BASELINE FALLBACK")
        for solution in SOLUTION_LIBRARY:
            if BASELINE_SITUATION in solution.get("situations", []):
                scored.append(_format_solution(solution, 0.4 * MAX_THEORETICAL_SCORE))

    # --------------------------------------------------
    # 6. Rank & return (TOP 6 to allow variety)
    # --------------------------------------------------
    ranked = sorted(scored, key=lambda x: x["confidence"], reverse=True)
    
    # UPDATED: Increased limit from 3 to 6
    top_solutions = ranked[:6]

    log_decision(
        request_id,
        raw_text,
        situations,
        constraints,
        [s["solution_id"] for s in top_solutions]
    )

    return {
        "request_id": request_id,
        "ranked_solutions": top_solutions,
        "is_fallback": is_fallback,
    }

# ======================================================
# Helper Functions
# ======================================================

def _extract_context(raw_text: str) -> Dict[str, str]:
    context = {}

    text_upper = raw_text.upper()
    detected_subject = "GENERAL"

    # UPDATED: Added specific math concepts to regex
    if re.search(r"\b(MATH|ALGEBRA|GEOMETRY|NUMBERS|SUM|TABLE|FRACTION|DECIMAL|RATIO)\b", text_upper):
        detected_subject = "MATH"
    elif re.search(r"\b(SCIENCE|PHYSICS|CHEMISTRY|BIOLOGY)\b", text_upper):
        detected_subject = "SCIENCE"
    elif re.search(r"\b(ENGLISH|HINDI|READING|WRITING|GRAMMAR)\b", text_upper):
        detected_subject = "ENGLISH"
    elif re.search(r"\b(HISTORY|GEOGRAPHY|CIVICS|SOCIAL)\b", text_upper):
        detected_subject = "SOCIAL SCIENCE"

    context["subject"] = detected_subject
    
    # Detect Class
    class_match = re.search(r"Class:\s*(?:Class\s*)?(\d+)", raw_text, re.IGNORECASE)
    if class_match:
        class_num = int(class_match.group(1))

        if class_num <= 2:
            detected_class = "CLASS_1_2"
        elif class_num <= 3:
            detected_class = "CLASS_2_3"
        elif class_num <= 5:
            detected_class = "CLASS_3_5"
        else:
            detected_class = "CLASS_5_10"
    else:
        detected_class = "ALL"

    context["class_range"] = detected_class

    return context


def _is_subject_relevant(solution: Dict, user_subject: str) -> bool:
    # Handle both 'subject' (string) and 'subjects' (list) keys for compatibility
    sol_subject = solution.get("subject", "")
    sol_subjects = solution.get("subjects", [])
    
    # Convert to list if it's a string
    if isinstance(sol_subject, str):
        sol_subject_list = [sol_subject.upper()] if sol_subject else []
    else:
        sol_subject_list = [s.upper() for s in sol_subject] if sol_subject else []
    
    # Combine with subjects list
    all_subjects = sol_subject_list + [s.upper() for s in sol_subjects]
    
    # Empty subject = GENERAL applicability (for behavior, wellbeing, management solutions)
    if not all_subjects or all(not s for s in all_subjects):
        return True
    
    # Accept GENERAL or ALL subjects
    if "GENERAL" in all_subjects or "ALL" in all_subjects:
        return True
    
    # Check if user_subject matches
    return user_subject.upper() in all_subjects


def _is_class_relevant(solution: Dict, user_class: str) -> bool:
    sol_class = solution.get("class_range", "ALL")

    if sol_class == "ALL" or user_class == "ALL":
        return True

    return sol_class == user_class


def _expand_situations(situations: Dict[str, float]) -> Dict[str, float]:
    expanded = dict(situations)

    for situation, score in situations.items():
        aliases = SITUATION_ALIASES.get(situation, set())
        for alias in aliases:
            expanded.setdefault(alias, score * 0.9)

    return expanded


def _passes_hard_constraints(solution: Dict, constraints: Dict[str, float]) -> bool:
    avoid_if = solution.get("constraints", {}).get("avoid_if", [])

    for avoid in avoid_if:
        if avoid in constraints:
            return False

    return True

def _instructional_boost(situation_id: str) -> float:
    """
    Boost instructional / subject-specific intent
    without breaking existing scoring logic.
    """
    if (
        situation_id.endswith("_CONFUSION")
        or "MISCONCEPTION" in situation_id
        or "CONCEPT" in situation_id
        or situation_id.startswith("GEOMETRY")
        or situation_id.startswith("FRACTIONS")
        or situation_id.startswith("RATIO")
        or situation_id.startswith("DECIMAL")
    ):
        return 2.5
    return 1.0

def _score_solution(solution: Dict, situations: Dict[str, float]) -> float:
    score = 0.0
    matches = 0
    weight = 1.0
    
    # Normalize detected situations to lowercase for matching
    situations_normalized = {k.lower(): v for k, v in situations.items()}
    
    for s in solution.get("situations", []):
        s_lower = s.lower()
        if s_lower in situations_normalized:
            base_score = situations_normalized.get(s_lower, 0.0)
            weight = _instructional_boost(s)
            score += situations_normalized[s_lower] * weight
            matches += 1
            print(
                f">>> DEBUG SCORE: solution={solution.get('solution_id')} | "
                f"situation={s} | base={base_score} | "
                f"weight={weight} | partial_score={base_score * weight}"
            )

    if matches > 1:
        score += 0.1

    score += EFFORT_SCORE.get(solution.get("effort_level"), 0.0)
    score += SAFETY_BONUS.get(solution.get("classroom_safety"), 0.0)
    if score > 0:
        print(
            f">>> DEBUG FINAL SCORE: solution={solution.get('solution_id')} | "
            f"matches={matches} | total_score={score}"
        )
    return score


def _format_solution(solution: Dict, raw_score: float) -> Dict:
    normalized = min(raw_score / MAX_THEORETICAL_SCORE, 1.0)
    normalized = max(normalized, 0.1)

    return {
        "solution_id": solution["solution_id"],
        "title": solution["preview"]["title"],
        "text": solution["preview"]["action_text"],
        "confidence": round(normalized, 2),
        "type": solution.get("topic_type", "GENERAL"),
    }