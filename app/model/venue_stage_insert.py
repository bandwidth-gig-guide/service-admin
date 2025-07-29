from pydantic import BaseModel

class VenueStageInsert(BaseModel):
    Title: str
    Description: str
    Capacity: int