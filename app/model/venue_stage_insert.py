from pydantic import BaseModel, field_validator
from typing import Optional
from uuid import UUID

class VenueStageInsert(BaseModel):
    StageID: Optional[UUID] = None
    Title: str
    Description: str
    Capacity: int

    @field_validator("StageID", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        return None if v == "" else v
