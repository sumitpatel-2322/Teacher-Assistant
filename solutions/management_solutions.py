from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

MANAGEMENT_SOLUTIONS = [
    {
        "solution_id": "mgmt_row_captains",
        "version": "1.0",
        "status": "active",
        "situations": ["LARGE_CLASS_SIZE", "LOGISTICAL_CHAOS"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_3_10",
        "topic_type": "CLASSROOM_MANAGEMENT",
        "learning_mode": "DELEGATION",
        "preview": {
            "title": "Row Captains (Monitors)",
            "action_text": "Assign one student per row to collect notebooks or distribute materials."
        },
        "details": {
            "objective": "To reduce distribution time in large classes (50+ students).",
            "steps": [
                "Select one responsible student for each row/bench.",
                "Give materials (worksheets/chalk) only to these captains.",
                "Ask them to pass it backward or sideways.",
                "For collection, they gather items from their row and bring them to your desk."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Authoritative"
        },
        "pedagogy": {
            "why_it_works": "Decentralizes logistics, saving 5-10 minutes of lesson time per class.",
            "cognitive_target": "efficiency"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_traffic_light_cards",
        "version": "1.0",
        "status": "active",
        "situations": ["CHECKING_UNDERSTANDING", "LARGE_CLASS_SIZE"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_1_8",
        "topic_type": "FORMATIVE_ASSESSMENT",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Traffic Light Cards",
            "action_text": "Students show Red (Stop/Confused), Yellow (Unsure), or Green (Understood) cards."
        },
        "details": {
            "objective": "To gauge the understanding of 60+ students instantly without grading.",
            "steps": [
                "Ask students to color three pages in their diary: Red, Yellow, Green.",
                "After a topic, ask: 'Show me your traffic light'.",
                "Green = 'I got it', Yellow = 'Doubt', Red = 'Help me'.",
                "If you see many Reds, re-teach immediately."
            ],
            "time_required_min": 2,
            "materials_needed": ["Colored Paper/Crayons"],
            "teacher_tone": "Inquisitive"
        },
        "pedagogy": {
            "why_it_works": "Provides immediate whole-class feedback that is impossible to get verbally in large groups.",
            "cognitive_target": "self_assessment"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_think_pair_share_large",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_PARTICIPATION", "PASSIVE_LEARNING"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_4_10",
        "topic_type": "ENGAGEMENT",
        "learning_mode": "PEER_LEARNING",
        "preview": {
            "title": "Think-Pair-Share (Large Class)",
            "action_text": "Students discuss with their bench partner before answering."
        },
        "details": {
            "objective": "To ensure every student speaks, even in a crowded room.",
            "steps": [
                "Pose a question (e.g., 'Why do plants need sun?').",
                "THINK: Give 1 minute of silence.",
                "PAIR: Ask them to discuss ONLY with the person sitting next to them.",
                "SHARE: Call on 3 random pairs to share their answer."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Encouraging"
        },
        "pedagogy": {
            "why_it_works": "Reduces the fear of public speaking and ensures 100% engagement simultaneously.",
            "cognitive_target": "active_processing"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_visual_noise_meter",
        "version": "1.0",
        "status": "active",
        "situations": ["HIGH_NOISE", "CLASSROOM_CHAOS"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_1_5",
        "topic_type": "BEHAVIOR_MANAGEMENT",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Visual Noise Meter",
            "action_text": "Draw a noise meter on the board to visually signal acceptable volume levels."
        },
        "details": {
            "objective": "To control noise without shouting.",
            "steps": [
                "Draw a gauge on the board with 3 levels: 'Ninja Mode' (Silence), 'Spy Talk' (Whisper), 'Stage Voice' (Loud).",
                "Use a magnet or chalk mark to indicate the current allowed level.",
                "If noise rises, simply move the marker to 'Ninja Mode' and wait."
            ],
            "time_required_min": 2,
            "materials_needed": ["Chalk", "Board"],
            "teacher_tone": "Calm"
        },
        "pedagogy": {
            "why_it_works": "Visual cues are processed faster than verbal warnings in chaotic environments.",
            "cognitive_target": "self_regulation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_exemplar_grading",
        "version": "1.0",
        "status": "active",
        "situations": ["GRADING_OVERLOAD", "LARGE_CLASS_SIZE"],
        "subjects": ["ENGLISH", "SOCIAL_SCIENCE"],
        "class_range": "CLASS_6_10",
        "topic_type": "ASSESSMENT",
        "learning_mode": "MODELING",
        "preview": {
            "title": "Exemplar Analysis (Rubric)",
            "action_text": "Show a 'perfect' answer and a 'flawed' answer instead of grading every paper immediately."
        },
        "details": {
            "objective": "To provide feedback to 60 students without grading 60 papers overnight.",
            "steps": [
                "Write a model answer on the board.",
                "Write an answer with common mistakes next to it.",
                "Ask students to swap notebooks with a neighbor.",
                "Have them mark the neighbor's work based on the model on the board."
            ],
            "time_required_min": 15,
            "materials_needed": ["Board", "Chalk"],
            "teacher_tone": "Analytical"
        },
        "pedagogy": {
            "why_it_works": "Peer grading reduces teacher workload and helps students understand the success criteria.",
            "cognitive_target": "critical_evaluation"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "mgmt_hand_signals",
        "version": "1.0",
        "status": "active",
        "situations": ["INTERRUPTIONS", "DISRUPTIVE_BEHAVIOR"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_1_10",
        "topic_type": "CLASSROOM_MANAGEMENT",
        "learning_mode": "NON_VERBAL",
        "preview": {
            "title": "Silent Hand Signals",
            "action_text": "Teach specific hand signals for 'Toilet', 'Water', and 'Question' to stop interruptions."
        },
        "details": {
            "objective": "To minimize verbal interruptions during teaching.",
            "steps": [
                "Establish codes: 1 finger = Toilet, 2 fingers = Water, Raised fist = Question.",
                "Tell students they don't need to ask permission verbally; just show the sign.",
                "You can nod 'yes' or shake head 'no' while continuing to teach."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Procedural"
        },
        "pedagogy": {
            "why_it_works": "Eliminates the 'May I go out?' chorus that breaks teaching flow.",
            "cognitive_target": "executive_function"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_exit_ticket_summary",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_RETENTION", "LARGE_CLASS_SIZE"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_5_10",
        "topic_type": "CLOSURE",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "One-Line Exit Ticket",
            "action_text": "Students must write one thing they learned on a scrap paper to leave the class."
        },
        "details": {
            "objective": "To ensure accountability and attention till the last minute.",
            "steps": [
                "5 minutes before the bell, stop teaching.",
                "Ask: 'Write one new word or concept you learned today on a small paper'.",
                "Stand at the door.",
                "Students hand over the slip as their 'ticket' to go out."
            ],
            "time_required_min": 5,
            "materials_needed": ["Scrap Paper"],
            "teacher_tone": "Expectant"
        },
        "pedagogy": {
            "why_it_works": "Forces retrieval practice and provides the teacher with a quick snapshot of class learning.",
            "cognitive_target": "memory_consolidation"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "mgmt_question_parking_lot",
        "version": "1.0",
        "status": "active",
        "situations": ["OFF_TOPIC_QUESTIONS", "TIME_MANAGEMENT"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_6_10",
        "topic_type": "CLASSROOM_FLOW",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "The Question Parking Lot",
            "action_text": "Designate a board space for questions to be answered later."
        },
        "details": {
            "objective": "To handle curiosity without derailment in large classes.",
            "steps": [
                "Draw a box in the corner of the blackboard titled 'Parking Lot'.",
                "If a student asks an off-topic question, say: 'Good question, let's park it'.",
                "Write it in the box.",
                "Address these in the last 5 minutes or next class."
            ],
            "time_required_min": 1,
            "materials_needed": ["Board space"],
            "teacher_tone": "Respectful"
        },
        "pedagogy": {
            "why_it_works": "Validates the student's curiosity while protecting instructional time.",
            "cognitive_target": "attention_management"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]