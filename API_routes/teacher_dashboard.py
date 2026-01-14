from fastapi import APIRouter, Request, Depends, Body, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from Database.db import get_connection
from typing import Optional

from API_routes.auth import require_login
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
    
    # Fetch User Preferences for Pre-fill
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT preferred_class, preferred_subject FROM teachers WHERE username = ?", (user['username'],))
    row = cursor.fetchone()
    conn.close()

    # Pass preferences to template
    prefill = {
        "class": row["preferred_class"] if row else "",
        "subject": row["preferred_subject"] if row else ""
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
    
    # Extract data safely
    class_name = payload.get("class_name", "").strip()
    subject = payload.get("subject", "").strip()
    topic = payload.get("topic", "").strip()
    question = payload.get("question", "").strip()

    # 1. Store Raw Input (Logging)
    store_raw_input(
        username=user["username"],
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
    # ✅ FIX: Use dictionary access ["key"] instead of .key
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
    data = await request.json()

    log_feedback(
        request_id=data.get("request_id"),
        solution_chosen=data.get("solution_id"),
        worked=data.get("worked"),
        feedback=data.get("feedback")
    )

    return {"success": True}