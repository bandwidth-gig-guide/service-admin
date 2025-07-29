from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from app.model.social_insert import SocialInsert

class ArtistInsert(BaseModel):
    Title: str
    Country: str
    City: str
    StateCode: str
    YearFounded: int
    Description: str
    SpotifyEmbedURL: Optional[HttpUrl] = None
    YoutubeEmbedURL: Optional[HttpUrl] = None
    ImageUrls: Optional[List[HttpUrl]] = None
    Socials: Optional[List[SocialInsert]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
