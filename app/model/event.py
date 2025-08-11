from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from app.model.event_price import EventPrice
from app.model.event_venue import EventVenue
from app.model.event_performance import EventPerformance
from app.model.social import Social

class Event(BaseModel):
    eventId: UUID
    title: str
    startDateTime: datetime
    description: str
    originalPostUrl: HttpUrl
    ticketSaleUrl: HttpUrl
    isFeatured: bool
    imageUrls: Optional[List[HttpUrl]] = None
    socials: Optional[List[Social]] = None
    types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    venue: EventVenue
    performances: List[EventPerformance]
    prices: List[EventPrice]

def format(tuple: tuple) -> Event:
    return Event (
        eventId = tuple[0],
        title = tuple[1],
        startDateTime = tuple[2],
        description = tuple[3],
        originalPostUrl = tuple[4],
        ticketSaleUrl = tuple[5],
        isFeatured = tuple[6],
        imageUrls = tuple[7] or [],
        socials = tuple[8] or [],
        types = tuple[9] or [],
        tags = tuple[10] or [],
        venue = tuple[11],
        performances = tuple[12] or [],
        prices = tuple[13] or []
    )
