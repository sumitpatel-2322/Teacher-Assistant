import re
from preprocessing.noise_words import NOISE_WORDS
from preprocessing.phrase_map import PHRASE_MAP
from preprocessing.typo_map import TYPO_MAP

print("\n>>> DEBUG: [Import] preprocessing/normalizer.py loaded") # <--- ADD THIS (Top Level)

def normalize_text(raw_text: str) -> str:
    """
    1. Lowercase
    2. Remove noise words
    3. Fix typos
    4. Map phrases to signals (e.g., "too loud" -> "noise_spike_signal")
    """
    # <--- ADD THIS BLOCK START --->
    print(f"\n>>> DEBUG [Normalizer] Input: '{raw_text}'")
    # <--- ADD THIS BLOCK END --->

    if not raw_text:
        return ""

    text = raw_text.lower().strip()
    
    # Remove special chars (keep spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # 1. Map Phrases (Longer phrases first to avoid partial matches)
    sorted_phrases = sorted(PHRASE_MAP.keys(), key=len, reverse=True)
    
    for phrase in sorted_phrases:
        if phrase in text:
            signal_token = PHRASE_MAP[phrase]
            # <--- ADD THIS OPTIONAL DEBUG --->
            print(f"   -> [Normalizer] Mapped phrase '{phrase}' to '{signal_token}'")
            # <--- END OPTIONAL DEBUG --->
            text = text.replace(phrase, f" {signal_token} ")

    # 2. Tokenize
    tokens = text.split()
    clean_tokens = []

    for t in tokens:
        # Fix typos
        if t in TYPO_MAP:
            t = TYPO_MAP[t]
        
        # Remove noise
        if t not in NOISE_WORDS:
            clean_tokens.append(t)

    normalized_output = " ".join(clean_tokens)

    # <--- ADD THIS BLOCK START --->
    print(f">>> DEBUG [Normalizer] Output: '{normalized_output}'")
    # <--- ADD THIS BLOCK END --->

    return normalized_output