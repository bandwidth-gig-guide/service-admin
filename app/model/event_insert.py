from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from app.model.event_price import EventPrice
from app.model.event_performance_insert import EventPerformanceInsert
from app.model.social import Social

class EventInsert(BaseModel):
    VenueID: UUID
    StageID: UUID
    Title: str
    Description: str
    StartDateTime: datetime
    EndDateTime: datetime
    OriginalPostUrl: HttpUrl
    TicketSaleUrl: HttpUrl
    ImageUrls: Optional[List[HttpUrl]] = None
    Socials: Optional[List[Social]] = None
    Types: Optional[List[str]] = None
    Tags: Optional[List[str]] = None
    Performances: List[EventPerformanceInsert]
    Prices: List[EventPrice]