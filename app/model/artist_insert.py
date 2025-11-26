from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from app.model.social_insert import SocialInsert
from app.model.image_insert import ImageInsert

class ArtistInsert(BaseModel):
    Title: str
    Country: str
    City: str
    StateCode: str
    YearFounded: int
    Description: str
    SpotifyEmbedURL: Optional[HttpUrl] = None
    YoutubeEmbedURL: Optional[HttpUrl] = None
    IsFeatured: bool
    Images: Optional[List[ImageInsert]] = None
    Socials: Optional[List[SocialInsert]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
