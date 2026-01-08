from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates 
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/brp")
def brp(request:Request):
    return templates.TemplateResponse("BRP.html",{
        "request":request
    })
