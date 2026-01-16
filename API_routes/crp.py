from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates 
from API_routes.auth import require_login
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/crp")
def crp(request:Request,
        user=Depends(require_login)):
    return templates.TemplateResponse("CRP.html",
    {
        "request":request,
        "user": user
    })