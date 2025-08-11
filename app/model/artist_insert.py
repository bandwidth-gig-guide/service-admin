from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from app.model.social_insert import SocialInsert

class ArtistInsert(BaseModel):
    title: str
    country: str
    city: str
    stateCode: str
    yearFounded: int
    description: str
    spotifyEmbedUrl: Optional[HttpUrl] = None
    youtubeEmbedUrl: Optional[HttpUrl] = None
    imageUrls: Optional[List[HttpUrl]] = None
    socials: Optional[List[SocialInsert]] = None
    types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
