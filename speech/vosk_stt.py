import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from pathlib import Path

SAMPLE_RATE = 16000
MODEL_PATH = Path(__file__).parent / "models" / "te" / "model"

class VoskSTT:
    def __init__(self, model_path=MODEL_PATH):
        if not model_path.exists():
            raise FileNotFoundError(f"Vosk model not found at {model_path}")

        self.model = Model(str(model_path))
        self.recognizer = KaldiRecognizer(self.model, SAMPLE_RATE)
        self.recognizer.SetWords(True)

        self.queue = queue.Queue()

    def _audio_callback(self, indata, frames, time, status):
        self.queue.put(bytes(indata))

    def listen(self):
        with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._audio_callback
        ):
            print("🎙️ Listening… Speak now (Ctrl+C to stop)")
            while True:
                data = self.queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "").strip()
                    if text:
                        return text