from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Show login page
@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

# Handle login form submission (AUTH CHECK)
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
                "request":request,
                "error":"User name does not exist!!"
            }
        )
    if user["password"]!= password:
        return templates.TemplateResponse(
            "login.html",
            {
                "request":request,
                "error":"Incorrect Password!!"
            }
        )

    # ✅ FIXED SESSION STORAGE
    request.session["user"] = {
        "username": username,
        "role": role
    }

    return RedirectResponse(
        url="/dashboard",
        status_code=302
    )

@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return templates.TemplateResponse(
        "logout.html",
        {
            "request":request
        }
    )
