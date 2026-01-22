from fastapi import APIRouter, Request, Depends, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from Database.db import get_connection
from typing import Optional
from pathlib import Path
import time

# Reliable Translation
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
# Authentication Dependency
try:
    from API_routes.auth import require_login
except ImportError:
    # Fallback if auth.py is missing
    async def require_login(request: Request):
        user = request.session.get("user")
        if not user:
            return RedirectResponse(url="/login")
        return user

# Decision Engine Imports
from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query
from decision_engine.logging import log_feedback

# ✅ Hybrid Service Imports
from decision_engine.llm_service import get_conversational_advice, get_general_chat_response

# Seed for consistent detection
DetectorFactory.seed = 0

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ==========================================
# 1. TEACHER DASHBOARD (GET)
# ==========================================
@router.get("/teacher")
async def teacher_dashboard(request: Request, user=Depends(require_login)):
    
    # 1. Security: Role Check
    if isinstance(user, RedirectResponse): return user
    if user.get("role") != "teacher":
         return RedirectResponse(url="/login?error=Unauthorized")

    conn = get_connection()
    # Use Row factory to allow accessing columns by name
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    # 2. Fetch User Details
    cursor.execute(
        "SELECT school_udise, classes, subjects FROM teachers WHERE employee_id = ?", 
        (user['username'],)
    )
    teacher_data = cursor.fetchone()
    
    prefill = {"class": "", "subject": ""}
    school_id = ""

    if teacher_data:
        prefill["class"] = teacher_data.get("classes", "")
        prefill["subject"] = teacher_data.get("subjects", "")
        school_id = (teacher_data.get("school_udise") or "").strip()

    # 3. Fetch Notices & Visits
    notices = []
    if school_id:
        # Guidance
        cursor.execute("SELECT * FROM guidance WHERE school_id = ? ORDER BY created_at DESC", (school_id,))
        for g in cursor.fetchall():
            notices.append({
                "type": "Guidance",
                "title": g["title"],
                "content": g["description"],
                "date": g["created_at"]
            })

        # Visits
        cursor.execute("SELECT * FROM visits WHERE school_id = ? ORDER BY visit_date ASC", (school_id,))
        for v in cursor.fetchall():
            notices.append({
                "type": "Visit",
                "title": "CRP Visit Scheduled",
                "content": f"Date: {v['visit_date']} at {v['visit_time']}",
                "date": v['created_at']
            })

    conn.close()

    # 4. Render Template with NO-CACHE Headers
    # This prevents the browser from storing the page, so 'Back' button forces a reload.
    response = templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "prefill": prefill,
            "notices": notices
        }
    )
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response

# =========================
# 2. CHAT API (The Hybrid Logic)
# =========================

