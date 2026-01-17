from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

PRODUCTIVITY_SOLUTIONS = [
    {
        "solution_id": "prod_batch_grading",
        "version": "1.0",
        "status": "active",
        "situations": ["GRADING_OVERLOAD", "ADMIN_STRESS"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "TIME_MANAGEMENT",
        "learning_mode": "METHODOLOGY",
        "preview": {
            "title": "Batch Grading Technique",
            "action_text": "Grade one specific question for the entire class before moving to the next question."
        },
        "details": {
            "objective": "To increase grading speed by 50% using muscle memory.",
            "steps": [
                "Do not grade Student A's full paper, then Student B's full paper.",
                "Instead, grade Question 1 for ALL 50 students.",
                "Then grade Question 2 for ALL 50 students.",
                "This keeps your brain focused on one answer key pattern."
            ],
            "time_required_min": 30,
            "materials_needed": ["Red Pen"],
            "teacher_tone": "Efficient"
        },
        "pedagogy": {
            "why_it_works": "Reduces 'cognitive switching costs' associated with changing topics frequently.",
            "cognitive_target": "efficiency"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_eisenhower_matrix",
        "version": "1.0",
        "status": "active",
        "situations": ["OVERWHELM", "PRIORITY_CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "PLANNING",
        "learning_mode": "COGNITIVE",
        "preview": {
            "title": "The 4-Box To-Do List (Eisenhower)",
            "action_text": "Sort your tasks into 4 boxes: Do Now, Schedule, Delegate, Delete."
        },
        "details": {
            "objective": "To stop doing 'Urgent' but 'Not Important' tasks.",
            "steps": [
                "Draw a 2x2 grid.",
                "Box 1 (Urgent+Important): Exam Papers (Do Now).",
                "Box 2 (Not Urgent+Important): Lesson Planning (Schedule).",
                "Box 3 (Urgent+Not Important): Register Update (Delegate to Monitor?).",
                "Box 4 (Neither): Decorating charts (Delete/Later)."
            ],
            "time_required_min": 10,
            "materials_needed": ["Paper"],
            "teacher_tone": "Strategic"
        },
        "pedagogy": {
            "why_it_works": "Forces cognitive filtering of tasks, reducing decision fatigue.",
            "cognitive_target": "executive_function"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_tick_only_feedback",
        "version": "1.0",
        "status": "active",
        "situations": ["GRADING_BACKLOG", "LARGE_CLASS_SIZE"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_6_10",
        "topic_type": "ASSESSMENT",
        "learning_mode": "MINIMALIST",
        "preview": {
            "title": "Tick-Only Marking",
            "action_text": "Stop writing comments. Use ticks for correct points and circle errors."
        },
        "details": {
            "objective": "To clear a backlog of 100+ notebooks quickly.",
            "steps": [
                "Tell students: 'Today I am checking for completion and key points only.'",
                "Scan the page. Tick the 3 keywords you are looking for.",
                "Circle mistakes but do NOT write the correction.",
                "Give verbal general feedback to the whole class instead."
            ],
            "time_required_min": 20,
            "materials_needed": ["Pen"],
            "teacher_tone": "Fast"
        },
        "pedagogy": {
            "why_it_works": "Written feedback is often unread by students; whole-class verbal feedback is more effective.",
            "cognitive_target": "feedback_loop"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_monitor_delegation",
        "version": "1.0",
        "status": "active",
        "situations": ["LOGISTICAL_CHAOS", "PAPERWORK"],
        "subjects": ["GENERAL"],
        "class_range": "CLASS_5_10",
        "topic_type": "DELEGATION",
        "learning_mode": "SOCIAL",
        "preview": {
            "title": "Student Admin Team",
            "action_text": "Assign students to handle date-writing, board cleaning, and register collection."
        },
        "details": {
            "objective": "To save 10 minutes of teacher time per day.",
            "steps": [
                "Appoint a 'Board Monitor' (Cleans board).",
                "Appoint a 'Date Monitor' (Writes date/subject every morning).",
                "Appoint a 'Register Monitor' (Collects notebooks in roll number order).",
                "Rotate these roles weekly."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Trusting"
        },
        "pedagogy": {
            "why_it_works": "Delegation builds student responsibility while freeing up teacher cognitive load.",
            "cognitive_target": "leadership"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_lesson_recycling",
        "version": "1.0",
        "status": "active",
        "situations": ["PLANNING_FATIGUE", "NO_TIME"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "PLANNING",
        "learning_mode": "REPETITION",
        "preview": {
            "title": "The 'Golden Lesson' Recycling",
            "action_text": "Reuse a successful lesson structure from last month for a new topic."
        },
        "details": {
            "objective": "To plan a lesson in 5 minutes.",
            "steps": [
                "Identify a lesson format that worked (e.g., 'Picture Dictation').",
                "Keep the *structure* (Show picture -> Write words -> Swap papers).",
                "Change only the *content* (Topic: Rivers instead of Mountains).",
                "Do not invent a new game every day."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Smart"
        },
        "pedagogy": {
            "why_it_works": "Routine structures reduce anxiety for both teacher and students.",
            "cognitive_target": "pattern_matching"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_pomodoro_grading",
        "version": "1.0",
        "status": "active",
        "situations": ["PROCRASTINATION", "GRADING_BOREDOM"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "TIME_MANAGEMENT",
        "learning_mode": "GAMIFIED",
        "preview": {
            "title": "20-Minute Grading Sprints",
            "action_text": "Set a timer for 20 minutes and race to grade as many as possible."
        },
        "details": {
            "objective": "To gamify the boring task of correction.",
            "steps": [
                "Stack the notebooks.",
                "Set a phone timer for 20 minutes.",
                "Goal: 'I must finish 15 books before the beep.'",
                "When beep sounds, stop. Walk for 2 minutes. Repeat."
            ],
            "time_required_min": 20,
            "materials_needed": ["Timer"],
            "teacher_tone": "Energetic"
        },
        "pedagogy": {
            "why_it_works": "Time-boxing creates artificial urgency, increasing focus and speed (Parkinson's Law).",
            "cognitive_target": "flow_state"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_voice_notes_planning",
        "version": "1.0",
        "status": "active",
        "situations": ["WRITER_BLOCK", "LESSON_PLANNING"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "PLANNING",
        "learning_mode": "AUDITORY",
        "preview": {
            "title": "Voice Note Lesson Planning",
            "action_text": "Dictate your lesson plan while walking to school instead of writing it."
        },
        "details": {
            "objective": "To utilize commute time for planning.",
            "steps": [
                "Open a voice recorder or WhatsApp (msg to self).",
                "Speak: 'Class 5 Math. Start with the pebble game. Then teach page 42. Homework is Q1.'",
                "Listen to it 5 mins before entering class.",
                "No need to write a formal diary unless mandatory."
            ],
            "time_required_min": 5,
            "materials_needed": ["Phone"],
            "teacher_tone": "Casual"
        },
        "pedagogy": {
            "why_it_works": "Verbal processing is often faster and more natural than written planning.",
            "cognitive_target": "verbal_memory"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_template_responses",
        "version": "1.0",
        "status": "active",
        "situations": ["PARENT_MESSAGES", "REPETITIVE_QUERIES"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "COMMUNICATION",
        "learning_mode": "AUTOMATION",
        "preview": {
            "title": "WhatsApp Template Replies",
            "action_text": "Save 3 standard replies for common parent complaints."
        },
        "details": {
            "objective": "To stop typing the same explanation to 40 parents.",
            "steps": [
                "Draft a polite message for 'Homework not done': 'Dear Parent, [Name] missed homework today. Please ensure it is done tonight. Thank you.'",
                "Save it in your notes app.",
                "Copy-paste whenever needed, just changing the name."
            ],
            "time_required_min": 5,
            "materials_needed": ["Phone"],
            "teacher_tone": "Professional"
        },
        "pedagogy": {
            "why_it_works": "Standardization ensures professional tone and saves emotional energy.",
            "cognitive_target": "efficiency"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_student_checkers",
        "version": "1.0",
        "status": "active",
        "situations": ["GRADING_OVERLOAD", "PEER_LEARNING"],
        "subjects": ["MATH", "SCIENCE"],
        "class_range": "CLASS_6_10",
        "topic_type": "ASSESSMENT",
        "learning_mode": "PEER_ASSISTED",
        "preview": {
            "title": "Peer Checking (Swapping)",
            "action_text": "Students swap notebooks and check objective answers."
        },
        "details": {
            "objective": "To grade objective questions instantly.",
            "steps": [
                "Ask students to swap notebooks with the person behind them.",
                "Read the answers aloud: '1 is A, 2 is C'.",
                "Students mark correct/incorrect with a pencil.",
                "Teacher only does a final signature."
            ],
            "time_required_min": 10,
            "materials_needed": ["None"],
            "teacher_tone": "Collaborative"
        },
        "pedagogy": {
            "why_it_works": "Students learn from seeing others' mistakes; instant feedback is better than delayed teacher feedback.",
            "cognitive_target": "evaluation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "prod_two_bag_system",
        "version": "1.0",
        "status": "active",
        "situations": ["WORK_LIFE_BALANCE", "DISORGANIZATION"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "ORGANIZATION",
        "learning_mode": "PHYSICAL_SETUP",
        "preview": {
            "title": "The 'To-Grade' vs 'Done' Pile",
            "action_text": "Physically separate finished and unfinished work to see progress."
        },
        "details": {
            "objective": "To visualize progress and reduce anxiety.",
            "steps": [
                "Keep two clear piles or bags on your desk.",
                "Left: 'To Do'. Right: 'Done'.",
                "As you grade, physically move the book.",
                "Seeing the 'Done' pile grow releases dopamine and motivation."
            ],
            "time_required_min": 1,
            "materials_needed": ["Two Trays/Bags"],
            "teacher_tone": "Organized"
        },
        "pedagogy": {
            "why_it_works": "Visual indicators of progress reduce the psychological weight of the task.",
            "cognitive_target": "motivation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]