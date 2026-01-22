"""
Language Instructional Solution Library
--------------------------------------
Curated demo-ready solutions covering:
- Concept clarification (reading, writing, grammar)
- Psychological reassurance (confidence, fear of language)
- Diagnostic checks (where language breaks down)

Scope:
- Offline-first
- Class-aware
- Focus on usable teacher moves, not worksheets
"""

LANGUAGE_INSTRUCTIONAL_SOLUTIONS = [

    # =========================================================
    # READING COMPREHENSION — BASIC MEANING
    # =========================================================

    {
        "solution_id": "reading_find_meaning_not_words",
        "subject": "LANGUAGE",
        "topic": "READING_COMPREHENSION",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Meaning Over Words",
            "action_text": "Shift focus from reading words to understanding meaning."
        },

        "details": {
            "objective": "Help students understand what they read",
            "steps": [
                "Ask student to read a short paragraph",
                "Ask: what happened in the story?",
                "Ignore pronunciation mistakes initially",
                "Focus on idea and sequence",
                "Correct language later"
            ]
        }
    },

    {
        "solution_id": "reading_psych_remove_fear",
        "subject": "LANGUAGE",
        "topic": "READING_COMPREHENSION",
        "class_range": "CLASS_3_5",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "It’s Okay to Read Slowly",
            "action_text": "Reduce fear associated with reading aloud."
        },

        "details": {
            "objective": "Lower anxiety around reading",
            "steps": [
                "Tell students speed is not important",
                "Allow silent reading first",
                "Praise effort, not fluency",
                "Avoid public correction",
                "Build comfort before accuracy"
            ]
        }
    },

    # =========================================================
    # READING COMPREHENSION — DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "reading_diagnostic_main_idea",
        "subject": "LANGUAGE",
        "topic": "READING_COMPREHENSION",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Main Idea Check",
            "action_text": "Check if the student understands the core idea."
        },

        "details": {
            "objective": "Identify whether difficulty is with meaning or decoding",
            "steps": [
                "Ask student to explain the paragraph in one sentence",
                "If they can, meaning is intact",
                "If not, re-read together",
                "Clarify idea before vocabulary",
                "Avoid grammar focus"
            ]
        }
    },

    # =========================================================
    # WRITING — SENTENCE FORMATION
    # =========================================================

    {
        "solution_id": "writing_sentence_thinking_first",
        "subject": "LANGUAGE",
        "topic": "SENTENCE_WRITING",
        "class_range": "CLASS_3_5",

        "student_profile": ["WEAK_FOUNDATION"],
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Think Then Write",
            "action_text": "Help students think before writing sentences."
        },

        "details": {
            "objective": "Improve sentence formation",
            "steps": [
                "Ask student to say the sentence aloud",
                "Help reorder words verbally",
                "Write only after sentence sounds correct",
                "Avoid grammar rules initially",
                "Refine later"
            ]
        }
    },

    # =========================================================
    # WRITING — PSYCHOLOGICAL
    # =========================================================

    {
        "solution_id": "writing_psych_remove_mistake_fear",
        "subject": "LANGUAGE",
        "topic": "SENTENCE_WRITING",
        "class_range": "CLASS_3_5",

        "student_profile": ["MATH_ANXIETY"],  # reused as general academic anxiety
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Mistakes Are Allowed",
            "action_text": "Reduce fear of writing wrong sentences."
        },

        "details": {
            "objective": "Encourage writing attempts",
            "steps": [
                "Tell students first draft can be wrong",
                "Avoid red-pen correction initially",
                "Focus on idea, not spelling",
                "Praise effort",
                "Correct gently later"
            ]
        }
    },

    # =========================================================
    # GRAMMAR — PARTS OF SPEECH (DIAGNOSTIC)
    # =========================================================

    {
        "solution_id": "grammar_diagnostic_word_function",
        "subject": "LANGUAGE",
        "topic": "GRAMMAR_PARTS_OF_SPEECH",
        "class_range": "CLASS_4_6",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "What Is This Word Doing?",
            "action_text": "Check understanding of word function."
        },

        "details": {
            "objective": "Identify confusion between naming and function",
            "steps": [
                "Underline a word in a sentence",
                "Ask what job the word is doing",
                "If naming fails, explain role first",
                "Avoid rule definitions",
                "Introduce term later"
            ]
        }
    },
        # =========================================================
    # READING — FLUENCY & EXPRESSION
    # =========================================================

    {
        "solution_id": "reading_fluency_phrase_chunks",
        "subject": "LANGUAGE",
        "topic": "READING_FLUENCY",
        "class_range": "CLASS_3_5",

        "student_profile": ["WEAK_FOUNDATION"],
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Read in Small Chunks",
            "action_text": "Improve fluency by grouping words into phrases."
        },

        "details": {
            "objective": "Help students read smoothly without word-by-word struggle",
            "steps": [
                "Mark short phrases in a sentence",
                "Ask student to read phrase by phrase",
                "Model expressive reading",
                "Avoid speed correction",
                "Gradually increase phrase length"
            ]
        }
    },

    {
        "solution_id": "reading_psych_remove_speed_pressure",
        "subject": "LANGUAGE",
        "topic": "READING_FLUENCY",
        "class_range": "CLASS_3_5",

        "student_profile": ["OVERWHELMED"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Reading Is Not a Race",
            "action_text": "Reduce pressure to read fast."
        },

        "details": {
            "objective": "Lower anxiety caused by speed comparison",
            "steps": [
                "Tell students everyone reads at different speeds",
                "Avoid timed reading",
                "Allow silent practice",
                "Praise steady improvement",
                "Focus on clarity over speed"
            ]
        }
    },

    # =========================================================
    # READING — DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "reading_diagnostic_decode_vs_understand",
        "subject": "LANGUAGE",
        "topic": "READING_FLUENCY",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Decoding or Understanding?",
            "action_text": "Check whether difficulty is with reading or comprehension."
        },

        "details": {
            "objective": "Separate decoding issues from comprehension issues",
            "steps": [
                "Read a sentence aloud to the student",
                "Ask them to explain meaning",
                "If meaning is clear, decoding is the issue",
                "If not, work on comprehension",
                "Choose next step accordingly"
            ]
        }
    },

    # =========================================================
    # WRITING — PARAGRAPH FORMATION
    # =========================================================

    {
        "solution_id": "writing_paragraph_one_idea",
        "subject": "LANGUAGE",
        "topic": "PARAGRAPH_WRITING",
        "class_range": "CLASS_4_6",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "One Idea, One Paragraph",
            "action_text": "Help students focus paragraphs around a single idea."
        },

        "details": {
            "objective": "Improve paragraph coherence",
            "steps": [
                "Ask student to say the main idea",
                "List 2–3 supporting points verbally",
                "Write sentences only for those points",
                "Avoid grammar correction initially",
                "Refine structure later"
            ]
        }
    },

    # =========================================================
    # WRITING — DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "writing_diagnostic_idea_vs_language",
        "subject": "LANGUAGE",
        "topic": "PARAGRAPH_WRITING",
        "class_range": "CLASS_4_6",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Idea or Language Problem?",
            "action_text": "Check whether difficulty is idea generation or language."
        },

        "details": {
            "objective": "Identify root cause of writing difficulty",
            "steps": [
                "Ask student to explain idea orally",
                "If idea is clear, language is the issue",
                "If idea is unclear, help brainstorm",
                "Avoid writing immediately",
                "Address root cause first"
            ]
        }
    },

    # =========================================================
    # GRAMMAR — TENSES (INSTRUCTIONAL)
    # =========================================================

    {
        "solution_id": "grammar_tense_time_line",
        "subject": "LANGUAGE",
        "topic": "GRAMMAR_TENSES",
        "class_range": "CLASS_4_6",

        "student_profile": ["PARTIAL_UNDERSTANDING"],
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Past, Present, Future Line",
            "action_text": "Explain tenses using a time line."
        },

        "details": {
            "objective": "Build intuitive understanding of tenses",
            "steps": [
                "Draw a simple time line",
                "Place yesterday, today, tomorrow",
                "Match sentences to each",
                "Avoid tense rules initially",
                "Introduce terms after clarity"
            ]
        }
    },

    # =========================================================
    # GRAMMAR — PSYCHOLOGICAL
    # =========================================================

    {
        "solution_id": "grammar_psych_rules_not_first",
        "subject": "LANGUAGE",
        "topic": "GRAMMAR_TENSES",
        "class_range": "CLASS_4_6",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Meaning Before Rules",
            "action_text": "Reduce fear caused by grammar rules."
        },

        "details": {
            "objective": "Lower anxiety around grammar",
            "steps": [
                "Tell students rules come later",
                "Focus on meaning of sentence",
                "Allow speaking before writing",
                "Avoid rule-heavy correction",
                "Introduce rules gradually"
            ]
        }
    },
    
]
