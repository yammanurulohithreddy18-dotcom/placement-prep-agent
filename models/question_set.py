from pydantic import BaseModel
from typing import List


class QuestionSet(BaseModel):
    company_name: str
    role: str
    questions: List[str]