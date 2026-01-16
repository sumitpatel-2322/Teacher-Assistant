"""
Solution Loader & Validator
---------------------------
Loads the solution library into memory and validates
basic structural integrity at startup.

Supported Sources:
1. solutions.py (Manual)
2. reddit_based_solutions.py (Scraped/Generated)
3. behavior_solutions.py (New Behavioral Strategies)
"""

from typing import List, Dict
from solutions.solutions import SOLUTION_LIBRARY as MANUAL_SOLUTIONS

# ✅ 1. Try to import Reddit Solutions
try:
    from solutions.reddit_based_solutions import REDDIT_SOLUTIONS
except ImportError:
    print("⚠️ WARNING: Could not load reddit_based_solutions.py. Using empty list.")
    REDDIT_SOLUTIONS = []
except AttributeError:
    print("⚠️ WARNING: reddit_based_solutions.py found but REDDIT_SOLUTIONS list is missing.")
    REDDIT_SOLUTIONS = []

# ✅ 2. Try to import Behavior Solutions
try:
    from solutions.behavior_solutions import BEHAVIOR_SOLUTIONS
except ImportError:
    # It's okay if this doesn't exist yet, just warn
    print("⚠️ WARNING: Could not load behavior_solutions.py. Using empty list.")
    BEHAVIOR_SOLUTIONS = []
except AttributeError:
    print("⚠️ WARNING: behavior_solutions.py found but BEHAVIOR_SOLUTIONS list is missing.")
    BEHAVIOR_SOLUTIONS = []

# Validation Keys
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
}

REQUIRED_PREVIEW_KEYS = {"title", "action_text"}
REQUIRED_DETAILS_KEYS = {"objective", "steps", "time_required_min"}


def validate_solution(solution: Dict) -> None:
    """
    Checks if a solution dictionary has all required keys.
    """
    missing = REQUIRED_TOP_LEVEL_KEYS - solution.keys()
    if missing:
        # We warn but don't stop execution, to be forgiving during development
        print(f"⚠️ Validation Warning: Solution '{solution.get('solution_id', '???')}' missing keys: {missing}")

    preview = solution.get("preview", {})
    if not REQUIRED_PREVIEW_KEYS.issubset(preview.keys()):
        print(f"❌ Invalid Preview in: {solution.get('solution_id')}")

    details = solution.get("details", {})
    if not REQUIRED_DETAILS_KEYS.issubset(details.keys()):
        print(f"❌ Invalid Details in: {solution.get('solution_id')}")


def load_solutions() -> List[Dict]:
    """
    Loads, merges, and validates all solutions from all sources.
    Returns a single combined list of solution dictionaries.
    """
    # 1. Merge Libraries
    combined_library = MANUAL_SOLUTIONS + REDDIT_SOLUTIONS + BEHAVIOR_SOLUTIONS
    
    print("-" * 50)
    print(f">>> LOADER REPORT:")
    print(f"   - Manual Solutions:   {len(MANUAL_SOLUTIONS)}")
    print(f"   - Reddit Solutions:   {len(REDDIT_SOLUTIONS)}")
    print(f"   - Behavior Solutions: {len(BEHAVIOR_SOLUTIONS)}")
    print(f"   - TOTAL LOADED:       {len(combined_library)}")
    print("-" * 50)

    # 2. Validate
    valid_solutions = []
    for sol in combined_library:
        try:
            validate_solution(sol)
            valid_solutions.append(sol)
        except Exception as e:
            print(f"Skipping invalid solution {sol.get('solution_id', 'unknown')}: {e}")

    return valid_solutions