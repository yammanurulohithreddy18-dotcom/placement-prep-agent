import json
import os
from datetime import datetime

USAGE_FILE = "usage.json"

TOKEN_LIMIT = 1000
DAILY_LIMIT = 50000

PRICE_PER_1K_TOKENS = 0.003


def load_usage():
    if not os.path.exists(USAGE_FILE):
        data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "tokens_used": 0
        }

        with open(USAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)

        return data

    with open(USAGE_FILE, "r") as f:
        data = json.load(f)

    today = datetime.now().strftime("%Y-%m-%d")

    if data.get("date") != today:
        data = {
            "date": today,
            "tokens_used": 0
        }

        with open(USAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    return data


def save_usage(data):
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def check_token_limit(tokens_requested):
    usage = load_usage()

    if usage["tokens_used"] + tokens_requested > TOKEN_LIMIT:
        return False

    usage["tokens_used"] += tokens_requested
    save_usage(usage)

    return True


def add_tokens(tokens):
    usage = load_usage()
    usage["tokens_used"] += tokens
    save_usage(usage)


def get_tokens_used():
    return load_usage()["tokens_used"]


def get_remaining_tokens():
    usage = load_usage()
    return TOKEN_LIMIT - usage["tokens_used"]


def get_cost():
    usage = load_usage()
    return round(
        (usage["tokens_used"] / 1000) * PRICE_PER_1K_TOKENS,
        6
    )