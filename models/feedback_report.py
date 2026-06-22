from pydantic import BaseModel
from typing import List


class FeedbackReport(BaseModel):
    score: int
    strengths: List[str]
    improvements: List[str]