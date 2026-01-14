import re

from preprocessing.typo_map import TYPO_MAP
from preprocessing.phrase_map import PHRASE_MAP
from preprocessing.noise_words import NOISE_WORDS


def normalize_text(raw_text: str) -> str:
    """
    Layer 1: Rule-based text normalization.
    Deterministic. No decisions.
    """

    if not raw_text:
        return ""

    # -------------------------
    # 1. Basic cleanup
    # -------------------------
    text = raw_text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # -------------------------
    # 2. Token-level typo correction
    # -------------------------
    tokens = []
    for token in text.split():
        tokens.append(TYPO_MAP.get(token, token))
    text = " ".join(tokens)

    # -------------------------
    # 3. Phrase-level normalization
    # -------------------------
    for phrase, replacement in PHRASE_MAP.items():
        pattern = r"\b" + re.escape(phrase) + r"\b"
        text = re.sub(pattern, replacement, text)

    # -------------------------
    # 4. Noise word removal
    # -------------------------
    final_tokens = [
        t for t in text.split()
        if t not in NOISE_WORDS
    ]

    return " ".join(final_tokens)
