from tenacity import retry, stop_after_attempt, wait_fixed
import json

from langchain_groq import ChatGroq

from models.company_profile import CompanyProfile
from rag.vectordb import collection

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def research_company(company: str, role: str):

    response = llm.invoke(
        f"""
Research {company} for a {role} interview.

Return ONLY valid JSON.

{{
    "company_name": "{company}",
    "founded": "year",
    "headquarters": "location",
    "tech_stack": [],
    "interview_rounds": [],
    "key_topics": [],
    "difficulty": "Easy/Medium/Hard"
}}
"""
    )

    summary = response.content

    print("\nAI RESPONSE:\n")
    print(summary)

    summary = summary.replace("```json", "")
    summary = summary.replace("```", "")
    summary = summary.strip()

    try:
        data = json.loads(summary)

    except Exception as e:

        print(f"Research Agent Error: {e}")

        data = {
            "company_name": company,
            "founded": "Unknown",
            "headquarters": "Unknown",
            "tech_stack": [],
            "interview_rounds": [],
            "key_topics": [],
            "difficulty": "Medium"
        }

    profile = CompanyProfile(
        company_name=data.get("company_name", company),
        founded=str(data.get("founded", "Unknown")),
        headquarters=data.get("headquarters", "Unknown"),
        tech_stack=data.get("tech_stack", []),
        interview_rounds=data.get("interview_rounds", []),
        key_topics=data.get("key_topics", []),
        difficulty=data.get("difficulty", "Medium")
    )

    try:
        collection.add(
            documents=[
                f"""
Company: {profile.company_name}
Founded: {profile.founded}
Headquarters: {profile.headquarters}
Tech Stack: {', '.join(profile.tech_stack)}
Interview Rounds: {', '.join(profile.interview_rounds)}
Key Topics: {', '.join(profile.key_topics)}
Difficulty: {profile.difficulty}
"""
            ],
            ids=[profile.company_name]
        )
    except Exception:
        pass

    return profile