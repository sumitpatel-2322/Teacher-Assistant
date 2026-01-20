from fastapi import APIRouter, UploadFile, File
import tempfile
import shutil
from pathlib import Path
import os

from transformers import pipeline
from decision_engine.engine import process_teacher_query

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
WHISPER_MODEL_PATH = BASE_DIR / "speech" / "models" / "whisper-tiny"

# Load Whisper Tiny once
whisper_asr = pipeline(
    "automatic-speech-recognition",
    model=str(WHISPER_MODEL_PATH),
    device=-1
)

@router.post("/api/teacher/voice")
async def handle_voice_input(audio: UploadFile = File(...)):
    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = Path(tmp.name)
    
    try:
        result = whisper_asr(str(tmp_path))
        text = result.get("text", "").strip()

        if not text:
            return {"error": "Could not understand audio"}

        try:
            solutions_data = process_teacher_query(text)
        except Exception:
            return {"error": "Internal processing error"}

        # Return flat structure
        return {
            "status": "success",
            "solutions": solutions_data["ranked_solutions"],
            "request_id": solutions_data["request_id"]
        }

    finally:
        if tmp_path.exists():
            tmp_path.unlink()