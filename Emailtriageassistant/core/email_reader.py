import json
import os

def load_emails():
    file_path = os.path.join("data", "sample_emails.json")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
