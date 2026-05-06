import json
from datetime import datetime
import os

FILE = "data/history.json"

def save_history(email, subject, status):
    record = {
        "email": email,
        "subject": subject,
        "status": status,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if not os.path.exists(FILE):
        data = []
    else:
        with open(FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.append(record)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def view_history():
    if not os.path.exists(FILE):
        print("No history found.")
        return

    with open(FILE, "r") as f:
        data = json.load(f)
        for item in data:
            print(item)