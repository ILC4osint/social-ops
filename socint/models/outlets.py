import datetime
from pydantic import BaseModel

class SocialMediaOutlet(BaseModel):
    name: str
    base_url: str
    search_endpoint: str
class SocPost(BaseModel):
    content: str
    comments: int
    timestamp: datetime.datetime
class Twit(SocPost):
    content: str
    retweets: int
class FbPost(BaseModel):
    content: str
