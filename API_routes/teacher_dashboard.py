from fastapi import APIRouter, Request, Depends, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from Database.db import get_connection
from typing import Optional
from pathlib import Path
import time

# Reliable Translation
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

# Internal Imports
from API_routes.auth import require_login
from decision_engine.raw_text.store import store_raw_input
from decision_engine.engine import process_teacher_query
from decision_engine.logging import log_feedback

# ✅ Hybrid Service Imports
from decision_engine.llm_service import get_conversational_advice, get_general_chat_response

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
    1. Checks User's Profile Preference (The "Boss").
    2. Handles Input (translates to English for the Engine).
    3. Greeting Guardrail: Stops 'Hello' from triggering math solutions.
    4. Tries Online LLM for conversation (Circuit Breaker).
    5. Falls back to Rule-Engine text if Offline.
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

            # If input is NOT English, translate to English for the engine
            if detected_input != 'en':
                print(f"DEBUG: Input detected as {detected_input}. Translating to English...")
                translator = GoogleTranslator(source='auto', target='en')
                processed_question = translator.translate(user_question)

        except Exception as e:
            print(f"WARNING: Input translation failed: {e}")

    # 🛑 GREETING GUARDRAIL 🛑
    # If input is short and looks like a greeting, FORCE the Engine to return nothing.
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

    # Return response
    response_data = {
        "status": "success",
        "request_id": engine_output["request_id"],
        "detected_language": target_lang, 
        "bot_message": bot_message, # <--- The conversational part
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