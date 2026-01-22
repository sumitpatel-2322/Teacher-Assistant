from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Database.db import get_connection
import shutil
import os
import uuid

# Import Auth
try:
    from API_routes.auth import require_login
except ImportError:
    # Fallback if auth not ready
    async def require_login(request: Request):
        return request.session.get("user")

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. GET PAGE (Render the Form)
# ==========================================
@router.get("/micro_add")
def micro_add_page(request: Request, user=Depends(require_login)):

    if isinstance(user, RedirectResponse):
        return user

    # Restrict to allowed roles (ARP, Teacher, BRP, CRP)
    # You can adjust this list based on who should be allowed to upload
    if user.get("role") not in ["arp", "teacher", "brp", "crp"]:
        return RedirectResponse(url="/dashboard")

    return templates.TemplateResponse(
        "micro_add.html",
        {"request": request, "user": user}
    )

# ==========================================
# 2. POST ACTION (Handle Upload)
# ==========================================
@router.post("/micro_add")
def micro_add_submit(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    class_level: str = Form(..., alias="class"), # 'class' is a reserved keyword in Python
    subject: str = Form(...),
    content_type: str = Form(...),
    duration: str = Form(...),
    file: UploadFile = File(...),
    user=Depends(require_login)
):
    if isinstance(user, RedirectResponse):
        return user

    # 1. SETUP UPLOAD DIRECTORY
    # We save to 'static/micro_uploads' so they are accessible via URL
    UPLOAD_DIR = "static/micro_uploads"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # 2. SAVE FILE
    # Generate unique name to prevent collisions (e.g. math.pdf -> 550e8400...pdf)
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_location = f"{UPLOAD_DIR}/{unique_filename}"
    
    # Write file to disk
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3. SAVE TO DATABASE
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO microlearning 
        (title, description, class_level, subject, content_type, duration, file_path, uploaded_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        title, 
        description, 
        class_level, 
        subject, 
        content_type, 
        duration, 
        f"/{file_location}", # Store web-accessible path (e.g. /static/micro_uploads/...)
        user['username']
    ))
    
    conn.commit()
    conn.close()

    # 4. REDIRECT
    # Send them back to the feed with a success message
    return RedirectResponse(url="/micro?success=ContentAdded", status_code=303)