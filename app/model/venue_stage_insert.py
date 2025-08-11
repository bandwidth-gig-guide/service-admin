from pydantic import BaseModel

class VenueStageInsert(BaseModel):
    title: str
    description: str
    capacity: int