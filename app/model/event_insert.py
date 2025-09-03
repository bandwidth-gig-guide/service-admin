from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime
from app.model.event_price import EventPrice
from app.model.event_venue import EventVenue
from app.model.event_performance_insert import EventPerformanceInsert
from app.model.social import Social
from app.model.image_insert import ImageInsert

class EventInsert(BaseModel):
    Title: str
    Description: str
    StartDateTime: datetime
    OriginalPostURL: HttpUrl
    TicketSaleURL: HttpUrl
    Images: Optional[List[ImageInsert]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    Venue: EventVenue
    Performances: List[EventPerformanceInsert]
    Prices: List[EventPrice]