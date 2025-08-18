from pydantic import BaseModel, HttpUrl
from uuid import UUID

class Image(BaseModel):
    ImageID: UUID
    Url: HttpUrl
    DisplayOrder: int