from tenacity import retry, stop_after_attempt, wait_fixed
import json

from langchain_groq import ChatGroq

from models.feedback_report import FeedbackReport

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def evaluate_answer(question: str, answer: str):

    response = llm.invoke(
        f"""
Evaluate this interview answer.

Question:
{question}

Answer:
{answer}

Return ONLY valid JSON.

Example:

{{
    "score": 8,
    "strengths": [
        "Clear communication",
        "Good technical explanation"
    ],
    "improvements": [
        "Add more details",
        "Use STAR format"
    ]
}}
"""
    )

    content = response.content

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:

        data = json.loads(content)

        return FeedbackReport(
            score=data["score"],
            strengths=data["strengths"],
            improvements=data["improvements"]
        )

    except Exception as e:

        print(f"Feedback Agent Error: {e}")

        return FeedbackReport(
            score=5,
            strengths=["Answer submitted"],
            improvements=["Could not evaluate automatically"]
        )


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def run_feedback(question, answer):
    return evaluate_answer(question, answer)