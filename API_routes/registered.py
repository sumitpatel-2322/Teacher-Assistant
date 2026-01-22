from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database.db import get_connection
import re

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/register")
async def registered(request: Request):
    form = await request.form()

    id = form.get("teacher_id")
    role = form.get("role")
    name = form.get("name")
    school_name = form.get("school_name")
    username = form.get("username")
    password = form.get("password")
    confirm_password = form.get("confirm_password")

    # -------------------------
    # BASIC VALIDATIONS
    # -------------------------
    if not username or not password:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "All fields are required"}
        )

    if password != confirm_password:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Passwords do not match"}
        )

    # -------------------------
    # PASSWORD STRENGTH CHECK
    # -------------------------
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if not re.match(pattern, password):
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": (
                    "Password must contain at least 8 characters, "
                    "one uppercase letter, one lowercase letter, "
                    "one digit, and one special character."
                )
            }
        )

    conn = get_connection()
    cursor = conn.cursor()

    # -------------------------
    # CHECK USERNAME EXISTS
    # -------------------------
    cursor.execute(
        "SELECT 1 FROM teachers WHERE username = ?",
        (username,)
    )

    if cursor.fetchone():
        conn.close()
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Username already exists"}
        )

    # -------------------------
    # INSERT NEW USER
    # -------------------------
    cursor.execute(
        "INSERT INTO teachers (id, name, role, school_name, username, password) VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, role, school_name, username, password)
    )

    conn.commit()
    conn.close()

    return RedirectResponse(
        "/login",
        status_code=302
    )
