from decision_engine.constants import (
    SITUATIONS,
    SUBJECTS,
    CLASS_RANGES,
    TOPIC_TYPES,
    LEARNING_MODES,
    CONSTRAINTS,
    EFFORT_LEVELS,
    SAFETY_LEVELS,
    NOISE_LEVELS,
    STUDENT_STATES,
)

REDDIT_SOLUTIONS = [
    {
        "solution_id": "guided_first_line_start",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["LOW_RECALL", "UNRESPONSIVE_CLASS"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "TASK_INITIATION",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Write the First Line Together",
            "action_text": "Write the first answer or sentence on the board and ask students to copy it."
        },
        "details": {
            "objective": "Help students overcome hesitation and start the task.",
            "steps": [
                "Write the first answer or sentence clearly on the board.",
                "Read it aloud once.",
                "Ask students to copy only that line.",
                "Pause briefly to ensure everyone has started.",
                "Say: 'Continue the rest in the same way.'"
            ],
            "time_required_min": 2,
            "materials_needed": ["board", "marker"],
            "teacher_tone": "calm"
        },
        "pedagogy": {
            "why_it_works": "Removes uncertainty about how to start and reduces cognitive load.",
            "cognitive_target": "task initiation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["HIGH_TIME_PRESSURE_EXAM"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "PASSIVE"
        },
        "tags": ["task_start", "scaffolding"]
    },
    {
        "solution_id": "think_then_pair_whisper",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["SILENT_CLASS", "LOW_CONFIDENCE"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPT_CHECK",
        "learning_mode": "PEER_ASSISTED",
        "preview": {
            "title": "Think, Then Pair (Whisper)",
            "action_text": "Give 30 seconds of thinking time, then let students whisper answers to a partner."
        },
        "details": {
            "objective": "Encourage participation without public pressure.",
            "steps": [
                "Ask a question and say: 'Think silently for 30 seconds.'",
                "Pair students with their bench partner.",
                "Allow quiet whisper discussion for one minute.",
                "Ask for volunteers after pairing.",
                "Acknowledge effort, not correctness."
            ],
            "time_required_min": 3,
            "materials_needed": [],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Private rehearsal builds confidence before public response.",
            "cognitive_target": "recall reinforcement"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["HIGH_NOISE_ENVIRONMENT"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "HESITANT"
        },
        "tags": ["peer_support", "low_pressure"]
    },
    {
        "solution_id": "reset_with_micro_pause",
        "version": 1,
        "status": "active",
        "response_style": "BEHAVIORAL",
        "situations": ["CLASS_NOISE_SPIKE", "LOSS_OF_FOCUS"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "CLASSROOM_RESET",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "30-Second Reset Pause",
            "action_text": "Pause the class briefly and reset attention with silence."
        },
        "details": {
            "objective": "Calm the room and regain attention without confrontation.",
            "steps": [
                "Stop speaking and stand silently.",
                "Wait until most students notice the silence.",
                "Say calmly: 'Let’s reset for 30 seconds.'",
                "Resume instruction after the pause."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Silence interrupts noise cycles without escalation.",
            "cognitive_target": "attention regulation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISTRACTED"
        },
        "tags": ["reset", "attention"]
    },
    {
        "solution_id": "neutral_boundary_statement",
        "version": 1,
        "status": "active",
        "response_style": "BEHAVIORAL",
        "situations": ["AUTHORITY_CHALLENGE", "MINOR_DEFIANCE"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "BEHAVIOR_MANAGEMENT",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Neutral Boundary Statement",
            "action_text": "Respond with a calm, factual boundary and move on."
        },
        "details": {
            "objective": "Maintain authority without escalating conflict.",
            "steps": [
                "State the expectation once in a neutral tone.",
                "Avoid debate or justification.",
                "Redirect attention back to the task.",
                "Follow up later if needed."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "firm_calm"
        },
        "pedagogy": {
            "why_it_works": "Limits power struggles by not engaging emotionally.",
            "cognitive_target": "self-regulation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["EMOTIONAL_OUTBURST"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "CHALLENGING"
        },
        "tags": ["boundaries", "authority"]
    },
    {
        "solution_id": "example_then_try",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["INSTRUCTION_CONFUSION", "LOW_RECALL"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "SKILL_PRACTICE",
        "learning_mode": "MODELED",
        "preview": {
            "title": "Example, Then Try",
            "action_text": "Solve one example fully, then ask students to try the next."
        },
        "details": {
            "objective": "Clarify expectations through modeling.",
            "steps": [
                "Work through one example step by step.",
                "Explain thinking aloud briefly.",
                "Point to the next question.",
                "Ask students to attempt independently."
            ],
            "time_required_min": 3,
            "materials_needed": ["board"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Concrete modeling bridges comprehension gaps.",
            "cognitive_target": "procedural understanding"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "CONFUSED"
        },
        "tags": ["modeling", "clarity"]
    },
    {
        "solution_id": "quick_yes_no_check",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["ASSUMED_UNDERSTANDING", "MISALIGNMENT"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "UNDERSTANDING_CHECK",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "Quick Yes/No Check",
            "action_text": "Ask for a silent thumbs up or down to gauge understanding."
        },
        "details": {
            "objective": "Rapidly assess understanding without calling out students.",
            "steps": [
                "Ask a clear yes/no question.",
                "Request thumbs up or down silently.",
                "Scan the room quickly.",
                "Adjust instruction if needed."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Provides instant feedback with minimal disruption.",
            "cognitive_target": "self-assessment"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["feedback", "quick_check"]
    },
    {
        "solution_id": "seat_partner_support",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["TASK_STUCK", "LOW_CONFIDENCE"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "PEER_SUPPORT",
        "learning_mode": "PAIR_WORK",
        "preview": {
            "title": "Seat Partner Support",
            "action_text": "Allow students to quietly consult their seat partner for one minute."
        },
        "details": {
            "objective": "Unblock students using peer clarification.",
            "steps": [
                "Allow one minute of quiet partner discussion.",
                "Ask students to return to individual work.",
                "Circulate briefly to monitor progress."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "permissive"
        },
        "pedagogy": {
            "why_it_works": "Peers often explain in accessible language.",
            "cognitive_target": "concept clarification"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["HISTORY_OF_OFF_TASK_TALK"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "STUCK"
        },
        "tags": ["peer_learning"]
    },
    {
        "solution_id": "verbal_restate_instruction",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["MISINTERPRETED_TASK", "CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "INSTRUCTION_CLARITY",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Restate Instructions Simply",
            "action_text": "Restate the task in one short sentence using simple language."
        },
        "details": {
            "objective": "Correct misunderstanding quickly.",
            "steps": [
                "Pause the class.",
                "Restate the task in one clear sentence.",
                "Check for nods or visual confirmation.",
                "Resume activity."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Simplification reduces misinterpretation.",
            "cognitive_target": "comprehension"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["clarity"]
    },
    {
        "solution_id": "short_individual_check_in",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["EMOTIONAL_DISTRACTION", "WITHDRAWN_STUDENT"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "EMOTIONAL_REGULATION",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Quiet Individual Check-In",
            "action_text": "Briefly check in with a student without stopping the class."
        },
        "details": {
            "objective": "Acknowledge emotion while keeping class flow.",
            "steps": [
                "Approach student quietly.",
                "Ask a short neutral question.",
                "Allow student to continue working or take a brief pause."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Recognition reduces emotional escalation.",
            "cognitive_target": "emotional regulation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["VISIBLE_DISTRESS_REQUIRING_REMOVAL"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISTRACTED"
        },
        "tags": ["emotion", "support"]
    },
    {
        "solution_id": "task_chunking_immediate",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TASK_OVERWHELM", "LOW_ENGAGEMENT"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "TASK_MANAGEMENT",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Chunk the Task",
            "action_text": "Break the task into two small visible steps and start with the first."
        },
        "details": {
            "objective": "Reduce overwhelm and increase engagement.",
            "steps": [
                "Divide the task into two short steps.",
                "Ask students to complete only step one.",
                "Acknowledge completion before moving to step two."
            ],
            "time_required_min": 3,
            "materials_needed": ["board"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Smaller goals increase perceived achievability.",
            "cognitive_target": "task persistence"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "OVERWHELMED"
        },
        "tags": ["chunking", "engagement"]
    },
    {
        "solution_id": "one_sentence_recap_prompt",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_RECALL", "CONTENT_DISCONNECT"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "RECAP",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "One-Sentence Recap",
            "action_text": "Ask students to recall the last concept in one simple sentence."
        },
        "details": {
            "objective": "Reactivate prior knowledge quickly.",
            "steps": [
                "Say: 'In one sentence, what did we learn last time?'",
                "Allow 20 seconds of silent thinking.",
                "Ask 1–2 volunteers to share.",
                "Restate the correct idea clearly."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Brief recall strengthens memory pathways.",
            "cognitive_target": "retrieval"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["recall", "retrieval"]
    },
    {
        "solution_id": "visible_timer_focus_burst",
        "version": 1,
        "status": "active",
        "response_style": "BEHAVIORAL",
        "situations": ["LOW_ENGAGEMENT", "DRIFTING_ATTENTION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "FOCUS_RESET",
        "learning_mode": "SELF_DIRECTED",
        "preview": {
            "title": "2-Minute Focus Burst",
            "action_text": "Set a visible timer and ask students to work silently until it ends."
        },
        "details": {
            "objective": "Restore focus using a short time-bound challenge.",
            "steps": [
                "Set a 2-minute timer visibly.",
                "Say: 'Work silently till the timer ends.'",
                "Do not interrupt during the time.",
                "Review progress briefly after."
            ],
            "time_required_min": 3,
            "materials_needed": ["timer"],
            "teacher_tone": "firm"
        },
        "pedagogy": {
            "why_it_works": "Short deadlines increase attention and effort.",
            "cognitive_target": "sustained attention"
        },
        "constraints": {
            "requires": ["VISIBLE_TIMER"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISTRACTED"
        },
        "tags": ["focus", "timeboxing"]
    },
    {
        "solution_id": "read_question_aloud_once",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["MISREAD_INSTRUCTIONS", "TASK_ERRORS"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "INSTRUCTION_SUPPORT",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Read the Question Aloud",
            "action_text": "Read the question aloud once before students attempt it."
        },
        "details": {
            "objective": "Prevent errors caused by misreading.",
            "steps": [
                "Ask students to pause.",
                "Read the question aloud slowly.",
                "Highlight key instruction words.",
                "Allow students to proceed."
            ],
            "time_required_min": 1,
            "materials_needed": ["question_text"],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Auditory reinforcement improves comprehension.",
            "cognitive_target": "instruction parsing"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["instruction", "clarity"]
    },
    {
        "solution_id": "board_outline_structure",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["WRITING_BLOCK", "STRUCTURE_CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "WRITING_SUPPORT",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Board Outline Structure",
            "action_text": "Draw a simple outline on the board before students write."
        },
        "details": {
            "objective": "Provide structure to reduce writing anxiety.",
            "steps": [
                "Draw 3–4 bullet points as an outline.",
                "Explain each point briefly.",
                "Ask students to write using the outline."
            ],
            "time_required_min": 3,
            "materials_needed": ["board"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Structure lowers cognitive overload in writing.",
            "cognitive_target": "organization"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "BLOCKED"
        },
        "tags": ["writing", "scaffolding"]
    },
    {
        "solution_id": "stand_and_stretch_reset",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["FATIGUE", "LOSS_OF_ENERGY"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "ENERGY_RESET",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "30-Second Stretch Reset",
            "action_text": "Ask students to stand and stretch briefly before continuing."
        },
        "details": {
            "objective": "Re-energize students without disrupting class flow.",
            "steps": [
                "Ask students to stand.",
                "Guide a simple stretch for 30 seconds.",
                "Ask students to sit and refocus."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "light"
        },
        "pedagogy": {
            "why_it_works": "Physical movement refreshes attention.",
            "cognitive_target": "alertness"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["STRICT_EXAM_CONDITION"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "TIRED"
        },
        "tags": ["energy", "reset"]
    },
    {
        "solution_id": "choice_between_two_tasks",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_MOTIVATION", "RESISTANCE"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "ENGAGEMENT",
        "learning_mode": "SELF_DIRECTED",
        "preview": {
            "title": "Offer Two Task Choices",
            "action_text": "Give students a choice between two equivalent tasks."
        },
        "details": {
            "objective": "Increase ownership and engagement.",
            "steps": [
                "Present two task options.",
                "Clarify both meet the same goal.",
                "Let students choose silently.",
                "Proceed with instruction."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Choice increases intrinsic motivation.",
            "cognitive_target": "engagement"
        },
        "constraints": {
            "requires": ["PREPARED_ALTERNATE_TASK"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "RESISTANT"
        },
        "tags": ["choice", "motivation"]
    },
    {
        "solution_id": "quick_board_check_answers",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["ANSWER_ANXIETY", "NON_PARTICIPATION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "ANSWER_CHECK",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "Board Check Answers",
            "action_text": "Write correct answers on the board for self-checking."
        },
        "details": {
            "objective": "Reduce fear of being wrong.",
            "steps": [
                "Write answers on the board.",
                "Ask students to self-check silently.",
                "Clarify common mistakes."
            ],
            "time_required_min": 2,
            "materials_needed": ["board"],
            "teacher_tone": "non-judgmental"
        },
        "pedagogy": {
            "why_it_works": "Self-checking avoids public evaluation.",
            "cognitive_target": "error awareness"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "ANXIOUS"
        },
        "tags": ["self_check", "confidence"]
    },
    {
        "solution_id": "short_walk_and_talk",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["MENTAL_FATIGUE", "LOW_INTERACTION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "DISCUSSION",
        "learning_mode": "PAIR_WORK",
        "preview": {
            "title": "Walk-and-Talk Pair",
            "action_text": "Allow pairs to walk briefly while discussing one question."
        },
        "details": {
            "objective": "Refresh thinking through movement and dialogue.",
            "steps": [
                "Assign one discussion question.",
                "Allow pairs to walk quietly for 2 minutes.",
                "Return and share key points."
            ],
            "time_required_min": 4,
            "materials_needed": [],
            "teacher_tone": "relaxed"
        },
        "pedagogy": {
            "why_it_works": "Movement stimulates cognitive engagement.",
            "cognitive_target": "idea generation"
        },
        "constraints": {
            "requires": ["SPACE_AVAILABLE"],
            "avoid_if": ["CLASSROOM_CONGESTION"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "TIRED"
        },
        "tags": ["movement", "discussion"]
    },
    {
        "solution_id": "sentence_starter_prompt",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["WRITING_HESITATION", "LOW_EXPRESSION"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "WRITING_SUPPORT",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Sentence Starter Prompt",
            "action_text": "Provide a sentence starter to help students begin writing."
        },
        "details": {
            "objective": "Lower entry barrier for written responses.",
            "steps": [
                "Write a sentence starter on the board.",
                "Ask students to complete it in their own words.",
                "Encourage continuation after first sentence."
            ],
            "time_required_min": 2,
            "materials_needed": ["board"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Starters reduce fear of blank pages.",
            "cognitive_target": "expression"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "BLOCKED"
        },
        "tags": ["writing", "confidence"]
    },
    {
        "solution_id": "end_with_one_clear_takeaway",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["CONFUSING_LESSON_END", "LOW_RETENTION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "CLOSURE",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "One Clear Takeaway",
            "action_text": "End the class by stating one clear takeaway sentence."
        },
        "details": {
            "objective": "Ensure students leave with a clear understanding.",
            "steps": [
                "Pause before dismissal.",
                "State one key idea clearly.",
                "Ask students to repeat it silently."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Focused closure improves retention.",
            "cognitive_target": "consolidation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["closure", "retention"]
    },
    {
        "solution_id": "choral_response_single_word",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_PARTICIPATION", "HESITANT_CLASS"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPT_CHECK",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "Choral One-Word Response",
            "action_text": "Ask the class to answer together using one word."
        },
        "details": {
            "objective": "Encourage participation without singling out students.",
            "steps": [
                "Ask a question with a one-word answer.",
                "Say: 'Everyone answer together.'",
                "Acknowledge the collective response.",
                "Proceed with the lesson."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "energetic"
        },
        "pedagogy": {
            "why_it_works": "Group response reduces fear of being wrong.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["NOISE_SENSITIVE_ENVIRONMENT"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "HESITANT"
        },
        "tags": ["participation", "recall"]
    },
    {
        "solution_id": "point_to_answer_choice",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["ANSWER_ANXIETY", "LOW_CONFIDENCE"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "UNDERSTANDING_CHECK",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "Point to the Answer",
            "action_text": "Ask students to point to the correct option instead of speaking."
        },
        "details": {
            "objective": "Check understanding without verbal pressure.",
            "steps": [
                "Write 2–3 options on the board.",
                "Ask students to point silently.",
                "Scan responses quickly.",
                "Clarify if needed."
            ],
            "time_required_min": 1,
            "materials_needed": ["board"],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Non-verbal response lowers participation barrier.",
            "cognitive_target": "recognition"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "ANXIOUS"
        },
        "tags": ["non_verbal", "confidence"]
    },
    {
        "solution_id": "write_then_share_optional",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["FEAR_OF_SPEAKING", "LOW_EXPRESSION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "EXPRESSION",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Write First, Share Optional",
            "action_text": "Let students write their response before asking for volunteers."
        },
        "details": {
            "objective": "Support expression without forcing speech.",
            "steps": [
                "Give a prompt.",
                "Allow one minute of writing.",
                "Invite volunteers to share.",
                "Summarize key ideas."
            ],
            "time_required_min": 3,
            "materials_needed": ["notebooks"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Writing organizes thoughts before speaking.",
            "cognitive_target": "expression"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["EXTREME_TIME_CONSTRAINT"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "HESITANT"
        },
        "tags": ["expression", "confidence"]
    },
    {
        "solution_id": "cold_call_with_pass_option",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ATTENTION", "SELECTIVE_PARTICIPATION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "ENGAGEMENT",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Cold Call with Pass Option",
            "action_text": "Call on students but allow them to say 'pass'."
        },
        "details": {
            "objective": "Increase attentiveness while preserving safety.",
            "steps": [
                "Explain that 'pass' is allowed.",
                "Ask a simple question.",
                "Call on a student by name.",
                "Accept response or pass calmly."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "respectful"
        },
        "pedagogy": {
            "why_it_works": "Accountability without humiliation.",
            "cognitive_target": "attention"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["HIGH_ANXIETY_CLASS"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "DISTRACTED"
        },
        "tags": ["attention", "safe_calling"]
    },
    {
        "solution_id": "visual_anchor_keyword",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["CONCEPT_DRIFT", "LOW_RETENTION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "CONCEPT_ANCHOR",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Keyword Anchor on Board",
            "action_text": "Write one key word on the board and refer back to it."
        },
        "details": {
            "objective": "Anchor attention to the core idea.",
            "steps": [
                "Write one key word on the board.",
                "Circle or underline it.",
                "Refer to it while explaining.",
                "Point back during questions."
            ],
            "time_required_min": 1,
            "materials_needed": ["board"],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Visual anchors support memory.",
            "cognitive_target": "concept retention"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DRIFTING"
        },
        "tags": ["visual", "retention"]
    },
    {
        "solution_id": "two_example_comparison",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["MISCONCEPTION", "CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "CONCEPT_CLARITY",
        "learning_mode": "MODELED",
        "preview": {
            "title": "Compare Two Examples",
            "action_text": "Show one correct and one incorrect example and compare."
        },
        "details": {
            "objective": "Clarify misconceptions explicitly.",
            "steps": [
                "Present a correct example.",
                "Present a common incorrect example.",
                "Ask what is different.",
                "Summarize the key rule."
            ],
            "time_required_min": 3,
            "materials_needed": ["board"],
            "teacher_tone": "analytical"
        },
        "pedagogy": {
            "why_it_works": "Contrast sharpens understanding.",
            "cognitive_target": "concept discrimination"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "CONFUSED"
        },
        "tags": ["misconception", "clarity"]
    },
    {
        "solution_id": "progress_check_mark",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_PROGRESS", "TASK_STALL"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "TASK_MONITORING",
        "learning_mode": "SELF_DIRECTED",
        "preview": {
            "title": "Progress Check Mark",
            "action_text": "Ask students to tick completed parts to see progress."
        },
        "details": {
            "objective": "Make progress visible and motivating.",
            "steps": [
                "Ask students to mark completed steps.",
                "Point out visible progress.",
                "Encourage continuation."
            ],
            "time_required_min": 1,
            "materials_needed": ["notebooks"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Visible progress increases persistence.",
            "cognitive_target": "task persistence"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "STUCK"
        },
        "tags": ["progress", "motivation"]
    },
    {
        "solution_id": "silent_read_then_discuss",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["RUSHED_ANSWERS", "SURFACE_LEARNING"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "DEEPENING",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Silent Read Then Discuss",
            "action_text": "Give quiet reading time before discussion."
        },
        "details": {
            "objective": "Improve depth of responses.",
            "steps": [
                "Ask students to read silently.",
                "Allow 1–2 minutes.",
                "Then open discussion."
            ],
            "time_required_min": 3,
            "materials_needed": ["text"],
            "teacher_tone": "calm"
        },
        "pedagogy": {
            "why_it_works": "Processing time improves quality of discussion.",
            "cognitive_target": "comprehension"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["SEVERE_TIME_PRESSURE"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "RUSHED"
        },
        "tags": ["reading", "depth"]
    },
    {
        "solution_id": "confidence_normalizing_statement",
        "version": 1,
        "status": "active",
        "response_style": "BEHAVIORAL",
        "situations": ["FEAR_OF_MISTAKES", "LOW_CONFIDENCE"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "CLASSROOM_CLIMATE",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Normalize Mistakes",
            "action_text": "State that mistakes are expected during learning."
        },
        "details": {
            "objective": "Reduce fear of making mistakes.",
            "steps": [
                "Say a normalizing statement.",
                "Give a quick example.",
                "Proceed with the task."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "reassuring"
        },
        "pedagogy": {
            "why_it_works": "Psychological safety improves engagement.",
            "cognitive_target": "risk-taking"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "ANXIOUS"
        },
        "tags": ["confidence", "safety"]
    },
    {
        "solution_id": "quick_board_summary_boxes",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["INFORMATION_OVERLOAD", "CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "SUMMARY",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Board Summary Boxes",
            "action_text": "Summarize content into 2–3 boxed points on the board."
        },
        "details": {
            "objective": "Reduce overload by summarizing visually.",
            "steps": [
                "Draw 2–3 boxes on the board.",
                "Write one key point in each.",
                "Refer back during questions."
            ],
            "time_required_min": 2,
            "materials_needed": ["board"],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Chunked summaries aid comprehension.",
            "cognitive_target": "organization"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "OVERWHELMED"
        },
        "tags": ["summary", "clarity"]
    },
    {
        "solution_id": "start_with_easy_win",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TASK_RESISTANCE", "LOW_CONFIDENCE"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "ENGAGEMENT",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Start with an Easy Win",
            "action_text": "Begin with a very simple question everyone can answer."
        },
        "details": {
            "objective": "Build momentum and confidence quickly.",
            "steps": [
                "Ask a very easy starter question.",
                "Acknowledge correct responses.",
                "Transition to the main task."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Early success increases willingness to engage.",
            "cognitive_target": "confidence activation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "INSECURE"
        },
        "tags": ["confidence", "momentum"]
    },
    {
        "solution_id": "repeat_student_answer_neutrally",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["UNCLEAR_RESPONSES", "LOW_CLARITY"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "ANSWER_PROCESSING",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Repeat Student Answer Clearly",
            "action_text": "Repeat a student’s answer clearly without judgment."
        },
        "details": {
            "objective": "Clarify ideas without evaluating publicly.",
            "steps": [
                "Listen to the student response.",
                "Repeat it clearly for the class.",
                "Connect it to the concept."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Clarification improves shared understanding.",
            "cognitive_target": "concept alignment"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCLEAR"
        },
        "tags": ["clarity", "listening"]
    },
    {
        "solution_id": "limit_response_time",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["RAMBLING_ANSWERS", "TIME_LOSS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "TIME_MANAGEMENT",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Limit Response Time",
            "action_text": "Ask students to answer in one sentence only."
        },
        "details": {
            "objective": "Keep responses focused and time-efficient.",
            "steps": [
                "State the one-sentence rule.",
                "Listen briefly.",
                "Summarize and move on."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "firm_calm"
        },
        "pedagogy": {
            "why_it_works": "Constraints improve clarity and pacing.",
            "cognitive_target": "concise expression"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["CREATIVE_DISCUSSION"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "VERBOSE"
        },
        "tags": ["time_control", "focus"]
    },
    {
        "solution_id": "seat_change_micro_adjustment",
        "version": 1,
        "status": "active",
        "response_style": "BEHAVIORAL",
        "situations": ["DISTRACTION_CLUSTER", "SIDE_TALK"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "BEHAVIOR_ADJUSTMENT",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Micro Seat Adjustment",
            "action_text": "Quietly adjust seating to reduce distraction."
        },
        "details": {
            "objective": "Reduce off-task behavior discreetly.",
            "steps": [
                "Identify distraction cluster.",
                "Move one student calmly.",
                "Resume instruction immediately."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "neutral"
        },
        "pedagogy": {
            "why_it_works": "Environment change alters behavior without confrontation.",
            "cognitive_target": "attention control"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["FIXED_SEATING"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISTRACTED"
        },
        "tags": ["behavior", "environment"]
    },
    {
        "solution_id": "highlight_common_mistake",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["REPEATED_ERRORS", "MISCONCEPTION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "ERROR_CORRECTION",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Highlight a Common Mistake",
            "action_text": "Point out a common mistake without naming students."
        },
        "details": {
            "objective": "Correct errors safely and collectively.",
            "steps": [
                "State the common mistake.",
                "Explain why it happens.",
                "Show the correct approach."
            ],
            "time_required_min": 2,
            "materials_needed": ["board"],
            "teacher_tone": "matter_of_fact"
        },
        "pedagogy": {
            "why_it_works": "Collective correction avoids embarrassment.",
            "cognitive_target": "error correction"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["errors", "clarification"]
    },
    {
        "solution_id": "predict_then_reveal",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_CURIOSITY", "PASSIVE_LISTENING"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "ENGAGEMENT",
        "learning_mode": "WHOLE_CLASS",
        "preview": {
            "title": "Predict Then Reveal",
            "action_text": "Ask students to predict an answer before revealing it."
        },
        "details": {
            "objective": "Activate curiosity and attention.",
            "steps": [
                "Pose a prediction question.",
                "Pause briefly.",
                "Reveal and explain the answer."
            ],
            "time_required_min": 2,
            "materials_needed": [],
            "teacher_tone": "curious"
        },
        "pedagogy": {
            "why_it_works": "Prediction increases engagement and retention.",
            "cognitive_target": "anticipation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "PASSIVE"
        },
        "tags": ["curiosity", "engagement"]
    },
    {
        "solution_id": "visual_step_numbering",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["PROCESS_CONFUSION", "MULTI_STEP_TASK"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "PROCESS_SUPPORT",
        "learning_mode": "GUIDED",
        "preview": {
            "title": "Number the Steps Visually",
            "action_text": "Number task steps clearly on the board."
        },
        "details": {
            "objective": "Clarify multi-step processes.",
            "steps": [
                "Write numbered steps on the board.",
                "Explain briefly.",
                "Refer to numbers during work."
            ],
            "time_required_min": 2,
            "materials_needed": ["board"],
            "teacher_tone": "clear"
        },
        "pedagogy": {
            "why_it_works": "Sequencing reduces cognitive overload.",
            "cognitive_target": "process tracking"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "OVERWHELMED"
        },
        "tags": ["process", "clarity"]
    },
    {
        "solution_id": "acknowledge_effort_publicly",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_MORALE", "DISENGAGEMENT"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "MOTIVATION",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Acknowledge Effort",
            "action_text": "Acknowledge effort without evaluating correctness."
        },
        "details": {
            "objective": "Boost morale and persistence.",
            "steps": [
                "Notice effort.",
                "State it briefly.",
                "Continue instruction."
            ],
            "time_required_min": 1,
            "materials_needed": [],
            "teacher_tone": "positive"
        },
        "pedagogy": {
            "why_it_works": "Effort recognition increases motivation.",
            "cognitive_target": "persistence"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["OVER_PRAISE_PATTERN"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "VERY_LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISCOURAGED"
        },
        "tags": ["motivation", "effort"]
    },
    {
        "solution_id": "rephrase_student_question",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["UNCLEAR_QUESTIONS", "CONFUSION"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "QUESTION_HANDLING",
        "learning_mode": "TEACHER_LED",
        "preview": {
            "title": "Rephrase the Question",
            "action_text": "Rephrase a student’s question clearly before answering."
        },
        "details": {
            "objective": "Ensure shared understanding of questions.",
        "steps": [
            "Listen to the question.",
            "Rephrase it simply.",
            "Answer the rephrased version."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "respectful"
    },
    "pedagogy": {
        "why_it_works": "Clarification prevents misunderstanding.",
        "cognitive_target": "question comprehension"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "CONFUSED"
    },
    "tags": ["questions", "clarity"]
},
{
    "solution_id": "end_task_with_visible_progress",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["UNFINISHED_WORK", "LOW_CLOSURE"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "TASK_CLOSURE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "End with Visible Progress",
        "action_text": "Highlight how much of the task was completed."
    },
    "details": {
        "objective": "Create a sense of completion.",
        "steps": [
            "Point out completed sections.",
            "Summarize progress.",
            "State next step clearly."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "affirming"
    },
    "pedagogy": {
        "why_it_works": "Closure improves satisfaction and continuity.",
        "cognitive_target": "task completion"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNCERTAIN"
    },
    "tags": ["closure", "continuity"]
},
{
    "solution_id": "micro_goal_for_next_five_minutes",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["OVERWHELM", "TASK_AVOIDANCE"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "TASK_FOCUS",
    "learning_mode": "GUIDED",
    "preview": {
        "title": "5-Minute Micro Goal",
        "action_text": "Set a small, clear goal for the next five minutes only."
    },
    "details": {
        "objective": "Reduce avoidance by narrowing focus.",
        "steps": [
            "State one small goal for the next five minutes.",
            "Write it visibly.",
            "Ask students to work only on that part.",
            "Acknowledge completion."
        ],
        "time_required_min": 5,
        "materials_needed": ["board"],
        "teacher_tone": "reassuring"
    },
    "pedagogy": {
        "why_it_works": "Short horizons reduce anxiety and increase action.",
        "cognitive_target": "task initiation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["EXAM_END_WINDOW"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "OVERWHELMED"
    },
    "tags": ["micro_goal", "focus"]
},
{
    "solution_id": "show_completed_student_work_anonymous",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["LOW_QUALITY_OUTPUT", "UNCLEAR_EXPECTATION"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "EXPECTATION_CLARITY",
    "learning_mode": "MODELED",
    "preview": {
        "title": "Show a Completed Example",
        "action_text": "Show an anonymous completed example to clarify expectations."
    },
    "details": {
        "objective": "Clarify what a finished answer looks like.",
        "steps": [
            "Select an anonymous sample.",
            "Show or rewrite it on the board.",
            "Point out key features.",
            "Ask students to continue."
        ],
        "time_required_min": 3,
        "materials_needed": ["board"],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Concrete examples reduce ambiguity.",
        "cognitive_target": "modeling"
    },
    "constraints": {
        "requires": ["AVAILABLE_SAMPLE"],
        "avoid_if": ["RISK_OF_IDENTIFICATION"]
    },
    "effort_level": "MEDIUM",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "medium",
        "student_state": "UNCERTAIN"
    },
    "tags": ["modeling", "clarity"]
},
{
    "solution_id": "silent_vote_multiple_choice",
    "version": 1,
    "status": "active",
    "response_style": "KINETIC",
    "situations": ["CHECKING_UNDERSTANDING", "LOW_PARTICIPATION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "UNDERSTANDING_CHECK",
    "learning_mode": "WHOLE_CLASS",
    "preview": {
        "title": "Silent Vote",
        "action_text": "Ask students to vote silently between options."
    },
    "details": {
        "objective": "Assess understanding quickly and safely.",
        "steps": [
            "Present 2–4 options.",
            "Ask for hands raised silently.",
            "Scan results.",
            "Clarify if needed."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Low-risk feedback enables adjustment.",
        "cognitive_target": "recognition"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "QUIET"
    },
    "tags": ["feedback", "quick_check"]
},
{
    "solution_id": "name_the_strategy_used",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["RANDOM_ATTEMPTS", "INEFFICIENT_METHODS"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "STRATEGY_AWARENESS",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Name the Strategy",
        "action_text": "Name the strategy being used before applying it."
    },
    "details": {
        "objective": "Increase intentional problem-solving.",
        "steps": [
            "State the strategy name.",
            "Explain when it is used.",
            "Apply it to the task."
        ],
        "time_required_min": 2,
        "materials_needed": [],
        "teacher_tone": "instructive"
    },
    "pedagogy": {
        "why_it_works": "Explicit strategy labeling improves transfer.",
        "cognitive_target": "metacognition"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["INTRODUCTORY_EXPOSURE_ONLY"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "GUESSING"
    },
    "tags": ["strategy", "metacognition"]
},
{
    "solution_id": "park_off_topic_question",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["OFF_TOPIC_INTERRUPTIONS", "TIME_DRAIN"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CLASSROOM_FLOW",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Park the Question",
        "action_text": "Acknowledge the question and park it for later."
    },
    "details": {
        "objective": "Maintain flow while respecting curiosity.",
        "steps": [
            "Acknowledge the question.",
            "Say it will be addressed later.",
            "Note it briefly.",
            "Continue lesson."
        ],
        "time_required_min": 1,
        "materials_needed": ["board_optional"],
        "teacher_tone": "respectful"
    },
    "pedagogy": {
        "why_it_works": "Defers without dismissing.",
        "cognitive_target": "attention management"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["QUESTION_IS_CORE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "INTERRUPTING"
    },
    "tags": ["flow", "time_management"]
},
{
    "solution_id": "explicit_transition_signal",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["MESSY_TRANSITION", "CONFUSION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "TRANSITION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Clear Transition Signal",
        "action_text": "Signal clearly when moving from one activity to another."
    },
    "details": {
        "objective": "Reduce confusion during activity changes.",
        "steps": [
            "Announce transition.",
            "State next activity clearly.",
            "Wait briefly before starting."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Clear cues reduce cognitive switching cost.",
        "cognitive_target": "task switching"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DISORIENTED"
    },
    "tags": ["transition", "clarity"]
},
{
    "solution_id": "write_key_terms_only",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["NOTE_OVERLOAD", "SLOW_PACING"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "NOTE_TAKING",
    "learning_mode": "GUIDED",
    "preview": {
        "title": "Key Terms Only",
        "action_text": "Ask students to write only key terms, not full notes."
    },
    "details": {
        "objective": "Improve pacing and reduce overload.",
        "steps": [
            "List key terms.",
            "Ask students to copy only terms.",
            "Explain orally."
        ],
        "time_required_min": 2,
        "materials_needed": ["board"],
        "teacher_tone": "efficient"
    },
    "pedagogy": {
        "why_it_works": "Selective note-taking improves listening.",
        "cognitive_target": "selective attention"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["EXAM_NOTE_REQUIREMENT"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "OVERLOADED"
    },
    "tags": ["notes", "pacing"]
},
{
    "solution_id": "redirect_with_task_reference",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["SIDE_CONVERSATION", "OFF_TASK_BEHAVIOR"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "BEHAVIOR_REDIRECTION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Redirect to Task",
        "action_text": "Redirect behavior by referencing the task, not the student."
    },
    "details": {
        "objective": "Correct behavior without personal confrontation.",
        "steps": [
            "State the task expectation.",
            "Avoid naming students.",
            "Continue instruction."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Task-focused language reduces defensiveness.",
        "cognitive_target": "self-regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["SEVERE_MISBEHAVIOR"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "OFF_TASK"
    },
    "tags": ["behavior", "redirection"]
},
{
    "solution_id": "quick_pair_check_before_submit",
    "version": 1,
    "status": "active",
    "response_style": "SOCIAL",
    "situations": ["CARELESS_ERRORS", "RUSHED_SUBMISSION"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "ERROR_PREVENTION",
    "learning_mode": "PAIR_WORK",
    "preview": {
        "title": "Pair Check",
        "action_text": "Allow a brief pair check before submission."
    },
    "details": {
        "objective": "Reduce careless mistakes.",
        "steps": [
            "Pair students.",
            "Give one minute to check work.",
            "Proceed to submission."
        ],
        "time_required_min": 2,
        "materials_needed": [],
        "teacher_tone": "procedural"
    },
    "pedagogy": {
        "why_it_works": "Peer review catches simple errors.",
        "cognitive_target": "error detection"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["STRICT_EXAM_RULES"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "medium",
        "student_state": "RUSHED"
    },
    "tags": ["accuracy", "peer_check"]
},
{
    "solution_id": "preemptive_confusion_warning",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["ANTICIPATED_CONFUSION", "NEW_CONCEPT_INTRO"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CONCEPT_INTRODUCTION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Normalize Confusion Upfront",
        "action_text": "Tell students that confusion is expected before introducing a new concept."
    },
    "details": {
        "objective": "Reduce anxiety before difficulty appears.",
        "steps": [
            "State that the concept may feel confusing at first.",
            "Reassure students this is normal.",
            "Begin explanation calmly."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "reassuring"
    },
    "pedagogy": {
        "why_it_works": "Expectation-setting reduces panic and shutdown.",
        "cognitive_target": "emotional regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "ANXIOUS"
    },
    "tags": ["normalization", "confidence"]
},
{
    "solution_id": "one_student_think_aloud_model",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["PROCESS_OPACITY", "LOW_STRATEGY_USE"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "STRATEGY_MODELING",
    "learning_mode": "MODELED",
    "preview": {
        "title": "Think Aloud Once",
        "action_text": "Model your thinking aloud for one example."
    },
    "details": {
        "objective": "Make invisible thinking visible.",
        "steps": [
            "Choose one example.",
            "Verbalize each thinking step.",
            "Solve the example completely.",
            "Ask students to try the next one."
        ],
        "time_required_min": 3,
        "materials_needed": ["board"],
        "teacher_tone": "explanatory"
    },
    "pedagogy": {
        "why_it_works": "Thinking models guide student strategy formation.",
        "cognitive_target": "strategic thinking"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["TIME_CRITICAL"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "GUESSING"
    },
    "tags": ["modeling", "strategy"]
},
{
    "solution_id": "pause_before_answering_student",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["IMMEDIATE_DEPENDENCE", "LOW_INDEPENDENCE"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "INDEPENDENCE_BUILDING",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Pause Before Answering",
        "action_text": "Pause briefly before answering student questions."
    },
    "details": {
        "objective": "Encourage independent thinking.",
        "steps": [
            "Pause for 3–5 seconds.",
            "Ask: 'What do you think?'",
            "Then guide if needed."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "patient"
    },
    "pedagogy": {
        "why_it_works": "Wait-time increases cognitive effort.",
        "cognitive_target": "independent reasoning"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["EMOTIONAL_DISTRESS"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DEPENDENT"
    },
    "tags": ["wait_time", "independence"]
},
{
    "solution_id": "write_question_then_explain",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["VERBAL_OVERLOAD", "MISSED_INSTRUCTIONS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "INSTRUCTION_CLARITY",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Write Then Explain",
        "action_text": "Write the question first, then explain it."
    },
    "details": {
        "objective": "Anchor attention before explanation.",
        "steps": [
            "Write the question fully.",
            "Pause for reading.",
            "Explain verbally."
        ],
        "time_required_min": 2,
        "materials_needed": ["board"],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Visual anchors support auditory processing.",
        "cognitive_target": "comprehension"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "LOST"
    },
    "tags": ["clarity", "anchoring"]
},
{
    "solution_id": "private_redirect_at_desk",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["REPEATED_OFF_TASK", "PUBLIC_CORRECTION_RISK"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "BEHAVIOR_SUPPORT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Quiet Desk Redirect",
        "action_text": "Redirect behavior quietly at the student’s desk."
    },
    "details": {
        "objective": "Correct behavior without public attention.",
        "steps": [
            "Approach student quietly.",
            "State expectation briefly.",
            "Leave immediately."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Private correction reduces defensiveness.",
        "cognitive_target": "self-regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["SAFETY_RISK"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DISTRACTING"
    },
    "tags": ["behavior", "discretion"]
},
{
    "solution_id": "summarize_then_continue",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["MID_LESSON_CONFUSION", "LOSS_OF_THREAD"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CLARIFICATION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Quick Summary Reset",
        "action_text": "Summarize briefly before continuing."
    },
    "details": {
        "objective": "Restore shared understanding mid-lesson.",
        "steps": [
            "Pause instruction.",
            "Summarize key idea in one sentence.",
            "Resume lesson."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Reorientation improves comprehension.",
        "cognitive_target": "concept integration"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "CONFUSED"
    },
    "tags": ["summary", "clarity"]
},
{
    "solution_id": "one_question_focus_rule",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["QUESTION_PILEUP", "TIME_PRESSURE"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "QUESTION_MANAGEMENT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "One Question at a Time",
        "action_text": "Limit discussion to one question at a time."
    },
    "details": {
        "objective": "Maintain clarity and pacing.",
        "steps": [
            "State the one-question rule.",
            "Address current question fully.",
            "Move to the next."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "firm_calm"
    },
    "pedagogy": {
        "why_it_works": "Focused discussion prevents overload.",
        "cognitive_target": "attention control"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["OPEN_DISCUSSION_MODE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "OVERLOADED"
    },
    "tags": ["focus", "questions"]
},
{
    "solution_id": "acknowledge_emotion_redirect_task",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["EMOTIONAL_DISRUPTION", "LOSS_OF_FOCUS"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "EMOTIONAL_CONTAINMENT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Acknowledge and Redirect",
        "action_text": "Acknowledge emotion briefly, then redirect to task."
    },
    "details": {
        "objective": "Contain emotion without derailing class.",
        "steps": [
            "Acknowledge feeling briefly.",
            "State next task clearly.",
            "Resume instruction."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "calm_supportive"
    },
    "pedagogy": {
        "why_it_works": "Validation reduces escalation.",
        "cognitive_target": "emotional regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["SEVERE_EMOTIONAL_EVENT"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UPSET"
    },
    "tags": ["emotion", "containment"]
},
{
    "solution_id": "restate_success_criteria",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["UNCLEAR_GOALS", "POOR_OUTPUT"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "EXPECTATION_RESET",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Restate Success Criteria",
        "action_text": "Restate what a good answer must include."
    },
    "details": {
        "objective": "Align student effort with expectations.",
        "steps": [
            "State 2–3 success points.",
            "Point to where they apply.",
            "Ask students to continue."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Clear criteria improves output quality.",
        "cognitive_target": "goal alignment"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "MISALIGNED"
    },
    "tags": ["expectations", "clarity"]
},
{
    "solution_id": "end_with_next_step_prompt",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["UNCERTAIN_ENDING", "LOW_CONTINUITY"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CLOSURE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "State the Next Step",
        "action_text": "End class by stating the immediate next step."
    },
    "details": {
        "objective": "Maintain continuity between lessons.",
        "steps": [
            "State what comes next clearly.",
            "Link it to today’s work.",
            "Dismiss class."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "assured"
    },
    "pedagogy": {
        "why_it_works": "Clear transitions improve learning flow.",
        "cognitive_target": "continuity"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNCERTAIN"
    },
    "tags": ["closure", "continuity"]
},
{
    "solution_id": "anticipate_common_error_before_task",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["RECURRING_MISTAKES", "TASK_START"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "ERROR_PREVENTION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Warn About Common Mistake",
        "action_text": "Briefly warn students about a common mistake before they begin."
    },
    "details": {
        "objective": "Prevent predictable errors proactively.",
        "steps": [
            "State the common mistake.",
            "Explain it in one line.",
            "Ask students to avoid it."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "matter_of_fact"
    },
    "pedagogy": {
        "why_it_works": "Forewarning improves error monitoring.",
        "cognitive_target": "error awareness"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["FIRST_TIME_EXPOSURE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "CARELESS"
    },
    "tags": ["error_prevention", "clarity"]
},
{
    "solution_id": "check_one_example_only",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["DEPENDENCE_ON_TEACHER", "CONFIDENCE_GAP"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "INDEPENDENCE_BUILDING",
    "learning_mode": "GUIDED",
    "preview": {
        "title": "Check Only One Example",
        "action_text": "Check only the first example, then ask students to continue alone."
    },
    "details": {
        "objective": "Reduce over-reliance on teacher validation.",
        "steps": [
            "Check one example publicly.",
            "Say the rest will not be checked now.",
            "Ask students to continue independently."
        ],
        "time_required_min": 2,
        "materials_needed": [],
        "teacher_tone": "firm_supportive"
    },
    "pedagogy": {
        "why_it_works": "Limited checking promotes self-reliance.",
        "cognitive_target": "independent practice"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["HIGH_STAKES_TASK"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DEPENDENT"
    },
    "tags": ["independence", "confidence"]
},
{
    "solution_id": "fast_finishers_extension_prompt",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["EARLY_FINISHERS", "IDLE_STUDENTS"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "DIFFERENTIATION",
    "learning_mode": "SELF_DIRECTED",
    "preview": {
        "title": "Extension for Early Finishers",
        "action_text": "Give a short extension task to students who finish early."
    },
    "details": {
        "objective": "Keep early finishers engaged without distracting others.",
        "steps": [
            "Prepare one extension question.",
            "Direct early finishers to it.",
            "Do not announce publicly."
        ],
        "time_required_min": 3,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Prevents boredom and off-task behavior.",
        "cognitive_target": "application"
    },
    "constraints": {
        "requires": ["PREPARED_EXTENSION"],
        "avoid_if": ["WHOLE_CLASS_SYNC_REQUIRED"]
    },
    "effort_level": "MEDIUM",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "medium",
        "student_state": "AHEAD"
    },
    "tags": ["differentiation", "engagement"]
},
{
    "solution_id": "slow_down_speech_signal",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["PROCESSING_LAG", "MISSED_CONTENT"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "DELIVERY_ADJUSTMENT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Slow Down Signal",
        "action_text": "Slow down speech intentionally when confusion appears."
    },
    "details": {
        "objective": "Improve comprehension through pacing.",
        "steps": [
            "Notice confusion cues.",
            "Slow speech and shorten sentences.",
            "Check understanding visually."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "deliberate"
    },
    "pedagogy": {
        "why_it_works": "Reduced pace improves processing.",
        "cognitive_target": "auditory comprehension"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "LOST"
    },
    "tags": ["pacing", "clarity"]
},
{
    "solution_id": "one_board_example_leave_visible",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["REFERENCE_NEED", "WORKING_MEMORY_LIMIT"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "WORK_SUPPORT",
    "learning_mode": "GUIDED",
    "preview": {
        "title": "Leave One Example Visible",
        "action_text": "Leave one solved example visible while students work."
    },
    "details": {
        "objective": "Support memory during independent work.",
        "steps": [
            "Solve one example.",
            "Do not erase it.",
            "Refer students to it as needed."
        ],
        "time_required_min": 2,
        "materials_needed": ["board"],
        "teacher_tone": "supportive"
    },
    "pedagogy": {
        "why_it_works": "External memory aids reduce cognitive load.",
        "cognitive_target": "working memory support"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "FORGETFUL"
    },
    "tags": ["reference", "scaffolding"]
},
{
    "solution_id": "address_whole_class_not_individual",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["PUBLIC_CORRECTION_RISK", "DEFENSIVENESS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "SAFE_CORRECTION",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Address the Whole Class",
        "action_text": "Address an issue to the whole class instead of an individual."
    },
    "details": {
        "objective": "Correct behavior without embarrassment.",
        "steps": [
            "State the expectation to the class.",
            "Avoid names or eye contact.",
            "Continue lesson."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Generalization reduces defensiveness.",
        "cognitive_target": "self-monitoring"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["SAFETY_ISSUE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DEFENSIVE"
    },
    "tags": ["safety", "correction"]
},
{
    "solution_id": "silent_individual_reset_minute",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["OVERSTIMULATION", "LOSS_OF_SELF_CONTROL"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "SELF_REGULATION",
    "learning_mode": "SELF_DIRECTED",
    "preview": {
        "title": "One Silent Minute",
        "action_text": "Give one silent minute to reset focus."
    },
    "details": {
        "objective": "Restore self-control without discussion.",
        "steps": [
            "Ask for complete silence.",
            "Wait one minute.",
            "Resume activity."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "calm"
    },
    "pedagogy": {
        "why_it_works": "Silence resets cognitive arousal.",
        "cognitive_target": "self-regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["PANIC_OR_DISTRESS"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "ZERO",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "OVERSTIMULATED"
    },
    "tags": ["reset", "regulation"]
},
{
    "solution_id": "explicit_time_warning",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["TIME_MISMANAGEMENT", "RUSHED_ENDING"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "TIME_AWARENESS",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Time Remaining Warning",
        "action_text": "State clearly how much time remains."
    },
    "details": {
        "objective": "Improve pacing awareness.",
        "steps": [
            "Announce time remaining.",
            "State what should be done in that time.",
            "Proceed."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Time cues improve task completion.",
        "cognitive_target": "time management"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNAWARE"
    },
    "tags": ["time", "pacing"]
},
{
    "solution_id": "close_loop_on_question",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["UNRESOLVED_QUERY", "CONFUSION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "QUESTION_CLOSURE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Close the Question Loop",
        "action_text": "Explicitly state when a question has been answered."
    },
    "details": {
        "objective": "Prevent lingering confusion.",
        "steps": [
            "Answer the question.",
            "State: 'This answers the question.'",
            "Move on."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "assured"
    },
    "pedagogy": {
        "why_it_works": "Explicit closure improves clarity.",
        "cognitive_target": "comprehension closure"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNCERTAIN"
    },
    "tags": ["closure", "questions"]
},
{
    "solution_id": "restate_instruction_before_release",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["CHAOTIC_START", "MISUNDERSTOOD_TASK"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "TASK_RELEASE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Restate Instructions Before Release",
        "action_text": "Restate the task once more before students begin."
    },
    "details": {
        "objective": "Ensure alignment before work starts.",
        "steps": [
            "Restate instructions briefly.",
            "Ask for nods or visual confirmation.",
            "Release students to work."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Final clarity prevents downstream confusion.",
        "cognitive_target": "task understanding"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["EXAM_CONDITIONS"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNSURE"
    },
    "tags": ["instructions", "alignment"]
},
{
    "solution_id": "announce_working_silence_window",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["NOISE_BUILDUP", "LOSS_OF_FOCUS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "FOCUS_CONTROL",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Silent Work Window",
        "action_text": "Announce a short silent working window."
    },
    "details": {
        "objective": "Stabilize attention without confrontation.",
        "steps": [
            "Announce a 2-minute silent work window.",
            "Start timing silently.",
            "Resume normal flow afterward."
        ],
        "time_required_min": 2,
        "materials_needed": ["timer_optional"],
        "teacher_tone": "firm_calm"
    },
    "pedagogy": {
        "why_it_works": "Clear boundaries reduce background noise.",
        "cognitive_target": "sustained attention"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["DISCUSSION_MODE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "CHATTERING"
    },
    "tags": ["focus", "silence"]
},
{
    "solution_id": "acknowledge_then_delay_help",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["HELP_SEEKING_DEPENDENCE", "INTERRUPTIONS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "INDEPENDENCE_SUPPORT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Acknowledge, Then Delay Help",
        "action_text": "Acknowledge a help request and ask the student to try first."
    },
    "details": {
        "objective": "Encourage persistence before assistance.",
        "steps": [
            "Acknowledge the request.",
            "Ask student to try for one minute.",
            "Return if still needed."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "supportive"
    },
    "pedagogy": {
        "why_it_works": "Delay increases effort and problem-solving.",
        "cognitive_target": "independence"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["HIGH_FRUSTRATION"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DEPENDENT"
    },
    "tags": ["independence", "persistence"]
},
{
    "solution_id": "reset_expectation_language",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["NEGATIVE_CLASS_TONE", "LOW_MORALE"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CLASSROOM_CLIMATE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Reset Expectation Language",
        "action_text": "Restate expectations using neutral, calm language."
    },
    "details": {
        "objective": "Stabilize tone and reduce tension.",
        "steps": [
            "Pause instruction briefly.",
            "Restate expectations neutrally.",
            "Resume lesson."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Tone reset prevents escalation.",
        "cognitive_target": "emotional regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "TENSE"
    },
    "tags": ["tone", "safety"]
},
{
    "solution_id": "switch_input_mode_briefly",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["Cognitive_FATIGUE", "LOSS_OF_ENGAGEMENT"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "MODE_SWITCH",
    "learning_mode": "GUIDED",
    "preview": {
        "title": "Switch Input Mode",
        "action_text": "Switch briefly from listening to writing or vice versa."
    },
    "details": {
        "objective": "Refresh attention through mode change.",
        "steps": [
            "Pause current mode.",
            "Switch to writing or listening.",
            "Return to original task."
        ],
        "time_required_min": 2,
        "materials_needed": ["notebooks_optional"],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Mode variation reduces mental fatigue.",
        "cognitive_target": "attention renewal"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["STRICT_EXAM"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "FATIGUED"
    },
    "tags": ["engagement", "reset"]
},
{
    "solution_id": "name_and_continue_rule",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["MINOR_RULE_BREAK", "FLOW_DISRUPTION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "RULE_ENFORCEMENT",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Name Rule and Continue",
        "action_text": "Name the rule briefly and continue teaching."
    },
    "details": {
        "objective": "Enforce rules without escalation.",
        "steps": [
            "Name the rule once.",
            "Do not debate.",
            "Continue instruction."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "firm_neutral"
    },
    "pedagogy": {
        "why_it_works": "Consistency maintains authority calmly.",
        "cognitive_target": "behavior regulation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["REPEATED_DEFIANCE"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "TESTING_LIMITS"
    },
    "tags": ["rules", "authority"]
},
{
    "solution_id": "single_example_then_release",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["OVER_TEACHING", "LOW_STUDENT_ACTION"],
    "subjects": ["GENERAL"],
    "class_range": "UPPER",
    "topic_type": "TASK_RELEASE",
    "learning_mode": "MODELED",
    "preview": {
        "title": "One Example Only",
        "action_text": "Demonstrate only one example before releasing students."
    },
    "details": {
        "objective": "Prevent over-scaffolding.",
        "steps": [
            "Demonstrate one example.",
            "Stop explanation.",
            "Release students to work."
        ],
        "time_required_min": 2,
        "materials_needed": ["board"],
        "teacher_tone": "decisive"
    },
    "pedagogy": {
        "why_it_works": "Early practice increases learning ownership.",
        "cognitive_target": "active learning"
    },
    "constraints": {
        "requires": [],
        "avoid_if": ["FIRST_EXPOSURE_COMPLEX"]
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "PASSIVE"
    },
    "tags": ["release", "ownership"]
},
{
    "solution_id": "check_body_language_scan",
    "version": 1,
    "status": "active",
    "response_style": "COGNITIVE",
    "situations": ["HIDDEN_CONFUSION", "MISSED_SIGNALS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "AWARENESS",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Body Language Scan",
        "action_text": "Quickly scan student body language for confusion."
    },
    "details": {
        "objective": "Detect confusion early.",
        "steps": [
            "Scan faces and posture.",
            "Pause if confusion is widespread.",
            "Clarify briefly."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "observant"
    },
    "pedagogy": {
        "why_it_works": "Non-verbal cues reveal understanding gaps.",
        "cognitive_target": "metacognitive monitoring"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNCLEAR"
    },
    "tags": ["awareness", "observation"]
},
{
    "solution_id": "verbal_checkpoint_question",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["ASSUMED_UNDERSTANDING", "GAPS"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "CHECKPOINT",
    "learning_mode": "WHOLE_CLASS",
    "preview": {
        "title": "Checkpoint Question",
        "action_text": "Ask one simple checkpoint question before moving on."
    },
    "details": {
        "objective": "Confirm readiness to proceed.",
        "steps": [
            "Ask a simple checkpoint question.",
            "Listen for confidence.",
            "Proceed or clarify."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "neutral"
    },
    "pedagogy": {
        "why_it_works": "Small checks prevent compounding gaps.",
        "cognitive_target": "understanding verification"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "UNCERTAIN"
    },
    "tags": ["checkpoint", "clarity"]
},
{
    "solution_id": "explicit_end_of_activity_signal",
    "version": 1,
    "status": "active",
    "response_style": "BEHAVIORAL",
    "situations": ["MESSY_ACTIVITY_END", "TRANSITION_CONFUSION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "ACTIVITY_CLOSURE",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Clear End Signal",
        "action_text": "Explicitly signal the end of an activity."
    },
    "details": {
        "objective": "Prevent confusion during transitions.",
        "steps": [
            "Announce activity end.",
            "Give one clear instruction.",
            "Transition calmly."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "clear"
    },
    "pedagogy": {
        "why_it_works": "Clear signals reduce transition chaos.",
        "cognitive_target": "task switching"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DISORIENTED"
    },
    "tags": ["transition", "closure"]
},
{
    "solution_id": "final_attention_anchor_statement",
    "version": 1,
    "status": "active",
    "response_style": "STRUCTURAL",
    "situations": ["END_OF_CLASS_DRIFT", "LOW_RETENTION"],
    "subjects": ["GENERAL"],
    "class_range": "ANY",
    "topic_type": "FINAL_ANCHOR",
    "learning_mode": "TEACHER_LED",
    "preview": {
        "title": "Final Anchor Sentence",
        "action_text": "End with one sentence students should remember."
    },
    "details": {
        "objective": "Anchor learning at class end.",
        "steps": [
            "State one key sentence clearly.",
            "Pause briefly.",
            "Dismiss class."
        ],
        "time_required_min": 1,
        "materials_needed": [],
        "teacher_tone": "assured"
    },
    "pedagogy": {
        "why_it_works": "Single anchors improve recall.",
        "cognitive_target": "memory consolidation"
    },
    "constraints": {
        "requires": [],
        "avoid_if": []
    },
    "effort_level": "LOW",
    "classroom_safety": "HIGH",
    "noise_level": "VERY_LOW",
    "works_best_when": {
        "class_strength": "any",
        "student_state": "DRIFTING"
    },
    "tags": ["retention", "closure"]
},
]