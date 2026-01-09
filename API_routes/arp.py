from fastapi import APIRouter, Request,Depends
from fastapi.templating import Jinja2Templates 
from API_routes.auth import require_login
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/arp")
def arp(
    request: Request,
    user=Depends(require_login)
):
    return templates.TemplateResponse(
        "ARP.html",
        {
            "request": request,
            "user": user
        }
    )
