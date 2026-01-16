from fastapi import APIRouter, Request, Depends, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from Database.db import get_connection
from typing import Optional

# Reliable Translation
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

# Internal Imports
from API_routes.auth import require_login
from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query
from decision_engine.logging import log_feedback

# Seed for consistent detection
DetectorFactory.seed = 0

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# =========================
# 1. PAGE LOAD (Sync)
# =========================
@router.get("/teacher")
async def teacher_dashboard(request: Request, user=Depends(require_login)):
    
    conn = get_connection()
    cursor = conn.cursor()
    # Fetch all preferences
    cursor.execute("SELECT preferred_class, preferred_subject, preferred_language FROM teachers WHERE username = ?", (user['username'],))
    row = cursor.fetchone()
    conn.close()

    prefill = {
        "class": row["preferred_class"] if row else "",
        "subject": row["preferred_subject"] if row else "",
        # Default to English if not set
        "language": row["preferred_language"] if row and row["preferred_language"] else "en"
    }

    return templates.TemplateResponse(
        "Teacher_dashboard.html",
        {
            "request": request,
            "user": user,
            "prefill": prefill 
        }
    )

# =========================
# 2. CHAT API (The Fix)
# =========================
@router.post("/api/teacher/ask")
async def ask_doubt_api(
    request: Request,
    user=Depends(require_login),
    payload: dict = Body(...)
):
    """
    Smart Multilingual API:
    1. Checks User's Profile Preference (The "Boss").
    2. Handles Input (translates to English for the Engine).
    3. Forces Output into Profile Language.
    """
    
    # 1. Fetch User's Preferred Language First
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT preferred_language FROM teachers WHERE username = ?", (user['username'],))
    row = cursor.fetchone()
    conn.close()

    # The Target Language for OUTPUT
    target_lang = row["preferred_language"] if row and row["preferred_language"] else "en"
    
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

            # HINGLISH HANDLING:
            # If detected as 'en' but user prefers 'hi', it MIGHT be Hinglish.
            # But standard translators struggle with Hinglish -> English without specific models.
            # We will rely on Google Translate's 'auto' which is decent at mixed script.
            
            # If input is NOT English, translate to English for the engine
            if detected_input != 'en':
                print(f"DEBUG: Input detected as {detected_input}. Translating to English...")
                translator = GoogleTranslator(source='auto', target='en')
                processed_question = translator.translate(user_question)
            
            # If input IS 'en' (or Hinglish detected as en), we send it to engine.
            # (Future improvement: specific Hinglish detection library)

        except Exception as e:
            print(f"WARNING: Input translation failed: {e}")

    # 2. Process with Engine
    raw_text = f"Class: {class_name}\nSubject: {subject}\nTopic: {topic}\nProblem: {processed_question}"
    engine_output = process_teacher_query(raw_text)

    # --- LAYER 2: OUTPUT TRANSLATION (Enforce Profile Pref) ---
    final_solutions = []
    
    # Initialize output translator if target is not English
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

    # Return response
    # CRITICAL: We send 'target_lang' back as 'detected_language'
    # This forces the Frontend to ask for details in the Profile Language
    response_data = {
        "status": "success",
        "request_id": engine_output["request_id"],
        "detected_language": target_lang, 
        "solutions": final_solutions
    }
    
    return JSONResponse(content=response_data)


# =========================
# 3. FEEDBACK API
# =========================
@router.post("/teacher/feedback")
async def teacher_feedback(
    request: Request,
    user=Depends(require_login)
):
    data = await request.json()

    log_feedback(
        request_id=data.get("request_id"),
        solution_chosen=data.get("solution_id"),
        worked=data.get("worked"),
        feedback=data.get("feedback")
    )

    return {"success": True}