from groq import Groq
import time
import os
from dotenv import load_dotenv

# <--- DEBUG START --->
print("\n>>> DEBUG: [Import] decision_engine/llm_service.py loaded")
# <--- DEBUG END --->

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = None

try:
    if GROQ_API_KEY and GROQ_API_KEY.startswith("gsk_"):
        client = Groq(api_key=GROQ_API_KEY)
        # <--- DEBUG START --->
        print(">>> DEBUG: [LLM Service] Groq Client initialized successfully.")
        # <--- DEBUG END --->
    else:
        print(">>> DEBUG: [LLM Service] No valid GROQ_API_KEY found. Hybrid mode disabled.")
except Exception as e:
    print(f"WARNING: Groq Client init failed: {e}")

def get_conversational_advice(problem_text, best_solution_title, lang="en"):
    """
    Hybrid Logic (Teaching Mode):
    - Tries to get a warm AI response in 2.0 seconds.
    - If timeout/offline, returns None (triggering fallback).
    """
    # <--- DEBUG START --->
    print(f">>> DEBUG: [LLM Service] 'get_conversational_advice' called for solution: '{best_solution_title}'")
    # <--- DEBUG END --->

    if not client:
        print(">>> DEBUG: [LLM Service] Client not available. Skipping.")
        return None

    # Prompt Engineering for "Teacher Persona"
    system_prompt = (
        "You are a helpful senior teacher mentor. "
        "The user has a classroom problem. We have identified a solution. "
        "Write a very short (1 sentence), warm, encouraging message recommending this solution. "
        "Do not list steps. Just be empathetic."
    )
    
    # Handle Language Instruction for LLM
    if lang == 'hi':
        system_prompt += " Reply in warm, natural Hindi (Devanagari)."
    elif lang != 'en':
        system_prompt += f" Reply in warm, natural {lang}."

    user_content = f"Problem: {problem_text}\nSolution: {best_solution_title}"

    try:
        start_time = time.time()
        
        # UPDATED MODEL: llama-3.3-70b-versatile
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=60,
            timeout=2.0 
        )
        
        response = chat_completion.choices[0].message.content
        duration = time.time() - start_time
        
        # <--- DEBUG START --->
        print(f">>> DEBUG: [LLM Service] Response received in {duration:.2f}s: '{response[:30]}...'")
        # <--- DEBUG END --->
        
        return response

    except Exception as e:
        print(f">>> DEBUG: [LLM Service] Failed or Timed Out: {e}")
        return None # Triggers raw text fallback

def get_general_chat_response(user_text, lang="en"):
    """
    Hybrid Logic (Chit-Chat Mode):
    Handles general conversation (Hello, Thanks, Who are you?) 
    when the Rule Engine finds no specific classroom solutions.
    """
    # <--- DEBUG START --->
    print(f">>> DEBUG: [LLM Service] 'get_general_chat_response' called. Input: '{user_text}'")
    # <--- DEBUG END --->

    if not client:
        return None

    # Prompt: Be a friendly colleague, not a robot.
    system_prompt = (
        "You are 'VEDA', a helpful, warm senior teacher mentor. "
        "The user is a teacher chatting with you. "
        "Reply to their greeting, gratitude, or general comment warmly and briefly (max 2 sentences). "
        "If they asked a complex teaching question that you don't understand, ask them to clarify."
    )
    
    if lang == 'hi':
        system_prompt += " Reply in warm, natural Hindi (Devanagari)."
    elif lang != 'en':
        system_prompt += f" Reply in warm, natural {lang}."

    try:
        # UPDATED MODEL: llama-3.3-70b-versatile
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=60,
            timeout=3.0
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f">>> DEBUG: [LLM Service] General Chat Failed: {e}")
        return None