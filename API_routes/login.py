from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection

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

    # 🚫 Disable browser caching (VERY IMPORTANT)
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
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM teachers WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "User name does not exist!!"
            }
        )

    if user["password"] != password:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Incorrect Password!!"
            }
        )

    # ✅ Store session
    request.session["user"] = {
        "username": username,
        "role": role
    }

    return RedirectResponse(url="/dashboard", status_code=302)


# =========================
# LOGOUT
# =========================
@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=302)
