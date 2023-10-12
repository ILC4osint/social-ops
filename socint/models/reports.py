import datetime
from pydantic import BaseModel

class Report(BaseModel):
    flagged_content: str
    timestamp: datetime.datetime
    evidence: str
