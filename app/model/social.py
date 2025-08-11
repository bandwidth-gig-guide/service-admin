from pydantic import BaseModel, HttpUrl

class Social(BaseModel):
    socialPlatform: str
    handle: str
    url: HttpUrl