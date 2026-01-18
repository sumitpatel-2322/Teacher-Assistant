from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

SCIENCE_SOLUTIONS = [
    {
        "solution_id": "sci_turmeric_indicator",
        "version": "1.0",
        "status": "active",
        "situations": ["NO_LAB_EQUIPMENT", "ABSTRACT_CONCEPT"],
        "subjects": ["SCIENCE", "CHEMISTRY"],
        "class_range": "CLASS_6_10",
        "topic_type": "EXPERIMENT",
        "learning_mode": "HANDS_ON",
        "preview": {
            "title": "Turmeric Acid Test",
            "action_text": "Use Turmeric (Haldi) and Soap to teach Acids and Bases without chemicals."
        },
        "details": {
            "objective": "To demonstrate chemical indicators using kitchen ingredients.",
            "steps": [
                "Mix Turmeric powder with water to make a yellow paste.",
                "Rub it on a white paper and let it dry (Yellow Strip).",
                "Apply Lemon Juice (Acid) -> No Change.",
                "Apply Soap Water (Base) -> Turns Red.",
                "Explain: Turmeric is a natural indicator."
            ],
            "time_required_min": 20,
            "materials_needed": ["Turmeric", "Soap", "Lemon", "Paper"],
            "teacher_tone": "Scientific"
        },
        "pedagogy": {
            "why_it_works": "Connects abstract chemistry concepts to daily life materials.",
            "cognitive_target": "observation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "sci_shadow_stick",
        "version": "1.0",
        "status": "active",
        "situations": ["NO_ELECTRICITY", "OUTDOOR_LESSON"],
        "subjects": ["SCIENCE", "PHYSICS"],
        "class_range": "CLASS_5_8",
        "topic_type": "ASTRONOMY",
        "learning_mode": "OBSERVATIONAL",
        "preview": {
            "title": "Shadow Stick Clock",
            "action_text": "Track the sun's movement using a stick in the ground."
        },
        "details": {
            "objective": "To understand earth's rotation and light/shadow.",
            "steps": [
                "Place a straight stick in the ground on a sunny morning.",
                "Mark the tip of the shadow with a stone.",
                "Wait 1 hour. Mark the new shadow tip.",
                "Ask: 'Did the sun move or did the earth move?'"
            ],
            "time_required_min": 10,
            "materials_needed": ["Stick", "Stones"],
            "teacher_tone": "Inquisitive"
        },
        "pedagogy": {
            "why_it_works": "Visualizing planetary motion is impossible without long-term observation.",
            "cognitive_target": "spatial_reasoning"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "sci_photosynthesis_roleplay",
        "version": "1.0",
        "status": "active",
        "situations": ["CONCEPT_CONFUSION", "BOREDOM"],
        "subjects": ["SCIENCE", "BIOLOGY"],
        "class_range": "CLASS_4_7",
        "topic_type": "PROCESS",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "The Plant Factory Roleplay",
            "action_text": "Students act as Roots, Leaves, and Sun to simulate photosynthesis."
        },
        "details": {
            "objective": "To visualize the inputs and outputs of photosynthesis.",
            "steps": [
                "Assign roles: Roots (Collect Water), Sun (Give Energy), Leaves (Cook).",
                "Roots 'pass' blue paper balls (Water) to Leaves.",
                "Sun 'throws' yellow balls (Light) to Leaves.",
                "Leaves mix them and throw out white balls (Oxygen) and keep green balls (Sugar).",
                "Ask: 'What happens if the Sun stops?'"
            ],
            "time_required_min": 15,
            "materials_needed": ["Colored Paper Balls"],
            "teacher_tone": "Energetic"
        },
        "pedagogy": {
            "why_it_works": "Systems thinking is best taught through simulation.",
            "cognitive_target": "process_understanding"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["MEDIUM"]
    },
    {
        "solution_id": "sci_water_cycle_bag",
        "version": "1.0",
        "status": "active",
        "situations": ["ABSTRACT_CONCEPT", "NO_LAB_EQUIPMENT"],
        "subjects": ["SCIENCE", "GEOGRAPHY"],
        "class_range": "CLASS_3_6",
        "topic_type": "ENVIRONMENT",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "Water Cycle in a Bag",
            "action_text": "Tape a plastic bag with water to the window to see evaporation/rain."
        },
        "details": {
            "objective": "To observe evaporation and condensation in real-time.",
            "steps": [
                "Pour a little water into a clear ziplock/plastic bag.",
                "Tape it tightly to a sunny window.",
                "Wait 1 hour.",
                "Point out the droplets forming at top (Clouds/Condensation) and running down (Rain).",
                "Explain the cycle."
            ],
            "time_required_min": 5,
            "materials_needed": ["Plastic Bag", "Tape", "Water"],
            "teacher_tone": "Observant"
        },
        "pedagogy": {
            "why_it_works": "Miniaturizing a large-scale phenomenon makes it graspable.",
            "cognitive_target": "scientific_observation"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "sci_pulse_check",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_ENGAGEMENT", "BODY_AWARENESS"],
        "subjects": ["SCIENCE", "BIOLOGY"],
        "class_range": "CLASS_4_8",
        "topic_type": "HUMAN_BODY",
        "learning_mode": "KINESTHETIC",
        "preview": {
            "title": "Jump and Check Pulse",
            "action_text": "Students measure heart rate before and after jumping."
        },
        "details": {
            "objective": "To understand the effect of exercise on the heart.",
            "steps": [
                "Show students how to find their pulse on the wrist/neck.",
                "Count beats for 15 seconds (Resting).",
                "Ask them to do 20 jumping jacks.",
                "Count beats again immediately.",
                "Ask: 'Why is it faster? (Muscles need more oxygen).'"
            ],
            "time_required_min": 10,
            "materials_needed": ["None"],
            "teacher_tone": "Active"
        },
        "pedagogy": {
            "why_it_works": "Direct physiological feedback creates instant engagement.",
            "cognitive_target": "cause_and_effect"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]