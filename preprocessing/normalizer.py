"""
Theme 1 Preprocessing
Text Normalizer
Standardizes text and maps phrases to signal tokens.
"""

import re
from preprocessing.noise_words import NOISE_WORDS
from preprocessing.phrase_map import PHRASE_MAP
from preprocessing.typo_map import TYPO_MAP

def normalize_text(raw_text: str) -> str:
    """
    1. Lowercase
    2. Remove noise words
    3. Fix typos
    4. Map phrases to signals (e.g., "too loud" -> "noise_spike_signal")
    """
    if not raw_text:
        return ""

    text = raw_text.lower().strip()
    
    # Remove special chars (keep spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # 1. Map Phrases (Longer phrases first to avoid partial matches)
    # We sort by length descending so "not listening" matches before "listening"
    sorted_phrases = sorted(PHRASE_MAP.keys(), key=len, reverse=True)
    
    for phrase in sorted_phrases:
        if phrase in text:
            signal_token = PHRASE_MAP[phrase]
            text = text.replace(phrase, f" {signal_token} ")

    # 2. Tokenize
    tokens = text.split()
    clean_tokens = []

    for t in tokens:
        # Fix typos
        t = TYPO_MAP.get(t, t)
        
        # Remove noise (unless it's a signal token we just added)
        if t not in NOISE_WORDS or "_signal" in t:
            clean_tokens.append(t)

    return " ".join(clean_tokens)