from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates 
from Database.db import get_connection
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/register")
def register(request:Request):
    return templates.TemplateResponse("register.html",{
        "request":request
    })
