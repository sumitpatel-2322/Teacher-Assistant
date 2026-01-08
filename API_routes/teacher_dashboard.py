from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates 
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/teacher")
def teacher_dashboard(request:Request):
    return templates.TemplateResponse("Teacher_dashboard.html",
                                      {"request":request})