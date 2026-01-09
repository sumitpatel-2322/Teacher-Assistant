from fastapi import APIRouter, Request,Depends
from API_routes.auth import require_login
from fastapi.templating import Jinja2Templates
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/teacher")
async def teacher_dashboard(request:Request,
                            user=Depends(require_login)):
    return templates.TemplateResponse("Teacher_dashboard.html",
                                      {"request":request,
                                       "user":user})