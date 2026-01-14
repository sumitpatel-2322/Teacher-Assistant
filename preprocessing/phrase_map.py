"""
Phrase-level normalization.
Maps multiple surface expressions to canonical signals.
NO situation detection here.
"""

PHRASE_MAP = {
    # attention related
    "not listening": "low_attention_signal",
    "not paying attention": "low_attention_signal",
    "no attention": "low_attention_signal",
    "students distracted": "low_attention_signal",
    "class distracted": "low_attention_signal",

    # silence / no response
    "silent class": "silent_class_signal",
    "students are silent": "silent_class_signal",
    "no one answering": "unresponsive_class_signal",
    "not responding": "unresponsive_class_signal",

    # confusion
    "students confused": "confusion_signal",
    "dont understand": "confusion_signal",
    "not clear": "confusion_signal",
    "instruction not clear": "confusion_signal",

    # noise
    "too much noise": "noise_spike_signal",
    "class noisy": "noise_spike_signal",
    "students shouting": "noise_spike_signal",

    # writing / task block
    "not writing": "writing_block_signal",
    "cant start writing": "writing_block_signal",
    "stuck writing": "writing_block_signal",

    # engagement / motivation
    "students bored": "low_engagement_signal",
    "class bored": "low_engagement_signal",
    "not interested": "low_engagement_signal",

    # fatigue
    "students tired": "fatigue_signal",
    "class tired": "fatigue_signal",
}