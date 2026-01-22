from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates 
from API_routes.auth import require_login
from Database.db import get_connection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. CRP DASHBOARD (GET)
# ==========================================
@router.get("/crp")
def crp(request: Request, user=Depends(require_login)):
    
    # 1. Security: Role Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "crp":
        return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # A. Fetch CRP Details
    cursor.execute("SELECT assigned_cluster, assigned_block FROM crps WHERE employee_id=?", (user['username'],))
    crp_info = cursor.fetchone()
    
    assigned_block = crp_info['assigned_block'] if crp_info else None
    assigned_cluster = crp_info['assigned_cluster'] if crp_info else None

    # B. Fetch Schools
    schools_data = []
    if assigned_block:
        cursor.execute("SELECT udise, name FROM schools WHERE block = ?", (assigned_block,))
    elif assigned_cluster:
        cursor.execute("SELECT udise, name FROM schools WHERE cluster = ?", (assigned_cluster,))
    else:
        cursor.execute("SELECT udise, name FROM schools")
        
    schools_data = cursor.fetchall()

    # C. Fetch Open Escalations
    cursor.execute("""
        SELECT e.*, t.name as teacher_name, s.name as school_name
        FROM escalations e
        LEFT JOIN teachers t ON e.teacher_id = t.employee_id
        LEFT JOIN schools s ON e.school_id = s.udise
        WHERE e.status = 'Open'
        ORDER BY e.created_at DESC
        LIMIT 10
    """)
    escalations = cursor.fetchall()

    # D. Fetch Insights (Failures)
    cursor.execute("""
        SELECT i.*, t.name as teacher_name 
        FROM interaction_logs i
        LEFT JOIN teachers t ON i.teacher_id = t.employee_id
        WHERE i.worked = 0
        ORDER BY i.created_at DESC
        LIMIT 10
    """)
    insights = cursor.fetchall()

    conn.close()

    response = templates.TemplateResponse("CRP.html", {
        "request": request,
        "user": user,
        "schools": schools_data,
        "escalations": escalations,
        "insights": insights
    })
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

# ==========================================
# 2. ACTIONS
# ==========================================
@router.post("/crp/upload-guidance")
async def upload_guidance(
    request: Request,
    school_id: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO guidance (crp_id, school_id, title, description)
        VALUES (?, ?, ?, ?)
    """, (user['username'], school_id, title, description))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/crp?success=GuidanceUploaded", status_code=303)

@router.post("/crp/schedule-visit")
async def schedule_visit(
    request: Request,
    school_id: str = Form(...),
    visit_date: str = Form(...),
    visit_time: str = Form(...),
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO visits (crp_id, school_id, visit_date, visit_time)
        VALUES (?, ?, ?, ?)
    """, (user['username'], school_id, visit_date, visit_time))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/crp?success=VisitScheduled", status_code=303)

# NEW: Close Escalation Action
@router.post("/crp/close-escalation")
async def close_escalation(
    request: Request,
    escalation_id: int = Form(...),
    user=Depends(require_login)
):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE escalations 
        SET status = 'Closed' 
        WHERE id = ?
    """, (escalation_id,))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/crp?success=TicketClosed", status_code=303)

# ==========================================
# 3. STATS API (FIXED)
# ==========================================
@router.get("/api/crp/stats")
async def get_crp_stats(school_id: str = None, user=Depends(require_login)):
    conn = get_connection()
    cursor = conn.cursor()
    
    where_clause = "WHERE 1=1"
    params = []
    
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
    
    # 2. HISTOGRAM (FIXED: Handle Empty Topics)
    # logic: If topic is empty string or NULL, label it 'General'
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