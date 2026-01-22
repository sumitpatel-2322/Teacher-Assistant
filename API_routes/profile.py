from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. VIEW PROFILE (GET)
# ==========================================
@router.get("/profile")
async def view_profile(request: Request):
    # Check Session
    user_session = request.session.get("user")
    if not user_session:
        return RedirectResponse(url="/login")

    role = user_session["role"]
    employee_id = user_session["username"]

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    user_data = None
    
    try:
        # Fetch Data based on Role
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

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "user": user_session,
        "profile": user_data,
        "role": role.upper()
    })


# ==========================================
# 2. UPDATE PROFILE (POST)
# ==========================================
@router.post("/profile/update")
async def update_profile(
    request: Request,
    # Common Fields
    name: str = Form(...),
    
    # Teacher Specific
    preferred_language: str = Form(None),
    subjects: str = Form(None),
    classes: str = Form(None),
    
    # Admin Specific
    domain: str = Form(None),
    specialization: str = Form(None) 
):
    user_session = request.session.get("user")
    if not user_session:
        return RedirectResponse(url="/login")

    role = user_session["role"]
    employee_id = user_session["username"]
    
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if role == "teacher":
            cursor.execute("""
                UPDATE teachers 
                SET name = ?, preferred_language = ?, subjects = ?, classes = ?
                WHERE employee_id = ?
            """, (name, preferred_language, subjects, classes, employee_id))
            
        elif role == "crp":
            cursor.execute("""
                UPDATE crps 
                SET name = ?, domain = ?
                WHERE employee_id = ?
            """, (name, domain, employee_id))
            
        elif role == "brp":
            cursor.execute("""
                UPDATE brps 
                SET name = ?, domain = ?
                WHERE employee_id = ?
            """, (name, domain, employee_id))
            
        elif role == "arp":
            cursor.execute("""
                UPDATE arps 
                SET name = ?, specialization = ?
                WHERE employee_id = ?
            """, (name, specialization, employee_id))
        
        conn.commit()
        
        # Update Session Name if changed
        user_session["name"] = name
        request.session["user"] = user_session
        
        return RedirectResponse(url="/profile?success=Updated", status_code=303)

    except Exception as e:
        print(f"Update Error: {e}")
        return RedirectResponse(url="/profile?error=UpdateFailed", status_code=303)
    finally:
        conn.close()