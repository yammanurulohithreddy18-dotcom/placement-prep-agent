from pydantic import BaseModel
from typing import List


class CompanyProfile(BaseModel):
    company_name: str
    founded: str
    headquarters: str
    tech_stack: List[str]
    interview_rounds: List[str]
    key_topics: List[str]
    difficulty: str