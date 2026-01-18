"""
solution_loader.py
------------------
SAFE priority-aware solution loader.

IMPORTANT:
- Returns a FLAT LIST (engine contract unchanged)
- Internally reorders solutions by intent priority
- Normalizes instructional solutions to match engine's 'situations' expectation
"""

# ----------------------------
# Existing solution libraries
# ----------------------------

from solutions.solutions import SOLUTIONS  # MAIN SOLUTIONS LIBRARY
from solutions.behavior_solutions import BEHAVIOR_SOLUTIONS
from solutions.management_solutions import MANAGEMENT_SOLUTIONS
from solutions.wellbeing_solutions import WELLBEING_SOLUTIONS
from solutions.productivity_solutions import PRODUCTIVITY_SOLUTIONS
from solutions.inclusive_solutions import INCLUSIVE_SOLUTIONS
from solutions.fln_solutions import FLN_SOLUTIONS
from solutions.reddit_based_solutions import REDDIT_SOLUTIONS
from solutions.science_solutions import SCIENCE_SOLUTIONS

# ----------------------------
# Instructional libraries
# ----------------------------

from instructional_concept_library.math.solutions import MATH_INSTRUCTIONAL_SOLUTIONS
from instructional_concept_library.science.solutions import SCIENCE_INSTRUCTIONAL_SOLUTIONS
from instructional_concept_library.language.solutions import LANGUAGE_INSTRUCTIONAL_SOLUTIONS
from instructional_concept_library.social_studies.solutions import SOCIAL_STUDIES_INSTRUCTIONAL_SOLUTIONS


def _is_diagnostic(solution: dict) -> bool:
    return solution.get("instruction_type") == "DIAGNOSTIC"

def _normalize_instructional_solution(sol: dict) -> dict:
    """
    Injects 'situations' key into instructional solutions 
    so the Engine can score them correctly.
    """
    # Create situations list if missing
    if "situations" not in sol:
        sol["situations"] = []
    
    # 1. Map 'student_profile' (e.g., CONCEPT_CONFUSION) to situations
    if "student_profile" in sol:
        sol["situations"].extend(sol["student_profile"])
        
    # 2. Map 'topic' (e.g., GEOMETRY_2D_3D) to situations
    # This allows the engine to match specific topics detected in text
    if "topic" in sol:
        sol["situations"].append(sol["topic"])
        
    return sol

def load_solutions():
    """
    Returns a SINGLE flat list of solutions,
    ordered by priority to guide the engine naturally.

    Priority order:
    1. Instructional (subject-specific)
    2. Diagnostic (subject-specific)
    3. Behavioral / Management
    4. Wellbeing
    5. Other support solutions
    """

    instructional = []
    diagnostic = []
    behavioral = []
    wellbeing = []
    other = []

    # --------------------------------------------------
    # Instructional Concept Libraries (HIGH PRIORITY)
    # --------------------------------------------------
    
    # Helper to process and sort into lists
    def process_lib(library):
        for sol in library:
            # Normalize first!
            norm_sol = _normalize_instructional_solution(sol)
            if _is_diagnostic(norm_sol):
                diagnostic.append(norm_sol)
            else:
                instructional.append(norm_sol)

    process_lib(MATH_INSTRUCTIONAL_SOLUTIONS)
    process_lib(SCIENCE_INSTRUCTIONAL_SOLUTIONS)
    process_lib(LANGUAGE_INSTRUCTIONAL_SOLUTIONS)
    process_lib(SOCIAL_STUDIES_INSTRUCTIONAL_SOLUTIONS)

    # --------------------------------------------------
    # Behavioral / Management (MID PRIORITY)
    # --------------------------------------------------

    behavioral.extend(BEHAVIOR_SOLUTIONS)
    behavioral.extend(MANAGEMENT_SOLUTIONS)

    # --------------------------------------------------
    # Wellbeing (LOW PRIORITY)
    # --------------------------------------------------

    wellbeing.extend(WELLBEING_SOLUTIONS)

    # --------------------------------------------------
    # Other Supporting Libraries (LOWEST PRIORITY)
    # --------------------------------------------------

    other.extend(SOLUTIONS)  # MAIN SOLUTIONS LIBRARY
    other.extend(PRODUCTIVITY_SOLUTIONS)
    other.extend(INCLUSIVE_SOLUTIONS)
    other.extend(FLN_SOLUTIONS)
    other.extend(REDDIT_SOLUTIONS)
    other.extend(SCIENCE_SOLUTIONS)

    # --------------------------------------------------
    # FINAL MERGED LIST (FLAT, ORDERED)
    # --------------------------------------------------

    return (
        instructional
        + diagnostic
        + behavioral
        + wellbeing
        + other
    )