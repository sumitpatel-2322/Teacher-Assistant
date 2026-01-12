from typing import Dict, List
import uuid
from decision_engine.situations import extract_signals
from decision_engine.solutions import SOLUTION_LIBRARY
from decision_engine.logging import log_decision

# Scoring constants (v1)

CONSTRAINT_FIT_BONUS = 0.2

EFFORT_SCORE = {
    "low": 0.4,
    "medium": 0.2,
    "high": 0.0
}

SAFETY_BONUS = 0.3
# Public Engine Entry Point
def process_teacher_query(raw_text: str) -> Dict[str, List[Dict]]:
    """
    Main Decision Engine entry point.

    Input:
        raw_text (str): messy teacher query

    Output:
        {
            "ranked_solutions": [
                {
                    "solution_id": str,
                    "text": str,
                    "confidence": float
                }
            ]
        }
    """

    # ---- Layer 2: signal extraction ----
    request_id=str(uuid.uuid4())
    signals = extract_signals(raw_text)

    situations = signals.get("situations", {})
    constraints = signals.get("constraints", {})

    scored_solutions: List[Dict] = []

    # ---- Evaluate each solution ----
    for solution in SOLUTION_LIBRARY:

        # Hard constraint filtering
        if not _passes_hard_constraints(solution, constraints):
            continue

        score = _score_solution(solution, situations, constraints)

        if score <= 0:
            continue

        scored_solutions.append({
            "solution_id": solution["solution_id"],
            "text": solution["action_text"],
            "confidence": round(score, 2)
        })

    # ---- Rank solutions ----
    ranked = sorted(
        scored_solutions,
        key=lambda x: x["confidence"],
        reverse=True
    )

    top_solutions = ranked[:5]

    # ---- Logging hook (silent, non-blocking) ----
    log_decision(
        request_id=request_id,
        raw_query=raw_text,
        situations=situations,
        constraints=constraints,
        solutions_shown=[s["solution_id"] for s in top_solutions]
    )

    return {
        "request_id":request_id,
        "ranked_solutions": top_solutions
    }
# Helper Functions
def _passes_hard_constraints(solution: Dict, constraints: Dict[str, float]) -> bool:
    """
    Filters out solutions that violate hard constraints.
    """

    # Required resources must exist
    for required in solution.get("requires", []):
        if required not in constraints:
            return False

    # Explicit avoid conditions
    for avoid in solution.get("avoid_if", []):
        if avoid in constraints:
            return False

    return True


def _score_solution(
    solution: Dict,
    situations: Dict[str, float],
    constraints: Dict[str, float]
) -> float:
    """
    Computes final score for a solution based on Theme 1 rules.
    """

    score = 0.0

    # 1. Situation match score
    for situation in solution.get("works_for", []):
        if situation in situations:
            score += situations[situation]

    # 2. Soft constraint compatibility bonus
    if _fits_constraints(solution, constraints):
        score += CONSTRAINT_FIT_BONUS

    # 3. Effort score
    effort = solution.get("effort", "high")
    score += EFFORT_SCORE.get(effort, 0.0)

    # 4. Classroom safety bonus
    if solution.get("classroom_safety") == "high":
        score += SAFETY_BONUS

    return score


def _fits_constraints(solution: Dict, constraints: Dict[str, float]) -> bool:
    """
    Soft constraint check (non-blocking).
    """
    for avoid in solution.get("avoid_if", []):
        if avoid in constraints:
            return False
    return True