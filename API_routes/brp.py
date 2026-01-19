from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates 
from fastapi.responses import JSONResponse, RedirectResponse
from API_routes.auth import require_login
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. BRP DASHBOARD (Page Load)
# ==========================================
@router.get("/brp")
async def brp_dashboard(request: Request, user=Depends(require_login)):
    
    # Security Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "brp":
        return RedirectResponse(url="/login")

    conn = get_connection()
    cursor = conn.cursor()
    
    # Fetch all CRPs to populate the dropdown
    # (In a real scenario, you might filter by the BRP's Block)
    cursor.execute("SELECT name, employee_id, assigned_cluster FROM crps")
    crps = cursor.fetchall()
    
    conn.close()

    return templates.TemplateResponse("BRP.html", {
        "request": request,
        "user": user,
        "crps": crps # Pass CRP list to template
    })

# ==========================================
# 2. CRP STATS API (For Charts)
# ==========================================
@router.get("/api/brp/crp-stats/{crp_id}")
async def get_crp_stats(crp_id: str, user=Depends(require_login)):
    """
    Returns activity counts for a specific CRP to populate charts.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Count Guidance Uploaded by this CRP
    cursor.execute("SELECT COUNT(*) FROM guidance WHERE crp_id = ?", (crp_id,))
    guidance_count = cursor.fetchone()[0]
    
    # 2. Count Visits Scheduled by this CRP
    cursor.execute("SELECT COUNT(*) FROM visits WHERE crp_id = ?", (crp_id,))
    visit_count = cursor.fetchone()[0]
    
    conn.close()
    
    return JSONResponse({
        "status": "success",
        "data": {
            "guidance": guidance_count,
            "visits": visit_count,
            "total_actions": guidance_count + visit_count
        }
    })