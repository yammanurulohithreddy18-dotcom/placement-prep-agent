from tenacity import retry, stop_after_attempt, wait_fixed
import json

from langchain_groq import ChatGroq

from models.question_set import QuestionSet

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def generate_questions(profile, role: str):

    response = llm.invoke(
        f"""
Generate 10 interview questions for a {role} position.

Company: {profile.company_name}

Tech Stack:
{", ".join(profile.tech_stack)}

Interview Rounds:
{", ".join(profile.interview_rounds)}

Key Topics:
{", ".join(profile.key_topics)}

Difficulty:
{profile.difficulty}

Create:
- 3 DSA questions
- 3 System Design questions
- 2 Leadership Principle questions
- 2 Behavioral questions

Return ONLY JSON.

Example:

{{
    "questions":[
        "Question 1",
        "Question 2"
    ]
}}
"""
    )

    content = response.content

    print("\nQUESTION AGENT RESPONSE:\n")
    print(content)

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:

        data = json.loads(content)

        return QuestionSet(
            company_name=profile.company_name,
            role=role,
            questions=data["questions"]
        )

    except Exception as e:

        print(f"Question Agent Error: {e}")

        return QuestionSet(
            company_name=profile.company_name,
            role=role,
            questions=[
                "Tell me about yourself.",
                "Explain a challenging project.",
                "What are your strengths?",
                "What are your weaknesses?",
                "Why do you want this role?"
            ]
        )