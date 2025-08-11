from pydantic import BaseModel, HttpUrl
from uuid import UUID

class EventVenue(BaseModel):
    venueId: UUID
    title: str
    stageId: UUID
    stageTitle: str
    imageUrl: HttpUrl
