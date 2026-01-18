"""
Layer 2: Rule-based Situation Detection
Maps signals (keywords/phrases) to Master Situations & Constraints.
Optimized for ALL tags found in the Solution Library (Instructional, FLN, Reddit, etc.).
"""

print("\n>>> DEBUG: [Import] decision_engine/situation_detector.py loaded")  # <--- DEBUG LINE

# Comprehensive Mapping based on FULL Solution Library Scan
SIGNAL_RULES = {
    # ==========================================
    # 1. CORE INSTRUCTIONAL MOMENTS (The "When")
    # ==========================================
    "start": "TASK_INITIATION",
    "begin": "TASK_INITIATION",
    "how to start": "TASK_INITIATION",
    "blank page": "WRITING_BLOCK",
    "stuck": "TASK_STALL",
    "transition": "MESSY_TRANSITION",
    "switch": "MESSY_TRANSITION",
    "moving": "MESSY_TRANSITION",
    "end of class": "END_OF_CLASS_DRIFT",
    "last minute": "END_OF_CLASS_DRIFT",
    "wrap up": "END_OF_CLASS_DRIFT",
    "finish": "EARLY_FINISHERS",
    "done": "EARLY_FINISHERS",
    "fast": "EARLY_FINISHERS",

    # ==========================================
    # 2. COGNITIVE STATES (The "Why")
    # ==========================================
    "confused": "CONFUSION",
    "don't understand": "CONFUSION",
    "lost": "MID_LESSON_CONFUSION",
    "blank face": "MID_LESSON_CONFUSION",
    "too much": "INFORMATION_OVERLOAD",
    "overwhelm": "INFORMATION_OVERLOAD",
    "forget": "LOW_RECALL",
    "recall": "LOW_RECALL",
    "remember": "LOW_RECALL",
    "slow": "PROCESSING_LAG",
    "lag": "PROCESSING_LAG",
    "tired": "FATIGUE",
    "sleepy": "FATIGUE",
    "boring": "BOREDOM",
    "bored": "BOREDOM",
    "give up": "LOW_MOTIVATION",
    "don't care": "LOW_MOTIVATION",
    "guessing": "RANDOM_ATTEMPTS",
    "random": "RANDOM_ATTEMPTS",

    # ==========================================
    # 3. CLASSROOM BEHAVIOR & MANAGEMENT
    # ==========================================
    "noise": "HIGH_NOISE",
    "noisy": "HIGH_NOISE",
    "loud": "HIGH_NOISE",
    "talk": "SIDE_TALK",
    "chat": "SIDE_TALK",
    "whisper": "SIDE_TALK",
    "defiant": "DISRESPECT_DEFIANCE",
    "rude": "DISRESPECT_DEFIANCE",
    "argue": "DISRESPECT_DEFIANCE",
    "no": "DISRESPECT_DEFIANCE",
    "interrupt": "INTERRUPTIONS",
    "question": "QUESTION_PILEUP",
    "ask": "QUESTION_PILEUP",
    "bathroom": "LOGISTICAL_CHAOS",
    "water": "LOGISTICAL_CHAOS",
    "pencil": "LOGISTICAL_CHAOS",
    "distracted": "DISTRACTIBILITY",
    "focus": "LOSS_OF_FOCUS",
    "fidget": "RESTLESSNESS",
    "sit still": "RESTLESSNESS",
    "can't sit": "RESTLESSNESS",
    "restless": "RESTLESSNESS",
    "adhd": "SHORT_ATTENTION_SPAN",
    "hyper": "OVERSTIMULATION",
    "excited": "OVERSTIMULATION",
    "quiet": "SILENT_CLASS",
    "silent": "SILENT_CLASS",
    "no answer": "UNRESPONSIVE_CLASS",

    # ==========================================
    # 4. ACADEMIC SPECIFICS (Subject Tags)
    # ==========================================
    # --- MATH ---
    "geometry": "GEOMETRY_2D_3D",
    "shape": "GEOMETRY_2D_3D",
    "circle": "GEOMETRY_2D_3D",
    "fraction": "FRACTIONS",
    "ratio": "RATIO_PROPORTION",
    "decimal": "DECIMALS",
    "point": "DECIMALS",
    "place value": "PLACE_VALUE",
    "tens": "PLACE_VALUE",
    "algebra": "BASIC_ALGEBRA",
    "variable": "BASIC_ALGEBRA",
    "x and y": "BASIC_ALGEBRA",
    "word problem": "MATH_DIFFICULTY",
    "count": "MATH_DIFFICULTY",

    # --- SCIENCE ---
    "experiment": "NO_LAB_EQUIPMENT",
    "lab": "NO_LAB_EQUIPMENT",
    "plant": "PLANTS_FUNCTIONS",
    "space": "ASTRONOMY",
    "sun": "ASTRONOMY",
    "body": "HUMAN_BODY",
    "heart": "HUMAN_BODY",
    "chemical": "NO_LAB_EQUIPMENT",

    # --- LANGUAGE ---
    "write": "WRITING_DIFFICULTY",
    "handwriting": "WRITING_DIFFICULTY",
    "spell": "READING_LANGUAGE_ISSUE",
    "read": "READING_LANGUAGE_ISSUE",
    "grammar": "GRAMMAR_ISSUES",
    "speak": "FEAR_OF_SPEAKING",
    "quiet": "SHYNESS",
    "shy": "SHYNESS",

    # ==========================================
    # 5. TEACHER PAIN POINTS
    # ==========================================
    "grade": "GRADING_OVERLOAD",
    "check": "GRADING_OVERLOAD",
    "marking": "GRADING_OVERLOAD",
    "parent": "ANGRY_PARENT",
    "complain": "ANGRY_PARENT",
    "upset": "ANGRY_PARENT",
    "blame": "ANGRY_PARENT",
    "admin": "ADMIN_STRESS",
    "plan": "LESSON_PLANNING",
    "time": "TIME_MANAGEMENT",
    "late": "TIME_MANAGEMENT",
    "rush": "TIME_MANAGEMENT",
    "pacing": "TIME_MANAGEMENT",
    "never enough time": "TIME_MANAGEMENT",
    "large": "LARGE_CLASS_SIZE",
    "crowd": "LARGE_CLASS_SIZE",
    "50": "LARGE_CLASS_SIZE",
    "60": "LARGE_CLASS_SIZE",
    
    # ==========================================
    # 6. COLLABORATIVE & PEDAGOGICAL KEYWORDS
    # ==========================================
    # Group work & collaboration
    "group": "MIXED_LEVELS",
    "project": "MIXED_LEVELS",
    "partner": "MIXED_LEVELS",
    "teamwork": "MIXED_LEVELS",
    "collaborate": "MIXED_LEVELS",
    "cooperative": "MIXED_LEVELS",
    
    # Confidence & participation
    "quiet": "SHYNESS_LOW_CONFIDENCE",
    "raises hand": "SHYNESS_LOW_CONFIDENCE",
    "confidence": "SHYNESS_LOW_CONFIDENCE",
    "participat": "SHYNESS_LOW_CONFIDENCE",
    "reluctant": "SHYNESS_LOW_CONFIDENCE",
    "withdrawn": "SHYNESS_LOW_CONFIDENCE",
    
    # Differentiation
    "finish": "MIXED_LEVELS",
    "early": "MIXED_LEVELS",
    "slow": "MIXED_LEVELS",
    "pace": "TIME_MANAGEMENT",
    "minutes": "TIME_MANAGEMENT",
    
    # Explanation & teaching
    "explain": "CONCEPT_CONFUSION",
    "tough topic": "CONCEPT_CONFUSION",
    "struggling": "CONCEPT_CONFUSION",
    "understand": "CONCEPT_CONFUSION",
    "teach": "CONCEPT_CONFUSION",
    
    # Interruptions & turn-taking
    "talking over": "INTERRUPTIONS",
    "interrupt": "INTERRUPTIONS",
    "finish thought": "INTERRUPTIONS",
    "turn taking": "INTERRUPTIONS",
    
    # ==========================================
    # GROUP PROJECT & COLLABORATIVE LEARNING
    # ==========================================
    "group project": "GROUP_PROJECT",
    "group work": "GROUP_PROJECT",
    "collaborative": "GROUP_PROJECT",
    "teamwork": "GROUP_PROJECT",
    "team": "GROUP_PROJECT",
    "partner work": "GROUP_PROJECT",
    "cooperative": "GROUP_PROJECT",
    "collaboration": "GROUP_PROJECT",

    # ==========================================
    # 6. PHRASE-MAPPED SIGNAL TOKENS (from preprocessing/phrase_map.py)
    # These intermediate signals bridge preprocessing output to situation detection
    # ==========================================
    # Classroom Chaos signals → CLASSROOM_CHAOS
    "chaos_signal": "CLASSROOM_CHAOS",
    
    # Low Engagement signals → BOREDOM / LOW_MOTIVATION
    "boredom_signal": "BOREDOM",
    
    # Low Attention signals → DISTRACTIBILITY / LOSS_OF_FOCUS
    "attention_signal": "LOSS_OF_FOCUS",
    
    # Concept Confusion signals → CONFUSION / MID_LESSON_CONFUSION
    "confusion_signal": "MID_LESSON_CONFUSION",
    
    # Memory Issues signals → LOW_RECALL
    "memory_signal": "LOW_RECALL",
    
    # Writing Issues signals → WRITING_DIFFICULTY
    "writing_signal": "WRITING_DIFFICULTY",
    
    # Reading/Language signals → READING_LANGUAGE_ISSUE
    "reading_signal": "READING_LANGUAGE_ISSUE",
    
    # Math Issues signals → MATH_DIFFICULTY
    "math_signal": "MATH_DIFFICULTY",
    
    # Shyness/Confidence signals → SHYNESS / FEAR_OF_SPEAKING
    "shyness_signal": "FEAR_OF_SPEAKING",
    
    # Time/Transition signals → MESSY_TRANSITION / END_OF_CLASS_DRIFT
    "time_signal": "MESSY_TRANSITION",
    
    # Mixed Levels signals → MIXED_READINESS_LEVELS
    "mixed_signal": "MIXED_READINESS_LEVELS",
    
    # Disrespect/Defiance signals → DISRESPECT_DEFIANCE
    "disrespect_signal": "DISRESPECT_DEFIANCE",
    
    # Home/Parent signals → ANGRY_PARENT (teacher pain point)
    "home_signal": "ANGRY_PARENT",
    
    # Resource signals → CLASSROOM_CHAOS (resource constraints cause chaos)
    "resource_signal": "CLASSROOM_CHAOS",
    
    # Emotional/Wellbeing signals → EMOTIONAL_WELLBEING
    "emotion_signal": "EMOTIONAL_WELLBEING",
}

