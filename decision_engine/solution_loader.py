"""
Solution Loader & Validator
---------------------------
Loads the solution library into memory and validates
basic structural integrity at startup.

Theme 1 rules:
- Read-only
- No mutation
- Fail fast on schema errors
"""

from typing import List, Dict
from solutions.solutions import SOLUTION_LIBRARY


REQUIRED_TOP_LEVEL_KEYS = {
    "solution_id",
    "version",
    "status",
    "situations",
    "subjects",
    "class_range",
    "topic_type",
    "learning_mode",
    "preview",
    "details",
    "constraints",
    "effort_level",
    "classroom_safety",
    "noise_level",
    "works_best_when",
}


REQUIRED_PREVIEW_KEYS = {"title", "action_text"}
REQUIRED_DETAILS_KEYS = {"objective", "steps", "time_required_min"}


def validate_solution(solution: Dict) -> None:
    missing = REQUIRED_TOP_LEVEL_KEYS - solution.keys()
    if missing:
        raise ValueError(
            f"Solution {solution.get('solution_id')} missing keys: {missing}"
        )

    preview = solution.get("preview", {})
    if not REQUIRED_PREVIEW_KEYS.issubset(preview.keys()):
        raise ValueError(
            f"Solution {solution['solution_id']} preview incomplete"
        )

    details = solution.get("details", {})
    if not REQUIRED_DETAILS_KEYS.issubset(details.keys()):
        raise ValueError(
            f"Solution {solution['solution_id']} details incomplete"
        )

    if not isinstance(details["steps"], list) or not details["steps"]:
        raise ValueError(
            f"Solution {solution['solution_id']} must have non-empty steps"
        )


def load_solutions() -> List[Dict]:
    """
    Loads and validates all solutions.
    Call once at app startup.
    """
    for sol in SOLUTION_LIBRARY:
        validate_solution(sol)

    return SOLUTION_LIBRARY
