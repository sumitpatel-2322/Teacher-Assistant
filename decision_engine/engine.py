from decision_engine.situations import detect_situation 
def process_input(raw_input: dict)-> dict:
    situation=detect_situation(raw_input["question"])
    return{
        "situation":situation,
        "class": raw_input["class"],
        "subject": raw_input["subject"],
        "topic": raw_input["topic"],
        "question": raw_input["question"]
    }