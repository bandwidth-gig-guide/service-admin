from pydantic import BaseModel, HttpUrl
from uuid import UUID

class EventVenueInsert(BaseModel):
    VenueID: UUID
    Title: str
    StageID: UUID
    StageTitle: str
    ImageURL: HttpUrl
