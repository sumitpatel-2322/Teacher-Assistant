from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Database.db import get_connection

# Import Auth
try:
    from API_routes.auth import require_login
except ImportError:
    # Fallback if auth not ready
    async def require_login(request: Request):
        return request.session.get("user")

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# COMMUNITY / MICRO-LEARNING FEED
# ==========================================
@router.get("/micro")
def microlearn_page(request: Request, user=Depends(require_login)):

    # 1. Security Check
    if isinstance(user, RedirectResponse):
        return user

    # We allow all roles (Teacher, ARP, CRP, BRP) to view the community feed.
    # If you strictly want only teachers, you can uncomment this:
    # if user.get("role") != "teacher":
    #     return RedirectResponse(url="/dashboard")

    # 2. Fetch Content from DB
    conn = get_connection()
    # Row factory allows accessing columns by name (row['title'])
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # Fetch all uploads, newest first
    cursor.execute("SELECT * FROM microlearning ORDER BY created_at DESC")
    contents = cursor.fetchall()
    
    conn.close()

    # 3. Render Template
    return templates.TemplateResponse(
        "micro.html",
        {
            "request": request, 
            "user": user,
            "contents": contents
        }
    )