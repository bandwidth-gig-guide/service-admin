from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from app.model.social_insert import SocialInsert
from app.model.venue_stage_insert import VenueStageInsert as Stage
from app.model.opening_hours import OpeningHours as Hours


class VenueInsert(BaseModel):
    Title: str
    City: str
    StateCode: str
    StreetAddress: str
    PostCode: int
    Description: str
    WebsiteUrl: Optional[HttpUrl]
    PhoneNumber: str
    GoogleMapsEmbedUrl: HttpUrl
    ImageUrls: List[HttpUrl] = []
    Socials: Optional[List[SocialInsert]] = []
    Types: Optional[List[str]] = []
    Tags: Optional[List[str]] = []
    VenueStages: List[Stage]
    OpeningHours: Optional[Hours] = None
