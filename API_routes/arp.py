from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates 
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/arp")
def arp(request:Request):
    return templates.TemplateResponse("ARP.html",{
        "request":request
    })
