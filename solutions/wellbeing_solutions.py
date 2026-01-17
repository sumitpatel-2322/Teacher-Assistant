from decision_engine.constants import SITUATIONS, SUBJECTS, EFFORT_LEVELS, SAFETY_LEVELS

WELLBEING_SOLUTIONS = [
    {
        "solution_id": "wb_parent_vent_rule",
        "version": "1.0",
        "status": "active",
        "situations": ["ANGRY_PARENT", "CONFLICT_RESOLUTION"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "PROFESSIONAL_SKILLS",
        "learning_mode": "COMMUNICATION",
        "preview": {
            "title": "The 2-Minute Vent Rule",
            "action_text": "Let the angry parent speak for 2 minutes without interrupting."
        },
        "details": {
            "objective": "To de-escalate anger by ensuring the parent feels heard.",
            "steps": [
                "Do not defend yourself immediately.",
                "Listen silently for 2 full minutes.",
                "Maintain eye contact and nod.",
                "Say: 'I can see why you are upset.'",
                "Once they run out of energy, move to facts."
            ],
            "time_required_min": 5,
            "materials_needed": ["None"],
            "teacher_tone": "Calm"
        },
        "pedagogy": {
            "why_it_works": "Anger requires an outlet; interrupting fuels the fire. Validation drains the emotion.",
            "cognitive_target": "emotional_regulation"
        },
        "effort_level": EFFORT_LEVELS["HIGH"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "wb_shared_goal_pivot",
        "version": "1.0",
        "status": "active",
        "situations": ["ARGUMENTATIVE_PARENT", "DISAGREEMENT"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "NEGOTIATION",
        "learning_mode": "VERBAL",
        "preview": {
            "title": "The Shared Goal Pivot",
            "action_text": "Remind the parent that you both want the same thing: the student's success."
        },
        "details": {
            "objective": "To turn a confrontation into a partnership.",
            "steps": [
                "When a parent argues, pause.",
                "Say: 'We both want [Student Name] to succeed, right?'",
                "Wait for them to agree.",
                "Say: 'Great, so let's figure out how we can help him do that.'",
                "Focus on the solution, not the blame."
            ],
            "time_required_min": 3,
            "materials_needed": ["None"],
            "teacher_tone": "Collaborative"
        },
        "pedagogy": {
            "why_it_works": "Reframes the teacher and parent as teammates vs. enemies.",
            "cognitive_target": "conflict_resolution"
        },
        "effort_level": EFFORT_LEVELS["MEDIUM"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "wb_doorway_reset",
        "version": "1.0",
        "status": "active",
        "situations": ["TEACHER_BURNOUT", "STRESS_CARRYOVER"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "SELF_CARE",
        "learning_mode": "MENTAL_ROUTINE",
        "preview": {
            "title": "The Doorway Reset",
            "action_text": "Touch the doorframe to mentally 'leave' stress outside the classroom."
        },
        "details": {
            "objective": "To prevent home stress from affecting teaching (and vice versa).",
            "steps": [
                "Pick a physical object (school gate or classroom door).",
                "Decide: 'When I cross this, I leave my home worries behind.'",
                "On the way out: 'When I cross this, I leave my school worries here.'",
                "Physically touch the frame to anchor the habit."
            ],
            "time_required_min": 1,
            "materials_needed": ["None"],
            "teacher_tone": "Self-reflective"
        },
        "pedagogy": {
            "why_it_works": "Cognitive compartmentalization reduces emotional exhaustion.",
            "cognitive_target": "mindfulness"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "wb_positive_file",
        "version": "1.0",
        "status": "active",
        "situations": ["LOW_MORALE", "DEPRESSION"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "MOTIVATION",
        "learning_mode": "VISUAL",
        "preview": {
            "title": "The 'Sunny Day' File",
            "action_text": "Keep a folder of thank-you notes and good drawings for bad days."
        },
        "details": {
            "objective": "To counteract negativity bias on tough days.",
            "steps": [
                "Create a folder (physical or on phone) named 'Sunny Day'.",
                "Save every thank-you note, good student drawing, or compliment.",
                "When you feel like a failure, open the file and read 3 items.",
                "Remind yourself of your impact."
            ],
            "time_required_min": 5,
            "materials_needed": ["Folder/Phone"],
            "teacher_tone": "Self-compassionate"
        },
        "pedagogy": {
            "why_it_works": "External evidence of success helps fight imposter syndrome and burnout.",
            "cognitive_target": "emotional_resilience"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    },
    {
        "solution_id": "wb_micro_mindfulness",
        "version": "1.0",
        "status": "active",
        "situations": ["HIGH_ANXIETY", "OVERWHELM"],
        "subjects": ["GENERAL"],
        "class_range": "ALL",
        "topic_type": "STRESS_MANAGEMENT",
        "learning_mode": "SOMATIC",
        "preview": {
            "title": "5-4-3-2-1 Grounding",
            "action_text": "Use your senses to stop a panic attack or high stress moment."
        },
        "details": {
            "objective": "To immediately lower cortisol levels during a chaotic day.",
            "steps": [
                "Stop and take a deep breath.",
                "Name 5 things you see.",
                "Name 4 things you can feel (e.g., chalk, table).",
                "Name 3 things you hear.",
                "Name 2 things you smell.",
                "Name 1 good thing about yourself."
            ],
            "time_required_min": 2,
            "materials_needed": ["None"],
            "teacher_tone": "Calm"
        },
        "pedagogy": {
            "why_it_works": "Forces the brain to switch from 'Fight or Flight' (Amygdala) to 'Observation' (Prefrontal Cortex).",
            "cognitive_target": "grounding"
        },
        "effort_level": EFFORT_LEVELS["LOW"],
        "classroom_safety": SAFETY_LEVELS["HIGH"]
    }
]