from pydantic import BaseModel
from uuid import UUID

class VenueStage(BaseModel):
    stageId: UUID
    title: str
    description: str
    capacity: int