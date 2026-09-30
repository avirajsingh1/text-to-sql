from typing import Literal
from pydantic import BaseModel

class QueryAnalysis(BaseModel):
    status: Literal["clear","needs clarification"]
    
    reason: str | None
    
    missing_information: list[str]
    
    clarification_question: str #| None