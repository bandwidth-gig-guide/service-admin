from pydantic import BaseModel, HttpUrl

class ImageInsert(BaseModel):
    Url: HttpUrl
    DisplayOrder: int