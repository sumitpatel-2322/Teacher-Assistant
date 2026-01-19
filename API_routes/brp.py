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
    
    # 1. Security Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "brp":
        return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # Fetch all CRPs for dropdown
    cursor.execute("SELECT name, employee_id, assigned_cluster FROM crps")
    crps = cursor.fetchall()
    
    conn.close()

    # 2. Render with NO-CACHE Headers
    response = templates.TemplateResponse("BRP.html", {
        "request": request,
        "user": user,
        "crps": crps
    })
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

# ==========================================
# 2. CRP STATS API (For Charts)
# ==========================================
@router.get("/api/brp/crp-stats/{crp_id}")
async def get_crp_stats(crp_id: str, user=Depends(require_login)):
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Count Guidance
    cursor.execute("SELECT COUNT(*) FROM guidance WHERE crp_id = ?", (crp_id,))
    guidance_count = cursor.fetchone()[0]
    
    # Count Visits
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