from datetime import datetime
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)


def store_raw_input(
    username: str,
    role: str,
    class_name: str,
    subject: str,
    topic: str,
    question: str
):
    timestamp = datetime.now().isoformat(timespec="seconds")

    filename = f"{timestamp.replace(':', '-')}_{username}.txt"
    file_path = os.path.join(DATA_DIR, filename)

    content = f"""timestamp: {timestamp}
role: {role}
username: {username}

class: {class_name}
subject: {subject}
topic: {topic}

question:
{question}
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path
