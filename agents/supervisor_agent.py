from agents.research_agent import research_company
from agents.question_agent import generate_questions
from agents.feedback_agent import evaluate_answer


def run_research(company: str, role: str):

    try:
        return research_company(company, role)

    except Exception as e:
        print(f"Supervisor Research Error: {e}")
        raise


def run_questions(profile, role: str):

    try:
        return generate_questions(profile, role)

    except Exception as e:
        print(f"Supervisor Question Error: {e}")
        raise


def run_feedback(question: str, answer: str):

    try:
        return evaluate_answer(question, answer)

    except Exception as e:
        print(f"Supervisor Feedback Error: {e}")
        raise