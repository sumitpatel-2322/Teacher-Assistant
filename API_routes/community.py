from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from API_routes.auth import require_login
import sqlite3
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# DB Path relative to main folder
DB_PATH = os.path.join("Database", "community.db")

def get_community_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_community_db():
    os.makedirs("Database", exist_ok=True)
    conn = get_community_db()
    try:
        # Posts Table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                teacher_name TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tag TEXT,
                likes INTEGER DEFAULT 0,
                disagrees INTEGER DEFAULT 0,
                shares INTEGER DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # Comments Table (Supports nesting via parent_id)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER,
                parent_id INTEGER,
                author TEXT,
                text TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"DB Init Error: {e}")
    finally:
        conn.close()

init_community_db()

# --- ROUTES ---

@router.get("/community")
def community_page(request: Request, user=Depends(require_login)):
    return templates.TemplateResponse("community.html", {"request": request, "user": user})

@router.get("/api/community/posts")
def get_posts(tag: str = None, sort: str = "top_agreed", user=Depends(require_login)):
    conn = get_community_db()
    cursor = conn.cursor()
    
    # Get posts + comment count
    base_query = '''
        SELECT p.*, 
        (SELECT COUNT(*) FROM comments c WHERE c.post_id = p.id) as comment_count 
        FROM posts p
    '''
    params = []
    
    if tag and tag != "All Topics":
        base_query += " WHERE p.tag = ?"
        params.append(tag)
    
    # Sorting Logic
    if sort == "newest": base_query += " ORDER BY p.timestamp DESC" # Use timestamp for newest
    elif sort == "oldest": base_query += " ORDER BY p.timestamp ASC"
    elif sort == "top_agreed": base_query += " ORDER BY (p.likes - p.disagrees) DESC, p.id DESC"
    elif sort == "less_agreed": base_query += " ORDER BY (p.likes - p.disagrees) ASC, p.id DESC"
    else: base_query += " ORDER BY p.id DESC"
    
    cursor.execute(base_query, tuple(params))
    posts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return posts

@router.post("/api/community/posts")
async def create_post(request: Request, user=Depends(require_login)):
    try:
        data = await request.json()
        if not data.get('title') or not data.get('content'):
             raise HTTPException(status_code=400, detail="Title and Content required")

        conn = get_community_db()
        conn.execute(
            "INSERT INTO posts (teacher_name, title, content, tag) VALUES (?, ?, ?, ?)",
            (user['username'], data['title'], data['content'], data['tag'])
        )
        conn.commit()
        conn.close()
        return {"message": "Post created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/community/posts/{post_id}/vote")
async def vote_post(post_id: int, request: Request, user=Depends(require_login)):
    data = await request.json()
    action = data.get("action")
    conn = get_community_db()
    
    if action == "add_agree":
        conn.execute("UPDATE posts SET likes = likes + 1 WHERE id = ?", (post_id,))
    elif action == "remove_agree":
        conn.execute("UPDATE posts SET likes = MAX(0, likes - 1) WHERE id = ?", (post_id,))
    elif action == "add_disagree":
        conn.execute("UPDATE posts SET disagrees = disagrees + 1 WHERE id = ?", (post_id,))
    elif action == "remove_disagree":
        conn.execute("UPDATE posts SET disagrees = MAX(0, disagrees - 1) WHERE id = ?", (post_id,))
        
    conn.commit()
    conn.close()
    return {"message": "Vote updated"}

@router.get("/api/community/posts/{post_id}/comments")
def get_comments(post_id: int, user=Depends(require_login)):
    conn = get_community_db()
    # Fetch all comments for post, frontend JS will build the tree
    rows = conn.execute("SELECT * FROM comments WHERE post_id = ? ORDER BY id ASC", (post_id,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

@router.post("/api/community/posts/{post_id}/comments")
def add_comment(post_id: int, author: str = Form(...), text: str = Form(...), parent_id: int = Form(None), user=Depends(require_login)):
    conn = get_community_db()
    conn.execute(
        "INSERT INTO comments (post_id, parent_id, author, text) VALUES (?, ?, ?, ?)", 
        (post_id, parent_id, author, text)
    )
    conn.commit()
    conn.close()
    return {"message": "Comment added"}

@router.get("/api/community/tags")
def get_tags(user=Depends(require_login)):
    conn = get_community_db()
    rows = conn.execute("SELECT DISTINCT tag FROM posts").fetchall()
    conn.close()
    existing = [row[0] for row in rows if row[0]]
    defaults = ["Classroom Management", "Maths Pedagogy", "FLN Basics", "Multi-Grade", "EdTech", "Teacher Wellbeing"]
    return ["All Topics"] + sorted(list(set(defaults + existing)))
