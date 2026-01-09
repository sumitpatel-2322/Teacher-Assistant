from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
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
async def login_check(request: Request):
    form = await request.form()

    username = form.get("username")
    password = form.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM teachers WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()

    # Invalid username
    if user is None:
        return {"error": "Invalid username"}

    # Invalid password
    if user["password"] != password:
        return {"error": "Invalid username or password"}

    # SUCCESS → render loggedin.html
    return templates.TemplateResponse(
        "loggedin.html",
        {"request": request}
    )