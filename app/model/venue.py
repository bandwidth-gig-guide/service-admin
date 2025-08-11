from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from app.model.social import Social
from app.model.opening_hours import OpeningHours as Hours
from app.model.venue_stage import VenueStage as Stage

class Venue(BaseModel):
    venueId: UUID
    title: str
    city: str
    stateCode: str
    streetAddress: str
    postCode: int
    description: str
    websiteUrl: HttpUrl
    phoneNumber: str
    googleMapsEmbedUrl: Optional[HttpUrl] = None
    isFeatured: bool
    imageUrls: Optional[List[HttpUrl]] = None
    socials: Optional[List[Social]] = None
    types: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    openingHours: Optional[Hours] = None
    upcomingEventIds: Optional[List[UUID]] = None
    venueStages: List[Stage]

def format(tuple: tuple) -> Venue:
    return Venue (
        venueId = tuple[0],
        title = tuple[1],
        city = tuple[2],
        stateCode = tuple[3],
        streetAddress = tuple[4],
        postCode = tuple[5],
        description = tuple[6],
        websiteUrl = tuple[7],
        phoneNumber = tuple[8],
        googleMapsEmbedUrl = tuple[9],
        isFeatured = tuple[10],
        imageUrls = tuple[11] or [],
        socials = tuple[12] or [],
        types = tuple[13] or [],
        tags = tuple[14] or [],
        openingHours = tuple[15],
        upcomingEventIds = tuple[16] or [],
        venueStages = tuple[17]
    )
