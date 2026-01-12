from pathlib import Path
from datetime import datetime
import pandas as pd

# -------------------------
# Paths
# -------------------------

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "decision_logs.csv"

COLUMNS = [
    "request_id",
    "timestamp",
    "raw_query",
    "situations",
    "constraints",
    "solutions_shown",
    "solution_chosen",
    "worked",
    "feedback"
]


# -------------------------
# Helpers
# -------------------------

def _ensure_log_file():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(LOG_FILE, index=False)


# -------------------------
# Decision logging (initial)
# -------------------------

def log_decision(
    request_id: str,
    raw_query: str,
    situations: dict,
    constraints: dict,
    solutions_shown: list,
    solution_chosen: str = None,
    worked: bool = None,
    feedback: str = None
):
    """
    Logs initial decision output.
    """

    try:
        _ensure_log_file()

        row = {
            "request_id":request_id,
            "timestamp": datetime.utcnow().isoformat(),
            "raw_query": raw_query,
            "situations": str(situations),
            "constraints": str(constraints),
            "solutions_shown": str(solutions_shown),
            "solution_chosen": solution_chosen,
            "worked": worked,
            "feedback": feedback
        }

        pd.DataFrame([row]).to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )

    except Exception:
        pass


# -------------------------
# Feedback logging (NEW)
# -------------------------

def log_feedback(
    request_id:str,
    solution_chosen: str,
    worked: bool,
    feedback: str = None
):
    """
    Updates the most recent log row with teacher feedback.
    """

    try:
        if not LOG_FILE.exists():
            return

        df = pd.read_csv(LOG_FILE)

        if df.empty:
            return

        match = df["request_id"] == request_id
        if not match.any():
            return

        idx = df[match].index[-1]

        df.at[idx, "solution_chosen"] = solution_chosen
        df.at[idx, "worked"] = worked
        df.at[idx, "feedback"] = feedback

        df.to_csv(LOG_FILE, index=False)

    except Exception:
        pass