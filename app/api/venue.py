from fastapi import APIRouter, Query

from typing import Optional
from uuid import UUID
from app.model.venue import Venue

from app.rest.venue.get import get_complete
from app.rest.venue.get_all_id import get_all_id


venue = APIRouter()


# GET
@venue.get("/{venue_id}", response_model=Venue)
def get_complete_(venue_id: UUID):
    return get_complete(venue_id)

# GET IDs | Filterable
@venue.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[list[str]] = Query(default=None),
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None)
):
    return get_all_id(
        name=name,
        stateCode=stateCode,
        city=city,
        types=types,
        tags=tags
    )