from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class EventBrief(BaseModel):
    eventId: UUID
    title: str
    startDateTime: datetime
    venueTitle: str
    isFeatured: bool
    imageUrl: Optional[HttpUrl] = None
    artistTitles: List[str]
    minPrice: int

def format(tuple: tuple) -> EventBrief:
    return EventBrief (
        eventId = tuple[0],
        title = tuple[1],
        startDateTime = tuple[2],
        venueTitle = tuple[3],
        isFeatured = tuple[4],
        imageUrl = tuple[5],
        artistTitles = tuple[6],
        minPrice = tuple[7]
    )