from agents.supervisor_agent import (
    run_research,
    run_questions
)

from agents.feedback_agent import run_feedback

from utils.logger import log_agent
from utils.history import get_company_profile

from models.company_profile import CompanyProfile


def company_workflow(company: str, role: str):

    cached = get_company_profile(company)

    if cached:

        log_agent(
            "Cache",
            f"Loaded {company} from cache"
        )

        profile = CompanyProfile(
            company_name=cached["company"],
            founded=cached["founded"],
            headquarters=cached["headquarters"],
            tech_stack=cached["tech_stack"],
            interview_rounds=cached["rounds"],
            key_topics=cached["topics"],
            difficulty=cached["difficulty"]
        )

        questions = run_questions(
            profile,
            role
        )

        return {
            "profile": profile,
            "questions": questions
        }

    log_agent(
        "ResearchAgent",
        f"Researching {company}"
    )

    profile = run_research(
        company,
        role
    )

    log_agent(
        "QuestionGeneratorAgent",
        f"Generating questions for {company}"
    )

    questions = run_questions(
        profile,
        role
    )

    return {
        "profile": profile,
        "questions": questions
    }


def feedback_workflow(
    question: str,
    answer: str
):

    log_agent(
        "FeedbackAgent",
        "Evaluating answer"
    )

    return run_feedback(
        question,
        answer
    )