import re
from typing import Dict, List
from decision_engine.situation_detector import detect_situations
from preprocessing.normalizer import normalize_text

def extract_signals(text: str) -> Dict[str, Dict[str, float]]:
    """
    Scans the user text for keywords and returns a dictionary of detected situations.
    
    INTEGRATION UPDATE:
    Now combines legacy Regex detection with the robust Keyword Mapping
    from situation_detector.py to ensure specific instructional tags are caught.
    """
    detected_situations = {}
    detected_constraints = {}
    
    text_lower = text.lower()
    
    # CRITICAL FIX: Normalize text BEFORE calling detect_situations
    # This ensures phrase-mapped tokens like "disrespect_signal" are available
    normalized_text = normalize_text(text)

    # ----------------------------------------------------
    # 1. RUN ROBUST KEYWORD DETECTOR (Layer 2 Integration)
    # ----------------------------------------------------
    # This captures specific tags like 'GEOMETRY_2D_3D', 'FRACTIONS', 'ANGRY_PARENT'
    # UPDATED: Pass normalized text so phrase-mapped signals are available
    keyword_matches = detect_situations(normalized_text)
    detected_situations.update(keyword_matches)

    # ----------------------------------------------------
    # 2. RUN LEGACY REGEX CHECKS (Layer 1 Constraints)
    # ----------------------------------------------------
    # Helper function to print debug info
    def check(pattern, label, confidence=1.0, is_constraint=False):
        match = re.search(pattern, text_lower)
        if match:
            print(f"   [SIGNAL FOUND] '{label}' triggered by keyword: '{match.group(0)}'")
            if is_constraint:
                detected_constraints[label] = confidence
            else:
                # Only add if not already detected by robust detector to avoid overwrite
                if label not in detected_situations:
                    detected_situations[label] = confidence
            return True
        return False

    # --- SCIENCE & RURAL CONTEXT ---
    check(r"(no|lack of|without|missing|don'?t have|do not have)\s+.*?(lab|equipment|microscope|chemical|beaker|science kit)", "NO_LAB_EQUIPMENT", 1.0)
    check(r"(electricity|power|internet|wifi|connection|signal)", "NO_ELECTRICITY", 1.0, is_constraint=True)

    # --- INCLUSION & SPECIAL NEEDS ---
    check(r"(slow|behind|lagging|struggle|weak)\s+(learner|student|child|kid)", "SLOW_LEARNER", 1.0)
    check(r"(focus|concentrate|attention|distracted|adhd|sit still|fidget)", "SHORT_ATTENTION_SPAN", 1.0)
    check(r"(blind|deaf|hear|see|vision|auditory|disability|handicap)", "SENSORY_IMPAIRMENT", 1.0)

    # --- PRODUCTIVITY ---
    check(r"(grading|marking|correction|checking)\s+(paper|book|exam|copy|copies|sheet)", "GRADING_OVERLOAD", 1.0)
    check(r"(stress|tired|burnout|exhausted|overwhelm|anxiety|depress|pressure)", "TEACHER_BURNOUT", 1.0)

    # --- CLASSROOM MANAGEMENT ---
    check(r"(large|crowd|many|50|60|70|80)\s+(student|class|kid|children)", "LARGE_CLASS_SIZE", 1.0)
    check(r"(noise|noisy|loud|shout|chaos|talk|chat|disrupt)", "HIGH_NOISE", 1.0)

    # --- FLN & BASICS ---
    check(r"(write|read|spell|letter|alphabet)", "READING_LANGUAGE_ISSUE", 1.0)
    check(r"(math|count|number|add|subtract)", "MATH_ANXIETY", 1.0)
    
    # --- PEDAGOGY ---
    check(r"(explain|teach|concept|understand).*?(cant|cannot|hard|difficult|fail)", "CONCEPT_CONFUSION", 1.0)

    return {
        "situations": detected_situations,
        "constraints": detected_constraints
    }
