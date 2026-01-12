from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates

from API_routes.auth import require_login
from decision_engine.logging import log_feedback
from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# =========================
# DASHBOARD (GET)
# =========================
@router.get("/teacher")
async def teacher_dashboard(
    request: Request,
    user=Depends(require_login)
):
    return templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "engine_output": None,
            "selected_class": None,
            "selected_subject": None,
            "selected_topic": None
        }
    )


# =========================
# ASK DOUBT (POST)
# =========================
@router.post("/teacher/ask")
async def ask_doubt(
    request: Request,
    class_name: str = Form(...),
    subject: str = Form(...),
    topic: str = Form(...),
    question: str = Form(...),
    user=Depends(require_login)
):
    # ----------------------------------
    # 1️⃣ Existing functionality (KEEP)
    # ----------------------------------
    store_raw_input(
        username=user["username"],
        role=user["role"],
        class_name=class_name.strip(),
        subject=subject.strip(),
        topic=topic.strip(),
        question=question.strip()
    )

    # ----------------------------------
    # 2️⃣ Structured input for engine
    # ----------------------------------
    engine_input = {
        "username": user["username"],
        "role": user["role"],
        "class": class_name.strip(),
        "subject": subject.strip(),
        "topic": topic.strip(),
        "question": question.strip()
    }
    raw_text = f"""
    Class: {class_name}
    Subject: {subject}
    Topic: {topic}
    Problem: {question}
    """
    # ----------------------------------
    # 3️⃣ Decision Engine call
    # ----------------------------------
    engine_output = process_teacher_query(raw_text)

    # ----------------------------------
    # 4️⃣ Render dashboard WITH state
    # ----------------------------------
    return templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "engine_output": engine_output,
            "selected_class": class_name,
            "selected_subject": subject,
            "selected_topic": topic
        }
    )


# =========================
# FEEDBACK (POST)
# =========================
@router.post("/teacher/feedback")
async def teacher_feedback(
    request: Request,
    user=Depends(require_login)
):
    """
    Receives teacher feedback for a specific decision engine request.
    Updates the correct log row using request_id.
    """

    data = await request.json()

    request_id = data.get("request_id")
    solution_id = data.get("solution_id")
    worked = data.get("worked")
    feedback = data.get("feedback", None)

    # -------------------------
    # Validation (STRICT)
    # -------------------------
    if not request_id:
        return {"success": False, "message": "request_id is required"}

    if not solution_id:
        return {"success": False, "message": "solution_id is required"}

    if worked is None or not isinstance(worked, bool):
        return {"success": False, "message": "worked must be boolean"}

    # -------------------------
    # Logging hook (CORE)
    # -------------------------
    log_feedback(
        request_id=request_id,
        solution_chosen=solution_id,
        worked=worked,
        feedback=feedback
    )

    return {
        "success": True,
        "message": "Feedback recorded successfully"
    }