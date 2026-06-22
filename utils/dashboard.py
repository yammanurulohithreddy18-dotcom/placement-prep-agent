from utils.history import get_history


def get_dashboard_data():
    history = get_history()

    if not history:
        return {
            "attempts": 0,
            "avg_score": 0,
            "best_score": 0,
            "worst_score": 0
        }

    scores = [item["score"] for item in history]

    return {
        "attempts": len(scores),
        "avg_score": round(sum(scores) / len(scores), 2),
        "best_score": max(scores),
        "worst_score": min(scores)
    }