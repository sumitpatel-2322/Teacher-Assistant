from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates 
from API_routes.auth import require_login
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. ARP DASHBOARD (GET)
# ==========================================
@router.get("/arp")
def arp(request: Request, user=Depends(require_login)):
    
    # 1. Security Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "arp":
        return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()

    # 2. Fetch ARP Details
    cursor.execute("SELECT assigned_block FROM arps WHERE employee_id=?", (user['username'],))
    arp_info = cursor.fetchone()
    assigned_block = arp_info['assigned_block'] if arp_info else None

    # 3. Fetch Schools (Return Dicts with UDISE, not just Names)
    schools_data = []
    if assigned_block:
        cursor.execute("SELECT udise, name FROM schools WHERE block = ?", (assigned_block,))
    else:
        cursor.execute("SELECT udise, name FROM schools")
        
    # Return the full list of dicts (udise, name)
    schools_data = cursor.fetchall()

    conn.close()

    # 4. Render
    response = templates.TemplateResponse(
        "ARP.html",
        {
            "request": request,
            "user": user,
            "schools": schools_data
        }
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response


# ==========================================
# 2. STATS API
# ==========================================
@router.get("/api/arp/stats")
def get_arp_stats(school_id: str = None, user=Depends(require_login)):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Base Query
    where_clause = "WHERE 1=1"
    params = []
    
    # Filter by School ID if selected
    if school_id:
        where_clause += " AND school_id = ?"
        params.append(school_id)
        
    # 1. PIE CHART
    cursor.execute(f"""
        SELECT 
            SUM(CASE WHEN worked = 1 THEN 1 ELSE 0 END) as success,
            SUM(CASE WHEN worked = 0 THEN 1 ELSE 0 END) as failed,
            SUM(CASE WHEN worked IS NULL THEN 1 ELSE 0 END) as unknown
        FROM interaction_logs
        {where_clause}
    """, tuple(params))
    
    row = cursor.fetchone()
    success = row[0] or 0
    failed = row[1] or 0
    unknown = row[2] or 0
    
    # 2. HISTOGRAM
    cursor.execute(f"""
        SELECT 
            CASE 
                WHEN topic IS NULL OR topic = '' THEN 'General' 
                ELSE topic 
            END as topic_label, 
            COUNT(*) as count
        FROM interaction_logs
        {where_clause} AND worked = 0 
        GROUP BY topic_label
        ORDER BY count DESC
        LIMIT 5
    """, tuple(params))
    
    topics = []
    counts = []
    for r in cursor.fetchall():
        topics.append(r[0])
        counts.append(r[1])
        
    conn.close()
    
    return JSONResponse({
        "pie_data": [success, failed, unknown],
        "hist_labels": topics,
        "hist_data": counts
    })