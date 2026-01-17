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
    },
    {
        "solution_id": "fln_matchbox_chest",
        "version": "1.0",
        "status": "active",
        "situations": ["DISORGANIZATION", "LETTER_RECOGNITION"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_1_2",
        "topic_type": "LITERACY",
        "learning_mode": "CRAFT_BASED",
        "preview": {
            "title": "The Matchbox Letter Chest",
            "action_text": "Glue empty matchboxes together to create a mini-drawer system for sorting letters."
        },
        "details": {
            "objective": "To practice alphabet sorting and fine motor skills.",
            "steps": [
                "Collect 26 empty matchboxes.",
                "Glue them in a grid (5x5 + 1).",
                "Write one letter (A-Z) on each drawer handle.",
                "Give students small paper chits with words or pictures.",
                "Ask them to put the chit into the correct starting-letter drawer."
            ],
            "time_required_min": 30,
            "materials_needed": ["Empty Matchboxes", "Glue", "Marker"],
            "teacher_tone": "Creative"
        },
        "pedagogy": {
            "why_it_works": "Gamifies sorting and categorization, a key pre-reading skill.",
            "cognitive_target": "classification"
        },
        "effort_level": EFFORT_LEVELS["HIGH"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_bangle_patterns",
        "version": "1.0",
        "status": "active",
        "situations": ["CONCEPT_CONFUSION"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1",
        "topic_type": "NUMERACY",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Bangle Patterning",
            "action_text": "Use colored bangles to teach sequencing and patterns."
        },
        "details": {
            "objective": "To understand logical sequences (Pre-math).",
            "steps": [
                "Collect old colored bangles (Red, Green, Blue).",
                "Start a pattern on a stick or rope: Red-Red-Green, Red-Red-Green.",
                "Ask the student: 'What comes next?'",
                "Let them slide the correct bangle on."
            ],
            "time_required_min": 15,
            "materials_needed": ["Bangles", "Stick/Rope"],
            "teacher_tone": "Playful"
        },
        "pedagogy": {
            "why_it_works": "Pattern recognition is the foundational logic for algebra and coding later in life.",
            "cognitive_target": "pattern_recognition"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_newspaper_hunt",
        "version": "1.0",
        "status": "active",
        "situations": ["READING_DIFFICULTY", "LOW_RESOURCES"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_2_3",
        "topic_type": "LITERACY",
        "learning_mode": "OBSERVATIONAL",
        "preview": {
            "title": "Newspaper Letter Hunt",
            "action_text": "Students circle specific letters or words in an old newspaper."
        },
        "details": {
            "objective": "To identify letters in different fonts and contexts.",
            "steps": [
                "Give each group an old newspaper page.",
                "Say: 'Circle every letter B you can find in 2 minutes.'",
                "Or: 'Find 3 words that start with M.'",
                "Count who found the most."
            ],
            "time_required_min": 10,
            "materials_needed": ["Old Newspapers", "Pencils"],
            "teacher_tone": "Competitive"
        },
        "pedagogy": {
            "why_it_works": "Exposes students to real-world print (environmental print) rather than just textbook fonts.",
            "cognitive_target": "visual_discrimination"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_tamarind_seed_math",
        "version": "1.0",
        "status": "active",
        "situations": ["MATH_DIFFICULTY", "NO_MANIPULATIVES"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_2",
        "topic_type": "NUMERACY",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Seed Addition (Chiyanka/Imli)",
            "action_text": "Use tamarind seeds (locally available) as counters for addition."
        },
        "details": {
            "objective": "To perform addition using local no-cost materials.",
            "steps": [
                "Ask students to bring tamarind seeds (or small stones) from home.",
                "Draw two circles on the floor.",
                "Put 5 seeds in one, 3 in the other.",
                "Ask students to slide them all into a big 'Answer Box' circle and count.",
                "Answer: 8."
            ],
            "time_required_min": 15,
            "materials_needed": ["Tamarind Seeds/Stones", "Chalk"],
            "teacher_tone": "Interactive"
        },
        "pedagogy": {
            "why_it_works": "Using familiar local objects reduces the cognitive load of 'school math'.",
            "cognitive_target": "arithmetic_operations"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_handspan_measure",
        "version": "1.0",
        "status": "active",
        "situations": ["CONCEPT_CONFUSION", "NO_RULERS"],
        "subjects": ["MATH"],
        "class_range": "CLASS_2",
        "topic_type": "MEASUREMENT",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Handspan Measurement",
            "action_text": "Measure classroom objects using handspans (Balishth) before using rulers."
        },
        "details": {
            "objective": "To understand the concept of length and the need for standard units.",
            "steps": [
                "Show how to stretch the hand from thumb to little finger (Handspan).",
                "Ask students to measure their desk: 'How many handspans?'",
                "Compare results: 'Why did Ravi get 8 and Sir get 5?'",
                "Explain that hands are different sizes -> Need for Scale (cm)."
            ],
            "time_required_min": 20,
            "materials_needed": ["None"],
            "teacher_tone": "Inquisitive"
        },
        "pedagogy": {
            "why_it_works": "History of math approach: Concrete (Body) -> Abstract (Ruler).",
            "cognitive_target": "measurement_concepts"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_blindfold_shape",
        "version": "1.0",
        "status": "active",
        "situations": ["SENSORY_NEED", "GEOMETRY_CONFUSION"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_3",
        "topic_type": "GEOMETRY",
        "learning_mode": "TACTILE",
        "preview": {
            "title": "Blindfold Shape Guess",
            "action_text": "Students guess the shape of an object by feeling it while blindfolded."
        },
        "details": {
            "objective": "To identify properties of 3D shapes (corners, edges, curves).",
            "steps": [
                "Blindfold a student.",
                "Hand them an object (Ball, Duster, Book).",
                "Ask: 'Does it have corners? Is it round?'",
                "Ask them to name the shape (Sphere, Cuboid).",
                "Class claps if correct."
            ],
            "time_required_min": 15,
            "materials_needed": ["Cloth", "Classroom Objects"],
            "teacher_tone": "Excited"
        },
        "pedagogy": {
            "why_it_works": "Isolating the tactile sense forces the brain to analyze geometric properties deeply.",
            "cognitive_target": "spatial_reasoning"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_sock_puppet_story",
        "version": "1.0",
        "status": "active",
        "situations": ["SHYNESS", "LOW_ORAL_SKILLS"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_1_2",
        "topic_type": "ORAL_LANGUAGE",
        "learning_mode": "ROLEPLAY",
        "preview": {
            "title": "Sock Puppet Storytelling",
            "action_text": "Use an old sock as a puppet to encourage shy students to speak."
        },
        "details": {
            "objective": "To develop oral language fluency.",
            "steps": [
                "Take an old sock. Draw eyes on the toe part.",
                "Put it on your hand.",
                "Have the puppet ask the student questions: 'What is your name?'",
                "Tell students: 'The puppet only speaks to you, not the teacher.'",
                "Encourage students to make their own puppets."
            ],
            "time_required_min": 20,
            "materials_needed": ["Old Socks", "Marker"],
            "teacher_tone": "Playful"
        },
        "pedagogy": {
            "why_it_works": "Projecting onto a puppet lowers social anxiety (Displacement effect).",
            "cognitive_target": "speaking_skills"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_water_bottle_bowling",
        "version": "1.0",
        "status": "active",
        "situations": ["MATH_BOREDOM"],
        "subjects": ["MATH"],
        "class_range": "CLASS_1_3",
        "topic_type": "NUMERACY",
        "learning_mode": "GAMIFIED",
        "preview": {
            "title": "Bottle Bowling (Subtraction)",
            "action_text": "Use empty water bottles as bowling pins to teach subtraction."
        },
        "details": {
            "objective": "To visualize subtraction as 'taking away'.",
            "steps": [
                "Set up 10 empty plastic bottles in a triangle.",
                "Roll a ball to knock them down.",
                "Count how many fell (e.g., 4).",
                "Equation: 10 - 4 = 6 standing.",
                "Write it on the board."
            ],
            "time_required_min": 20,
            "materials_needed": ["Plastic Bottles", "Ball"],
            "teacher_tone": "Energetic"
        },
        "pedagogy": {
            "why_it_works": "Physical action makes the abstract concept of 'minus' concrete and fun.",
            "cognitive_target": "subtraction"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "fln_leaf_sorting",
        "version": "1.0",
        "status": "active",
        "situations": ["NATURE_WALK", "CONCEPT_CONFUSION"],
        "subjects": ["MATH", "SCIENCE"],
        "class_range": "CLASS_1_2",
        "topic_type": "PRE_MATH",
        "learning_mode": "OBSERVATIONAL",
        "preview": {
            "title": "Nature Sorting (Leaves)",
            "action_text": "Sort leaves by size, color, and shape."
        },
        "details": {
            "objective": "To learn classification attributes (Big/Small, Green/Brown).",
            "steps": [
                "Go outside and collect fallen leaves.",
                "Ask students to make piles.",
                "Pile 1: Big Leaves. Pile 2: Small Leaves.",
                "Pile 3: Brown Leaves. Pile 4: Green Leaves.",
                "Explain that we are 'sorting' data."
            ],
            "time_required_min": 20,
            "materials_needed": ["Leaves"],
            "teacher_tone": "Calm"
        },
        "pedagogy": {
            "why_it_works": "Classification is the first step towards organized thinking and set theory.",
            "cognitive_target": "data_handling"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "fln_name_card_scramble",
        "version": "1.0",
        "status": "active",
        "situations": ["LITERACY_START"],
        "subjects": ["ENGLISH", "HINDI"],
        "class_range": "CLASS_1",
        "topic_type": "LITERACY",
        "learning_mode": "PUZZLE",
        "preview": {
            "title": "Name Card Puzzle",
            "action_text": "Cut a student's name card into pieces and ask them to reassemble it."
        },
        "details": {
            "objective": "To recognize letter order in their own name.",
            "steps": [
                "Write the student's name on a card (e.g., R-A-J-U).",
                "Cut the card between the letters.",
                "Jumble the pieces.",
                "Ask the student to put them back in order.",
                "Glue it onto a new sheet."
            ],
            "time_required_min": 10,
            "materials_needed": ["Paper", "Scissors", "Glue"],
            "teacher_tone": "Encouraging"
        },
        "pedagogy": {
            "why_it_works": "Personal names are the most meaningful text for a child, ensuring high engagement.",
            "cognitive_target": "word_construction"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]