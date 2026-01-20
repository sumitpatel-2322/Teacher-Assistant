from transformers import WhisperProcessor, WhisperForConditionalGeneration
from pathlib import Path

# Define the target path exactly as your app expects it
# Based on your voice.py: BASE_DIR / "speech" / "models" / "whisper-tiny"
output_path = Path("speech/models/whisper-tiny")
output_path.mkdir(parents=True, exist_ok=True)

print(f"Downloading Whisper-Tiny to {output_path}...")

# Download model and processor from Hugging Face Hub
model_id = "openai/whisper-tiny"
processor = WhisperProcessor.from_pretrained(model_id)
model = WhisperForConditionalGeneration.from_pretrained(model_id)

# Save them locally
processor.save_pretrained(output_path)
model.save_pretrained(output_path)

print("✅ Model downloaded successfully! You can now run the app.")