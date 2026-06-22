from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def ask_company(company, role, context, question):

    prompt = f"""
You are an interview preparation assistant.

Company: {company}
Role: {role}

Company Research:
{context}

User Question:
{question}

Answer using the company profile.
Be specific.
Format nicely.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content