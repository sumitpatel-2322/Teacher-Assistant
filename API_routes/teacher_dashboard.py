from fastapi import APIRouter, Request,Depends,Form
from decision_engine.raw_text.store import store_raw_input
from fastapi.responses import RedirectResponse
from API_routes.auth import require_login
from fastapi.templating import Jinja2Templates
from decision_engine.engine import process_input
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.get("/teacher")
async def teacher_dashboard(request:Request,
                            user=Depends(require_login)):
    return templates.TemplateResponse("Teacher_dashboard.html",
                                      {"request":request,
                                       "user":user})
@router.post("/teacher/ask")
def ask_doubt(
    request:Request,
    class_name:str=Form(...),
    subject:str=Form(...),
    topic:str=Form(...),
    question:str=Form(...),
    user=Depends(require_login)
):
    store_raw_input(
        username=user["username"],
        role=user["role"],
        class_name=class_name.strip(),
        subject=subject.strip(),
        topic=topic.strip(),
        question=question.strip()
    )
    raw_input={
        "class":class_name,
        "subject":subject,
        "topic":topic,
        "question":question
    }
    engine_output=process_input(raw_input)
    print("ENGINE OUTPUT >>>>",engine_output)
    return RedirectResponse(
        url="/teacher",
        status_code=302
    )