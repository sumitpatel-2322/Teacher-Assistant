from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

FLN_SOLUTIONS = [
    {
        "solution_id": "fln_sand_tracing",
        "version": "1.0",
        "status": "active",
        "situations": ["WRITING_DIFFICULTY", "FINE_MOTOR_ISSUES"],
        "subjects": ["HINDI", "ENGLISH"],
        "class_range": "CLASS_1_2",
        "topic_type": "LITERACY",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Sand Tray Tracing",
            "action_text": "Use a tray of sand or dirt for students to trace letters with their fingers before using a pencil."
        },
        "details": {
            "objective": "To build muscle memory for letter shapes without the stress of holding a pencil.",
            "steps": [
                "Fill a plate or tray with fine sand (or dry soil/rice).",
                "Show the letter card to the student.",
                "Ask them to trace the shape in the sand using their index finger.",
                "Shake the tray gently to 'erase' and try again."
            ],
            "time_required_min": 10,
            "materials_needed": ["Tray/Plate", "Sand/Soil"],
            "teacher_tone": "Encouraging"
        },
        "pedagogy": {
            "why_it_works": "Reduces friction and fear of making mistakes; aligns with NIPUN Bharat's 'play-based' approach.",
            "cognitive_target": "motor_skill_development"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_pebble_counting",
        "version": "1.0",
        "status": "active",
        "situations": ["CONCEPT_CONFUSION", "MATH_DIFFICULTY"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_2",
        "topic_type": "NUMERACY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Pebble Grouping (Concrete Counting)",
            "action_text": "Use stones or bottle caps to physically demonstrate addition and grouping."
        },
        "details": {
            "objective": "To move from rote counting to understanding quantity.",
            "steps": [
                "Ask students to collect 10 small pebbles each.",
                "Write a number (e.g., '5') on the board.",
                "Ask students to place exactly 5 pebbles on their desk.",
                "Now ask them to make two groups from those 5 (e.g., 2 and 3).",
                "Explain that 2 + 3 makes 5."
            ],
            "time_required_min": 15,
            "materials_needed": ["Pebbles", "Bottle Caps", "Seeds"],
            "teacher_tone": "Interactive"
        },
        "pedagogy": {
            "why_it_works": "Concrete operations are essential before moving to abstract numbers (Piagetian stage).",
            "cognitive_target": "number_sense"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_word_detective",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_ENGAGEMENT", "READING_LANGUAGE_ISSUE"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_1_3",
        "topic_type": "LITERACY",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Classroom Word Detective",
            "action_text": "Turn reading into a hunt by labeling objects in the room."
        },
        "details": {
            "objective": "To connect written words with real-world objects.",
            "steps": [
                "Write labels for common objects (Door, Window, Blackboard, Table).",
                "Give a label to a student.",
                "Ask them to run and stick it on the correct object.",
                "Have the whole class read the word aloud once stuck."
            ],
            "time_required_min": 20,
            "materials_needed": ["Paper", "Tape/Glue"],
            "teacher_tone": "Excited"
        },
        "pedagogy": {
            "why_it_works": "Connects text to environment, making reading relevant and active.",
            "cognitive_target": "vocabulary_building"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_clay_letters",
        "version": "1.0",
        "status": "active",
        "situations": ["WRITING_DIFFICULTY", "BOREDOM"],
        "subjects": ["HINDI", "ENGLISH"],
        "class_range": "CLASS_1_2",
        "topic_type": "LITERACY",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Clay/Dough Letter Molding",
            "action_text": "Students shape letters using clay or wheat dough."
        },
        "details": {
            "objective": "To visualize the curves and lines of letters.",
            "steps": [
                "Provide a small ball of clay or wheat dough to students.",
                "Demonstrate how to roll it into a 'snake'.",
                "Ask them to bend the snake to make 'S', 'L', 'O'.",
                "Let them dry and trace them with fingers later."
            ],
            "time_required_min": 20,
            "materials_needed": ["Clay", "Wheat Dough"],
            "teacher_tone": "Patient"
        },
        "pedagogy": {
            "why_it_works": "3D representation of 2D letters helps spatial understanding.",
            "cognitive_target": "letter_recognition"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_market_day",
        "version": "1.0",
        "status": "active",
        "situations": ["MATH_DIFFICULTY", "LOW_ENGAGEMENT"],
        "subjects": ["MATH"],
        "class_range": "CLASS_2_4",
        "topic_type": "NUMERACY",
        "learning_mode": "ROLEPLAY",
        "preview": {
            "title": "The Classroom Market",
            "action_text": "Simulate a vegetable market to teach simple addition and subtraction."
        },
        "details": {
            "objective": "To apply math concepts to daily life transactions.",
            "steps": [
                "Assign 3 students as 'shopkeepers' with items (pencils, erasers) and price tags (₹2, ₹5).",
                "Give other students paper 'money'.",
                "Students must buy items and calculate the change.",
                "Rotate roles after 10 minutes."
            ],
            "time_required_min": 30,
            "materials_needed": ["Paper Money", "Classroom Objects"],
            "teacher_tone": "Observant"
        },
        "pedagogy": {
            "why_it_works": "Contextualizes math, removing the fear of abstract numbers.",
            "cognitive_target": "financial_literacy"
        },
        "effort_level": EFFORT_LEVELS["HIGH"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_story_sequencing",
        "version": "1.0",
        "status": "active",
        "situations": ["READING_LANGUAGE_ISSUE", "MEMORY_RETENTION_ISSUE"],
        "subjects": ["HINDI", "ENGLISH"],
        "class_range": "CLASS_1_3",
        "topic_type": "LITERACY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Picture Story Sequencing",
            "action_text": "Use 3-4 pictures to retell a story in the correct order."
        },
        "details": {
            "objective": "To understand narrative structure (Beginning, Middle, End).",
            "steps": [
                "Draw or cut out 3 scenes from a known story (e.g., Thirsty Crow).",
                "Jumble them up and stick them on the board.",
                "Ask a student to come rearrange them in the correct order.",
                "Ask another student to narrate what is happening in each picture."
            ],
            "time_required_min": 15,
            "materials_needed": ["Picture Cards"],
            "teacher_tone": "Curious"
        },
        "pedagogy": {
            "why_it_works": "Visual scaffolding helps students organize thoughts before speaking/writing.",
            "cognitive_target": "logical_sequencing"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_number_jump",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_ENGAGEMENT", "RESTLESSNESS"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_2",
        "topic_type": "NUMERACY",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Number Line Jump",
            "action_text": "Draw a number line on the floor; students jump to solve math problems."
        },
        "details": {
            "objective": "To physically experience addition (forward) and subtraction (backward).",
            "steps": [
                "Draw a number line (0-10) on the floor with chalk.",
                "Ask a student to stand on '3'.",
                "Say 'Add 2'. Student jumps forward 2 steps.",
                "Ask 'Where are you now?' (5).",
                "Say 'Minus 1'. Student jumps backward 1 step."
            ],
            "time_required_min": 15,
            "materials_needed": ["Chalk"],
            "teacher_tone": "Energetic"
        },
        "pedagogy": {
            "why_it_works": "Gross motor movement aids memory retention for energetic children.",
            "cognitive_target": "arithmetic_operations"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_sight_word_bingo",
        "version": "1.0",
        "status": "active",
        "situations": ["READING_LANGUAGE_ISSUE"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_2_3",
        "topic_type": "LITERACY",
        "learning_mode": "GAMIFIED",
        "preview": {
            "title": "Sight Word Bingo",
            "action_text": "A game to recognize common words instantly without spelling them out."
        },
        "details": {
            "objective": "To increase reading speed by recognizing high-frequency words.",
            "steps": [
                "Create a 3x3 grid on paper for students with common words (The, Is, And, He).",
                "Call out a word randomly.",
                "Students must circle the word if they have it.",
                "First one to circle 3 in a row yells 'Bingo'."
            ],
            "time_required_min": 15,
            "materials_needed": ["Paper", "Pencils"],
            "teacher_tone": "Excited"
        },
        "pedagogy": {
            "why_it_works": "Gamification increases focus and repetition required for sight word mastery.",
            "cognitive_target": "reading_fluency"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_shape_walk",
        "version": "1.0",
        "status": "active",
        "situations": ["CONCEPT_CONFUSION"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_2",
        "topic_type": "NUMERACY",
        "learning_mode": "OBSERVATIONAL",
        "preview": {
            "title": "The Shape Walk",
            "action_text": "Take a walk outside to find geometric shapes in nature/buildings."
        },
        "details": {
            "objective": "To identify 2D shapes in the real world.",
            "steps": [
                "Take students to the playground or school veranda.",
                "Ask them to find something 'Round' (Circle).",
                "Ask them to find something with '3 corners' (Triangle).",
                "Have them draw what they found in their notebook."
            ],
            "time_required_min": 20,
            "materials_needed": ["None"],
            "teacher_tone": "Exploratory"
        },
        "pedagogy": {
            "why_it_works": "Moves learning from the textbook to the environment, reinforcing relevance.",
            "cognitive_target": "geometry_basics"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_sound_circles",
        "version": "1.0",
        "status": "active",
        "situations": ["READING_LANGUAGE_ISSUE"],
        "subjects": ["HINDI", "ENGLISH"],
        "class_range": "CLASS_1",
        "topic_type": "LITERACY",
        "learning_mode": "AUDITORY",
        "preview": {
            "title": "Initial Sound Circles",
            "action_text": "Group students based on the starting sound of their names or assigned words."
        },
        "details": {
            "objective": "To develop phonemic awareness (identifying sounds).",
            "steps": [
                "Say a sound clearly (e.g., 'Puh' for P).",
                "Ask students whose names start with 'P' to stand in a circle.",
                "Ask them to say other words starting with 'P' (Pen, Parrot).",
                "Repeat for other sounds."
            ],
            "time_required_min": 10,
            "materials_needed": ["None"],
            "teacher_tone": "Rhythmic"
        },
        "pedagogy": {
            "why_it_works": "Phonemic awareness is the primary predictor of early reading success.",
            "cognitive_target": "phonics"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]