from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime
from app.model.event_price import EventPrice
from app.model.event_venue import EventVenue
from app.model.event_performance_insert import EventPerformanceInsert
from app.model.social import Social

class EventInsert(BaseModel):
    title: str
    description: str
    startDateTime: datetime
    endDateTime: datetime
    originalPostUrl: HttpUrl
    ticketSaleUrl: HttpUrl
    imageUrls: Optional[List[HttpUrl]] = None
    socials: Optional[List[Social]] = None
    types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    venue: EventVenue
    performances: List[EventPerformanceInsert]
    prices: List[EventPrice]