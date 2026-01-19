from fastapi import APIRouter, Request, Depends, Body, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from Database.db import get_connection
from typing import Optional

# Authentication Dependency
try:
    from API_routes.auth import require_login
except ImportError:
    # Fallback if auth.py is missing
    async def require_login(request: Request):
        user = request.session.get("user")
        if not user:
            return RedirectResponse(url="/login")
        return user

# Decision Engine Imports
from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query
from decision_engine.logging import log_feedback

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. TEACHER DASHBOARD (GET)
# Fetches User Info, School Context, Notices, & Visits
# ==========================================
@router.get("/teacher")
async def teacher_dashboard(request: Request, user=Depends(require_login)):
    
    # Security: Ensure only teachers access this
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "teacher":
         return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    cursor = conn.cursor()
    
    # ---------------------------------------------------------
    # A. Fetch Teacher Details (School & Preferences)
    # ---------------------------------------------------------
    # We need the 'school_udise' to find relevant notices/visits
    cursor.execute(
        "SELECT school_udise, classes, subjects FROM teachers WHERE employee_id = ?", 
        (user['username'],)
    )
    teacher_data = cursor.fetchone()
    
    prefill = {"class": "", "subject": ""}
    school_id = ""

    if teacher_data:
        prefill["class"] = teacher_data["classes"]
        prefill["subject"] = teacher_data["subjects"]
        school_id = teacher_data["school_udise"] # This links Teacher -> School

    # ---------------------------------------------------------
    # B. Fetch Notices & Visits for this School
    # ---------------------------------------------------------
    notices = []
    
    if school_id:
        # 1. Get Guidance Notices (Uploaded by CRP for this School)
        cursor.execute("SELECT * FROM guidance WHERE school_id = ? ORDER BY created_at DESC", (school_id,))
        guidance_list = cursor.fetchall()
        
        for g in guidance_list:
            notices.append({
                "type": "Guidance",
                "title": g["title"],
                "content": g["description"],
                "date": g["created_at"]
            })

        # 2. Get Scheduled Visits (Scheduled by CRP for this School)
        cursor.execute("SELECT * FROM visits WHERE school_id = ? ORDER BY visit_date ASC", (school_id,))
        visit_list = cursor.fetchall()
        
        for v in visit_list:
            notices.append({
                "type": "Visit",
                "title": "CRP Visit Scheduled",
                "content": f"Date: {v['visit_date']} at {v['visit_time']}",
                "date": v['created_at']
            })

    conn.close()

    # ---------------------------------------------------------
    # C. Render Template
    # ---------------------------------------------------------
    return templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "prefill": prefill,
            "notices": notices  # Pass the combined list to the UI
        }
    )


# ==========================================
# 2. CHAT API (POST)
# Handles AI Queries from the Chat Interface
# ==========================================
@router.post("/api/teacher/ask")
async def ask_doubt_api(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    """
    Receives JSON payload from Chatbot JS.
    Returns JSON response with ranked solutions.
    """
    if isinstance(user, RedirectResponse): return user
    
    # Extract data safely
    class_name = payload.get("class_name", "").strip()
    subject = payload.get("subject", "").strip()
    topic = payload.get("topic", "").strip()
    question = payload.get("question", "").strip()

    # 1. Store Raw Input (For Analytics/Logging)
    store_raw_input(
        username=user["username"], # This is the employee_id
        role=user["role"],
        class_name=class_name,
        subject=subject,
        topic=topic,
        question=question
    )

    # 2. Process with Decision Engine
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


# ==========================================
# 3. FEEDBACK API (POST)
# Handles Thumbs Up/Down or Written Feedback
# ==========================================
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