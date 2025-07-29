from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EventPerformanceInsert(BaseModel):
    ArtistID: UUID
    SetListPosition: int
    StartDateTime: datetime
    EndDateTime: datetime