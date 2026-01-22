from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates 
from Database.db import get_connection
import hashlib # Standard library for basic hashing

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Initialize Tables on startup (Optional, good for Hackathons)
from Database.models import create_tables
create_tables()

@router.get("/register")
def register_page(request: Request):
    # --- FETCH DATA FOR DROPDOWNS ---
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Fetch Schools for Teacher Dropdown (UDISE + Name)
    cursor.execute("SELECT udise, name FROM schools ORDER BY name")
    schools_list = cursor.fetchall()
    
    # 2. Fetch Unique Blocks for CRP Dropdown
    # We use DISTINCT to get the list of unique blocks available in the system
    cursor.execute("SELECT DISTINCT block FROM schools WHERE block IS NOT NULL ORDER BY block")
    blocks_list = [row[0] for row in cursor.fetchall()]

    conn.close()

    return templates.TemplateResponse("register.html", {
        "request": request,
        "schools": schools_list, # List of (udise, name)
        "blocks": blocks_list    # List of strings ['Block A', 'Block B'...]
    })

@router.post("/register")
async def register_user(
    request: Request,
    role: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    
    # Teacher Fields (Optional because role might be 'admin')
    tname: str = Form(None),
    tid: str = Form(None),
    school_ucode: str = Form(None), # This now receives the UDISE from the dropdown
    emailid: str = Form(None),
    preferedlanguage: str = Form(None),
    subjects: list[str] = Form(None), # Receives list ["math", "science"]
    classes: list[str] = Form(None, alias="class"), # Alias handles 'name="class"'
    
    # Admin Fields (Optional because role might be 'teacher')
    full_name: str = Form(None),
    cid: str = Form(None),
    emailid_admin: str = Form(None),
    designation: str = Form(None), # crp, brp, arp
    assign_cluster: str = Form(None), # This now receives the BLOCK name from the dropdown (for CRP)
    domain: str = Form(None)
):
    
    # 1. Basic Validation
    if password != confirm_password:
        return templates.TemplateResponse("register.html", {
            "request": request, 
            "error": "Passwords do not match!"
        })

    # Simple Hashing (Use bcrypt for production)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # ==========================================
        # LOGIC FOR TEACHERS
        # ==========================================
        if role == 'teacher':
            # Convert Lists to Strings for SQLite (e.g., ["1","2"] -> "1, 2")
            subjects_str = ", ".join(subjects) if subjects else ""
            classes_str = ", ".join(classes) if classes else ""
            
            cursor.execute("""
                INSERT INTO teachers (name, employee_id, school_udise, email, password, preferred_language, subjects, classes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (tname, tid, school_ucode, emailid, hashed_password, preferedlanguage, subjects_str, classes_str))
            
            conn.commit()
            print(f"Teacher {tname} registered successfully.")
            return RedirectResponse(url="/login", status_code=303)

        # ==========================================
        # LOGIC FOR ADMINS (CRP / BRP / ARP)
        # ==========================================
        elif role == 'admin':
            if designation == 'crp':
                # For CRP, 'assign_cluster' form field now holds the BLOCK name
                cursor.execute("""
                    INSERT INTO crps (name, employee_id, email, password, assigned_block, assigned_cluster, domain)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (full_name, cid, emailid_admin, hashed_password, assign_cluster, "All", domain))
                
            elif designation == 'brp':
                cursor.execute("""
                    INSERT INTO brps (name, employee_id, email, password, assigned_block, domain)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (full_name, cid, emailid_admin, hashed_password, assign_cluster, domain))
                
            elif designation == 'arp':
                # Note: ARP uses 'specialization' which we map from 'domain' here
                cursor.execute("""
                    INSERT INTO arps (name, employee_id, email, password, assigned_block, specialization)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (full_name, cid, emailid_admin, hashed_password, assign_cluster, domain))

            conn.commit()
            print(f"{designation.upper()} {full_name} registered successfully.")
            return RedirectResponse(url="/login", status_code=303)

    except Exception as e:
        conn.rollback()
        print(f"Error during registration: {e}")
        
        # RE-FETCH DATA if we need to show the page again with an error
        cursor.execute("SELECT udise, name FROM schools ORDER BY name")
        schools_list = cursor.fetchall()
        cursor.execute("SELECT DISTINCT block FROM schools WHERE block IS NOT NULL ORDER BY block")
        blocks_list = [row[0] for row in cursor.fetchall()]

        return templates.TemplateResponse("register.html", {
            "request": request, 
            "schools": schools_list,
            "blocks": blocks_list,
            "error": f"Registration Failed. ID or Email might already exist."
        })
    finally:
        conn.close()

    # Fallback
    return RedirectResponse(url="/login", status_code=303)