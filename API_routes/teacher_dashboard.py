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
# ==========================================
@router.get("/teacher")
async def teacher_dashboard(request: Request, user=Depends(require_login)):
    
    # 1. Security: Role Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "teacher":
         return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    # Use Row factory to allow accessing columns by name
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # 2. Fetch User Details
    cursor.execute(
        "SELECT school_udise, classes, subjects FROM teachers WHERE employee_id = ?", 
        (user['username'],)
    )
    teacher_data = cursor.fetchone()
    
    prefill = {"class": "", "subject": ""}
    school_id = ""

    if teacher_data:
        prefill["class"] = teacher_data.get("classes", "")
        prefill["subject"] = teacher_data.get("subjects", "")
        school_id = (teacher_data.get("school_udise") or "").strip()

    # 3. Fetch Notices & Visits
    notices = []
    if school_id:
        # Guidance
        cursor.execute("SELECT * FROM guidance WHERE school_id = ? ORDER BY created_at DESC", (school_id,))
        for g in cursor.fetchall():
            notices.append({
                "type": "Guidance",
                "title": g["title"],
                "content": g["description"],
                "date": g["created_at"]
            })

        # Visits
        cursor.execute("SELECT * FROM visits WHERE school_id = ? ORDER BY visit_date ASC", (school_id,))
        for v in cursor.fetchall():
            notices.append({
                "type": "Visit",
                "title": "CRP Visit Scheduled",
                "content": f"Date: {v['visit_date']} at {v['visit_time']}",
                "date": v['created_at']
            })

    conn.close()

    # 4. Render Template with NO-CACHE Headers
    # This prevents the browser from storing the page, so 'Back' button forces a reload.
    response = templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "prefill": prefill,
            "notices": notices
        }
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response


# ==========================================
# 2. CHAT API (POST)
# ==========================================
@router.post("/api/teacher/ask")
async def ask_doubt_api(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    if isinstance(user, RedirectResponse): return user
    
    # Extract data safely
    class_name = payload.get("class_name", "").strip()
    subject = payload.get("subject", "").strip()
    topic = payload.get("topic", "").strip()
    question = payload.get("question", "").strip()

    # Store Raw Input
    store_raw_input(
        username=user["username"], 
        role=user["role"],
        class_name=class_name,
        subject=subject,
        topic=topic,
        question=question
    )

    # Process with Decision Engine
    raw_text = f"Class: {class_name}\nSubject: {subject}\nTopic: {topic}\nProblem: {question}"
    engine_output = process_teacher_query(raw_text)

    # Return JSON
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