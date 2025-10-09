from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class VenueStageInsert(BaseModel):
    StageID: Optional[UUID]
    Title: str
    Description: str
    Capacity: int