from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from app.model.social_insert import SocialInsert
from app.model.venue_stage_insert import VenueStageInsert as Stage
from app.model.opening_hours import OpeningHours as Hours
from app.model.image_insert import ImageInsert


class VenueInsert(BaseModel):
    Title: str
    City: str
    StateCode: str
    StreetAddress: str
    PostCode: int
    Description: str
    WebsiteURL: Optional[HttpUrl]
    PhoneNumber: str
    GoogleMapsEmbedURL: HttpUrl
    IsFeatured: bool = False
    IsMonitored: bool = False
    Images: List[ImageInsert] = []
    Socials: Optional[List[SocialInsert]] = []
    Types: Optional[List[str]] = []
    Tags: Optional[List[str]] = []
    VenueStages: List[Stage]
    OpeningHours: Optional[Hours] = None
