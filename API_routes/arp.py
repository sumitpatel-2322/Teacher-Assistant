from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
from API_routes.auth import require_login

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/arp")
def arp(request: Request, user=Depends(require_login)):
    
    # 1. Security Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "arp":
        return RedirectResponse(url="/login?error=Unauthorized")

    # 2. Render with NO-CACHE Headers
    response = templates.TemplateResponse(
        "ARP.html",
        {
            "request": request,
            "user": user
        }
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response