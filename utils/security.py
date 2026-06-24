import re

MAX_COMPANY_LENGTH = 100

PROMPT_INJECTION_PATTERNS = [
    "ignore all previous instructions",
    "forget previous instructions",
    "system prompt",
    "reveal your prompt",
    "act as",
    "bypass",
    "jailbreak",
    "developer message",
]

def validate_company_input(company: str):
    if not company:
        return False, "Company name cannot be empty."

    if len(company) > MAX_COMPANY_LENGTH:
        return False, "Company name must be under 100 characters."

    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern.lower() in company.lower():
            return False, "Potential prompt injection detected."

    if re.search(r"(DROP TABLE|SELECT \*|DELETE FROM|INSERT INTO)", company, re.I):
        return False, "SQL-like input detected."

    return True, ""