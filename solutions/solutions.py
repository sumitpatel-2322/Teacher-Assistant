"""
Theme 1 Decision Engine
Solution Library (Structured, Immutable, In-Memory)
"""

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

# ======================================================
# SOLUTION LIBRARY
# ======================================================

SOLUTION_LIBRARY = [
    {
        "solution_id": "peer_teaching_math_mixed_levels",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": [SITUATIONS["MIXED_LEARNING_LEVELS"], SITUATIONS["LOW_ATTENTION"]],
        "subjects": [SUBJECTS["MATH"]],
        "class_range": CLASS_RANGES["MIDDLE"],
        "topic_type": TOPIC_TYPES["CONCEPTUAL"],
        "learning_mode": LEARNING_MODES["VERBAL"],
        "preview": {
            "title": "Peer Teaching in Pairs",
            "action_text": "Pair fast learners with struggling students and let them explain the steps."
        },
        "details": {
            "objective": "Help struggling students understand the concept through peer explanation.",
            "steps": [
                "Identify students who have completed the task correctly.",
                "Pair each confident student with a struggling peer.",
                "Ask the confident student to explain the steps verbally.",
                "Move around the class and listen for misconceptions.",
                "Clarify common mistakes once all pairs finish."
            ],
            "time_required_min": 5,
            "materials_needed": [],
            "teacher_tone": "calm",
        },
        "pedagogy": {
            "why_it_works": "Peer explanations use familiar language and reduce hesitation.",
            "cognitive_target": "understanding",
        },
        "constraints": {
            "requires": [],
            "avoid_if": [CONSTRAINTS["TIME_PRESSURE"]],
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"],
        "noise_level": NOISE_LEVELS["MEDIUM"],
        "works_best_when": {
            "class_strength": "large",
            "student_state": STUDENT_STATES["MIXED"],
        },
        "tags": ["peer_learning", "differentiation", "math"],
    },
    {
        "solution_id": "silent_think_time_general_low_attention",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": [SITUATIONS["LOW_ATTENTION"]],
        "subjects": [SUBJECTS["GENERAL"]],
        "class_range": CLASS_RANGES["MIDDLE"],
        "topic_type": TOPIC_TYPES["CONCEPTUAL"],
        "learning_mode": LEARNING_MODES["MIXED"],
        "preview": {
            "title": "Silent Think Time",
            "action_text": "Pause the class and give students two minutes to think quietly."
        },
        "details": {
            "objective": "Reset attention and allow students to mentally refocus.",
            "steps": [
                "Ask students to stop writing and sit quietly.",
                "Give them two minutes to think about the last concept explained.",
                "After time ends, ask one or two students to share their thoughts.",
            ],
            "time_required_min": 3,
            "materials_needed": [],
            "teacher_tone": "calm",
        },
        "pedagogy": {
            "why_it_works": "Silence helps reduce cognitive overload and restores focus.",
            "cognitive_target": "attention",
        },
        "constraints": {
            "requires": [],
            "avoid_if": [],
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"],
        "noise_level": NOISE_LEVELS["LOW"],
        "works_best_when": {
            "class_strength": "any",
            "student_state": STUDENT_STATES["RESTLESS"],
        },
        "tags": ["attention_reset", "focus"],
    },
    {
        "solution_id": "visual_math_story_primary",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["LOW_ENGAGEMENT", "CONCEPT_NOT_CLEAR"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Use Visual Stories for Basic Arithmetic",
            "action_text": "Create a simple story problem using pictures and characters to demonstrate addition or subtraction."
        },
        "details": {
            "objective": "To help students visualize mathematical operations through storytelling.",
            "steps": [
                "Choose an arithmetic concept (e.g., addition).",
                "Create a story with characters (e.g., animals collecting fruits).",
                "Draw the story step-by-step on the board while narrating it.",
                "Ask students to suggest the next part of the story using numbers.",
                "Write the numeric equation and solve it together."
            ],
            "time_required_min": 15,
            "materials_needed": ["blackboard", "chalk", "optional: flashcards or story props"],
            "teacher_tone": "enthusiastic"
        },
        "pedagogy": {
            "why_it_works": "Visual narratives build comprehension, reduce abstraction, and increase engagement.",
            "cognitive_target": "understanding"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["storytelling", "arithmetic", "visual_learning"]
    },
    {
        "solution_id": "circle_time_inclusivity_primary",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["STUDENT_ISOLATED", "LOW_PARTICIPATION"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "SOCIAL_EMOTIONAL",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Morning Circle for Participation",
            "action_text": "Begin class with an inclusive circle time to allow every student to share something verbally."
        },
        "details": {
            "objective": "To promote inclusivity, verbal expression, and classroom bonding.",
            "steps": [
                "Arrange students in a circle at the start of class.",
                "Ask an open-ended question (e.g., What made you smile today?).",
                "Give each student a chance to speak (no interruptions).",
                "Model listening by acknowledging each response.",
                "Close the circle with a positive group affirmation."
            ],
            "time_required_min": 10,
            "materials_needed": [],
            "teacher_tone": "warm"
        },
        "pedagogy": {
            "why_it_works": "Routine sharing builds empathy and classroom cohesion.",
            "cognitive_target": "expression"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "QUIET"
        },
        "tags": ["inclusion", "circle_time", "expression"]
    },
    {
        "solution_id": "group_poster_science_mixed",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["MIXED_LEARNING_LEVELS", "LOW_ENGAGEMENT"],
        "subjects": ["SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "APPLICATION",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Make a Poster on Environmental Topics",
            "action_text": "In groups, make a poster on a science topic like water conservation or pollution."
        },
        "details": {
            "objective": "To foster collaboration and real-world science application.",
            "steps": [
                "Divide class into small mixed-ability groups.",
                "Assign each group a sub-topic (e.g., air pollution).",
                "Give chart paper and markers.",
                "Ask students to draw and label a poster showing problems and solutions.",
                "Groups present their posters to the class."
            ],
            "time_required_min": 20,
            "materials_needed": ["chart paper", "markers", "reference books"],
            "teacher_tone": "facilitative"
        },
        "pedagogy": {
            "why_it_works": "Team tasks reinforce cooperation and topic retention through creative expression.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": ["STATIONERY"],
            "avoid_if": []
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "MIXED"
        },
        "tags": ["science", "group_work", "poster"]
    },
    {
        "solution_id": "think_pair_share_language_upper",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ATTENTION", "DISENGAGEMENT"],
        "subjects": ["LANGUAGE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Think-Pair-Share Exercise",
            "action_text": "Pose a question, let students think, discuss in pairs, and then share."
        },
        "details": {
            "objective": "Encourage deeper thinking and student voice in language learning.",
            "steps": [
                "Ask an open-ended question based on the day's topic.",
                "Give 30 seconds for students to think silently.",
                "Pair students to discuss for 2 minutes.",
                "Invite volunteers to share their pair’s insights.",
                "Summarize with your own take."
            ],
            "time_required_min": 7,
            "materials_needed": [],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Small steps break fear of speaking and deepen reflection.",
            "cognitive_target": "analysis"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "LOW_ATTENTION"
        },
        "tags": ["language", "student_voice", "interactive"]
    },
    {
        "solution_id": "exit_card_reflection_secondary",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["UNCLEAR_UNDERSTANDING"],
        "subjects": ["GENERAL"],
        "class_range": "SECONDARY",
        "topic_type": "REFLECTIVE",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Exit Card at Lesson End",
            "action_text": "Ask students to write down the main idea and one question at the end of class."
        },
        "details": {
            "objective": "To reflect on what was learned and identify gaps.",
            "steps": [
                "Distribute small slips or notebooks at end of class.",
                "Ask each student to write one thing they learned and one doubt.",
                "Collect all cards before dismissal.",
                "Review them to plan the next class.",
                "Address patterns or misconceptions next day."
            ],
            "time_required_min": 5,
            "materials_needed": ["paper slips", "pens"],
            "teacher_tone": "reflective"
        },
        "pedagogy": {
            "why_it_works": "Reflection helps consolidate learning and offers feedback for teaching.",
            "cognitive_target": "evaluation"
        },
        "constraints": {
            "requires": ["STATIONERY"],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "ANY"
        },
        "tags": ["assessment", "reflection", "secondary"]
    },
    {
        "solution_id": "language_picture_prompt_primary",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["RELUCTANT_TO_WRITE", "IDEA_BLOCK"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "CREATIVE",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Use Picture Prompts to Inspire Writing",
            "action_text": "Show a picture and ask students to write a story or description based on what they see."
        },
        "details": {
            "objective": "Encourage creativity and descriptive writing in young learners.",
            "steps": [
                "Select a colorful and interesting picture (e.g., a market, a park).",
                "Display it on the board or distribute copies.",
                "Ask students to describe what’s happening in the picture.",
                "Let them write a short paragraph or story based on their imagination.",
                "Invite volunteers to read out their writing."
            ],
            "time_required_min": 15,
            "materials_needed": ["picture printouts or digital image display", "notebooks"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Visual stimuli unlock creative thinking and help generate ideas.",
            "cognitive_target": "expression"
        },
        "constraints": {
            "requires": ["VISUAL_DISPLAY"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "QUIET"
        },
        "tags": ["writing", "creativity", "visual"]
    },
    {
        "solution_id": "math_manipulative_sorting_game",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONCEPT_NOT_CLEAR", "RESTLESS_CLASS"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Sorting Game with Manipulatives",
            "action_text": "Give physical objects to sort by shape, size, or color for math classification practice."
        },
        "details": {
            "objective": "Help children understand classification and patterning in early mathematics.",
            "steps": [
                "Bring a mix of objects (buttons, blocks, shapes).",
                "Give each group a tray of mixed objects.",
                "Ask them to sort by a given rule (e.g., color or shape).",
                "Discuss different sorting strategies and results.",
                "Let groups present and explain their sorting logic."
            ],
            "time_required_min": 12,
            "materials_needed": ["manipulatives (shapes, buttons, etc.)"],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Tactile experiences help internalize abstract mathematical ideas.",
            "cognitive_target": "categorization"
        },
        "constraints": {
            "requires": ["CLASSROOM_MATERIALS"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "RESTLESS"
        },
        "tags": ["math", "manipulatives", "sorting"]
    },
    {
        "solution_id": "peer_review_language_secondary",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_SELF_AWARENESS", "WEAK_WRITING"],
        "subjects": ["LANGUAGE"],
        "class_range": "SECONDARY",
        "topic_type": "EVALUATION",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Peer Review for Writing Assignments",
            "action_text": "Have students exchange drafts and give each other structured feedback."
        },
        "details": {
            "objective": "Improve writing skills and critical thinking through peer feedback.",
            "steps": [
                "Teach students a simple feedback format (e.g., what I liked, what could be improved).",
                "Pair them up and exchange writing pieces.",
                "Ask each to give 2 comments: one praise and one suggestion.",
                "Give time to revise their work based on peer input.",
                "Ask volunteers to share their revised drafts."
            ],
            "time_required_min": 15,
            "materials_needed": ["writing samples", "feedback sheets"],
            "teacher_tone": "constructive"
        },
        "pedagogy": {
            "why_it_works": "Feedback from peers increases ownership and awareness of writing quality.",
            "cognitive_target": "evaluation"
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
            "student_state": "MIXED"
        },
        "tags": ["peer_review", "writing", "feedback"]
    },
    {
        "solution_id": "science_role_play_cells_upper",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LOW_RETENTION", "BOREDOM"],
        "subjects": ["SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "DRAMATIC",
        "preview": {
            "title": "Role-Play a Cell",
            "action_text": "Students act as cell organelles to learn their functions in a fun way."
        },
        "details": {
            "objective": "To understand cell organelles and their functions through embodied learning.",
            "steps": [
                "List major organelles (nucleus, mitochondria, etc.) and their functions.",
                "Assign one organelle to each student or group.",
                "Give them time to prepare a small act or gesture representing their function.",
                "Have the 'cell' act performed by the class in sequence.",
                "Discuss and summarize the learning points."
            ],
            "time_required_min": 20,
            "materials_needed": ["labels or simple props for organelles"],
            "teacher_tone": "energetic"
        },
        "pedagogy": {
            "why_it_works": "Role-play aids memory and transforms abstract topics into real experience.",
            "cognitive_target": "understanding"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["science", "biology", "role_play"]
    },
    {
        "solution_id": "formative_quiz_gamified_secondary",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["UNCLEAR_UNDERSTANDING", "LOW_MOTIVATION"],
        "subjects": ["GENERAL"],
        "class_range": "SECONDARY",
        "topic_type": "ASSESSMENT",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Gamified Quiz for Formative Assessment",
            "action_text": "Use a point-based quiz competition to check topic understanding in an engaging way."
        },
        "details": {
            "objective": "Check understanding in a non-threatening and engaging format.",
            "steps": [
                "Prepare 10–15 questions based on the topic.",
                "Divide class into 3–4 teams.",
                "Assign points for correct answers and bonus points for harder ones.",
                "Rotate question turns across teams.",
                "Debrief with key learning at the end."
            ],
            "time_required_min": 15,
            "materials_needed": ["questions", "score chart"],
            "teacher_tone": "lively"
        },
        "pedagogy": {
            "why_it_works": "Gamification boosts engagement while offering formative feedback.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "ANY"
        },
        "tags": ["quiz", "assessment", "gamification"]
    },
    {
        "solution_id": "group_poster_reflection_environment",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ENGAGEMENT", "PASSIVE_LEARNING"],
        "subjects": ["EVS"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "REFLECTIVE",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Poster-Making on Environmental Issues",
            "action_text": "Students make group posters highlighting local environmental concerns and solutions."
        },
        "details": {
            "objective": "Promote awareness and reflection on environmental topics.",
            "steps": [
                "Divide students into small groups.",
                "Assign each group a specific environmental concern (e.g., plastic use, deforestation).",
                "Ask them to brainstorm causes, effects, and solutions.",
                "Provide art materials to make a visual poster.",
                "Facilitate a gallery walk where groups present their posters."
            ],
            "time_required_min": 25,
            "materials_needed": ["chart paper", "markers", "glue", "magazines"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Group reflection and artistic expression deepen awareness and teamwork.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": ["ART_SUPPLIES"],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "MIXED"
        },
        "tags": ["environment", "group_work", "visual_learning"]
    },
    {
        "solution_id": "math_estimation_market_game",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LOW_PARTICIPATION", "REAL_WORLD_DISCONNECT"],
        "subjects": ["MATH"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "APPLICATION",
        "learning_mode": "ROLEPLAY",
        "preview": {
            "title": "Estimation Game Using a Fake Market",
            "action_text": "Create a role-play market scenario where students estimate total costs of items."
        },
        "details": {
            "objective": "Practice estimation and addition in a real-life inspired setting.",
            "steps": [
                "Set up a fake 'market' with price tags on everyday items.",
                "Distribute role cards: buyers and shopkeepers.",
                "Ask buyers to pick 3–5 items and estimate total cost.",
                "Shopkeepers confirm actual total using math.",
                "Compare estimation vs. actual, reflect on gaps."
            ],
            "time_required_min": 20,
            "materials_needed": ["item pictures", "price tags", "play money"],
            "teacher_tone": "enthusiastic"
        },
        "pedagogy": {
            "why_it_works": "Situational games simulate real-world tasks, anchoring math concepts.",
            "cognitive_target": "estimation"
        },
        "constraints": {
            "requires": ["ROLEPLAY_SPACE"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "ACTIVE"
        },
        "tags": ["math", "estimation", "roleplay"]
    },
    {
        "solution_id": "science_think_pair_share_concepts",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["CONFUSION", "QUIET_CLASS"],
        "subjects": ["SCIENCE"],
        "class_range": "SECONDARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Think-Pair-Share for Concept Clarity",
            "action_text": "Pose a question, let students think alone, then discuss in pairs before sharing out."
        },
        "details": {
            "objective": "Clarify science concepts through collaborative verbal reasoning.",
            "steps": [
                "Pose a conceptual question (e.g., Why do objects fall at the same rate?).",
                "Let students think individually for 2 minutes.",
                "Pair them to discuss their answers.",
                "Invite pairs to share conclusions with the class.",
                "Summarize the concept with correct explanation."
            ],
            "time_required_min": 10,
            "materials_needed": [],
            "teacher_tone": "inquisitive"
        },
        "pedagogy": {
            "why_it_works": "Encourages every student to think, speak, and listen — reducing passivity.",
            "cognitive_target": "reasoning"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "QUIET"
        },
        "tags": ["science", "collaboration", "verbal_learning"]
    },
    {
        "solution_id": "integrated_storytelling_social_science",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TOPIC_DISCONNECT", "MONOTONY"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "NARRATIVE",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Tell a Story with a Historical Twist",
            "action_text": "Weave a fictional story that includes real historical facts and events."
        },
        "details": {
            "objective": "Improve historical memory through engaging storytelling.",
            "steps": [
                "Pick a topic (e.g., Mughal period).",
                "Create or narrate a fictional character living in that era.",
                "Let students guess real vs. fictional events.",
                "Pause and ask reflective questions.",
                "Close with a summary linking to textbook points."
            ],
            "time_required_min": 12,
            "materials_needed": ["story script (optional)"],
            "teacher_tone": "dramatic"
        },
        "pedagogy": {
            "why_it_works": "Narratives trigger emotion and curiosity, aiding memory and interest.",
            "cognitive_target": "engagement"
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
            "student_state": "DISINTERESTED"
        },
        "tags": ["history", "storytelling", "engagement"]
    },
    {
        "solution_id": "mind_map_revision_session",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TOPIC_OVERLOAD", "REVISION"],
        "subjects": ["GENERAL"],
        "class_range": "SECONDARY",
        "topic_type": "REVIEW",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Mind Map for Revision",
            "action_text": "Draw a central concept and branch out key ideas as a visual study tool."
        },
        "details": {
            "objective": "Consolidate information visually for revision and concept mapping.",
            "steps": [
                "Write the main topic at the center of the board (e.g., Digestive System).",
                "Ask students to recall sub-topics and map them as branches.",
                "Add keywords, diagrams, or examples under each branch.",
                "Use colors or symbols to show connections.",
                "Review the full mind map as a class and clear doubts."
            ],
            "time_required_min": 10,
            "materials_needed": ["board", "colored markers"],
            "teacher_tone": "collaborative"
        },
        "pedagogy": {
            "why_it_works": "Mind mapping supports visual learning and concept linking during review.",
            "cognitive_target": "synthesis"
        },
        "constraints": {
            "requires": ["BOARD_SPACE"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "STRESSED"
        },
        "tags": ["revision", "visual", "study_techniques"]
    },
    {
        "solution_id": "math_movement_fraction_game",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONCEPT_NOT_CLEAR", "LOW_RETENTION"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Move to Your Fraction",
            "action_text": "Students move to spaces labeled with different fractions after solving prompts."
        },
        "details": {
            "objective": "Reinforce understanding of fractions using physical movement.",
            "steps": [
                "Mark sections of the classroom floor with fraction labels (e.g., 1/2, 1/3, 3/4).",
                "Call out prompts like 'What is half of 8?' or 'Go to 3/4 if you ate three of four parts.'",
                "Students move to the correct fraction space.",
                "Discuss why they chose that section.",
                "Summarize with 2–3 examples on the board."
            ],
            "time_required_min": 12,
            "materials_needed": ["masking tape or chalk"],
            "teacher_tone": "energizing"
        },
        "pedagogy": {
            "why_it_works": "Physical movement builds stronger memory links with math concepts.",
            "cognitive_target": "concept association"
        },
        "constraints": {
            "requires": ["SPACE"],
            "avoid_if": ["CROWDING"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "MEDIUM",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "RESTLESS"
        },
        "tags": ["fractions", "movement", "math"]
    },
    {
        "solution_id": "science_nature_walk_observation",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LACK_OF_ATTENTION", "DISENGAGEMENT"],
        "subjects": ["SCIENCE"],
        "class_range": "PRIMARY",
        "topic_type": "OBSERVATIONAL",
        "learning_mode": "EXPERIENTIAL",
        "preview": {
            "title": "Nature Walk Observation",
            "action_text": "Take students outside to observe plants, insects, and patterns in nature."
        },
        "details": {
            "objective": "Encourage observation and curiosity using real environments.",
            "steps": [
                "Brief students on what to observe (e.g., leaf shapes, insect movements).",
                "Take them outside the classroom for 10–15 minutes.",
                "Ask them to silently observe and draw/write what they see.",
                "Group discussion when back: What did they notice?",
                "Link observations to the current science topic."
            ],
            "time_required_min": 20,
            "materials_needed": ["notebooks", "pencils"],
            "teacher_tone": "calm"
        },
        "pedagogy": {
            "why_it_works": "Real-world exposure builds intrinsic motivation and observation skills.",
            "cognitive_target": "awareness"
        },
        "constraints": {
            "requires": ["SAFE_OPEN_AREA"],
            "avoid_if": ["RAINY_WEATHER"]
        },
        "effort_level": "LOW",
        "classroom_safety": "MEDIUM",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "INATTENTIVE"
        },
        "tags": ["observation", "nature", "science"]
    },
    {
        "solution_id": "language_character_hot_seat",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LOW_IMAGINATION", "PASSIVE_LEARNING"],
        "subjects": ["LANGUAGE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CREATIVE",
        "learning_mode": "DRAMATIC",
        "preview": {
            "title": "Hot Seat Character Game",
            "action_text": "Students role-play as a story character and answer peer questions."
        },
        "details": {
            "objective": "Enhance understanding of character traits and motivations.",
            "steps": [
                "Select a character from a story the class has read.",
                "Pick one student to sit in the ‘hot seat’ and answer questions in character.",
                "Rest of the class asks about the character’s feelings, choices, etc.",
                "Rotate roles to allow different characters.",
                "Reflect on how characters can be interpreted differently."
            ],
            "time_required_min": 15,
            "materials_needed": ["chair", "optional costume prop"],
            "teacher_tone": "fun"
        },
        "pedagogy": {
            "why_it_works": "Role play builds empathy and deepens literary comprehension.",
            "cognitive_target": "interpretation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["BEHAVIORAL_ISSUES"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "BASIC_INVOLVEMENT"
        },
        "tags": ["language", "roleplay", "characters"]
    },
    {
        "solution_id": "science_simple_experiment_air_pressure",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["BORING_CLASS", "THEORY_OVERLOAD"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "DEMONSTRATION",
        "learning_mode": "EXPERIENTIAL",
        "preview": {
            "title": "Air Pressure in Action",
            "action_text": "Demonstrate air pressure using an inverted glass of water."
        },
        "details": {
            "objective": "Show the concept of air pressure in a memorable way.",
            "steps": [
                "Fill a glass to the brim with water.",
                "Place a thick card on top, flip quickly and carefully.",
                "Hold it upside down — water remains inside!",
                "Ask students: why didn’t the water fall?",
                "Explain the concept of atmospheric pressure holding the card."
            ],
            "time_required_min": 5,
            "materials_needed": ["glass", "water", "card"],
            "teacher_tone": "excited"
        },
        "pedagogy": {
            "why_it_works": "Demonstrations grab attention and concretize abstract concepts.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": ["CLEAN_UP_READY"],
            "avoid_if": ["NO_SUPPLIES"]
        },
        "effort_level": "LOW",
        "classroom_safety": "MEDIUM",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNENGAGED"
        },
        "tags": ["experiment", "science", "air_pressure"]
    },
    {
        "solution_id": "group_discussion_ethics_social",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_CRITICAL_THINKING", "SHALLOW_RESPONSES"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "SECONDARY",
        "topic_type": "DISCUSSION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Group Debate on Ethical Dilemmas",
            "action_text": "Split the class into sides and let them debate a social or ethical question."
        },
        "details": {
            "objective": "Improve argumentation and reasoning skills.",
            "steps": [
                "Pick a topic like 'Should uniforms be mandatory?'.",
                "Divide the class into pro and con sides.",
                "Give 5 minutes prep time for both.",
                "Allow 3 rounds of arguments (opening, rebuttal, conclusion).",
                "Reflect as a group: what made an argument strong or weak?"
            ],
            "time_required_min": 20,
            "materials_needed": [],
            "teacher_tone": "facilitator"
        },
        "pedagogy": {
            "why_it_works": "Structured debate activates logic, articulation, and respectful disagreement.",
            "cognitive_target": "critical_thinking"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "VERBAL"
        },
        "tags": ["debate", "social_science", "discussion"]
    },
    {
        "solution_id": "pair_discussion_inclusive_values",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["DISRUPTIVE_BEHAVIOR", "LACK_OF_RESPECT"],
        "subjects": ["MORAL_EDUCATION"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "VALUES",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Pair Discussion on Respect",
            "action_text": "Pairs discuss what respect means in the classroom and beyond."
        },
        "details": {
            "objective": "Build respectful classroom behavior through values clarification.",
            "steps": [
                "Write the word 'Respect' on the board.",
                "Ask students to pair up and list actions that show respect.",
                "Let them share personal experiences where respect was shown or not.",
                "Discuss how respect affects learning and emotions.",
                "Conclude with 2–3 class rules based on mutual respect."
            ],
            "time_required_min": 10,
            "materials_needed": [],
            "teacher_tone": "empathetic"
        },
        "pedagogy": {
            "why_it_works": "Personal reflection and dialogue helps internalize social-emotional learning.",
            "cognitive_target": "value awareness"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "DISRUPTIVE"
        },
        "tags": ["respect", "values", "inclusive_education"]
    },
    {
        "solution_id": "math_skip_counting_game",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["ROUTINE_BOREDOM", "RECALL_DIFFICULTY"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "PRACTICE",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Skip Counting Jump Game",
            "action_text": "Students jump steps while chanting skip-count numbers."
        },
        "details": {
            "objective": "Reinforce skip counting through movement and rhythm.",
            "steps": [
                "Mark floor spots as 'counting stations' in a line.",
                "Call out skip count series (e.g., 5, 10, 15...).",
                "Students jump from one number to next while chanting.",
                "Group reflection: where did they stumble?",
                "Use flashcards for next round as challenge."
            ],
            "time_required_min": 10,
            "materials_needed": ["chalk", "space"],
            "teacher_tone": "lively"
        },
        "pedagogy": {
            "why_it_works": "Movement plus repetition strengthens number retention in younger students.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": ["PHYSICAL_SPACE"],
            "avoid_if": ["CLASS_TOO_FULL"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "BORED"
        },
        "tags": ["math", "skip_counting", "movement"]
    },
    {
        "solution_id": "science_sorting_activity_matter",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["THEORY_OVERLOAD", "VISUAL_LEARNERS"],
        "subjects": ["SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CATEGORIZATION",
        "learning_mode": "HANDS_ON",
        "preview": {
            "title": "Sorting Solids, Liquids, Gases",
            "action_text": "Groups sort real-life materials into states of matter categories."
        },
        "details": {
            "objective": "Identify and classify states of matter using real-world objects.",
            "steps": [
                "Bring materials: water bottle, balloon, stone, etc.",
                "Groups examine each item and decide the state of matter.",
                "Sort into labeled boxes: Solid, Liquid, Gas.",
                "Each group explains reasoning.",
                "Wrap up with board summary and follow-up questions."
            ],
            "time_required_min": 15,
            "materials_needed": ["objects of different states"],
            "teacher_tone": "inquiry-based"
        },
        "pedagogy": {
            "why_it_works": "Tactile handling improves conceptual clarity for abstract topics.",
            "cognitive_target": "classification"
        },
        "constraints": {
            "requires": ["OBJECT_KIT"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "VISUAL"
        },
        "tags": ["matter", "sorting", "science"]
    },
    {
        "solution_id": "language_sentence_chain_game",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["PASSIVITY", "GRAMMAR_ISSUES"],
        "subjects": ["LANGUAGE"],
        "class_range": "MIDDLE",
        "topic_type": "LANGUAGE_PRACTICE",
        "learning_mode": "ORAL",
        "preview": {
            "title": "Sentence Chain Speaking Game",
            "action_text": "Each student adds a word to build a meaningful sentence in sequence."
        },
        "details": {
            "objective": "Practice grammar and sequencing collaboratively.",
            "steps": [
                "Start with a simple word (e.g., 'The').",
                "Next student adds a word ('boy'), followed by next ('ran'), and so on.",
                "Chain builds into a full sentence.",
                "Reflect: Was it grammatically correct?",
                "Restart with new themes."
            ],
            "time_required_min": 8,
            "materials_needed": [],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Real-time feedback and peer collaboration make grammar fun and memorable.",
            "cognitive_target": "language sequencing"
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
            "student_state": "PASSIVE"
        },
        "tags": ["language", "grammar", "game"]
    },
    {
        "solution_id": "visual_timeline_history_topic",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["CHRONOLOGY_CONFUSION", "FACT_OVERLOAD"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "SEQUENCE",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Build a History Timeline",
            "action_text": "Class constructs a visual timeline with events and images."
        },
        "details": {
            "objective": "Understand historical sequence through collaborative timeline creation.",
            "steps": [
                "Give students key events with dates.",
                "Ask them to draw or write each event on a strip of paper.",
                "Stick strips in sequence on board or wall.",
                "Add relevant pictures or symbols.",
                "Summarize connections between events."
            ],
            "time_required_min": 15,
            "materials_needed": ["chart paper", "markers"],
            "teacher_tone": "structured"
        },
        "pedagogy": {
            "why_it_works": "Visual timelines help grasp temporal relationships and causality.",
            "cognitive_target": "sequencing"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "OVERLOADED"
        },
        "tags": ["timeline", "history", "visual"]
    },
    {
        "solution_id": "poster_activity_classroom_rules",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["RULE_BREAKING", "DISENGAGED_STUDENTS"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "BEHAVIOR",
        "learning_mode": "CREATIVE",
        "preview": {
            "title": "Design a Classroom Rules Poster",
            "action_text": "Groups make creative posters about agreed classroom rules."
        },
        "details": {
            "objective": "Involve students in defining and visualizing classroom norms.",
            "steps": [
                "Discuss important classroom rules as a class.",
                "Divide into groups and assign each group 1–2 rules.",
                "Ask them to make colorful posters illustrating those rules.",
                "Display posters around classroom.",
                "Reflect on which rules are most important and why."
            ],
            "time_required_min": 20,
            "materials_needed": ["chart paper", "colors", "sketch pens"],
            "teacher_tone": "collaborative"
        },
        "pedagogy": {
            "why_it_works": "Students feel ownership of norms they help create and visualize.",
            "cognitive_target": "internalization"
        },
        "constraints": {
            "requires": ["ART_SUPPLIES"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISTRACTED"
        },
        "tags": ["rules", "participation", "visual"]
    },
    {
        "solution_id": "math_story_problem_making",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["APPLICATION_ISSUES", "MATH_FEAR"],
        "subjects": ["MATH"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "APPLICATION",
        "learning_mode": "CREATIVE",
        "preview": {
            "title": "Create Your Own Word Problem",
            "action_text": "Students write and solve story-based math problems."
        },
        "details": {
            "objective": "Apply math concepts by constructing realistic story problems.",
            "steps": [
                "Revise a concept like multiplication or measurement.",
                "Ask students to imagine a story where this concept applies.",
                "They write a short paragraph posing a word problem.",
                "Exchange problems with peers and solve each other's.",
                "Discuss what made some problems easier/harder."
            ],
            "time_required_min": 15,
            "materials_needed": ["notebooks", "pens"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Ownership over questions reduces math anxiety and shows real-life use.",
            "cognitive_target": "application"
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
            "student_state": "DISENGAGED"
        },
        "tags": ["math", "word_problems", "application"]
    },
    {
        "solution_id": "silent_signals_classroom_management",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["NOISE_CONTROL", "TIME_MANAGEMENT"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "MANAGEMENT",
        "learning_mode": "BEHAVIORAL",
        "preview": {
            "title": "Use of Silent Signals",
            "action_text": "Teach simple hand gestures to manage classroom transitions."
        },
        "details": {
            "objective": "Smoothly transition between activities without verbal interruptions.",
            "steps": [
                "Teach hand signals for ‘quiet’, ‘attention’, ‘line up’, etc.",
                "Practice the signals for a day using games.",
                "Use signals consistently instead of shouting instructions.",
                "Reinforce usage by awarding ‘signal star’ to best responders.",
                "Reflect weekly on how well signals are followed."
            ],
            "time_required_min": 7,
            "materials_needed": ["hand signal chart"],
            "teacher_tone": "firm and positive"
        },
        "pedagogy": {
            "why_it_works": "Non-verbal cues reduce chaos and improve transition efficiency.",
            "cognitive_target": "behavioral conditioning"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "LOUD"
        },
        "tags": ["classroom_management", "nonverbal", "signals"]
    },
    {
        "solution_id": "reading_corner_language_fluency",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["READING_GAP", "SILENT_CLASS"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "FLUENCY",
        "learning_mode": "READING",
        "preview": {
            "title": "Create a Reading Corner",
            "action_text": "Set up a space where students can read books freely."
        },
        "details": {
            "objective": "Increase exposure to language through casual reading.",
            "steps": [
                "Dedicate a corner of the room with a mat and books.",
                "Ask students to choose 1–2 books each week.",
                "Allow 10 minutes of silent reading daily.",
                "Let students narrate or draw a picture about what they read.",
                "Update books weekly from school library or donations."
            ],
            "time_required_min": 10,
            "materials_needed": ["story books", "mat"],
            "teacher_tone": "nurturing"
        },
        "pedagogy": {
            "why_it_works": "Voluntary reading boosts vocabulary and fluency with minimal stress.",
            "cognitive_target": "reading habit"
        },
        "constraints": {
            "requires": ["BOOK_CORNER"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "SHY"
        },
        "tags": ["reading", "language", "corner"]
    },
    {
        "solution_id": "home_chart_parent_interaction",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["PARENT_DISCONNECT", "LACK_OF_SUPPORT"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "HOME_SUPPORT",
        "learning_mode": "COLLABORATIVE",
        "preview": {
            "title": "Home Learning Chart",
            "action_text": "Create a chart where parents record support activities at home."
        },
        "details": {
            "objective": "Involve parents in classroom learning through structured interaction.",
            "steps": [
                "Design a simple weekly home chart (e.g., read aloud, revise tables).",
                "Send it home with the student every Monday.",
                "Parents tick activities done and sign at week end.",
                "Review chart every Monday and acknowledge participation.",
                "Use patterns to guide future homework."
            ],
            "time_required_min": 5,
            "materials_needed": ["printed charts"],
            "teacher_tone": "collaborative"
        },
        "pedagogy": {
            "why_it_works": "Parent involvement is a predictor of long-term student success.",
            "cognitive_target": "home reinforcement"
        },
        "constraints": {
            "requires": ["PARENT_COMMUNICATION"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "LOW_SUPPORT"
        },
        "tags": ["parents", "homework", "engagement"]
    },
    {
        "solution_id": "mind_map_for_topic_recall",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["RECALL_DIFFICULTY", "TOPIC_REVISION"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "REVIEW",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Create a Mind Map",
            "action_text": "Students create mind maps to revise complex science topics."
        },
        "details": {
            "objective": "Enhance memory by organizing information visually.",
            "steps": [
                "Choose a key topic (e.g., water cycle).",
                "Draw a central circle with topic name.",
                "Branch out with keywords, concepts, and examples.",
                "Use images and color codes for clarity.",
                "Students present their mind maps to peers."
            ],
            "time_required_min": 12,
            "materials_needed": ["chart paper", "color pens"],
            "teacher_tone": "facilitative"
        },
        "pedagogy": {
            "why_it_works": "Visual structuring strengthens associations and memory pathways.",
            "cognitive_target": "synthesis"
        },
        "constraints": {
            "requires": ["CHART_PAPER"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["mindmap", "revision", "science"]
    },
    {
        "solution_id": "think_pair_share_reflection",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["PASSIVITY", "ONE_WORD_ANSWERS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "REFLECTION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Think-Pair-Share",
            "action_text": "Students reflect individually, pair up to discuss, then share with class."
        },
        "details": {
            "objective": "Encourage thoughtful reflection and expression.",
            "steps": [
                "Pose a reflective question to class.",
                "Give students 1 minute to think silently.",
                "Pair them to discuss answers.",
                "Invite pairs to share responses with class.",
                "Summarize common themes on the board."
            ],
            "time_required_min": 8,
            "materials_needed": [],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Promotes deeper thinking and safer speaking environment.",
            "cognitive_target": "reflection"
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
        "tags": ["reflection", "collaboration", "engagement"]
    },
    {
        "solution_id": "art_integration_for_history",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["FACT_MEMORIZATION", "LOW_ENGAGEMENT"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CULTURE",
        "learning_mode": "CREATIVE",
        "preview": {
            "title": "Make a Historical Scene Poster",
            "action_text": "Students create posters of scenes from historical events."
        },
        "details": {
            "objective": "Visualize key moments from history to aid memory.",
            "steps": [
                "Assign events like Dandi March, Ashoka’s edicts, etc.",
                "Groups sketch a scene from the event with captions.",
                "Include date and location info in poster.",
                "Present the poster and explain the event.",
                "Display posters for ongoing reference."
            ],
            "time_required_min": 15,
            "materials_needed": ["drawing paper", "colors"],
            "teacher_tone": "inspirational"
        },
        "pedagogy": {
            "why_it_works": "Art supports emotional connection and long-term retention.",
            "cognitive_target": "visual memory"
        },
        "constraints": {
            "requires": ["ART_SUPPLIES"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "BORED"
        },
        "tags": ["history", "art_integration", "visual"]
    },
    {
        "solution_id": "daily_question_wall",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["DAILY_ENGAGEMENT_DROP", "LACK_OF_CURIOSITY"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "QUESTIONING",
        "learning_mode": "REFLECTIVE",
        "preview": {
            "title": "Question of the Day Wall",
            "action_text": "Post a daily question on the board that students answer in a notebook."
        },
        "details": {
            "objective": "Promote daily curiosity and consistent reflection.",
            "steps": [
                "Prepare one open-ended question per day.",
                "Post it on a designated classroom board.",
                "Give 3–5 minutes of silent response time each morning.",
                "Occasionally discuss a few interesting responses.",
                "Let students submit their own questions weekly."
            ],
            "time_required_min": 5,
            "materials_needed": ["chalk board", "notebooks"],
            "teacher_tone": "thoughtful"
        },
        "pedagogy": {
            "why_it_works": "Routines build habits and self-expression in safe formats.",
            "cognitive_target": "curiosity"
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
            "student_state": "SILENT"
        },
        "tags": ["questioning", "routine", "reflection"]
    },
    {
        "solution_id": "topic_anchor_chart_display",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TOPIC_OVERLOAD", "FAST_CONTENT_SHIFT"],
        "subjects": ["SCIENCE", "MATH"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Create Anchor Charts",
            "action_text": "Display key formulas or diagrams for ongoing topics."
        },
        "details": {
            "objective": "Help students retain key concepts over time.",
            "steps": [
                "Identify the most critical concepts from current unit.",
                "Ask students to help make visual anchor charts.",
                "Use clear visuals, color, and big fonts.",
                "Place charts around the classroom as reference.",
                "Update with each new unit."
            ],
            "time_required_min": 10,
            "materials_needed": ["chart paper", "markers"],
            "teacher_tone": "clarifying"
        },
        "pedagogy": {
            "why_it_works": "Persistent visuals reinforce conceptual clarity and independence.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": ["WALL_SPACE"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["anchor_chart", "math", "science", "visual_aid"]
    },
    {
        "solution_id": "science_lab_rotation_demo",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["PRACTICAL_CONCEPT_GAP", "LACK_OF_EXPERIMENTATION"],
        "subjects": ["SCIENCE"],
        "class_range": "SECONDARY",
        "topic_type": "EXPERIMENTAL",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Lab Rotation Activity",
            "action_text": "Students rotate through simple experiment stations in groups."
        },
        "details": {
            "objective": "Encourage hands-on exploration of core scientific principles.",
            "steps": [
                "Set up 3–4 tables with different basic experiments (e.g., magnetism, density).",
                "Brief each group on safety and materials.",
                "Let each group rotate every 5–7 minutes.",
                "Record observations and reflect at end of session.",
                "Summarize learnings together."
            ],
            "time_required_min": 25,
            "materials_needed": ["lab kits", "station cards", "worksheet"],
            "teacher_tone": "observant"
        },
        "pedagogy": {
            "why_it_works": "Hands-on activities enhance retention and appeal to tactile learners.",
            "cognitive_target": "exploration"
        },
        "constraints": {
            "requires": ["SCIENCE_LAB"],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "MEDIUM",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "INQUISITIVE"
        },
        "tags": ["science", "lab", "experimentation"]
    },
    {
        "solution_id": "story_circle_language_expression",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["SPEAKING_HESITATION", "LANGUAGE_GAP"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "EXPRESSION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Story Circle",
            "action_text": "Students sit in a circle and build a story together."
        },
        "details": {
            "objective": "Build oral fluency through collaborative storytelling.",
            "steps": [
                "Begin with an opening line like 'Once upon a time…'",
                "Each student adds one sentence in turn.",
                "Teacher may write story on board as it progresses.",
                "Summarize and appreciate creativity.",
                "Repeat weekly with different themes."
            ],
            "time_required_min": 10,
            "materials_needed": [],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Interactive, low-pressure speech builds confidence in hesitant speakers.",
            "cognitive_target": "oral expression"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "SHY"
        },
        "tags": ["storytelling", "language", "oral"]
    },
    {
        "solution_id": "student_led_daily_summary",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_RETENTION", "PASSIVE_LEARNING"],
        "subjects": ["GENERAL"],
        "class_range": "MIDDLE",
        "topic_type": "REINFORCEMENT",
        "learning_mode": "REFLECTIVE",
        "preview": {
            "title": "Student-Led Daily Summary",
            "action_text": "One student recaps the day's learning at the end of class."
        },
        "details": {
            "objective": "Encourage synthesis and responsibility through student recaps.",
            "steps": [
                "Assign one student per day to be 'summary leader'.",
                "At end of class, they summarize what was learned.",
                "Class may add anything missed.",
                "Provide gentle feedback and rotate daily.",
                "Optionally record on board or chart."
            ],
            "time_required_min": 5,
            "materials_needed": [],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Teaching others or summarizing reinforces understanding.",
            "cognitive_target": "recall and synthesis"
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
            "student_state": "FORGETFUL"
        },
        "tags": ["summary", "reflection", "ownership"]
    },
    {
        "solution_id": "interactive_quiz_bellwork",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["TRANSITION_DELAY", "SLOW_START"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "RECALL",
        "learning_mode": "GAME",
        "preview": {
            "title": "Bellwork Quiz Warm-Up",
            "action_text": "Use a short quiz as a quick start to class."
        },
        "details": {
            "objective": "Activate prior knowledge and start class with energy.",
            "steps": [
                "Prepare 3–5 recall questions from previous lesson.",
                "Write them on board before students arrive.",
                "As students settle, they begin writing answers.",
                "Review answers as class warm-up discussion.",
                "Rotate quiz leader responsibility weekly."
            ],
            "time_required_min": 7,
            "materials_needed": ["blackboard"],
            "teacher_tone": "energetic"
        },
        "pedagogy": {
            "why_it_works": "Predictable structure activates prior learning quickly.",
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
            "class_strength": "medium",
            "student_state": "SLOW_STARTERS"
        },
        "tags": ["bellwork", "quiz", "recall"]
    },
    {
        "solution_id": "chalk_talk_visual_participation",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["DOMINATING_VOICES", "RELUCTANT_SPEAKERS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "EXPRESSION",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Chalk Talk",
            "action_text": "Silent written discussion on the board or large chart."
        },
        "details": {
            "objective": "Enable equal participation through silent expression.",
            "steps": [
                "Pose a central question or prompt.",
                "Place chart paper on wall or use board.",
                "Students write their responses silently.",
                "Allow students to respond to each other’s comments.",
                "Debrief together after writing phase ends."
            ],
            "time_required_min": 10,
            "materials_needed": ["chart paper", "markers"],
            "teacher_tone": "inclusive"
        },
        "pedagogy": {
            "why_it_works": "Gives space to introverted students and ensures equity in voice.",
            "cognitive_target": "expression"
        },
        "constraints": {
            "requires": ["WALL_SPACE"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "MIXED"
        },
        "tags": ["chalk_talk", "participation", "visual"]
    },
    {
        "solution_id": "math_board_game_concepts",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["CONCEPTUAL_GAP", "LOW_PARTICIPATION"],
        "subjects": ["MATH"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "GAME",
        "preview": {
            "title": "Math Concept Board Game",
            "action_text": "Students solve problems in a board game format to master math concepts."
        },
        "details": {
            "objective": "Improve engagement and conceptual clarity through gamification.",
            "steps": [
                "Create a board with numbered steps or zones (like snakes & ladders).",
                "Prepare concept-based questions for each level (fractions, geometry, etc.).",
                "Divide students into teams and take turns rolling dice to advance.",
                "A correct answer allows movement; a wrong one skips the turn.",
                "Declare winner and recap key learning points."
            ],
            "time_required_min": 20,
            "materials_needed": ["game board", "dice", "question cards"],
            "teacher_tone": "cheerful"
        },
        "pedagogy": {
            "why_it_works": "Gamification maintains energy and repetition builds understanding.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": ["CLASS_TIME"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "UNENGAGED"
        },
        "tags": ["math", "games", "engagement"]
    },
    {
        "solution_id": "subject_specific_role_play",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["MONOTONY", "LOW_IMPACT_LESSONS"],
        "subjects": ["SOCIAL_SCIENCE", "SCIENCE", "LANGUAGE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CONTEXTUAL",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Role Play Historical or Scientific Events",
            "action_text": "Students act out key historical or scientific concepts to bring them alive."
        },
        "details": {
            "objective": "Deepen contextual understanding through enactment.",
            "steps": [
                "Select a concept (e.g., life of a freedom fighter, water cycle).",
                "Assign roles to groups with simple props.",
                "Practice scenes and dialogue briefly.",
                "Perform the short play for class.",
                "Discuss learnings and student feelings post-activity."
            ],
            "time_required_min": 25,
            "materials_needed": ["props", "space"],
            "teacher_tone": "enthusiastic"
        },
        "pedagogy": {
            "why_it_works": "Active participation and emotional connection reinforce long-term memory.",
            "cognitive_target": "contextualization"
        },
        "constraints": {
            "requires": ["OPEN_SPACE"],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "MEDIUM",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["role_play", "history", "science", "language"]
    },
    {
        "solution_id": "reading_buddy_system",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["MIXED_READING_LEVELS", "READING_ANXIETY"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "FLUENCY",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Reading Buddy System",
            "action_text": "Pair fluent readers with hesitant ones to read aloud together."
        },
        "details": {
            "objective": "Improve reading fluency through guided peer interaction.",
            "steps": [
                "Identify students who read fluently and those who need support.",
                "Pair them based on comfort and balance.",
                "Assign short storybooks or text passages.",
                "Both students read aloud alternately, with stronger buddy guiding.",
                "Rotate buddies every few weeks."
            ],
            "time_required_min": 10,
            "materials_needed": ["storybooks"],
            "teacher_tone": "gentle"
        },
        "pedagogy": {
            "why_it_works": "Peer modeling reduces anxiety and reinforces learning.",
            "cognitive_target": "fluency"
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
            "student_state": "ANXIOUS"
        },
        "tags": ["reading", "language", "peer_support"]
    },
    {
        "solution_id": "anchor_word_wall",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["VOCABULARY_LAG", "WEAK_LANGUAGE_SKILLS"],
        "subjects": ["LANGUAGE", "SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "VOCABULARY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Create a Word Wall",
            "action_text": "Display key vocabulary words related to current topics on the wall."
        },
        "details": {
            "objective": "Reinforce vocabulary through visual display and review.",
            "steps": [
                "Pick 4–5 key words from the weekly lesson.",
                "Write each word on a colorful card with definition and visual.",
                "Stick them on the classroom wall in a designated area.",
                "Refer to these during class; conduct quick reviews often.",
                "Replace or rotate words weekly."
            ],
            "time_required_min": 8,
            "materials_needed": ["cards", "stickers", "wall space"],
            "teacher_tone": "reinforcing"
        },
        "pedagogy": {
            "why_it_works": "Repeated visual exposure builds language familiarity.",
            "cognitive_target": "retention"
        },
        "constraints": {
            "requires": ["WALL_SPACE"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "BEGINNER"
        },
        "tags": ["word_wall", "vocabulary", "language"]
    },
    {
        "solution_id": "home_connect_parent_project",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["HOME_SUPPORT_LACK", "PARENT_ENGAGEMENT_GAP"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "COMMUNITY",
        "learning_mode": "INTEGRATED",
        "preview": {
            "title": "Home Connection Project",
            "action_text": "Assign a mini project that involves family input or interaction."
        },
        "details": {
            "objective": "Strengthen home-school connection via collaborative activity.",
            "steps": [
                "Design a task like ‘Interview a family elder’ or ‘Draw your neighborhood’.",
                "Explain to students what kind of help they may seek from home.",
                "Give a week for completion with flexible formats (drawing, writing, photo).",
                "Display outcomes in class or present in small groups.",
                "Send a thank-you note or message to guardians."
            ],
            "time_required_min": 0,
            "materials_needed": ["assignment sheet"],
            "teacher_tone": "inclusive"
        },
        "pedagogy": {
            "why_it_works": "Involving family increases relevance and emotional value.",
            "cognitive_target": "personalization"
        },
        "constraints": {
            "requires": ["PARENT_SUPPORT"],
            "avoid_if": ["LACK_OF_HOME_ACCESS"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISCONNECTED"
        },
        "tags": ["home", "project", "parent_involvement"]
    },
    {
        "solution_id": "gallery_walk_reflection",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LOW_ENGAGEMENT", "SHALLOW_REFLECTION"],
        "subjects": ["GENERAL"],
        "class_range": "SECONDARY",
        "topic_type": "REFLECTION",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Gallery Walk",
            "action_text": "Students walk around to observe and reflect on each other's work."
        },
        "details": {
            "objective": "Promote reflection and peer appreciation through shared displays.",
            "steps": [
                "Ask students to prepare visual posters or charts on a topic.",
                "Arrange the posters around the classroom.",
                "Divide class into groups to walk around silently and take notes.",
                "After the walk, lead a discussion or ask for feedback forms.",
                "Optionally include peer voting or appreciation badges."
            ],
            "time_required_min": 15,
            "materials_needed": ["poster materials", "display space"],
            "teacher_tone": "reflective"
        },
        "pedagogy": {
            "why_it_works": "Movement and visual interaction deepen attention and recall.",
            "cognitive_target": "meta-cognition"
        },
        "constraints": {
            "requires": ["WALL_SPACE"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "OBSERVATIONAL"
        },
        "tags": ["reflection", "gallery", "peer_feedback"]
    },
    {
        "solution_id": "concept_cartoon_debate",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["MISCONCEPTION_PERSISTENCE"],
        "subjects": ["SCIENCE", "SOCIAL_SCIENCE"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "DISCUSSION",
        "preview": {
            "title": "Concept Cartoon Debate",
            "action_text": "Use cartoon illustrations to stimulate conceptual discussion and correction."
        },
        "details": {
            "objective": "Correct common misconceptions through guided discussion.",
            "steps": [
                "Show a cartoon with characters expressing different views on a concept.",
                "Ask students to vote on who they agree with and why.",
                "Facilitate a debate and slowly guide toward the correct understanding.",
                "Reveal scientific or factual explanation at the end.",
                "Encourage students to make their own cartoon based on the topic."
            ],
            "time_required_min": 15,
            "materials_needed": ["printed cartoons", "board"],
            "teacher_tone": "provocative"
        },
        "pedagogy": {
            "why_it_works": "Visual-provocative setup uncovers beliefs and allows clarification.",
            "cognitive_target": "misconception correction"
        },
        "constraints": {
            "requires": ["PRIOR_CONTENT_KNOWLEDGE"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["cartoon", "debate", "conceptual"]
    },
    {
        "solution_id": "mind_map_consolidation",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TOPIC_COMPLEXITY", "LOW_SYNTHESIS"],
        "subjects": ["SCIENCE", "SOCIAL_SCIENCE", "GENERAL"],
        "class_range": "SECONDARY",
        "topic_type": "SYNTHESIS",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Mind Mapping Activity",
            "action_text": "Create a collective mind map on the board to consolidate learning."
        },
        "details": {
            "objective": "Help students link subtopics and retain complex structures.",
            "steps": [
                "Draw the central concept on the board.",
                "Ask students to contribute branches representing sub-concepts.",
                "Use arrows and colors to show relationships.",
                "Refine and clean up the map together.",
                "Encourage copying it into notebooks or extending it at home."
            ],
            "time_required_min": 12,
            "materials_needed": ["board", "markers"],
            "teacher_tone": "collaborative"
        },
        "pedagogy": {
            "why_it_works": "Visual hierarchy aids long-term retention and comprehension.",
            "cognitive_target": "integration"
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
            "student_state": "OVERWHELMED"
        },
        "tags": ["mind_map", "synthesis", "visual"]
    },
    {
        "solution_id": "concept_matching_cards",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONCEPTUAL_GAP", "STUDENT_DISENGAGEMENT"],
        "subjects": ["SCIENCE", "MATH", "GENERAL"],
        "class_range": "UPPER_PRIMARY",
        "topic_type": "RECALL",
        "learning_mode": "GAME",
        "preview": {
            "title": "Concept Matching Cards",
            "action_text": "Match terms with definitions or concepts with images in a card game."
        },
        "details": {
            "objective": "Boost concept recall using a fast-paced matching activity.",
            "steps": [
                "Prepare sets of cards: one side with terms, the other with matching definitions or pictures.",
                "Shuffle and distribute evenly among groups.",
                "Time-bound challenge to match correctly in groups.",
                "Review each pair aloud and clarify doubts.",
                "Use for weekly revision sessions."
            ],
            "time_required_min": 10,
            "materials_needed": ["cards"],
            "teacher_tone": "lively"
        },
        "pedagogy": {
            "why_it_works": "Engages through movement and visual association.",
            "cognitive_target": "retrieval"
        },
        "constraints": {
            "requires": ["PREPARATION"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "BORED"
        },
        "tags": ["matching", "cards", "revision"]
    },
    {
        "solution_id": "picture_prompt_writing_spark",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["WRITING_BLOCK", "CREATIVITY_LAG"],
        "subjects": ["LANGUAGE"],
        "class_range": "MIDDLE",
        "topic_type": "EXPRESSION",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Picture Prompt Writing",
            "action_text": "Display an image and ask students to write a story or dialogue inspired by it."
        },
        "details": {
            "objective": "Stimulate creative writing using visual cues.",
            "steps": [
                "Show an interesting or ambiguous image on the board.",
                "Ask students to write a short story, conversation, or poem inspired by the image.",
                "Give 10 minutes of silent writing.",
                "Invite 2–3 students to read aloud.",
                "Optionally display writings on a board or wall."
            ],
            "time_required_min": 15,
            "materials_needed": ["images", "writing paper"],
            "teacher_tone": "open"
        },
        "pedagogy": {
            "why_it_works": "Visuals bypass writer’s block and provide rich stimulus.",
            "cognitive_target": "creativity"
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
            "student_state": "CREATIVELY_STUCK"
        },
        "tags": ["writing", "creativity", "language"]
    },
    {
        "solution_id": "timeline_activity_history_upper",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["SEQUENTIAL_CONFUSION", "LOW_ENGAGEMENT"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Timeline Creation for Historical Events",
            "action_text": "Students create a timeline to sequence key events and visualize cause-effect."
        },
        "details": {
            "objective": "Enhance chronological understanding and retention of history events.",
            "steps": [
                "Introduce the key events from the topic (e.g., Indian Independence Movement).",
                "Provide students with event cards or dates and brief descriptions.",
                "Ask students to arrange them in a timeline format (wall/poster or floor layout).",
                "Facilitate a discussion on causes, consequences, and patterns.",
                "Let students explain one segment of the timeline to the class."
            ],
            "time_required_min": 20,
            "materials_needed": ["chart paper", "event cards", "markers"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Visual sequencing aids memory and clarifies complex relationships.",
            "cognitive_target": "organization"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["history", "visual", "timeline"]
    },
    {
        "solution_id": "concept_corners_movement_check",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONCEPTUAL_MISUNDERSTANDING"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Concept Corners",
            "action_text": "Use room corners to represent answer choices; students move to express their understanding."
        },
        "details": {
            "objective": "Check conceptual understanding through physical movement.",
            "steps": [
                "Label 4 corners of the room with possible answer choices (A, B, C, D).",
                "Ask a conceptual question with 4 possible answers.",
                "Students walk to the corner they believe is correct.",
                "Discuss each option and clarify misconceptions.",
                "Let students self-correct if they wish to change their answer."
            ],
            "time_required_min": 10,
            "materials_needed": ["chart papers", "tape"],
            "teacher_tone": "interactive"
        },
        "pedagogy": {
            "why_it_works": "Movement activates engagement and exposes hidden misconceptions.",
            "cognitive_target": "clarification"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["PHYSICAL_LIMITATIONS"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "LOW_RESPONSIVENESS"
        },
        "tags": ["formative", "movement", "science"]
    },
    {
        "solution_id": "anchor_chart_recall_language",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["FORGETFULNESS", "LACK_OF_REFERENCE"],
        "subjects": ["LANGUAGE"],
        "class_range": "MIDDLE",
        "topic_type": "SKILL_BASED",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Anchor Chart for Writing Structures",
            "action_text": "Display key structures of writing (e.g., opening, body, conclusion) on a chart."
        },
        "details": {
            "objective": "Support student writing through consistent visible reference.",
            "steps": [
                "Prepare an anchor chart showing structure of a paragraph or essay.",
                "Include sentence starters or linking phrases.",
                "Display prominently in the classroom.",
                "Before writing tasks, ask students to refer to the chart.",
                "Update or expand chart with student contributions over time."
            ],
            "time_required_min": 5,
            "materials_needed": ["chart paper", "markers"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Visual scaffolds improve independence and retention in writing.",
            "cognitive_target": "reinforcement"
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
            "student_state": "FORGETFUL"
        },
        "tags": ["language", "writing", "anchor_chart"]
    },
    {
        "solution_id": "silent_observation_diary_science",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_PARTICIPATION", "DISTRACTION"],
        "subjects": ["SCIENCE"],
        "class_range": "PRIMARY",
        "topic_type": "OBSERVATIONAL",
        "learning_mode": "INTRAPERSONAL",
        "preview": {
            "title": "Silent Observation Diary",
            "action_text": "Give students a leaf or object to observe silently and write/draw their notes."
        },
        "details": {
            "objective": "Build observational skills and independent inquiry.",
            "steps": [
                "Distribute a natural object (leaf, rock, feather) to each student.",
                "Give a sheet or notebook and ask them to silently observe and record details.",
                "Encourage drawings, labels, or patterns.",
                "After 10 mins, discuss their observations together.",
                "Highlight different types of noticing: shape, color, texture, etc."
            ],
            "time_required_min": 15,
            "materials_needed": ["objects", "paper", "pencils"],
            "teacher_tone": "calm"
        },
        "pedagogy": {
            "why_it_works": "Silence deepens focus; drawing and writing build memory and inquiry habits.",
            "cognitive_target": "attention"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "DISTRACTED"
        },
        "tags": ["observation", "science", "silent"]
    },
    {
        "solution_id": "exit_ticket_wrap_up_any",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LESSON_WRAP_UP", "UNCHECKED_UNDERSTANDING"],
        "subjects": ["GENERAL"],
        "class_range": "ANY",
        "topic_type": "REVIEW",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Exit Ticket Wrap-up",
            "action_text": "Ask students to write one thing they learned and one question before leaving."
        },
        "details": {
            "objective": "Assess lesson comprehension in a quick, low-pressure format.",
            "steps": [
                "At the end of the class, distribute a slip or use notebooks.",
                "Ask students to write one new thing they understood and one lingering question.",
                "Collect responses anonymously.",
                "Scan responses to inform next lesson plan or clarification.",
                "Use 1–2 samples to start the next class."
            ],
            "time_required_min": 5,
            "materials_needed": ["paper slips", "pen"],
            "teacher_tone": "open"
        },
        "pedagogy": {
            "why_it_works": "Quick self-assessment promotes metacognition and supports feedback loop.",
            "cognitive_target": "reflection"
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
            "student_state": "NEEDS_CLOSURE"
        },
        "tags": ["exit_ticket", "reflection", "review"]
    },
    {
        "solution_id": "roleplay_historical_figures",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["LOW_ENGAGEMENT", "PASSIVE_LEARNING"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "INTERPERSONAL",
        "preview": {
            "title": "Roleplay Historical Figures",
            "action_text": "Students take on roles of historical figures and act out debates or decisions."
        },
        "details": {
            "objective": "Make history interactive and empathetic through dramatization.",
            "steps": [
                "Assign students key historical figures relevant to the topic (e.g., Gandhi, Nehru, Jinnah).",
                "Give them a day to prepare a 2-minute introduction as that figure.",
                "Facilitate a mock debate or town hall meeting with pre-set topics.",
                "Encourage questions from classmates.",
                "Conclude with a reflection on how decisions impacted society."
            ],
            "time_required_min": 20,
            "materials_needed": ["name tags", "reference notes"],
            "teacher_tone": "dramatic"
        },
        "pedagogy": {
            "why_it_works": "Enacting roles deepens emotional connection and understanding of historical context.",
            "cognitive_target": "empathy"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["SEVERE_TIME_CONSTRAINT"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "INATTENTIVE"
        },
        "tags": ["history", "roleplay", "engagement"]
    },
    {
        "solution_id": "visual_mind_map_science_topic",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["TOPIC_CONFUSION", "EXCESSIVE_CONTENT"],
        "subjects": ["SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "THEMATIC",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Mind Map for Concept Integration",
            "action_text": "Guide students to build a topic-wide mind map linking subtopics."
        },
        "details": {
            "objective": "Help students see topic interrelations through visual diagrams.",
            "steps": [
                "Write the central topic on the board (e.g., Nutrition).",
                "Ask students to suggest subtopics and draw branches.",
                "Expand with examples, terms, and processes.",
                "Color-code related branches (e.g., types of nutrients, deficiency diseases).",
                "Encourage students to recreate and personalize in notebooks."
            ],
            "time_required_min": 15,
            "materials_needed": ["blackboard", "chalks", "notebooks"],
            "teacher_tone": "guiding"
        },
        "pedagogy": {
            "why_it_works": "Visual mapping helps integrate and retain large chunks of content.",
            "cognitive_target": "synthesis"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "CONFUSED"
        },
        "tags": ["mind_map", "science", "visual"]
    },
    {
        "solution_id": "peer_feedback_checklist_language",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["NO_FEEDBACK", "WRITING_QUALITY_ISSUE"],
        "subjects": ["LANGUAGE"],
        "class_range": "SECONDARY",
        "topic_type": "SKILL_BASED",
        "learning_mode": "INTERPERSONAL",
        "preview": {
            "title": "Peer Feedback with Checklist",
            "action_text": "Use a checklist to guide peer-to-peer review in writing assignments."
        },
        "details": {
            "objective": "Promote critical evaluation and revision in student writing.",
            "steps": [
                "Create a feedback checklist with items like 'clear opening', 'supporting details', 'grammar', etc.",
                "Distribute copies to all students.",
                "Have each student exchange notebooks with a peer.",
                "Peers review writing using the checklist and provide notes.",
                "Writers reflect and revise accordingly."
            ],
            "time_required_min": 15,
            "materials_needed": ["feedback checklists", "notebooks"],
            "teacher_tone": "constructive"
        },
        "pedagogy": {
            "why_it_works": "Structured peer review enhances ownership and learning through social comparison.",
            "cognitive_target": "evaluation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["peer_review", "language", "writing"]
    },
    {
        "solution_id": "collaborative_poster_topic_summary",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["TOPIC_CONSOLIDATION", "END_OF_UNIT"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "REVIEW",
        "learning_mode": "INTERPERSONAL",
        "preview": {
            "title": "Group Poster Summary",
            "action_text": "Groups create a poster summarizing key learnings of the unit."
        },
        "details": {
            "objective": "Support group synthesis and topic revision collaboratively.",
            "steps": [
                "Divide the class into small groups.",
                "Assign each group a sub-topic or theme from the unit.",
                "Provide chart paper and markers.",
                "Ask them to create a poster with visuals, facts, definitions, etc.",
                "Conduct a poster walk or gallery presentation with peer questions."
            ],
            "time_required_min": 25,
            "materials_needed": ["chart papers", "markers", "tape"],
            "teacher_tone": "facilitator"
        },
        "pedagogy": {
            "why_it_works": "Collaborative creation supports summarization and peer teaching.",
            "cognitive_target": "recall + synthesis"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "NEEDS_REVISION"
        },
        "tags": ["poster", "revision", "groupwork"]
    },
    {
        "solution_id": "theme_box_stimulus_story",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["IDEA_GENERATION_ISSUE", "MONOTONY"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "EXPRESSION",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Theme Box for Story Building",
            "action_text": "Use a mystery box of themed objects to spark student storytelling."
        },
        "details": {
            "objective": "Stimulate imaginative storytelling using physical prompts.",
            "steps": [
                "Prepare a box with 5–6 objects related to a theme (e.g., jungle: leaf, toy animal, binoculars).",
                "Let each student pick one object without looking.",
                "Ask them to create a story using their object as the main character or clue.",
                "Share stories orally or draw/write them depending on level.",
                "Rotate box themes weekly to keep it fresh."
            ],
            "time_required_min": 15,
            "materials_needed": ["box", "themed objects", "notebooks"],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Tactile prompts ground imagination in tangible cues, ideal for young learners.",
            "cognitive_target": "imagination"
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
            "student_state": "BORED"
        },
        "tags": ["storytelling", "language", "primary"]
    },
    {
        "solution_id": "concept_basket_ball_review",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["END_OF_TOPIC", "LOW_ATTENTION"],
        "subjects": ["SCIENCE", "MATH", "SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "REVIEW",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Basketball Concept Quiz",
            "action_text": "Students toss a ball into a box to answer review questions."
        },
        "details": {
            "objective": "Make revision fun and active with a kinesthetic quiz.",
            "steps": [
                "Prepare 10–15 concept check questions from the topic.",
                "Place a basket or box at the front of the class.",
                "Divide students into 2–3 teams.",
                "Ask a question; if answered correctly, student takes a shot.",
                "Award points for both answer and shot accuracy."
            ],
            "time_required_min": 20,
            "materials_needed": ["soft ball", "basket/box"],
            "teacher_tone": "energetic"
        },
        "pedagogy": {
            "why_it_works": "Engages students physically while reinforcing key concepts.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["SPACE_LIMITATION"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISTRACTED"
        },
        "tags": ["quiz", "movement", "recap"]
    },
    {
        "solution_id": "exit_ticket_emotion_check",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["STUDENT_ANXIETY", "UNEXPRESSED_DOUBTS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "REFLECTIVE",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Exit Ticket with Emotions",
            "action_text": "Before leaving, students write what they learned and how they felt."
        },
        "details": {
            "objective": "Gauge student understanding and emotional state after lessons.",
            "steps": [
                "Give each student a slip with two prompts: 'I learned...', 'I felt...'.",
                "Students fill it silently before exiting.",
                "Review responses post-class to identify confusions and concerns.",
                "Follow up next day on common patterns.",
                "Use the feedback to adjust pace or method."
            ],
            "time_required_min": 5,
            "materials_needed": ["exit slips", "pen/pencil"],
            "teacher_tone": "empathetic"
        },
        "pedagogy": {
            "why_it_works": "Combines metacognition with emotional expression, deepening learning bonds.",
            "cognitive_target": "self-awareness"
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
            "student_state": "QUIETLY_STRESSED"
        },
        "tags": ["exit_ticket", "reflection", "wellbeing"]
    },
    {
        "solution_id": "math_quiz_pass_the_chalk",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["FAST_FINISHERS", "BOREDOM"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "PRACTICE",
        "learning_mode": "COMPETITIVE",
        "preview": {
            "title": "Pass-the-Chalk Quiz",
            "action_text": "Students race to answer a chain of math questions on the board."
        },
        "details": {
            "objective": "Practice speed and accuracy in calculations.",
            "steps": [
                "Line students in two teams in front of the board.",
                "One by one, they write the answer to a math problem and pass the chalk.",
                "The team that finishes all problems first wins.",
                "Rotate teams every few rounds.",
                "Emphasize correct solutions over speed."
            ],
            "time_required_min": 10,
            "materials_needed": ["board", "chalk", "timer"],
            "teacher_tone": "lively"
        },
        "pedagogy": {
            "why_it_works": "Turns drill into a fun and energetic group competition.",
            "cognitive_target": "fluency"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["OVER_CROWDING"]
        },
        "effort_level": "LOW",
        "classroom_safety": "MEDIUM",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "ENERGETIC"
        },
        "tags": ["math", "quiz", "movement"]
    },
    {
        "solution_id": "science_art_concept_poster",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["TOPIC_MISUNDERSTANDING", "DULL_LECTURE_STYLE"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Concept Poster Making",
            "action_text": "Students create an artistic poster of the concept learned."
        },
        "details": {
            "objective": "Encourage concept consolidation using visual representation.",
            "steps": [
                "Assign students a concept from the chapter (e.g., evaporation).",
                "Ask them to represent it visually using drawings, symbols, and keywords.",
                "Display posters in class for peer review.",
                "Allow brief presentations to explain poster choices.",
                "Offer feedback on clarity and creativity."
            ],
            "time_required_min": 20,
            "materials_needed": ["chart paper", "color pencils", "markers"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Fosters creativity while reinforcing core scientific principles.",
            "cognitive_target": "representation"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNENGAGED"
        },
        "tags": ["poster", "science", "creative"]
    },
    {
        "solution_id": "timeline_activity_history_topic",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["TOPIC_SEQUENCE_ISSUE", "CONFUSION_IN_DATES"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "THEMATIC",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Create a Visual Timeline",
            "action_text": "Students plot key events from the topic on a class-wide timeline."
        },
        "details": {
            "objective": "Help students understand chronological flow and cause-effect.",
            "steps": [
                "Assign students 2–3 key events from a topic.",
                "Provide them chart strips to note event title and year.",
                "Students paste their strips in correct order on a class wall.",
                "Review the timeline together and ask questions.",
                "Optionally connect events using colored threads or arrows."
            ],
            "time_required_min": 15,
            "materials_needed": ["chart strips", "adhesive", "markers"],
            "teacher_tone": "inquisitive"
        },
        "pedagogy": {
            "why_it_works": "Chronological visualization aids better recall and understanding of historical flow.",
            "cognitive_target": "sequencing"
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
            "student_state": "LOST_IN_SEQUENCE"
        },
        "tags": ["timeline", "history", "visual"]
    },
    {
        "solution_id": "language_class_hot_seat_game",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["VOCABULARY_GAP", "MONOTONY"],
        "subjects": ["LANGUAGE"],
        "class_range": "UPPER",
        "topic_type": "VOCABULARY",
        "learning_mode": "ORAL",
        "preview": {
            "title": "Hot Seat Vocabulary Game",
            "action_text": "Guess the word from classmates’ clues while sitting in the 'hot seat'."
        },
        "details": {
            "objective": "Reinforce vocabulary through peer interaction.",
            "steps": [
                "Write 10 vocabulary words on slips (1 word per slip).",
                "One student sits facing the class with back to the board.",
                "Write one word on the board.",
                "Class gives clues (not the word) to help the student guess.",
                "Time each turn and rotate students in the hot seat."
            ],
            "time_required_min": 10,
            "materials_needed": ["word slips", "board"],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Encourages active recall and builds communication confidence.",
            "cognitive_target": "retrieval"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "LOW",
        "classroom_safety": "MEDIUM",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "BORED"
        },
        "tags": ["vocabulary", "game", "language"]
    },
    {
        "solution_id": "science_flashcard_chain_game",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_RETENTION", "TOPIC_REVISION"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "RECALL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Flashcard Chain Game",
            "action_text": "Students pass flashcards and answer rapidly in a chain to reinforce learning."
        },
        "details": {
            "objective": "Boost memory and participation through fast-paced Q&A.",
            "steps": [
                "Prepare flashcards with one question per card.",
                "Divide class into 3–4 groups.",
                "First student answers and passes the card to the next.",
                "Each group forms a chain; monitor accuracy and pace.",
                "Encourage peer correction and cheerleading."
            ],
            "time_required_min": 12,
            "materials_needed": ["question flashcards"],
            "teacher_tone": "motivating"
        },
        "pedagogy": {
            "why_it_works": "Repetition builds recall, group structure boosts involvement.",
            "cognitive_target": "reinforcement"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "FORGETFUL"
        },
        "tags": ["flashcards", "review", "science"]
    },
    {
        "solution_id": "environmental_skit_presentation",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["AWARENESS_NEEDED", "PASSIVE_LEARNING"],
        "subjects": ["SCIENCE", "SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "THEMATIC",
        "learning_mode": "PERFORMATIVE",
        "preview": {
            "title": "Skit on Environmental Issues",
            "action_text": "Groups perform short skits highlighting environmental challenges."
        },
        "details": {
            "objective": "Promote social awareness and team collaboration.",
            "steps": [
                "Assign themes like water pollution, plastic use, etc.",
                "Groups write and rehearse 3–5 minute skits.",
                "Perform in class or for other sections.",
                "Encourage costumes or props from recycled items.",
                "Facilitate reflection: 'What message did the skit give you?'"
            ],
            "time_required_min": 30,
            "materials_needed": ["props (optional)", "space to perform"],
            "teacher_tone": "inspirational"
        },
        "pedagogy": {
            "why_it_works": "Combines empathy, creativity, and collaborative execution.",
            "cognitive_target": "social consciousness"
        },
        "constraints": {
            "requires": ["TIME", "GROUP_PREPARATION"],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["skit", "environment", "performance"]
    },
    {
        "solution_id": "gallery_walk_topic_connections",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["TOPIC_OVERLOAD", "DIVERSE_IDEAS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "REVIEW",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Gallery Walk for Connections",
            "action_text": "Students walk around reviewing peers’ posters and leaving comments."
        },
        "details": {
            "objective": "Allow peer learning and idea exposure across the class.",
            "steps": [
                "Each group creates a visual summary of a sub-topic on chart paper.",
                "Stick posters on the wall across the room.",
                "Give sticky notes to each student to comment/ask on 2 posters.",
                "Rotate in silence to maintain focus.",
                "Review collected questions/comments as a whole class."
            ],
            "time_required_min": 20,
            "materials_needed": ["chart paper", "sticky notes"],
            "teacher_tone": "facilitative"
        },
        "pedagogy": {
            "why_it_works": "Encourages movement, curiosity, and peer teaching.",
            "cognitive_target": "connection-making"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "MENTALLY_TIRED"
        },
        "tags": ["gallery_walk", "peer_learning", "review"]
    },
    {
        "solution_id": "student_generated_quiz",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_ENGAGEMENT", "TOPIC_REVISION"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "RECALL",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Student-Generated Quiz",
            "action_text": "Let students create quiz questions for peers based on the topic."
        },
        "details": {
            "objective": "Reinforce learning through peer-generated questions.",
            "steps": [
                "Ask students to write 3–5 MCQs or short questions on a completed topic.",
                "Collect and curate a mix of strong questions.",
                "Distribute quizzes across groups and allow peer-solving.",
                "Review responses together and highlight tricky questions.",
                "Offer feedback on question clarity and logic."
            ],
            "time_required_min": 20,
            "materials_needed": ["paper", "pen"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Creating questions forces deeper processing of content.",
            "cognitive_target": "recall and analysis"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "PASSIVE"
        },
        "tags": ["assessment", "recall", "peer_learning"]
    },
    {
        "solution_id": "parent_feedback_wall",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LACK_OF_HOME_SUPPORT"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "SCHOOL_HOME_LINK",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Parent Feedback Wall",
            "action_text": "Collect short comments from parents about their child’s learning and display them."
        },
        "details": {
            "objective": "Strengthen parent-school communication and student motivation.",
            "steps": [
                "Send home a small form asking parents to write one line of feedback about class/home learning.",
                "Collect responses over a week.",
                "Select positive or helpful messages to display on a classroom board.",
                "Read a few aloud every Friday.",
                "Discuss improvements or appreciations."
            ],
            "time_required_min": 10,
            "materials_needed": ["paper slips", "board"],
            "teacher_tone": "respectful"
        },
        "pedagogy": {
            "why_it_works": "Brings in parental voice and increases learner accountability.",
            "cognitive_target": "social validation"
        },
        "constraints": {
            "requires": ["PARENT_COMMUNICATION_CHANNEL"],
            "avoid_if": ["NO_PARENTAL_ACCESS"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "NEEDS_MOTIVATION"
        },
        "tags": ["parental_involvement", "motivation"]
    },
    {
        "solution_id": "community_resource_showcase",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["RELEVANCE_GAP"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "CIVIC",
        "learning_mode": "DISCUSSION",
        "preview": {
            "title": "Community Resource Showcase",
            "action_text": "Students bring stories or photos of local services (post office, clinics, etc.) to class."
        },
        "details": {
            "objective": "Link textbook topics to real community examples.",
            "steps": [
                "Assign students to identify a local resource (school, shop, post office).",
                "Ask them to interview someone or observe how it works.",
                "Bring back one picture, sketch, or short story.",
                "Each student shares their input in 1–2 minutes.",
                "Tie discussion to textbook chapters (e.g., community roles)."
            ],
            "time_required_min": 20,
            "materials_needed": ["pictures or student notes"],
            "teacher_tone": "curious"
        },
        "pedagogy": {
            "why_it_works": "Relates concepts to familiar settings, making learning contextual.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "DISCONNECTED"
        },
        "tags": ["community", "local_knowledge", "civic_learning"]
    },
    {
        "solution_id": "multi_grade_peer_rotation",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["MIXED_CLASSROOM", "LOW_PARTICIPATION"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "MANAGEMENT",
        "learning_mode": "GROUP",
        "preview": {
            "title": "Peer Rotation in Multi-grade Setup",
            "action_text": "Older students rotate helping younger ones during activity time."
        },
        "details": {
            "objective": "Foster mutual learning and manage workload in multi-grade classrooms.",
            "steps": [
                "Group students by age or level.",
                "Assign 1–2 older students to each group of younger peers.",
                "Design a common activity (drawing, simple quiz, sorting) that older students can explain.",
                "Allow 15–20 minutes for peer facilitation.",
                "Appreciate and rotate roles weekly."
            ],
            "time_required_min": 20,
            "materials_needed": ["simple activity materials"],
            "teacher_tone": "trusting"
        },
        "pedagogy": {
            "why_it_works": "Distributes responsibility and allows for peer modeling.",
            "cognitive_target": "collaborative understanding"
        },
        "constraints": {
            "requires": ["VARIED_CLASS_LEVELS"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "MIXED"
        },
        "tags": ["multi_grade", "peer_learning", "group_work"]
    },
    {
        "solution_id": "student_reflection_cards",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_SELF_AWARENESS", "BEHAVIORAL_ISSUES"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "REFLECTIVE",
        "learning_mode": "WRITTEN",
        "preview": {
            "title": "Reflection Cards After Class",
            "action_text": "Give students a short card to reflect on how they participated and felt."
        },
        "details": {
            "objective": "Encourage self-awareness and constructive self-checking.",
            "steps": [
                "Distribute cards with 2–3 prompts: What did I learn? What did I enjoy? What could I do better?",
                "Give 5 minutes after lesson.",
                "Collect anonymously (or not, based on intent).",
                "Read select reflections to address trends next day.",
                "Repeat weekly as a routine."
            ],
            "time_required_min": 7,
            "materials_needed": ["reflection slips or paper"],
            "teacher_tone": "non-judgmental"
        },
        "pedagogy": {
            "why_it_works": "Metacognition helps students monitor and improve learning behavior.",
            "cognitive_target": "self-regulation"
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
            "student_state": "RESTLESS"
        },
        "tags": ["reflection", "behavior", "metacognition"]
    },
    {
        "solution_id": "concept_mapping_self_check",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["REVISION", "LOW_CONFIDENCE"],
        "subjects": ["SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Concept Mapping as Self-Check",
            "action_text": "Ask students to draw concept maps from memory to self-check understanding."
        },
        "details": {
            "objective": "Enable learners to visually structure and revise their understanding.",
            "steps": [
                "Provide a blank chart or ask students to create one on paper.",
                "Give 10–15 minutes to independently map out key terms and connections from the topic.",
                "Ask students to exchange maps and add 2–3 missing links.",
                "Display a teacher map for comparison.",
                "Clarify key errors together."
            ],
            "time_required_min": 15,
            "materials_needed": ["paper", "pencil"],
            "teacher_tone": "supportive"
        },
        "pedagogy": {
            "why_it_works": "Visual recall aids memory and reinforces relationships between concepts.",
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
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["concept_map", "visual_learning", "science"]
    },
    {
        "solution_id": "poster_competition_value_education",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["BEHAVIORAL_ISSUES", "LOW_VALUE_SENSITIVITY"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "VALUES",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Value Education Poster Competition",
            "action_text": "Conduct a group poster-making activity on themes like honesty or kindness."
        },
        "details": {
            "objective": "Promote ethical thinking and teamwork through visual representation.",
            "steps": [
                "Divide class into small groups and assign each a value (honesty, cooperation, etc.).",
                "Give 30 minutes to discuss and make a poster that conveys this value.",
                "Display all posters around the class.",
                "Let each group explain their poster in 1–2 minutes.",
                "Reward effort and originality."
            ],
            "time_required_min": 35,
            "materials_needed": ["chart paper", "colors", "markers"],
            "teacher_tone": "uplifting"
        },
        "pedagogy": {
            "why_it_works": "Values become concrete when visualized and discussed collaboratively.",
            "cognitive_target": "moral reasoning"
        },
        "constraints": {
            "requires": ["BASIC_ART_MATERIALS"],
            "avoid_if": []
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISCONNECTED"
        },
        "tags": ["values", "visual_learning", "group_work"]
    },
    {
        "solution_id": "question_sort_diagnosis",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["CONCEPTUAL_CONFUSION"],
        "subjects": ["MATH"],
        "class_range": "MIDDLE",
        "topic_type": "DIAGNOSTIC",
        "learning_mode": "SORTING",
        "preview": {
            "title": "Question Sort for Diagnosis",
            "action_text": "Ask students to sort sample problems into 'clear', 'doubtful', and 'confusing'."
        },
        "details": {
            "objective": "Help teacher identify areas of confusion via student self-tagging.",
            "steps": [
                "Give students a set of 6–8 small problems on a topic.",
                "Ask them to attempt and sort them into 3 piles: clear, doubtful, confusing.",
                "Let them explain 1 example from the confusing pile.",
                "Use results to group and re-teach accordingly.",
                "Repeat next day with new topic."
            ],
            "time_required_min": 20,
            "materials_needed": ["question cards", "pouches/envelopes"],
            "teacher_tone": "non-judgmental"
        },
        "pedagogy": {
            "why_it_works": "Sorting builds metacognition and enables targeted reteaching.",
            "cognitive_target": "diagnosis"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "CONFUSED"
        },
        "tags": ["diagnostic", "sorting", "math"]
    },
    {
        "solution_id": "case_based_discussion_history",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ENGAGEMENT", "MEMORIZATION_HEAVY_TOPIC"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "DISCUSSION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Case-Based Historical Discussions",
            "action_text": "Give a short case/scenario from a historical period and initiate debate."
        },
        "details": {
            "objective": "Develop reasoning and empathy with historical perspectives.",
            "steps": [
                "Provide a fictional or real scenario based in a historical context.",
                "Divide students into 2–3 roles/groups (e.g., traders, kings, farmers).",
                "Pose a dilemma or decision-making moment.",
                "Let each group argue from their viewpoint.",
                "Conclude with reflection on actual history vs. imagined responses."
            ],
            "time_required_min": 30,
            "materials_needed": ["case prompt"],
            "teacher_tone": "provocative"
        },
        "pedagogy": {
            "why_it_works": "Discussion makes static content dynamic and promotes perspective-taking.",
            "cognitive_target": "critical thinking"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["TIME_PRESSURE"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "PASSIVE"
        },
        "tags": ["history", "debate", "case_method"]
    },
    {
        "solution_id": "keyword_bingo_concepts",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["REVISION", "LOW_PARTICIPATION"],
        "subjects": ["LANGUAGE", "SCIENCE"],
        "class_range": "PRIMARY",
        "topic_type": "RECALL",
        "learning_mode": "GAME",
        "preview": {
            "title": "Keyword Bingo",
            "action_text": "Play Bingo using key vocabulary from a chapter."
        },
        "details": {
            "objective": "Make revision fun while reinforcing key terms.",
            "steps": [
                "Prepare bingo sheets with topic-related keywords.",
                "Call out definitions, examples, or images related to words.",
                "Students mark matching terms on their sheets.",
                "First student to complete a row or full sheet wins.",
                "Discuss key concepts briefly after game."
            ],
            "time_required_min": 20,
            "materials_needed": ["bingo templates", "markers"],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Combines play with revision, increasing retention.",
            "cognitive_target": "recall"
        },
        "constraints": {
            "requires": ["BASIC_PRINT_MATERIALS"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "DISENGAGED"
        },
        "tags": ["game", "revision", "language", "science"]
    },
    {
        "solution_id": "student_created_flashcards_revision",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["REVISION", "LOW_RECALL"],
        "subjects": ["SCIENCE", "MATH"],
        "class_range": "MIDDLE",
        "topic_type": "RECALL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Student-Made Flashcards",
            "action_text": "Ask students to create flashcards for key terms and quiz each other."
        },
        "details": {
            "objective": "Enhance recall by having students process and summarize content.",
            "steps": [
                "Assign key terms or concepts from the chapter.",
                "Ask students to write the term on one side and the definition/example on the back.",
                "Pair up students to quiz each other.",
                "Encourage creativity (drawings, mnemonics).",
                "Store flashcards for later practice rounds."
            ],
            "time_required_min": 20,
            "materials_needed": ["index cards", "pens"],
            "teacher_tone": "encouraging"
        },
        "pedagogy": {
            "why_it_works": "Creating learning materials deepens understanding and builds ownership.",
            "cognitive_target": "retention"
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
            "student_state": "NEEDS_REVISION"
        },
        "tags": ["flashcards", "peer_quiz", "revision"]
    },
    {
        "solution_id": "traffic_light_self_assessment",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONFIDENCE_CHECK", "CONCEPTUAL_DOUBT"],
        "subjects": ["GENERAL"],
        "class_range": "PRIMARY",
        "topic_type": "SELF_ASSESSMENT",
        "learning_mode": "REFLECTIVE",
        "preview": {
            "title": "Traffic Light Check-In",
            "action_text": "Use color cards to help students self-assess their understanding."
        },
        "details": {
            "objective": "Encourage students to reflect on their grasp of a concept.",
            "steps": [
                "Give each student 3 color cards: red (don’t understand), yellow (unsure), green (confident).",
                "After teaching a topic, ask them to raise a card.",
                "Use this input to adjust instruction (reteach, pair, or proceed).",
                "Keep responses anonymous to reduce pressure.",
                "Repeat weekly to build habit."
            ],
            "time_required_min": 5,
            "materials_needed": ["colored paper cards"],
            "teacher_tone": "open and trusting"
        },
        "pedagogy": {
            "why_it_works": "Students become aware of their learning status and teachers can tailor help.",
            "cognitive_target": "self-awareness"
        },
        "constraints": {
            "requires": ["COLOR_MATERIALS"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "MIXED"
        },
        "tags": ["formative", "reflection", "visual"]
    },
    {
        "solution_id": "story_retelling_sequence_game",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ATTENTION", "LISTENING_ISSUES"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "COMPREHENSION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Story Retelling with Sequence Game",
            "action_text": "Narrate a story and have students retell it in parts using cue cards."
        },
        "details": {
            "objective": "Improve listening, memory, and sequencing.",
            "steps": [
                "Read a short story to the class.",
                "Distribute cue cards with key events (shuffled).",
                "Students work in groups to arrange the events in correct order.",
                "Ask one student from each group to retell the story using the cards.",
                "Discuss which parts were remembered and why."
            ],
            "time_required_min": 20,
            "materials_needed": ["cue cards"],
            "teacher_tone": "narrative and engaging"
        },
        "pedagogy": {
            "why_it_works": "Sequencing supports logical thinking and strengthens comprehension.",
            "cognitive_target": "memory and order"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "DISTRACTED"
        },
        "tags": ["listening", "storytelling", "language"]
    },
    {
        "solution_id": "estimate_and_measure_walk",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["CONCEPTUAL_BLUR", "INATTENTION"],
        "subjects": ["MATH"],
        "class_range": "PRIMARY",
        "topic_type": "APPLICATION",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Estimate and Measure Walk",
            "action_text": "Take students around the school to estimate and measure objects."
        },
        "details": {
            "objective": "Apply length and measurement concepts to real objects.",
            "steps": [
                "Split class into pairs with measuring tapes or rulers.",
                "Assign 5–6 school objects (door, bench, blackboard).",
                "Ask each pair to first estimate, then measure.",
                "Record and compare estimates vs. actuals.",
                "Wrap up with a reflection on errors and surprises."
            ],
            "time_required_min": 30,
            "materials_needed": ["measuring tapes", "worksheets"],
            "teacher_tone": "exploratory"
        },
        "pedagogy": {
            "why_it_works": "Movement anchors abstract concepts in real contexts.",
            "cognitive_target": "application"
        },
        "constraints": {
            "requires": ["OUTDOOR_ACCESS"],
            "avoid_if": ["SPACE_LIMITED"]
        },
        "effort_level": "HIGH",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "UNENGAGED"
        },
        "tags": ["measurement", "movement", "real_life"]
    },
    {
        "solution_id": "value_chain_game_respect",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["BEHAVIORAL_ISSUES"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "PRIMARY",
        "topic_type": "VALUES",
        "learning_mode": "ROLE_PLAY",
        "preview": {
            "title": "Respect Chain Game",
            "action_text": "Use a roleplay chain to demonstrate and reinforce respectful behavior."
        },
        "details": {
            "objective": "Demonstrate the ripple effect of respectful interactions.",
            "steps": [
                "Begin with a small skit showing one student being kind or respectful.",
                "That student then passes it forward to the next (help, kind word, etc.).",
                "Continue the chain till every student participates.",
                "Debrief on how it felt to receive and give respect.",
                "Reflect on applying it in real situations."
            ],
            "time_required_min": 20,
            "materials_needed": [],
            "teacher_tone": "supportive and warm"
        },
        "pedagogy": {
            "why_it_works": "Creates emotional buy-in through experience, not preaching.",
            "cognitive_target": "values internalization"
        },
        "constraints": {
            "requires": [],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "RESISTANT"
        },
        "tags": ["values", "role_play", "respect"]
    },
    {
        "solution_id": "community_interview_home_assignment",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["LOW_ENGAGEMENT", "REAL_WORLD_DISCONNECT"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "APPLICATION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Interview a Community Member",
            "action_text": "Assign students to interview local elders on social or historical themes."
        },
        "details": {
            "objective": "Connect textbook knowledge with real-life social understanding.",
            "steps": [
                "Identify a unit (e.g., professions, governance, freedom struggle).",
                "Ask students to find someone in the community with relevant experience.",
                "Guide them on 5–6 respectful questions.",
                "Students write a short report on what they learned.",
                "Facilitate in-class sharing of unique responses."
            ],
            "time_required_min": 30,
            "materials_needed": ["notebooks"],
            "teacher_tone": "collaborative"
        },
        "pedagogy": {
            "why_it_works": "Bridges formal knowledge with lived experiences, boosts empathy.",
            "cognitive_target": "socio-emotional understanding"
        },
        "constraints": {
            "requires": ["PARENT_SUPPORT"],
            "avoid_if": ["SAFETY_CONCERNS"]
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "DISCONNECTED"
        },
        "tags": ["community", "application", "project"]
    },
    {
        "solution_id": "science_doodle_notes_concept_summary",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["BOREDOM", "LOW_RECALL"],
        "subjects": ["SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "CONCEPTUAL",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Doodle Notes for Concept Maps",
            "action_text": "Let students draw their understanding of a topic in doodles + keywords."
        },
        "details": {
            "objective": "Visualize and summarize scientific concepts creatively.",
            "steps": [
                "Explain a scientific concept using visual examples.",
                "Ask students to make a doodle-based summary sheet: icons + keywords.",
                "Encourage metaphors and humorous connections.",
                "Display a few on the board for peer discussion.",
                "Store sheets in a revision wall or folder."
            ],
            "time_required_min": 20,
            "materials_needed": ["A4 sheets", "color pens"],
            "teacher_tone": "creative and flexible"
        },
        "pedagogy": {
            "why_it_works": "Dual coding theory: words + visuals improve recall and interest.",
            "cognitive_target": "encoding"
        },
        "constraints": {
            "requires": ["STATIONERY"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "DISENGAGED"
        },
        "tags": ["visual", "summary", "science"]
    },
    {
        "solution_id": "language_choral_reading_fluency",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["FLUENCY_ISSUE", "SILENT_CLASS"],
        "subjects": ["LANGUAGE"],
        "class_range": "PRIMARY",
        "topic_type": "FLUENCY",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Choral Reading for Confidence",
            "action_text": "Whole class reads aloud together to build fluency and reduce fear."
        },
        "details": {
            "objective": "Build confidence and rhythm in reading aloud.",
            "steps": [
                "Choose a simple, rhythmical passage (poem/story).",
                "Read aloud once, then have the whole class read with you.",
                "Repeat twice with different intonations.",
                "Ask a few confident students to read solo.",
                "Rotate through students over the week."
            ],
            "time_required_min": 10,
            "materials_needed": ["reading text"],
            "teacher_tone": "energetic and supportive"
        },
        "pedagogy": {
            "why_it_works": "Reduces anxiety through group activity, builds oral fluency.",
            "cognitive_target": "oral language"
        },
        "constraints": {
            "requires": [],
            "avoid_if": ["HIGH_NOISE_SENSITIVITY"]
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "HESITANT"
        },
        "tags": ["fluency", "reading", "group"]
    },
    {
        "solution_id": "gallery_walk_math_problem_solving",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["PASSIVITY", "LOW_PARTICIPATION"],
        "subjects": ["MATH"],
        "class_range": "UPPER",
        "topic_type": "APPLICATION",
        "learning_mode": "KINETIC",
        "preview": {
            "title": "Gallery Walk for Problem Solving",
            "action_text": "Post unsolved problems around the class, and rotate teams to solve them."
        },
        "details": {
            "objective": "Create movement and peer learning while solving problems.",
            "steps": [
                "Post 4–5 problems (charts) around the classroom.",
                "Divide students into teams; each starts at a different problem.",
                "Give 5 minutes at each station, then rotate.",
                "Final team solves and presents the solution for that chart.",
                "Review as a class."
            ],
            "time_required_min": 25,
            "materials_needed": ["chart papers", "markers"],
            "teacher_tone": "facilitator"
        },
        "pedagogy": {
            "why_it_works": "Combines collaboration, motion, and problem-solving.",
            "cognitive_target": "engagement"
        },
        "constraints": {
            "requires": ["SPACE"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "medium",
            "student_state": "INACTIVE"
        },
        "tags": ["math", "movement", "problem_solving"]
    },
    {
        "solution_id": "self_check_station_assessment",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["LARGE_CLASS", "FEEDBACK_DELAY"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "FORMATIVE_ASSESSMENT",
        "learning_mode": "SELF_DIRECTED",
        "preview": {
            "title": "Self-Check Stations",
            "action_text": "Set up answer keys at learning corners for students to self-assess worksheets."
        },
        "details": {
            "objective": "Empower students to check their own work and learn from errors.",
            "steps": [
                "Create 3–4 self-check corners with answer keys.",
                "Distribute worksheet tasks to students.",
                "After solving, students visit corners to compare with keys.",
                "Highlight mismatches and write corrections.",
                "Teacher monitors quietly and supports as needed."
            ],
            "time_required_min": 30,
            "materials_needed": ["answer keys", "worksheets"],
            "teacher_tone": "non-intrusive"
        },
        "pedagogy": {
            "why_it_works": "Fosters independence and saves grading time in large classes.",
            "cognitive_target": "meta-cognition"
        },
        "constraints": {
            "requires": ["PRINT_RESOURCES"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "large",
            "student_state": "SEEKING_FEEDBACK"
        },
        "tags": ["assessment", "self_learning", "worksheets"]
    },
    {
        "solution_id": "student_charter_creation_activity",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["DISCIPLINE_ISSUE", "LOW_OWNERSHIP"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": ["BEHAVIOR"],
        "learning_mode": "COLLABORATIVE",
        "preview": {
            "title": "Create a Student Charter",
            "action_text": "Co-create classroom rules with students to promote ownership and values."
        },
        "details": {
            "objective": "Encourage responsibility and shared values in classroom conduct.",
            "steps": [
                "Ask students to brainstorm key values (honesty, teamwork, etc.).",
                "Facilitate discussion on classroom behavior linked to each value.",
                "Draft a 'Student Charter' in groups and combine final version.",
                "Display charter visibly in class.",
                "Review it monthly together."
            ],
            "time_required_min": 25,
            "materials_needed": ["chart paper", "markers"],
            "teacher_tone": "inclusive"
        },
        "pedagogy": {
            "why_it_works": "Boosts ownership and group norms by including student voice.",
            "cognitive_target": "values internalization"
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
            "student_state": "DEFIANT"
        },
        "tags": ["charter", "behavior", "ownership"]
    },
    {
        "solution_id": "conflict_resolution_roleplay",
        "version": 1,
        "status": "active",
        "response_style": "KINETIC",
        "situations": ["BULLYING", "DISPUTES"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "UPPER",
        "topic_type": "SOCIAL_SKILLS",
        "learning_mode": "PERFORMATIVE",
        "preview": {
            "title": "Conflict Resolution Roleplay",
            "action_text": "Let students act out common peer conflicts and propose fair resolutions."
        },
        "details": {
            "objective": "Model empathy, fairness, and assertiveness in resolving problems.",
            "steps": [
                "Choose 2–3 realistic conflict situations (e.g., teasing, exclusion).",
                "Divide class into groups and assign one roleplay each.",
                "Let them enact and pause midway for class to discuss choices.",
                "Restart with suggested alternative actions.",
                "Wrap up with a reflective Q&A."
            ],
            "time_required_min": 30,
            "materials_needed": ["scenario slips"],
            "teacher_tone": "neutral facilitator"
        },
        "pedagogy": {
            "why_it_works": "Practices social-emotional strategies through safe simulations.",
            "cognitive_target": "empathy"
        },
        "constraints": {
            "requires": ["PSYCHOLOGICAL_SAFETY"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "MEDIUM",
        "noise_level": "HIGH",
        "works_best_when": {
            "class_strength": "small",
            "student_state": "INTERPERSONAL_ISSUES"
        },
        "tags": ["conflict", "roleplay", "social_skills"]
    },
    {
        "solution_id": "cartoon_strip_topic_summary",
        "version": 1,
        "status": "active",
        "response_style": "COGNITIVE",
        "situations": ["LOW_RECALL", "WRITING_BLOCK"],
        "subjects": ["SCIENCE", "SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "SUMMARY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Topic Summary via Cartoon Strip",
            "action_text": "Let students draw comic-style sequences of a recently covered topic."
        },
        "details": {
            "objective": "Encourage synthesis and sequence building using visual storytelling.",
            "steps": [
                "Assign a topic like 'Photosynthesis' or 'Water Cycle'.",
                "Students plan a cartoon strip with 4–6 boxes showing concept flow.",
                "They draw visuals and write dialogue/thought bubbles.",
                "Facilitate a cartoon gallery walk.",
                "Use some for bulletin board display."
            ],
            "time_required_min": 25,
            "materials_needed": ["chart sheets", "markers"],
            "teacher_tone": "playful"
        },
        "pedagogy": {
            "why_it_works": "Promotes synthesis through drawing and sequencing.",
            "cognitive_target": "summarization"
        },
        "constraints": {
            "requires": ["ART_MATERIALS"],
            "avoid_if": []
        },
        "effort_level": "MEDIUM",
        "classroom_safety": "HIGH",
        "noise_level": "MEDIUM",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "BORED"
        },
        "tags": ["comic", "visual_summary", "science"]
    },
    {
        "solution_id": "student_feedback_station",
        "version": 1,
        "status": "active",
        "response_style": "STRUCTURAL",
        "situations": ["LOW_REFLECTION", "UNRESPONSIVE_CLASS"],
        "subjects": ["GENERAL"],
        "class_range": "UPPER",
        "topic_type": "SELF_ASSESSMENT",
        "learning_mode": "SELF_DIRECTED",
        "preview": {
            "title": "Feedback Station for Reflection",
            "action_text": "Install a station where students drop quick feedback after class."
        },
        "details": {
            "objective": "Foster student voice and reflection habits.",
            "steps": [
                "Set up a box labeled 'Student Voice Station'.",
                "Place slips with 2 questions: ‘What helped you today?’ and ‘What confused you?’",
                "Students drop slips as exit activity.",
                "Read selected ones aloud next day to show value.",
                "Use patterns to inform your instruction."
            ],
            "time_required_min": 5,
            "materials_needed": ["slips", "box"],
            "teacher_tone": "welcoming"
        },
        "pedagogy": {
            "why_it_works": "Normalizes reflection and gives feedback channel to the teacher.",
            "cognitive_target": "meta-cognition"
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
            "student_state": "PASSIVE"
        },
        "tags": ["reflection", "feedback", "self_learning"]
    },
    {
        "solution_id": "family_talk_assignment_ethics",
        "version": 1,
        "status": "active",
        "response_style": "SOCIAL",
        "situations": ["VALUES_CONFUSION", "DISCONNECTED"],
        "subjects": ["SOCIAL_SCIENCE"],
        "class_range": "MIDDLE",
        "topic_type": "ETHICS",
        "learning_mode": "HOME_LINKED",
        "preview": {
            "title": "Family Talk Assignment",
            "action_text": "Ask students to discuss moral dilemmas with family and bring insights."
        },
        "details": {
            "objective": "Bridge school-home on value education.",
            "steps": [
                "Assign a situation (e.g., 'You found money in school').",
                "Ask students to ask 2–3 family members what they would do.",
                "Note responses without judgment.",
                "Share perspectives in a circle time.",
                "Compare with textbook or classroom ethic."
            ],
            "time_required_min": 15,
            "materials_needed": ["notebooks"],
            "teacher_tone": "non-judgmental"
        },
        "pedagogy": {
            "why_it_works": "Includes diverse worldviews, personalizes ethical reasoning.",
            "cognitive_target": "values clarification"
        },
        "constraints": {
            "requires": ["PARENT_SUPPORT"],
            "avoid_if": []
        },
        "effort_level": "LOW",
        "classroom_safety": "HIGH",
        "noise_level": "LOW",
        "works_best_when": {
            "class_strength": "any",
            "student_state": "UNCERTAIN"
        },
        "tags": ["ethics", "home_link", "reflection"]
    }
]