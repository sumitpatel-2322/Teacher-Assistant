from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates 
from Database.db import get_connection
router=APIRouter()
templates=Jinja2Templates(directory="templates")
@router.post("/registered")
async def registered(request:Request):
    form= await request.form()
    
    username=form.get("username")
    password=form.get("password")
    confirm_password=form.get("confirm_password")
    if (not username or not password):
        return {"error":"All fields are required"}
    if (password!=confirm_password):
        return {"error":"Passwords do not match"}
    
    conn=get_connection()
    cursor=conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO teachers(username,password) VALUES(?,?)",(username,password)
        )
        conn.commit()
    except Exception:
        conn.close()
        return {"error": "Username already exists"}
    conn.close()
    return templates.TemplateResponse("registered.html",{
        "request":request})
