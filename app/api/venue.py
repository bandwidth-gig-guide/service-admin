from fastapi import APIRouter, Query, Body, status

from typing import Optional
from uuid import UUID
from app.model.venue import Venue
from app.model.venue_insert import VenueInsert

from app.rest.venue.get import get_complete
from app.rest.venue.get_all_id import get_all_id
from app.rest.venue.post import post
from app.rest.venue.put import put
from app.rest.venue.delete import delete


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

# POST
@venue.post("/", response_model=UUID, status_code=status.HTTP_201_CREATED)
def post_(venue: VenueInsert = Body(...)):
    return post(venue)

# PUT
@venue.put("/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_(venue_id: UUID, venue: VenueInsert = Body(...)):
    return put(venue_id, venue)

# DELETE
@venue.delete("/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_(venue_id: UUID):
    return delete(venue_id)