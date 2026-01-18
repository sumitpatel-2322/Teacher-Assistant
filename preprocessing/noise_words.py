"""
Noise words to remove during normalization.
Negations like 'not', 'no', 'never' are intentionally excluded.
"""
print("\n>>> DEBUG: [Import] preprocessing/noise_words.py loaded")
NOISE_WORDS = {
    "please",
    "sir",
    "mam",
    "actually",
    "basically",
    "kind",
    "of",
    "uh",
    "um",
    "umm",
    "hey",
    "ok",
    "okay",
}
