from pydantic import BaseModel, HttpUrl

class SocialInsert(BaseModel):
    SocialPlatform: str
    Handle: str
    Url: HttpUrl
