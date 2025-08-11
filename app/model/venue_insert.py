from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from app.model.social_insert import SocialInsert
from app.model.venue_stage_insert import VenueStageInsert as Stage
from app.model.opening_hours import OpeningHours as Hours


class VenueInsert(BaseModel):
    title: str
    city: str
    stateCode: str
    streetAddress: str
    postCode: int
    description: str
    websiteUrl: Optional[HttpUrl]
    phoneNumber: str
    googleMapsEmbedUrl: HttpUrl
    imageUrls: List[HttpUrl] = []
    socials: Optional[List[SocialInsert]] = []
    types: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    venueStages: List[Stage]
    openingHours: Optional[Hours] = None
