# FILE: Teacher-Assistant/solutions/__init__.py

from .behavior_solutions import BEHAVIOR_SOLUTIONS
from .reddit_based_solutions import REDDIT_SOLUTIONS
from .fln_solutions import FLN_SOLUTIONS
from .science_solutions import SCIENCE_SOLUTIONS
from .management_solutions import MANAGEMENT_SOLUTIONS
from .wellbeing_solutions import WELLBEING_SOLUTIONS
from .inclusive_solutions import INCLUSIVE_SOLUTIONS
from .productivity_solutions import PRODUCTIVITY_SOLUTIONS
from .solutions import SOLUTIONS as GENERAL_SOLUTIONS
try:
    from .solutions import SOLUTION_LIBRARY as MANUAL_SOLUTIONS
except ImportError:
    MANUAL_SOLUTIONS = []
# Combine all lists into one master repository
SOLUTIONS = (
    BEHAVIOR_SOLUTIONS +
    REDDIT_SOLUTIONS +
    FLN_SOLUTIONS +
    SCIENCE_SOLUTIONS +
    MANAGEMENT_SOLUTIONS +
    WELLBEING_SOLUTIONS +
    INCLUSIVE_SOLUTIONS +
    PRODUCTIVITY_SOLUTIONS +
    GENERAL_SOLUTIONS   
)

__all__ = ["SOLUTIONS"]