"""
Math Instructional Concept Library
---------------------------------
This file contains ALL math-related instructional solutions.

Scope:
- Topic-specific (fractions, geometry, ratios, etc.)
- Class-range aware
- Prerequisite-aware
- Includes BOTH:
  1. Instructional / conceptual explanations
  2. Psychological reassurance & confidence-building teacher moves

Design philosophy:
- Explain concepts without becoming a textbook
- Support students emotionally before pushing correctness
- Concrete → pictorial → abstract progression
- Offline-first, teacher-action focused
"""

MATH_INSTRUCTIONAL_SOLUTIONS = [

    # =========================================================
    # GEOMETRY — 2D vs 3D (Circle vs Sphere)
    # =========================================================

    {
        "solution_id": "circle_vs_sphere_object_comparison",
        "subject": "MATH",
        "topic": "GEOMETRY_2D_3D",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "prerequisites": ["SHAPE_RECOGNITION"],

        "approach": "CONCRETE_TO_PICTORIAL",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Circle vs Sphere using Real Objects",
            "action_text": "Use flat and solid objects to show the difference between a circle and a sphere."
        },

        "details": {
            "objective": "Help students distinguish between flat (2D) and solid (3D) shapes",
            "steps": [
                "Draw a circle on the board",
                "Show a bangle or coin and let students touch it",
                "Show a ball and let students roll it",
                "Ask which one rolls and which stays flat",
                "Explain: circle is flat (2D), sphere is solid (3D)"
            ]
        }
    },

    {
        "solution_id": "normalize_confusion_geometry",
        "subject": "MATH",
        "topic": "GEOMETRY_2D_3D",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION", "MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Normalize Geometry Confusion",
            "action_text": "Reassure students that confusing 2D and 3D shapes is common."
        },

        "details": {
            "objective": "Reduce anxiety so students are mentally ready to understand shapes",
            "steps": [
                "Tell students that many learners confuse these shapes initially",
                "Clarify that mistakes are part of learning",
                "Pause evaluation or correction briefly",
                "Encourage students to try again without fear",
                "Resume explanation once students appear relaxed"
            ]
        }
    },

    {
        "solution_id": "confidence_before_correctness_geometry",
        "subject": "MATH",
        "topic": "GEOMETRY_2D_3D",
        "class_range": "CLASS_3_5",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "CONFIDENCE_REBUILDING",

        "preview": {
            "title": "Confidence Before Correctness",
            "action_text": "Build student confidence before focusing on correct answers."
        },

        "details": {
            "objective": "Prevent shutdown by rewarding effort first",
            "steps": [
                "Ask an easy sorting question (flat or solid)",
                "Acknowledge every attempt positively",
                "Avoid immediate correction",
                "Highlight partial understanding",
                "Introduce formal terms only after confidence improves"
            ]
        }
    },

    # =========================================================
    # FRACTIONS — Weak Foundation Support
    # =========================================================

    {
        "solution_id": "fractions_equal_sharing_basic",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["WEAK_FOUNDATION"],
        "prerequisites": ["ADDITION", "SUBTRACTION", "EQUAL_PARTS"],

        "approach": "CONCRETE_TO_PICTORIAL",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Fractions as Equal Sharing",
            "action_text": "Explain fractions by equally sharing objects before using numbers."
        },

        "details": {
            "objective": "Build part–whole understanding",
            "steps": [
                "Use a chapati or paper circle",
                "Divide it equally among students",
                "Ask if everyone got the same amount",
                "Introduce 1/2 or 1/4 after sharing is clear",
                "Avoid formal notation initially"
            ]
        }
    },

    {
        "solution_id": "reduce_fraction_anxiety",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Reduce Fraction Fear",
            "action_text": "Lower anxiety by separating understanding from calculation."
        },

        "details": {
            "objective": "Make fractions feel approachable",
            "steps": [
                "Tell students fractions are about sharing, not calculations",
                "Avoid tests or written work initially",
                "Allow oral responses",
                "Praise reasoning even if answers are incorrect",
                "Move to symbols only after comfort increases"
            ]
        }
    },

    # =========================================================
    # RATIOS — Foundation Bridging
    # =========================================================

    {
        "solution_id": "ratio_as_comparison_story",
        "subject": "MATH",
        "topic": "RATIO_PROPORTION",
        "class_range": "CLASS_5_7",

        "student_profile": ["WEAK_FOUNDATION"],
        "prerequisites": ["FRACTIONS", "MULTIPLICATION"],

        "approach": "STORY_BASED",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Ratios as Simple Comparisons",
            "action_text": "Explain ratios using everyday comparison stories."
        },

        "details": {
            "objective": "Introduce ratios without formulas",
            "steps": [
                "Use examples like boys vs girls in class",
                "Ask which group is more without numbers",
                "Introduce ratio language verbally",
                "Avoid symbols like ':' initially",
                "Only formalize after conceptual clarity"
            ]
        }
    },

    {
        "solution_id": "reassure_before_ratio_formulas",
        "subject": "MATH",
        "topic": "RATIO_PROPORTION",
        "class_range": "CLASS_5_7",

        "student_profile": ["OVERWHELMED"],
        "instruction_type": "COGNITIVE_LOAD_REDUCTION",

        "preview": {
            "title": "Reassure Before Ratio Formulas",
            "action_text": "Reduce overload by delaying symbolic representation."
        },

        "details": {
            "objective": "Prevent early confusion and shutdown",
            "steps": [
                "Tell students formulas are not required yet",
                "Focus only on comparison meaning",
                "Use verbal explanations",
                "Confirm understanding before writing",
                "Introduce symbols at the very end"
            ]
        }
    },
        # =========================================================
    # PLACE VALUE — Weak Number Sense (Class 2–4)
    # =========================================================

    {
        "solution_id": "place_value_building_blocks",
        "subject": "MATH",
        "topic": "PLACE_VALUE",
        "class_range": "CLASS_2_4",

        "student_profile": ["WEAK_FOUNDATION", "CONCEPT_CONFUSION"],
        "prerequisites": ["COUNTING", "GROUPING"],

        "approach": "CONCRETE_TO_PICTORIAL",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Place Value with Grouping",
            "action_text": "Build place value understanding using groups of tens and ones."
        },

        "details": {
            "objective": "Help students understand tens and ones meaningfully",
            "steps": [
                "Give students loose objects (stones, sticks)",
                "Group them in sets of ten",
                "Label each group as one 'ten'",
                "Show remaining objects as 'ones'",
                "Relate the grouping to written numbers"
            ]
        }
    },

    {
        "solution_id": "reduce_place_value_anxiety",
        "subject": "MATH",
        "topic": "PLACE_VALUE",
        "class_range": "CLASS_2_4",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Reduce Place Value Anxiety",
            "action_text": "Reassure students that confusion in place value is common."
        },

        "details": {
            "objective": "Lower fear around large numbers",
            "steps": [
                "Tell students large numbers are just small numbers grouped",
                "Avoid time pressure",
                "Encourage verbal explanation instead of written answers",
                "Praise effort, not speed",
                "Reintroduce written form slowly"
            ]
        }
    },

    # =========================================================
    # DECIMALS — Transition from Whole Numbers (Class 4–6)
    # =========================================================

    {
        "solution_id": "decimals_as_extended_fractions",
        "subject": "MATH",
        "topic": "DECIMALS",
        "class_range": "CLASS_4_6",

        "student_profile": ["CONCEPT_CONFUSION"],
        "prerequisites": ["FRACTIONS", "PLACE_VALUE"],

        "approach": "PICTORIAL",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Decimals as Parts of One",
            "action_text": "Explain decimals as extensions of fractions and place value."
        },

        "details": {
            "objective": "Build intuition for decimals",
            "steps": [
                "Draw a square and divide into ten equal parts",
                "Shade parts to represent tenths",
                "Link shaded parts to decimal notation",
                "Compare shaded fractions and decimals",
                "Avoid operations initially"
            ]
        }
    },

    {
        "solution_id": "confidence_bridge_decimals",
        "subject": "MATH",
        "topic": "DECIMALS",
        "class_range": "CLASS_4_6",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "CONFIDENCE_REBUILDING",

        "preview": {
            "title": "Confidence Bridge for Decimals",
            "action_text": "Build confidence before introducing decimal calculations."
        },

        "details": {
            "objective": "Prevent fear during transition to decimals",
            "steps": [
                "Connect decimals to familiar fractions",
                "Allow students to explain in words",
                "Delay written calculations",
                "Validate partial understanding",
                "Gradually introduce numeric operations"
            ]
        }
    },

    # =========================================================
    # BASIC ALGEBRA — Variables Introduction (Class 5–7)
    # =========================================================

    {
        "solution_id": "variables_as_empty_boxes",
        "subject": "MATH",
        "topic": "BASIC_ALGEBRA",
        "class_range": "CLASS_5_7",

        "student_profile": ["CONCEPT_CONFUSION"],
        "prerequisites": ["ADDITION", "SUBTRACTION"],

        "approach": "REPRESENTATIONAL",
        "instruction_type": "CONCEPT_CLARIFICATION",

        "preview": {
            "title": "Variables as Empty Boxes",
            "action_text": "Introduce variables as unknown values using simple boxes."
        },

        "details": {
            "objective": "Demystify variables",
            "steps": [
                "Draw a box instead of a letter",
                "Write simple equations with boxes",
                "Ask students to guess the missing number",
                "Replace the box with a letter later",
                "Reassure students that letters just stand for numbers"
            ]
        }
    },

    {
        "solution_id": "algebra_anxiety_normalization",
        "subject": "MATH",
        "topic": "BASIC_ALGEBRA",
        "class_range": "CLASS_5_7",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Normalize Algebra Anxiety",
            "action_text": "Reduce fear by normalizing difficulty with letters in math."
        },

        "details": {
            "objective": "Lower resistance to algebra",
            "steps": [
                "Tell students many people fear letters in math at first",
                "Explain that algebra builds on arithmetic they already know",
                "Encourage guessing and checking",
                "Avoid correcting harshly",
                "Reinforce that mistakes help learning"
            ]
        }
    },
        # =========================================================
    # GEOMETRY — 2D vs 3D (DIAGNOSTIC)
    # =========================================================

    {
        "solution_id": "geometry_2d_3d_diagnostic_flat_vs_solid",
        "subject": "MATH",
        "topic": "GEOMETRY_2D_3D",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Flat vs Solid Check",
            "action_text": "Identify whether confusion is about depth, movement, or drawing."
        },

        "details": {
            "objective": "Diagnose the exact source of 2D vs 3D confusion",
            "steps": [
                "Show a drawn circle and a ball",
                "Ask: which one can roll?",
                "Ask: which one can you draw without lifting your pencil?",
                "Observe student reasoning before explaining",
                "Choose explanation based on response"
            ]
        }
    },

    # =========================================================
    # FRACTIONS — DIAGNOSTIC SOLUTIONS
    # =========================================================

    {
        "solution_id": "fractions_diagnostic_equal_parts",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["WEAK_FOUNDATION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Equal Parts Check",
            "action_text": "Check whether the student understands equal sharing."
        },

        "details": {
            "objective": "Identify gaps in equal grouping understanding",
            "steps": [
                "Draw a shape on the board",
                "Ask the student to divide it into equal parts",
                "Observe whether parts are equal",
                "If unequal, revisit grouping before fractions",
                "Do not introduce symbols yet"
            ]
        }
    },

    {
        "solution_id": "fractions_diagnostic_denominator_trap",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Bigger Number Trap",
            "action_text": "Check if the student thinks larger denominator means larger fraction."
        },

        "details": {
            "objective": "Detect denominator size misconception",
            "steps": [
                "Ask: which is bigger, 1/2 or 1/4?",
                "Listen to the explanation, not just the answer",
                "If student says 1/4 is bigger, address part-size meaning",
                "Use visual comparison next",
                "Delay calculations"
            ]
        }
    },

    # =========================================================
    # RATIOS — DIAGNOSTIC SOLUTIONS
    # =========================================================

    {
        "solution_id": "ratios_diagnostic_comparison_without_numbers",
        "subject": "MATH",
        "topic": "RATIO_PROPORTION",
        "class_range": "CLASS_5_7",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Comparison Without Numbers",
            "action_text": "Check if the student understands comparison conceptually."
        },

        "details": {
            "objective": "Diagnose whether confusion is conceptual or symbolic",
            "steps": [
                "Ask verbally: are there more boys or girls in class?",
                "Do not use numbers or symbols",
                "If student hesitates, comparison concept is weak",
                "Use real-life comparisons before ratios",
                "Avoid introducing ':' symbol initially"
            ]
        }
    },

    {
        "solution_id": "ratios_diagnostic_ratio_vs_fraction",
        "subject": "MATH",
        "topic": "RATIO_PROPORTION",
        "class_range": "CLASS_5_7",

        "student_profile": ["OVERWHELMED"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Ratio vs Fraction Check",
            "action_text": "Check if the student confuses ratios with fractions."
        },

        "details": {
            "objective": "Identify symbol-level confusion",
            "steps": [
                "Ask if 2:3 means the same as 2/3",
                "Listen for explanation",
                "If confused, strip symbols and explain comparison",
                "Delay written representation",
                "Reintroduce notation later"
            ]
        }
    },

    # =========================================================
    # PLACE VALUE — DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "place_value_diagnostic_grouping_check",
        "subject": "MATH",
        "topic": "PLACE_VALUE",
        "class_range": "CLASS_2_4",

        "student_profile": ["WEAK_FOUNDATION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Grouping Check",
            "action_text": "Check whether the student understands grouping into tens."
        },

        "details": {
            "objective": "Detect absence of grouping intuition",
            "steps": [
                "Ask the student to make 23 using objects",
                "Observe if they group into tens",
                "If counting individually, revisit grouping",
                "Use bundles to explain tens",
                "Delay written numbers"
            ]
        }
    },

    # =========================================================
    # DECIMALS — PSYCHOLOGICAL + DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "decimals_psych_normalize_dot_fear",
        "subject": "MATH",
        "topic": "DECIMALS",
        "class_range": "CLASS_4_6",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Normalize Decimal Fear",
            "action_text": "Reduce fear caused by the decimal point."
        },

        "details": {
            "objective": "Lower anxiety around decimal notation",
            "steps": [
                "Tell students decimals are just another way of writing parts",
                "Avoid calculations initially",
                "Use verbal explanations first",
                "Reassure that confusion is common",
                "Proceed slowly to symbols"
            ]
        }
    },

    {
        "solution_id": "decimals_diagnostic_magnitude_confusion",
        "subject": "MATH",
        "topic": "DECIMALS",
        "class_range": "CLASS_4_6",

        "student_profile": ["CONCEPT_CONFUSION"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Decimal Size Check",
            "action_text": "Check whether the student understands decimal magnitude."
        },

        "details": {
            "objective": "Detect confusion about decimal size",
            "steps": [
                "Ask which is bigger: 0.5 or 0.25",
                "Ask the student to explain why",
                "If confused, relate decimals to fractions",
                "Use visual models",
                "Delay operations"
            ]
        }
    },

    # =========================================================
    # ALGEBRA — DIAGNOSTIC
    # =========================================================

    {
        "solution_id": "algebra_diagnostic_letter_fear",
        "subject": "MATH",
        "topic": "BASIC_ALGEBRA",
        "class_range": "CLASS_5_7",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "DIAGNOSTIC",

        "preview": {
            "title": "Letter Fear Check",
            "action_text": "Check if difficulty is due to fear of letters."
        },

        "details": {
            "objective": "Separate logical understanding from symbol fear",
            "steps": [
                "Replace variables with empty boxes",
                "Ask student to solve",
                "If successful, fear is symbolic",
                "Reintroduce letters slowly",
                "Reassure that letters represent numbers"
            ]
        }
    },
        # =========================================================
    # FRACTIONS — PSYCHOLOGICAL (CONFIDENCE & OVERWHELM)
    # =========================================================

    {
        "solution_id": "fractions_psych_confidence_first_success",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "CONFIDENCE_REBUILDING",

        "preview": {
            "title": "Early Success First",
            "action_text": "Build confidence before formal fraction teaching."
        },

        "details": {
            "objective": "Prevent shutdown by ensuring early success",
            "steps": [
                "Ask a very easy sharing question",
                "Acknowledge the correct response clearly",
                "Avoid introducing symbols immediately",
                "Reinforce that the student already understands the idea",
                "Proceed gradually to fraction notation"
            ]
        }
    },

    {
        "solution_id": "fractions_psych_reduce_overload",
        "subject": "MATH",
        "topic": "FRACTIONS",
        "class_range": "CLASS_3_5",

        "student_profile": ["OVERWHELMED"],
        "instruction_type": "COGNITIVE_LOAD_REDUCTION",

        "preview": {
            "title": "Remove Symbols Temporarily",
            "action_text": "Reduce overload by removing numbers and symbols."
        },

        "details": {
            "objective": "Lower cognitive pressure during learning",
            "steps": [
                "Avoid writing fractions on the board initially",
                "Use only words like half and quarter",
                "Check understanding orally",
                "Introduce symbols only after comfort increases",
                "Keep pace slow and predictable"
            ]
        }
    },

    # =========================================================
    # GEOMETRY — PSYCHOLOGICAL (ANXIETY)
    # =========================================================

    {
        "solution_id": "geometry_psych_normalize_spatial_confusion",
        "subject": "MATH",
        "topic": "GEOMETRY_2D_3D",
        "class_range": "CLASS_3_5",

        "student_profile": ["MATH_ANXIETY"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Normalize Spatial Confusion",
            "action_text": "Reassure students that shape confusion is common."
        },

        "details": {
            "objective": "Reduce anxiety related to spatial concepts",
            "steps": [
                "Tell students many people confuse flat and solid shapes",
                "Share that mistakes are expected while learning",
                "Pause correction briefly",
                "Encourage trying without fear",
                "Proceed to explanation once relaxed"
            ]
        }
    },

    # =========================================================
    # RATIOS — PSYCHOLOGICAL (CONFIDENCE)
    # =========================================================

    {
        "solution_id": "ratios_psych_confidence_before_symbols",
        "subject": "MATH",
        "topic": "RATIO_PROPORTION",
        "class_range": "CLASS_5_7",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "CONFIDENCE_REBUILDING",

        "preview": {
            "title": "Confidence Before Ratio Symbols",
            "action_text": "Build comfort with comparison before notation."
        },

        "details": {
            "objective": "Prevent fear caused by ratio notation",
            "steps": [
                "Use verbal comparison examples",
                "Confirm understanding without numbers",
                "Praise correct reasoning",
                "Delay ':' symbol introduction",
                "Transition slowly to written ratios"
            ]
        }
    },

    # =========================================================
    # PLACE VALUE — PSYCHOLOGICAL (OVERWHELM)
    # =========================================================

    {
        "solution_id": "place_value_psych_reduce_number_fear",
        "subject": "MATH",
        "topic": "PLACE_VALUE",
        "class_range": "CLASS_2_4",

        "student_profile": ["OVERWHELMED"],
        "instruction_type": "PSYCHOLOGICAL_REASSURANCE",

        "preview": {
            "title": "Reduce Fear of Large Numbers",
            "action_text": "Make large numbers feel manageable."
        },

        "details": {
            "objective": "Lower anxiety related to big numbers",
            "steps": [
                "Explain large numbers as small groups combined",
                "Avoid time pressure",
                "Use physical grouping",
                "Encourage verbal explanation",
                "Gradually move to written form"
            ]
        }
    },

    # =========================================================
    # DECIMALS — PSYCHOLOGICAL (CONFIDENCE)
    # =========================================================

    {
        "solution_id": "decimals_psych_confidence_gradual_symbols",
        "subject": "MATH",
        "topic": "DECIMALS",
        "class_range": "CLASS_4_6",

        "student_profile": ["LOW_CONFIDENCE"],
        "instruction_type": "CONFIDENCE_REBUILDING",

        "preview": {
            "title": "Gradual Introduction of Decimal Symbols",
            "action_text": "Introduce decimals slowly to build confidence."
        },

        "details": {
            "objective": "Support students during transition to decimals",
            "steps": [
                "Begin with fractions the student knows",
                "Relate fractions to decimals verbally",
                "Avoid written decimals initially",
                "Praise partial understanding",
                "Introduce decimal notation at the end"
            ]
        }
    }
]