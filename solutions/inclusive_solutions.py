from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

INCLUSIVE_SOLUTIONS = [
    {
        "solution_id": "incl_balloon_vibration",
        "version": "1.0",
        "status": "active",
        "situations": ["SENSORY_IMPAIRMENT", "INCLUSIVE_EDUCATION"],
        "subjects": ["MUSIC", "PHYSICS"],
        "class_range": "ALL",
        "topic_type": "INCLUSION",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Balloon Vibration (Hearing Impaired)",
            "action_text": "Use a balloon to help deaf/hard-of-hearing students 'feel' the sound."
        },
        "details": {
            "objective": "To include hearing-impaired students in music or rhythm activities.",
            "steps": [
                "Inflate a balloon comfortably.",
                "Ask the student to hold it with both hands efficiently.",
                "Play a drum or bass-heavy music nearby.",
                "The balloon amplifies vibrations, allowing them to feel the beat.",
                "Ask them to tap their foot along with the vibration."
            ],
            "time_required_min": 5,
            "materials_needed": ["Balloon", "Drum/Speaker"],
            "teacher_tone": "Inclusive"
        },
        "pedagogy": {
            "why_it_works": "Vibrotactile feedback substitutes auditory input, bridging the sensory gap.",
            "cognitive_target": "sensory_integration"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_pomodoro_for_kids",
        "version": "1.0",
        "status": "active",
        "situations": ["SLOW_LEARNER", "SHORT_ATTENTION_SPAN"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_5_10",
        "topic_type": "STUDY_SKILL",
        "learning_mode": "TIME_MANAGEMENT",
        "preview": {
            "title": "The 25-5 Rule (Pomodoro)",
            "action_text": "Teach slow learners to study for 25 minutes and break for 5."
        },
        "details": {
            "objective": "To prevent cognitive overload in students who struggle to focus.",
            "steps": [
                "Draw a 'Tomato' (Pomodoro) on the board.",
                "Explain: 'Our brain is like a battery. It runs out after 25 minutes.'",
                "Set a timer for 25 mins: Focus ONLY on one task.",
                "When bell rings, take a 5-minute 'Brain Break' (stretch/water).",
                "Repeat."
            ],
            "time_required_min": 2,
            "materials_needed": ["Timer"],
            "teacher_tone": "Structured"
        },
        "pedagogy": {
            "why_it_works": "Chunking time reduces the intimidation of large tasks for slow learners.",
            "cognitive_target": "executive_function"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_color_coded_notes",
        "version": "1.0",
        "status": "active",
        "situations": ["DYSLEXIA", "READING_DIFFICULTY"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "ALL",
        "topic_type": "LITERACY_SUPPORT",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Color-Coded Sentences",
            "action_text": "Use different colored chalks for Nouns, Verbs, and Adjectives."
        },
        "details": {
            "objective": "To help students visually distinguish sentence parts.",
            "steps": [
                "Establish a code: Red = Action (Verb), Blue = Thing (Noun), Green = Description (Adjective).",
                "Write a sentence on the board using these colors.",
                "Ask students to underline words in their book with matching crayons.",
                "Reduces the 'wall of text' effect."
            ],
            "time_required_min": 10,
            "materials_needed": ["Colored Chalk/Markers"],
            "teacher_tone": "Visual"
        },
        "pedagogy": {
            "why_it_works": "Visual segmentation aids processing for dyslexic and visual learners.",
            "cognitive_target": "syntactic_processing"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_buddy_system",
        "version": "1.0",
        "status": "active",
        "situations": ["SLOW_LEARNER", "ISOLATION"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "PEER_SUPPORT",
        "learning_mode": "SOCIAL",
        "preview": {
            "title": "The Buddy System",
            "action_text": "Pair a slow learner with a patient, empathetic peer (not necessarily the topper)."
        },
        "details": {
            "objective": "To provide constant low-stakes support without teacher intervention.",
            "steps": [
                "Identify 'Helper' students (look for kindness, not just high marks).",
                "Seat them next to struggling students.",
                "Rule: 'Ask your Buddy first, then ask the Teacher.'",
                "Rotate buddies every month to prevent fatigue."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Strategic"
        },
        "pedagogy": {
            "why_it_works": "Lowers the social anxiety of asking questions publicly.",
            "cognitive_target": "social_scaffolding"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_audio_text_bridge",
        "version": "1.0",
        "status": "active",
        "situations": ["READING_DIFFICULTY", "LOW_LITERACY"],
        "subjects": ["LANGUAGES"],
        "class_range": "ALL",
        "topic_type": "LITERACY",
        "learning_mode": "AUDITORY",
        "preview": {
            "title": "Read-Along Audio",
            "action_text": "Record yourself reading the chapter and share the audio file."
        },
        "details": {
            "objective": "To allow slow readers to keep up with the story flow.",
            "steps": [
                "Record the chapter on your phone (WhatsApp voice note).",
                "Share it with parents/students group.",
                "Ask student to listen to it while moving their finger under the text in the book.",
                "This links the sound to the written word."
            ],
            "time_required_min": 15,
            "materials_needed": ["Phone"],
            "teacher_tone": "Supportive"
        },
        "pedagogy": {
            "why_it_works": "Multisensory input (See + Hear) reinforces word recognition.",
            "cognitive_target": "fluency"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_exam_scaffold",
        "version": "1.0",
        "status": "active",
        "situations": ["EXAM_ANXIETY", "SLOW_WRITING"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_6_10",
        "topic_type": "ASSESSMENT",
        "learning_mode": "SCAFFOLDED",
        "preview": {
            "title": "Fill-in-the-Blank Exam Answers",
            "action_text": "Provide sentence starters for long answers."
        },
        "details": {
            "objective": "To test knowledge, not writing speed.",
            "steps": [
                "Instead of asking 'Explain Photosynthesis (5 marks)', give a skeleton.",
                "Write: 'Photosynthesis is a process where plants use ____ and ____ to make food.'",
                "Allow the student to fill gaps.",
                "Gradually reduce the gaps over the year."
            ],
            "time_required_min": 10,
            "materials_needed": ["Worksheet"],
            "teacher_tone": "Adaptive"
        },
        "pedagogy": {
            "why_it_works": "Reduces output anxiety while still verifying conceptual understanding.",
            "cognitive_target": "retrieval_practice"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_fidget_allowance",
        "version": "1.0",
        "status": "active",
        "situations": ["ADHD", "RESTLESSNESS"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "BEHAVIOR_MANAGEMENT",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Silent Fidget Allowance",
            "action_text": "Allow restless students to hold a stress ball or doodle while listening."
        },
        "details": {
            "objective": "To channel physical energy so the brain can focus.",
            "steps": [
                "Give the student a 'silent' fidget tool (piece of blu-tack, rubber band, sponge).",
                "Rule: 'It must be silent and hidden in your hand.'",
                "Explain that moving their hands helps them listen.",
                "Don't punish the movement if they are looking at you."
            ],
            "time_required_min": 1,
            "materials_needed": ["Rubber band/Sponge"],
            "teacher_tone": "Understanding"
        },
        "pedagogy": {
            "why_it_works": "For ADHD brains, low-level motor activity increases cortical arousal and focus.",
            "cognitive_target": "attention_regulation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_large_print",
        "version": "1.0",
        "status": "active",
        "situations": ["VISUAL_IMPAIRMENT", "EYE_STRAIN"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "ACCESSIBILITY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Large Print Worksheets",
            "action_text": "Photocopy worksheets at 125% zoom for struggling readers."
        },
        "details": {
            "objective": "To reduce visual crowding.",
            "steps": [
                "When copying a worksheet, use the 'Zoom' feature.",
                "Or simply write fewer questions on the blackboard in much larger font.",
                "Ensure high contrast (White chalk on clean black surface)."
            ],
            "time_required_min": 5,
            "materials_needed": ["Copier/Chalk"],
            "teacher_tone": "Accommodating"
        },
        "pedagogy": {
            "why_it_works": "Visual crowding is a major barrier for many undiagnosed eye issues.",
            "cognitive_target": "visual_perception"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_oral_testing",
        "version": "1.0",
        "status": "active",
        "situations": ["WRITING_DISABILITY", "DYSGRAPHIA"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "ASSESSMENT",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Oral Knowledge Check",
            "action_text": "Ask the student to say the answer instead of writing it."
        },
        "details": {
            "objective": "To separate knowledge from writing ability.",
            "steps": [
                "If a student fails a written test, pull them aside.",
                "Ask the same questions verbally.",
                "If they answer correctly, give them partial credit.",
                "This boosts confidence: 'You know it, you just struggle to write it.'"
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Encouraging"
        },
        "pedagogy": {
            "why_it_works": "Validates intelligence separate from motor skills.",
            "cognitive_target": "confidence"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "incl_preferential_seating",
        "version": "1.0",
        "status": "active",
        "situations": ["DISTRACTIBILITY", "HEARING_ISSUE"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "CLASSROOM_SETUP",
        "learning_mode": "ENVIRONMENTAL",
        "preview": {
            "title": "T-Zone Seating",
            "action_text": "Seat struggling students in the 'T-Zone' (Front rows and center)."
        },
        "details": {
            "objective": "To maximize teacher proximity and minimize distraction.",
            "steps": [
                "Imagine a 'T' shape in the room (Front row + Center aisle).",
                "Move slow learners or distracted students into this zone.",
                "Move independent high-achievers to the corners.",
                "This allows you to tap the desk of a struggling student easily."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Strategic"
        },
        "pedagogy": {
            "why_it_works": "Proximity control is the most effective non-verbal management tool.",
            "cognitive_target": "attention"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]