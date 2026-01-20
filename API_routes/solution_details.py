"""
API Route: Solution Details
---------------------------
Fetches detailed solution content after teacher selects a solution.
Now supports on-the-fly translation for detailed steps.
"""

from fastapi import APIRouter, Depends, Query
from API_routes.auth import require_login
from decision_engine.solution_service import get_solution_details

# ✅ NEW IMPORT: Reliable Translator
from deep_translator import GoogleTranslator

router = APIRouter()

@router.get("/solution/details/{solution_id}")
async def fetch_solution_details(
    solution_id: str,
    # ✅ Catch the ?lang=hi parameter
    lang: str = Query("en", description="Target language code (e.g., 'hi', 'te')"),
    user=Depends(require_login),
):
    """
    Returns detailed execution steps for a selected solution.
    If 'lang' is provided and not 'en', it translates the content.
    """

    # 1. Fetch original English details
    details = get_solution_details(solution_id)
    
    if not details:
        return {
            "success": False,
            "message": "Solution not found"
        }

    # 2. Translate if requested (and language is supported/valid)
    if lang and lang != 'en':
        try:
            # Initialize Translator
            translator = GoogleTranslator(source='auto', target=lang)
            
            # --- Translate 'Why It Works' (Pedagogy) ---
            if "pedagogy" in details and "why_it_works" in details["pedagogy"]:
                original_why = details["pedagogy"]["why_it_works"]
                if original_why:
                    details["pedagogy"]["why_it_works"] = translator.translate(original_why)

            # --- Translate 'Steps' (List of strings) ---
            # We handle the nested structure 'details' -> 'steps' or direct 'steps'
            steps_list = []
            if "details" in details and "steps" in details["details"]:
                steps_list = details["details"]["steps"]
            elif "steps" in details:
                steps_list = details["steps"]

            if steps_list and isinstance(steps_list, list):
                # Translate item by item (Safe & Reliable)
                translated_steps = [translator.translate(step) for step in steps_list]
                
                # Write back to the correct location
                if "details" in details and "steps" in details["details"]:
                    details["details"]["steps"] = translated_steps
                else:
                    details["steps"] = translated_steps
            
            # --- Translate 'Objective' ---
            if "details" in details and "objective" in details["details"]:
                obj = details["details"]["objective"]
                if obj:
                    details["details"]["objective"] = translator.translate(obj)

            # --- Translate Title/Action Text (for the Modal Header) ---
            if "preview" in details:
                if "title" in details["preview"]:
                    details["preview"]["title"] = translator.translate(details["preview"]["title"])
                if "action_text" in details["preview"]:
                    details["preview"]["action_text"] = translator.translate(details["preview"]["action_text"])

        except Exception as e:
            print(f"WARNING: Detail translation failed for {lang}: {e}")
            # Fail silently and return English rather than crashing

    return {
        "success": True,
        "data": details
    }