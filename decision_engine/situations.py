def detect_situation(question: str) -> str:
    q = question.lower()

    if any(word in q for word in [
        "not responding", "no response", "noise", "chaos", "not listening","not paying attention"
        "attention", "discipline", "silent class"
    ]):
        return "ATTENTION_AND_DISCIPLINE_BREAKDOWN"

    if any(word in q for word in [
        "no time", "running out of time", "short period",
        "syllabus pressure", "time left"
    ]):
        return "TIME_PRESSURE_SITUATION"

    if any(word in q for word in [
        "not understanding", "confused", "concept", "difficult",
        "clarify", "misunderstood"
    ]):
        return "CONCEPTUAL_CONFUSION"

    if any(word in q for word in [
        "activity failed", "didn't work", "group work failed",
        "students confused during activity"
    ]):
        return "ACTIVITY_FAILURE"

    if any(word in q for word in [
        "projector", "internet", "mic", "speaker",
        "technical issue", "power cut"
    ]):
        return "TECHNICAL_BREAKDOWN"

    if any(word in q for word in [
        "special needs", "aggressive", "withdrawn",
        "emotional", "isolated student"
    ]):
        return "STUDENT_BEHAVIOR_EDGE_CASE"

    return "UNCLASSIFIED"
