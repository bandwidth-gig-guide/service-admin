from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social

class Artist(BaseModel):
    artistId: UUID
    title: str
    country: str
    city: str
    stateCode: str
    yearFounded: int
    description: str
    spotifyEmbedUrl: Optional[HttpUrl] = None
    youtubeEmbedUrl: Optional[HttpUrl] = None
    isFeatured: bool
    imageUrls: Optional[List[HttpUrl]] = None
    socials: Optional[List[Social]] = None
    types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    upcomingEventIds: Optional[List[UUID]] = None

def format(tuple: tuple) -> Artist:
    return Artist(
        artistId=tuple[0],
        title=tuple[1],
        country=tuple[2],
        city=tuple[3],
        stateCode=tuple[4],
        yearFounded=tuple[5],
        description=tuple[6],
        spotifyEmbedUrl=tuple[7],
        youtubeEmbedUrl=tuple[8],
        isFeatured=tuple[9],
        imageUrls=tuple[10] or [],
        socials=tuple[11] or [],
        types=tuple[12] or [],
        tags=tuple[13] or [],
        upcomingEventIds=tuple[14] or []
    )