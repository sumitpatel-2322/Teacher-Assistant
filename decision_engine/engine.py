"""
Theme 1 Decision Engine
Core Runtime Logic (Schema-Aware)
"""

import uuid
import re
from typing import Dict, List
from decision_engine.diversity_selector import select_diverse_solutions
from decision_engine.situations import extract_signals
from decision_engine.solution_loader import load_solutions
from decision_engine.logging import log_decision
from decision_engine.constants import EFFORT_LEVELS, SAFETY_LEVELS, SITUATIONS
from decision_engine.situation_aliases import SITUATION_ALIASES

# ======================================================
# Runtime constants (v1)
# ======================================================

CONSTRAINT_FIT_BONUS = 0.2

EFFORT_SCORE = {
    EFFORT_LEVELS["LOW"]: 0.4,
    EFFORT_LEVELS["MEDIUM"]: 0.2,
    EFFORT_LEVELS["HIGH"]: 0.0,
}

SAFETY_BONUS = {
    SAFETY_LEVELS["HIGH"]: 0.3,
    SAFETY_LEVELS["MEDIUM"]: 0.1,
}

BASELINE_SITUATION = SITUATIONS["GENERAL_CLASSROOM_SUPPORT"]

# ======================================================
# Load solution library once
# ======================================================

SOLUTION_LIBRARY = load_solutions()


# ======================================================
# Public Engine Entry Point
# ======================================================

def process_teacher_query(raw_text: str) -> Dict[str, List[Dict]]:
    """
    Main Decision Engine entry point.
    """
    print(f">>> DEBUG: Engine.py received query: '{raw_text}'")

    request_id = str(uuid.uuid4())

    # 1. Extract Metadata (Subject) explicitly from the raw text headers
    context = _extract_context(raw_text)
    user_subject = context.get("subject", "GENERAL")
    print(f">>> DEBUG: Detected User Subject: {user_subject}")

    # 2. Signal extraction
    signals = extract_signals(raw_text)
    situations = signals.get("situations", {})
    constraints = signals.get("constraints", {})
    
    print(f">>> DEBUG: Extracted situations: {list(situations.keys())}")

    # 3. Expand situations using aliases
    expanded_situations = _expand_situations(situations)

    scored: List[Dict] = []
    
    # DEBUG COUNTERS
    reject_subject = 0
    reject_situation = 0
    total_checked = 0

    # -------------------------
    # Primary pass: Situation-Driven
    # -------------------------
    for solution in SOLUTION_LIBRARY:
        total_checked += 1

        # Check Subject Match
        if not _is_subject_relevant(solution, user_subject):
            reject_subject += 1
            continue

        # Check Situation Match
        if expanded_situations and not _matches_situations(solution, expanded_situations):
            reject_situation += 1
            continue

        # Check Constraints
        if not _passes_hard_constraints(solution, constraints):
            continue

        # Calculate Score
        score = _score_solution(solution, expanded_situations, constraints)
        if score <= 0:
            continue

        scored.append({
            "solution_id": solution["solution_id"],
            "title": solution["preview"]["title"],
            "text": solution["preview"]["action_text"],
            "confidence": round(score, 2),
        })

    print(f">>> DEBUG: Pass finished. Checked {total_checked}. Rejections -> Subject: {reject_subject} | Situation: {reject_situation}")

    # -------------------------
    # Fallback Logic (The Safety Net)
    # -------------------------
    is_fallback = False
    
    if not scored:
        is_fallback = True
        print(">>> DEBUG: ⚠️ FALLBACK TRIGGERED - Attempting Standard Fallback...")
        
        fallback_situations = {BASELINE_SITUATION: 1.0}

        # Level 1: Try Fallback Solutions matching the SUBJECT
        for solution in SOLUTION_LIBRARY:
            if not _is_subject_relevant(solution, user_subject): continue
            if BASELINE_SITUATION not in solution.get("situations", []): continue
            if not _passes_hard_constraints(solution, constraints): continue
            
            score = _score_solution(solution, fallback_situations, constraints)
            scored.append(_format_solution(solution, score))

        # Level 2: Emergency Fallback (Ignore Subject)
        if not scored:
            print(">>> DEBUG: 🚨 EMERGENCY FALLBACK - Ignoring Subject Filter to ensure output.")
            for solution in SOLUTION_LIBRARY:
                if BASELINE_SITUATION not in solution.get("situations", []): continue
                # We still respect hardware constraints (e.g., no internet)
                if not _passes_hard_constraints(solution, constraints): continue
                
                score = _score_solution(solution, fallback_situations, constraints)
                scored.append(_format_solution(solution, score))

    # -------------------------
    # Rank & select
    # -------------------------
    ranked = sorted(scored, key=lambda x: x["confidence"], reverse=True)
    top_solutions = select_diverse_solutions(
        ranked=ranked,
        max_results=5,
        seed=request_id,
    )

    log_decision(request_id, raw_text, situations, constraints, [s["solution_id"] for s in top_solutions])
    print(f">>> DEBUG: Engine selected {len(top_solutions)} solutions. (Fallback: {is_fallback})")
    
    return {
        "request_id": request_id,
        "ranked_solutions": top_solutions,
        "is_fallback": is_fallback 
    }


# ======================================================
# Helper Functions
# ======================================================

def _format_solution(solution, score):
    return {
        "solution_id": solution["solution_id"],
        "title": solution["preview"]["title"],
        "text": solution["preview"]["action_text"],
        "confidence": round(score, 2),
    }

def _extract_context(raw_text: str) -> Dict[str, str]:
    context = {}
    subject_match = re.search(r"Subject:\s*(.*)", raw_text, re.IGNORECASE)
    if subject_match:
        context["subject"] = subject_match.group(1).strip().upper()
    return context

def _is_subject_relevant(solution: Dict, user_subject: str) -> bool:
    sol_subjects = [s.upper() for s in solution.get("subjects", [])]
    if "GENERAL" in sol_subjects or "ALL" in sol_subjects: return True
    if not user_subject: return True
    for sol_sub in sol_subjects:
        if sol_sub in user_subject or user_subject in sol_sub: return True
    return False

def _expand_situations(situations: Dict[str, float]) -> Dict[str, float]:
    expanded = dict(situations)
    for situation, score in situations.items():
        aliases = SITUATION_ALIASES.get(situation, set())
        for alias in aliases:
            expanded.setdefault(alias, score * 0.9)
    return expanded

def _matches_situations(solution: Dict, situations: Dict[str, float]) -> bool:
    for s in solution.get("situations", []):
        if s in situations: return True
    return False

def _passes_hard_constraints(solution: Dict, constraints: Dict[str, float]) -> bool:
    requires = solution.get("constraints", {}).get("requires", [])
    avoid_if = solution.get("constraints", {}).get("avoid_if", [])
    for req in requires:
        if req not in constraints: return False
    for avoid in avoid_if:
        if avoid in constraints: return False
    return True

def _score_solution(solution: Dict, situations: Dict[str, float], constraints: Dict[str, float]) -> float:
    score = 0.0
    for s in solution.get("situations", []):
        if s in situations: score += situations[s]
    if _fits_constraints(solution, constraints): score += CONSTRAINT_FIT_BONUS
    score += EFFORT_SCORE.get(solution.get("effort_level"), 0.0)
    score += SAFETY_BONUS.get(solution.get("classroom_safety"), 0.0)
    return score

def _fits_constraints(solution: Dict, constraints: Dict[str, float]) -> bool:
    avoid_if = solution.get("constraints", {}).get("avoid_if", [])
    for avoid in avoid_if:
        if avoid in constraints: return False
    return True