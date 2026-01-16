from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection
import hashlib

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# =========================
# SHOW LOGIN PAGE
# =========================
@router.get("/login")
def login(request: Request):

    # 🔒 If already logged in → block login page
    if "user" in request.session:
        return RedirectResponse(url="/dashboard", status_code=302)

    response = templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

    # 🚫 Disable browser caching
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


# =========================
# HANDLE LOGIN
# =========================
@router.post("/login")
async def login_check(
    request: Request,
    username: str = Form(...), # User enters ID or Email here
    password: str = Form(...),
    role: str = Form(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    # 1. DETERMINE TABLE BASED ON ROLE
    # We map the dropdown values to the correct Database Table
    role_table_map = {
        "teacher": "teachers",
        "crp": "crps",
        "brp": "brps",
        "arp": "arps"
    }
    
    table_name = role_table_map.get(role)
    
    if not table_name:
        return templates.TemplateResponse("login.html", {
            "request": request, "error": "Invalid Role Selected"
        })

    # 2. HASH THE PASSWORD (To match registration)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # 3. QUERY THE CORRECT TABLE
    # We check if 'username' input matches either 'employee_id' OR 'email'
    try:
        cursor.execute(
            f"SELECT * FROM {table_name} WHERE employee_id = ? OR email = ?",
            (username, username)
        )
        user = cursor.fetchone()
    except Exception as e:
        print(f"Login Error: {e}")
        return templates.TemplateResponse("login.html", {
            "request": request, "error": "Database Error or Table missing."
        })
    finally:
        conn.close()

    # 4. VALIDATE USER
    if user is None:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": f"User ID not found in {role.upper()} database!"
            }
        )

    # 5. VALIDATE PASSWORD
    # 'user' is a Row object, accessing columns by name
    stored_password = user["password"]

    if stored_password != hashed_password:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Incorrect Password!!"
            }
        )

    # ✅ 6. SUCCESS - STORE SESSION
    request.session["user"] = {
        "id": user["id"],
        "name": user["name"],
        "username": user["employee_id"], # Store their ID for reference
        "role": role,
        # Store jurisdiction info for dashboard logic later
        "school_udise": user["school_udise"] if role == "teacher" else None,
        "assigned_area": user["assigned_cluster"] if role == "crp" else (user["assigned_block"] if role in ["brp", "arp"] else None)
    }

    # Redirect to Dashboard (Ensure you have a /dashboard route!)
    return RedirectResponse(url="/dashboard", status_code=303)


# =========================
# LOGOUT
# =========================
@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)