from pydantic import BaseModel, HttpUrl

class SocialInsert(BaseModel):
    socialPlatform: str
    handle: str
    url: HttpUrl
