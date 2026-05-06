import csv
import json

def load_csv(path):
    contacts = []
    try:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append({
                    "name": row.get("name", ""),
                    "email": row.get("email", "").lower(),
                    "company": row.get("company", "")
                })
        return contacts
    except Exception as e:
        print("Error loading CSV:", e)
        return []


def load_json(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            for user in data:
                user["email"] = user.get("email", "").lower()
            return data
    except Exception as e:
        print("Error loading JSON:", e)
        return []