from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

try:
    from API_routes.auth import require_login
except ImportError:
    async def require_login(request: Request):
        user = request.session.get("user")
        if not user:
            return RedirectResponse(url="/login")
        return user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/micro_add")
async def micro_add_page(request: Request, user=Depends(require_login)):

    if isinstance(user, RedirectResponse):
        return user

    # Optional: restrict to ARP / teacher
    if user.get("role") not in ["arp", "teacher"]:
        return RedirectResponse(url="/dashboard")

    return templates.TemplateResponse(
        "micro_add.html",
        {"request": request, "user": user}
    )
