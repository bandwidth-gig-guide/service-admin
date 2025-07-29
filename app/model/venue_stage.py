from pydantic import BaseModel
from uuid import UUID

class VenueStage(BaseModel):
    StageID: UUID
    Title: str
    Description: str
    Capacity: int