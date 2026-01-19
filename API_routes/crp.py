from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
from API_routes.auth import require_login
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/crp")
def crp(request: Request, user=Depends(require_login)):
    
    # 1. Security: Role Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "crp":
        return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # Fetch distinct schools so the CRP can select one
    cursor.execute("SELECT DISTINCT school_udise FROM teachers")
    schools = [row["school_udise"] for row in cursor.fetchall()]
    
    conn.close()

    # 2. Render with NO-CACHE Headers
    response = templates.TemplateResponse("CRP.html", {
        "request": request,
        "user": user,
        "schools": schools 
    })
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

# --- HANDLE GUIDANCE UPLOAD ---
@router.post("/crp/upload-guidance")
async def upload_guidance(
    request: Request,
    school_id: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO guidance (crp_id, school_id, title, description)
        VALUES (?, ?, ?, ?)
    """, (user['username'], school_id, title, description))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/crp?success=GuidanceUploaded", status_code=303)

# --- HANDLE SCHEDULE VISIT ---
@router.post("/crp/schedule-visit")
async def schedule_visit(
    request: Request,
    school_id: str = Form(...),
    visit_date: str = Form(...),
    visit_time: str = Form(...),
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO visits (crp_id, school_id, visit_date, visit_time)
        VALUES (?, ?, ?, ?)
    """, (user['username'], school_id, visit_date, visit_time))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/crp?success=VisitScheduled", status_code=303)