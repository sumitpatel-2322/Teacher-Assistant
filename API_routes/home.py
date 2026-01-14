from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    user = request.session.get("user")  # ✅ get logged-in user (or None)

    return templates.TemplateResponse(
        "Home_page.html",
        {
            "request": request,
            "user": user   # ✅ pass to HTML
        }
    )