@router.post("/api/teacher/ask")
async def ask_doubt_api(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    """
    Smart Hybrid API:
    1. Checks User's Profile Preference.
    2. Handles Input (translates to English).
    3. Greeting Guardrail.
    4. Tries Online LLM.
    5. Falls back to Rule-Engine.
    6. LOGS interaction to Database for CRP Insights.
    """
    if isinstance(user, RedirectResponse): return user
    
    # 1. Fetch User's Preferred Language & School ID
    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    
    cursor.execute("SELECT preferred_language, school_udise FROM teachers WHERE employee_id = ?", (user['username'],))
    row = cursor.fetchone()
    
    # The Target Language for OUTPUT
    target_lang = row["preferred_language"] if row and row["preferred_language"] else "en"
    school_id = row["school_udise"] if row else "UNKNOWN"
    
    # Extract data
    class_name = payload.get("class_name", "").strip()
    subject = payload.get("subject", "").strip()
    topic = payload.get("topic", "").strip()
    user_question = payload.get("question", "").strip()

    processed_question = user_question

    # --- LAYER 1: INPUT PROCESSING ---
    if user_question:
        try:
            # Detect language of the specific query
            try:
                detected_input = detect(user_question)
            except:
                detected_input = 'en'

            # If input is NOT English, translate to English for the engine
            if detected_input != 'en':
                print(f"DEBUG: Input detected as {detected_input}. Translating to English...")
                translator = GoogleTranslator(source='auto', target='en')
                processed_question = translator.translate(user_question)

        except Exception as e:
            print(f"WARNING: Input translation failed: {e}")

    # 🛑 GREETING GUARDRAIL 🛑
    is_greeting = False
    greetings = ["hello", "hi", "hey", "greetings", "namaste", "hola", "thanks", "thank you", "good morning", "good evening"]
    
    # Clean text to check
    clean_text = processed_question.lower().strip().replace("!", "").replace(".", "")
    
    # Logic: If text is short (< 6 words) AND contains a greeting
    if len(clean_text.split()) < 6 and any(g == clean_text or clean_text.startswith(g + " ") for g in greetings):
        is_greeting = True
        print("DEBUG: Greeting detected! Skipping Rule Engine.")

    # 2. Process with Engine (Core Logic)
    if is_greeting:
        # Mock an empty engine response to force Chit-Chat mode
        engine_output = {"request_id": f"chat_{int(time.time())}", "ranked_solutions": []}
    else:
        # Run the actual engine
        raw_text = f"Class: {class_name}\nSubject: {subject}\nTopic: {topic}\nProblem: {processed_question}"
        engine_output = process_teacher_query(raw_text)

    # --- LAYER 2: HYBRID CONVERSATION LAYER ---
    final_solutions = []
    bot_message = ""

    # CASE A: Engine Found Solutions (Teaching Mode)
    if engine_output["ranked_solutions"]:
        best_sol = engine_output["ranked_solutions"][0]
        
        # 1. Hybrid Header (LLM or Raw)
        llm_reply = get_conversational_advice(
            problem_text=processed_question,
            best_solution_title=best_sol['title'],
            lang=target_lang
        )
        if llm_reply:
            bot_message = llm_reply
            print("DEBUG: Served via Groq (Online - Teaching)")
        else:
            # Fallback Header
            if target_lang == 'hi':
                bot_message = f"मुझे {len(engine_output['ranked_solutions'])} सुझाव मिले। '{best_sol['title']}' आज़माएँ।"
            else:
                bot_message = f"Found {len(engine_output['ranked_solutions'])} suggestions. Try '{best_sol['title']}'."
                print("DEBUG: Served via Fallback (Offline - Teaching)")

    # CASE B: No Solutions (Chit-Chat Mode)
    else:
        # 2. Try General Chat LLM
        # We use the ORIGINAL user_question (preserves tone), not the English translation
        chat_reply = get_general_chat_response(user_question, lang=target_lang)
        
        if chat_reply:
            bot_message = chat_reply
            print("DEBUG: Served via Groq (Online - ChitChat)")
        else:
            # Final Fallback if LLM fails too
            if target_lang == 'hi':
                bot_message = "मैं सुन रहा हूँ। कृपया अपनी कक्षा की समस्या साझा करें।"
            else:
                bot_message = "I'm listening. Please share your classroom challenge."
                print("DEBUG: Served via Fallback (Offline - ChitChat)")


    # B. Translate Solution Cards (Force Profile Pref)
    out_translator = None
    if target_lang != 'en':
        try:
            out_translator = GoogleTranslator(source='en', target=target_lang)
        except Exception as e:
            print(f"WARNING: Output translator init failed: {e}")

    for s in engine_output["ranked_solutions"]:
        title_out = s.get("title", "")
        text_out = s.get("text", "")

        # Translate if we have a translator
        if out_translator:
            try:
                title_out = out_translator.translate(title_out)
                text_out = out_translator.translate(text_out)
            except Exception as e:
                print(f"WARNING: Translation failed for card {s['solution_id']}: {e}")

        final_solutions.append({
            "id": s["solution_id"], 
            "title": title_out,
            "text": text_out,
            "confidence": s["confidence"]
        })

    # --- KEY UPDATE: Log to DB for Insights ---
    try:
        cursor.execute("""
            INSERT INTO interaction_logs (request_id, teacher_id, school_id, topic, query_text, solution_shown)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            engine_output["request_id"], 
            user['username'], 
            school_id,
            topic, 
            user_question, 
            final_solutions[0]['title'] if final_solutions else "Chit-Chat/No Solution"
        ))
        conn.commit()
    except Exception as e:
        print(f"DB Log Error: {e}")

    conn.close()

    # Store Raw Input (Legacy file store)
    store_raw_input(
        username=user["username"], 
        role=user["role"],
        class_name=class_name,
        subject=subject,
        topic=topic,
        question=user_question
    )

    # Return JSON
    response_data = {
        "status": "success",
        "request_id": engine_output["request_id"],
        "detected_language": target_lang, 
        "bot_message": bot_message, 
        "solutions": final_solutions
    }
    
    return JSONResponse(content=response_data)


# ==========================================
# 3. FEEDBACK API (POST)
# ==========================================
@router.post("/teacher/feedback")
async def teacher_feedback(
    request: Request,
    user=Depends(require_login)
):
    if isinstance(user, RedirectResponse): return user

    data = await request.json()
    request_id = data.get("request_id")
    worked = data.get("worked")

    # 1. Update Legacy CSV Log
    log_feedback(
        request_id=request_id,
        solution_chosen=data.get("solution_id"),
        worked=worked,
        feedback=data.get("feedback")
    )

    # 2. Update DB for CRP Insights
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE interaction_logs 
            SET worked = ? 
            WHERE request_id = ?
        """, (worked, request_id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"DB Feedback Update Error: {e}")

    return {"success": True}

# ==========================================
# 4. ESCALATION API (POST) - "Get Help from Expert"
# ==========================================
@router.post("/api/teacher/escalate")
async def escalate_to_expert(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    """
    Allows teachers to directly send a query to the CRP/Expert.
    """
    if isinstance(user, RedirectResponse): return user

    query_text = payload.get("query", "").strip()
    if not query_text:
        return JSONResponse({"status": "error", "message": "Empty query"}, status_code=400)

    try:
        conn = get_connection()
        conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
        cursor = conn.cursor()
        
        # Get School ID
        cursor.execute("SELECT school_udise FROM teachers WHERE employee_id = ?", (user['username'],))
        row = cursor.fetchone()
        school_id = row["school_udise"] if row else "UNKNOWN"

        # Insert Escalation
        cursor.execute("""
            INSERT INTO escalations (teacher_id, school_id, query_text)
            VALUES (?, ?, ?)
        """, (user['username'], school_id, query_text))
        
        conn.commit()
        conn.close()
        
        return JSONResponse({"status": "success", "message": "Sent to Expert"})
    except Exception as e:
        print(f"Escalation Error: {e}")
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)