def detect_situations(normalized_text: str) -> dict:
    """
    Scans the text for keywords and returns a dictionary of detected situations.
    Returns: {situation_id: score}
    """
    # <--- DEBUG START --->
    print(f"\n>>> DEBUG [Situation Detector] Scanning text: '{normalized_text}'")
    # <--- DEBUG END --->

    situation_scores = {}
    if not normalized_text:
        return situation_scores

    text_lower = normalized_text.lower()

    # Direct keyword mapping
    for keyword, situation_tag in SIGNAL_RULES.items():
        if keyword in text_lower:
            # We give a high confidence score for direct matches
            situation_scores[situation_tag] = 1.0
            
            # Smart Inference Chains - COMPREHENSIVE (Enhanced from original)
            
            # Behavioral/Cognitive Cascades
            if situation_tag == "SIDE_TALK":
                situation_scores.setdefault("DISTRACTIBILITY", 0.8)
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.6)
            
            if situation_tag == "QUESTION_PILEUP":
                situation_scores.setdefault("TIME_MANAGEMENT", 0.7)
                situation_scores.setdefault("INTERRUPTIONS", 0.8)
                
            if situation_tag == "WRITING_BLOCK":
                situation_scores.setdefault("TASK_INITIATION", 0.9)
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.7)
                
            if situation_tag == "MID_LESSON_CONFUSION":
                situation_scores.setdefault("CONFUSION", 1.0)
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.8)
            
            # Confusion Detection Enhancement
            if "_CONFUSION" in situation_tag:
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.9)
            
            # NEW: Emotional & Engagement Cascades
            if situation_tag == "FATIGUE":
                situation_scores.setdefault("EMOTIONAL_WELLBEING", 0.85)
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.75)
            
            if situation_tag == "BOREDOM":
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.9)
                situation_scores.setdefault("LOW_MOTIVATION", 0.85)
            
            if situation_tag == "LOW_MOTIVATION":
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.85)
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.6)
            
            # NEW: Task & Time Management Cascades
            if situation_tag == "EARLY_FINISHERS":
                situation_scores.setdefault("MIXED_LEVELS", 0.95)
            
            if situation_tag == "TASK_STALL":
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.85)
                situation_scores.setdefault("LOW_MOTIVATION", 0.75)
            
            if situation_tag == "MESSY_TRANSITION":
                situation_scores.setdefault("TIME_MANAGEMENT", 0.8)
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.7)
            
            if situation_tag == "END_OF_CLASS_DRIFT":
                situation_scores.setdefault("TIME_MANAGEMENT", 0.85)
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.7)
            
            # NEW: Classroom Behavior Cascades
            if situation_tag == "OVERSTIMULATION":
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.8)
                situation_scores.setdefault("EMOTIONAL_WELLBEING", 0.75)
            
            if situation_tag == "RESTLESSNESS":
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.85)
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.7)
            
            if situation_tag == "DISTRACTIBILITY":
                situation_scores.setdefault("LOW_ATTENTION", 0.85)
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.65)
            
            if situation_tag == "SILENT_CLASS":
                situation_scores.setdefault("SHYNESS", 0.8)
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.75)
            
            if situation_tag == "UNRESPONSIVE_CLASS":
                situation_scores.setdefault("LOW_ENGAGEMENT", 0.9)
                situation_scores.setdefault("LOW_ATTENTION", 0.8)
            
            # NEW: Processing & Memory Cascades
            if situation_tag == "PROCESSING_LAG":
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.8)
                situation_scores.setdefault("LOW_RECALL", 0.7)
            
            if situation_tag == "LOW_RECALL":
                situation_scores.setdefault("MEMORY_RETENTION_ISSUE", 0.9)
            
            # NEW: Math Topic Cascades
            if situation_tag in ["GEOMETRY_2D_3D", "FRACTIONS", "RATIO_PROPORTION", "DECIMALS", "PLACE_VALUE", "BASIC_ALGEBRA"]:
                situation_scores.setdefault("MATH_DIFFICULTY", 0.95)
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.85)
            
            # NEW: Science Topic Cascades
            if situation_tag in ["PLANTS_FUNCTIONS", "ASTRONOMY", "HUMAN_BODY"]:
                situation_scores.setdefault("CONCEPT_CONFUSION", 0.9)
            
            # NEW: Language Topic Cascades
            if situation_tag == "GRAMMAR_ISSUES":
                situation_scores.setdefault("READING_LANGUAGE_ISSUE", 0.9)
                situation_scores.setdefault("WRITING_DIFFICULTY", 0.7)
            
            if situation_tag == "FEAR_OF_SPEAKING":
                situation_scores.setdefault("SHYNESS", 0.95)
                situation_scores.setdefault("LOW_CONFIDENCE", 0.85)
            
            if situation_tag == "SHYNESS":
                situation_scores.setdefault("SHYNESS_LOW_CONFIDENCE", 0.95)
            
            # NEW: GROUP PROJECT Cascade
            if situation_tag == "GROUP_PROJECT":
                situation_scores.setdefault("MIXED_LEVELS", 0.95)
                situation_scores.setdefault("CLASSROOM_CHAOS", 0.7)
                situation_scores.setdefault("TIME_MANAGEMENT", 0.6)

    # <--- DEBUG START --->
    if situation_scores:
        print(f">>> DEBUG [Situation Detector] MATCH FOUND: {list(situation_scores.keys())}")
    else:
        print(">>> DEBUG [Situation Detector] NO MATCHES found.")
    # <--- DEBUG END --->

    return situation_scores