from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

BEHAVIOR_SOLUTIONS = [
    {
        "solution_id": "private_reset_talk",
        "version": "1.0",
        "status": "active",
        "situations": [SITUATIONS["DISRESPECT_DEFIANCE"], SITUATIONS["CLASSROOM_CHAOS"]],
        "subjects": [SUBJECTS["GENERAL"]],
        "class_range": "ALL",
        "topic_type": "BEHAVIOR",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "The Private Reset Talk",
            "action_text": "De-escalate rudeness by speaking privately, not publicly."
        },
        "details": {
            "objective": "To stop defiance without causing a scene.",
            "steps": [
                "Do not argue with the student in front of the class.",
                "Calmly say: 'We need to discuss this later. Please continue your work.'",
                "Wait for a quiet moment or end of class.",
                "Speak to them privately: 'I noticed you were upset. What's going on?'",
                "Reinforce the rule firmly but respectfully."
            ],
            "time_required_min": 5
        },
        "constraints": {},
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"],
    },
    {
        "solution_id": "broken_record_technique",
        "version": "1.0",
        "status": "active",
        "situations": [SITUATIONS["DISRESPECT_DEFIANCE"]],
        "subjects": [SUBJECTS["GENERAL"]],
        "class_range": "ALL",
        "topic_type": "BEHAVIOR",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "Broken Record Technique",
            "action_text": "Repeat the instruction calmly to avoid an argument."
        },
        "details": {
            "objective": "To enforce a rule without getting drawn into a debate.",
            "steps": [
                "Give the instruction clearly (e.g., 'Please sit down').",
                "If the student argues, acknowledge them but repeat the instruction: 'I hear you, but please sit down.'",
                "Keep your voice neutral and flat.",
                "Repeat up to 3 times. If they still refuse, issue a standard consequence calmly."
            ],
            "time_required_min": 2
        },
        "constraints": {},
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"],
    }
]