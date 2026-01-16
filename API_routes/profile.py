from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection
from API_routes.auth import require_login

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# =========================
# GET: Show Profile Page
# =========================
@router.get("/profile")
def show_profile(request: Request, user=Depends(require_login)):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Fetch latest data for this user
    cursor.execute("SELECT * FROM teachers WHERE username = ?", (user['username'],))
    teacher_data = cursor.fetchone()
    conn.close()

    return templates.TemplateResponse(
        "profile.html", 
        {
            "request": request, 
            "user": user, 
            "data": teacher_data
        }
    )

# =========================
# POST: Update Preferences
# =========================
# API_routes/profile.py

@router.post("/profile/update")
def update_profile(
    request: Request,
    class_name: str = Form(...),
    subject: str = Form(...),
    language: str = Form("en"),  # 👈 NEW FIELD
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Update preferences including language
    cursor.execute("""
        UPDATE teachers 
        SET preferred_class = ?, preferred_subject = ?, preferred_language = ? 
        WHERE username = ?
    """, (class_name, subject, language, user['username']))
    
    conn.commit()
    conn.close()
    
    return RedirectResponse(url="/teacher", status_code=303)