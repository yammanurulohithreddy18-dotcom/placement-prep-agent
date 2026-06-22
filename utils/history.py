import json
from pathlib import Path

HISTORY_FILE = "memory/interview_history.json"
PROFILE_FILE = "memory/company_profiles.json"


def ensure_file(file_path):
    if not Path(file_path).exists():
        with open(file_path, "w") as f:
            json.dump([], f)


def load_json(file_path):
    ensure_file(file_path)

    with open(file_path, "r") as f:
        return json.load(f)


def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------
# Interview History
# -------------------------

def save_attempt(company, role, question, score):

    data = load_json(HISTORY_FILE)

    data.append({
        "company": company,
        "role": role,
        "question": question,
        "score": score
    })

    save_json(HISTORY_FILE, data)


def get_history():
    return load_json(HISTORY_FILE)


# -------------------------
# Company Profiles
# -------------------------

def save_company_profile(profile):

    data = load_json(PROFILE_FILE)

    company_name = profile.company_name.lower()

    exists = any(
        item["company"].lower() == company_name
        for item in data
    )

    if exists:
        return

    data.append({
        "company": profile.company_name,
        "founded": profile.founded,
        "headquarters": profile.headquarters,
        "tech_stack": profile.tech_stack,
        "difficulty": profile.difficulty,
        "rounds": profile.interview_rounds,
        "topics": profile.key_topics,
        "tips": profile.key_topics[:3]
    })

    save_json(PROFILE_FILE, data)


def get_company_profiles():
    return load_json(PROFILE_FILE)


def get_company_profile(company_name):

    profiles = get_company_profiles()

    for profile in profiles:

        if profile["company"].lower() == company_name.lower():
            return profile

    return None