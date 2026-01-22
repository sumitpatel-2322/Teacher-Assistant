from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/dashboard")
def dashboard(request: Request):
    if "user" not in request.session:
        return RedirectResponse(url="/login", status_code=302)

    role = request.session["user"]["role"]

    # ✅ Role-based redirect
    if role == "teacher":
        return RedirectResponse(url="/teacher", status_code=302)
    elif role == "crp":
        return RedirectResponse(url="/crp", status_code=302)
    elif role == "brp":
        return RedirectResponse(url="/brp", status_code=302)
    elif role == "arp":
        return RedirectResponse(url="/arp", status_code=302)
    return RedirectResponse(url="/login", status_code=302)
