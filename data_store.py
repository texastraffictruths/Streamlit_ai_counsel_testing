import json

DATA_FILE = "cases_data.json"

def save_cases(cases):
    with open(DATA_FILE, "w") as f:
        json.dump(cases, f)

def load_cases():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
