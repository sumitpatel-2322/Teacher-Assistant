from typing import Dict

from speech.vosk_stt import VoskSTT
from transformers import pipeline
import torch
from pathlib import Path


# Languages for which Vosk streaming models are available
VOSK_SUPPORTED_LANGS = {"en", "hi", "te"}


class STTAdapter:
    def __init__(self):
        self._vosk_instances = {}
        self._whisper = None

    def _get_vosk(self, lang: str) -> VoskSTT:
        if lang not in self._vosk_instances:
            self._vosk_instances[lang] = VoskSTT(lang=lang)
        return self._vosk_instances[lang]

    def _get_whisper(self):
        if self._whisper is None:
            model_path = Path("speech/models/whisper-tiny")
            device = -1  # force CPU
            self._whisper = pipeline(
                "automatic-speech-recognition",
                model=str(model_path),
                device=device
            )
        return self._whisper

    def transcribe(self, lang: str, mode: str = "auto") -> Dict[str, str]:
        """
        lang: language code (e.g., en, hi, te, kn, mr)
        mode: auto | live | one-shot
        """

        # Auto-routing logic
        if mode == "auto":
            if lang in VOSK_SUPPORTED_LANGS:
                mode = "live"
            else:
                mode = "one-shot"

        if mode == "live":
            vosk = self._get_vosk(lang)
            text = vosk.listen()
            return {
                "text": text,
                "language": lang,
                "engine": "vosk",
                "mode": "live"
            }

        if mode == "one-shot":
            whisper = self._get_whisper()
            result = whisper("speech_input.wav")
            return {
                "text": result["text"],
                "language": lang,
                "engine": "whisper-tiny",
                "mode": "one-shot"
            }

        raise ValueError(f"Invalid mode: {mode}")