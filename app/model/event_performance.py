from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime

class EventPerformance(BaseModel):
    artistId: UUID
    title: str
    imageUrl: HttpUrl
    setListPosition: int
    startDateTime: datetime