from datetime import datetime


LOG_FILE = "memory/agent_logs.txt"


def log_agent(agent_name, action):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LOG_FILE, "a") as f:
        f.write(
            f"[{timestamp}] "
            f"{agent_name}: "
            f"{action}\n"
        )