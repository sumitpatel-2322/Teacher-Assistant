from fastapi import APIRouter, UploadFile, File
import tempfile
import shutil
from pathlib import Path
import os
from decision_engine.engine import process_teacher_query

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
WHISPER_MODEL_PATH = BASE_DIR / "speech" / "models" / "whisper-tiny"

# Global variable to store the model instance (Lazy Loaded)
whisper_asr = None

@router.post("/api/teacher/voice")
async def handle_voice_input(audio: UploadFile = File(...)):
    global whisper_asr

    # 1. LAZY IMPORT CHECK
    # This ensures the server starts even if libraries are missing in case of online deployment.
    try:
        from transformers import pipeline
    except ImportError:
        return {
            "status": "error",
            "error": "Voice AI libraries (torch/transformers) are not installed on this server. Please use Text Mode."
        }

    # 2. LAZY MODEL LOADING
    # Only load the heavy 200MB model the first time someone actually uses voice.
    if whisper_asr is None:
        try:
            print(">>> Loading Whisper Model into Memory (First Run)...")
            whisper_asr = pipeline(
                "automatic-speech-recognition",
                model=str(WHISPER_MODEL_PATH),
                device=-1  # CPU Mode
            )
            print(">>> Whisper Model Loaded Successfully.")
        except Exception as e:
            print(f"ERROR: Failed to load Whisper model: {e}")
            return {
                "status": "error",
                "error": "Voice model could not be loaded. Server may be out of RAM."
            }

    # 3. PROCESS AUDIO
    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = Path(tmp.name)
    
    try:
        # Run Inference
        try:
            result = whisper_asr(str(tmp_path))
            text = result.get("text", "").strip()
        except Exception as e:
            return {"status": "error", "error": f"Speech processing failed: {str(e)}"}

        if not text:
            return {"status": "error", "error": "Could not understand audio"}

        # Get Solutions
        try:
            solutions_data = process_teacher_query(text)
        except Exception:
            return {"status": "error", "error": "Internal processing error"}

        # Return flat structure
        return {
            "status": "success",
            "solutions": solutions_data["ranked_solutions"],
            "request_id": solutions_data["request_id"]
        }

    finally:
        # Cleanup temp file
        if tmp_path.exists():
            tmp_path.unlink()