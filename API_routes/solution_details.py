"""
API Route: Solution Details
---------------------------
Fetches detailed solution content after teacher selects a solution.
"""

from fastapi import APIRouter, Depends
from API_routes.auth import require_login
from decision_engine.solution_service import get_solution_details

router = APIRouter()


@router.get("/solution/details/{solution_id}")
async def fetch_solution_details(
    solution_id: str,
    user=Depends(require_login),
):
    """
    Returns detailed execution steps for a selected solution.
    """

    details = get_solution_details(solution_id)
    if not details:
        return {
            "success": False,
            "message": "Solution not found"
        }

    return {
        "success": True,
        "data": details
    }
