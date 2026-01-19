from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/profile")
async def view_profile(request: Request):
    # 1. Check Session
    user_session = request.session.get("user")
    if not user_session:
        return RedirectResponse(url="/login")

    role = user_session["role"]
    employee_id = user_session["username"] # This holds the ID (e.g., T-101)

    conn = get_connection()
    cursor = conn.cursor()
    user_data = None

    try:
        # 2. Fetch Data based on Role
        if role == "teacher":
            cursor.execute("SELECT * FROM teachers WHERE employee_id = ?", (employee_id,))
        elif role == "crp":
            cursor.execute("SELECT * FROM crps WHERE employee_id = ?", (employee_id,))
        elif role == "brp":
            cursor.execute("SELECT * FROM brps WHERE employee_id = ?", (employee_id,))
        elif role == "arp":
            cursor.execute("SELECT * FROM arps WHERE employee_id = ?", (employee_id,))
        
        user_data = cursor.fetchone()

    except Exception as e:
        print(f"Profile Error: {e}")
    finally:
        conn.close()

    if not user_data:
        return RedirectResponse(url="/login?error=ProfileNotFound")

    # 3. Render Profile Page
    # We pass 'user_data' which contains the full DB row (name, email, etc.)
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "user": user_session,     # Session info
        "profile": user_data,     # Full DB details
        "role": role.upper()
    })