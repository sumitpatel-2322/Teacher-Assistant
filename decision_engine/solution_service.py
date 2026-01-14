"""
Solution Retrieval Service
--------------------------
Fetches detailed solution content by solution_id.
Used after teacher selects a solution preview.

Theme 1 rules:
- No re-scoring
- No re-filtering
- Pure lookup
"""

from typing import Dict, Optional
from decision_engine.solution_loader import load_solutions

# Load once
SOLUTION_LIBRARY = load_solutions()

# Build fast lookup map
_SOLUTION_MAP = {s["solution_id"]: s for s in SOLUTION_LIBRARY}


def get_solution_details(solution_id: str) -> Optional[Dict]:
    """
    Returns the detailed solution block for a given solution_id.
    """

    solution = _SOLUTION_MAP.get(solution_id)
    if not solution:
        return None

    return {
        "solution_id": solution["solution_id"],
        "title": solution["preview"]["title"],
        "details": solution["details"],
        "pedagogy": solution.get("pedagogy", {}),
    }
