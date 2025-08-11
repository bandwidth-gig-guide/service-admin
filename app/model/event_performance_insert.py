from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EventPerformanceInsert(BaseModel):
    artistId: UUID
    setListPosition: int
    startDateTime: datetime
    endDateTime: datetime