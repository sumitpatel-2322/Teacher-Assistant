from fastapi import APIRouter, Request, Depends, Body, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from Database.db import get_connection
from typing import Optional

# Ensure this import exists in your project structure
# If you haven't defined 'require_login' in API_routes/auth.py yet, 
# you can replace "user=Depends(require_login)" with manual session checking.
try:
    from API_routes.auth import require_login
except ImportError:
    # Fallback if auth.py is missing (Temporary fix for development)
    async def require_login(request: Request):
        user = request.session.get("user")
        if not user:
            return RedirectResponse(url="/login")
        return user

from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query
from decision_engine.logging import log_feedback

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# =========================
# 1. PAGE LOAD (Sync)
# =========================
@router.get("/teacher")
async def teacher_dashboard(request: Request, user=Depends(require_login)):
    
    # 1. Check if user is actually a teacher (Security)
    if isinstance(user, RedirectResponse): return user # Handle fallback redirect
    
    if user.get("role") != "teacher":
         return RedirectResponse(url="/login?error=Unauthorized")

    # 2. Fetch User Preferences using NEW Schema
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # UPDATED QUERY: Uses 'classes', 'subjects' and 'employee_id'
        # Note: user['username'] holds the employee_id from login.py
        cursor.execute(
            "SELECT classes, subjects FROM teachers WHERE employee_id = ?", 
            (user['username'],)
        )
        row = cursor.fetchone()
    except Exception as e:
        print(f"DB Error in Dashboard: {e}")
        row = None
    finally:
        conn.close()

    # 3. Pass data to template
    # The DB stores "Math, Science" as a string. We pass it directly.
    prefill = {
        "class": row["classes"] if row else "",     # Fixed column name
        "subject": row["subjects"] if row else ""   # Fixed column name
    }

    return templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "prefill": prefill 
        }
    )

# =========================
# 2. CHAT API (Async)
# =========================
@router.post("/api/teacher/ask")
async def ask_doubt_api(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    """
    Receives JSON payload from Chatbot JS.
    Returns JSON response with solutions.
    """
    if isinstance(user, RedirectResponse): return user
    
    # Extract data safely
    class_name = payload.get("class_name", "").strip()
    subject = payload.get("subject", "").strip()
    topic = payload.get("topic", "").strip()
    question = payload.get("question", "").strip()

    # 1. Store Raw Input (Logging)
    # Ensure 'store_raw_input' is updated to handle new schema if it touches DB
    store_raw_input(
        username=user["username"], # This is employee_id
        role=user["role"],
        class_name=class_name,
        subject=subject,
        topic=topic,
        question=question
    )

    # 2. Process with Engine
    raw_text = f"Class: {class_name}\nSubject: {subject}\nTopic: {topic}\nProblem: {question}"
    engine_output = process_teacher_query(raw_text)

    # 3. Return JSON structure for Frontend
    response_data = {
        "status": "success",
        "request_id": engine_output["request_id"],
        "solutions": [
            {
                "id": s["solution_id"], 
                "text": s["text"], 
                "confidence": s["confidence"]
            } 
            for s in engine_output["ranked_solutions"]
        ]
    }
    
    return JSONResponse(content=response_data)


# =========================
# 3. FEEDBACK API (Async)
# =========================
@router.post("/teacher/feedback")
async def teacher_feedback(
    request: Request,
    user=Depends(require_login)
):
    if isinstance(user, RedirectResponse): return user

    data = await request.json()

    log_feedback(
        request_id=data.get("request_id"),
        solution_chosen=data.get("solution_id"),
        worked=data.get("worked"),
        feedback=data.get("feedback")
    )

    return {"success": True}