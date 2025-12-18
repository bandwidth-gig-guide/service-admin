from fastapi import APIRouter, Query, Body, status

from typing import Optional
from uuid import UUID
from app.model.venue import Venue
from app.model.venue_insert import VenueInsert
from app.cache.redis import make_key, cache_wrap, invalidate_cache
from app.cache.key import RECORD, VENUE

from app.rest.venue.get import get_complete
from app.rest.venue.get_all_id import get_all_id
from app.rest.venue.get_all_id_and_title import get_all_id_and_title
from app.rest.venue.post import post
from app.rest.venue.put import put
from app.rest.venue.delete import delete

venue = APIRouter()


# GET IDs and Title
@venue.get("/id-and-title", response_model=list[dict])
def get_all_id_and_title_():
    key = make_key(VENUE.ADMIN_IDS)
    return cache_wrap(key, lambda: get_all_id_and_title())


# GET
@venue.get("/{venue_id}", response_model=Venue)
def get_complete_(venue_id: UUID):
    key = make_key(VENUE.ADMIN_DETAILED, record_id=str(venue_id))
    return cache_wrap(key, lambda: get_complete(venue_id))


# GET IDs | Filterable
@venue.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[list[str]] = Query(default=None),
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None)
):
    filters = {
        "name": name,
        "stateCode": stateCode,
        "city": city,
        "types": types,
        "tags": tags,
    }
    key= make_key(VENUE.IDS, **filters)
    return cache_wrap(key, lambda: get_all_id(**filters))


# POST
@venue.post("/", response_model=UUID, status_code=status.HTTP_201_CREATED)
def post_(venue: VenueInsert = Body(...)):
    venue_id = post(venue)
    invalidate_cache(RECORD.VENUE)
    return venue_id


# PUT
@venue.put("/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_(venue_id: UUID, venue: VenueInsert = Body(...)):
    put(venue_id, venue)
    invalidate_cache(RECORD.VENUE, record_id=str(venue_id))


# DELETE
@venue.delete("/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_(venue_id: UUID):
    delete(venue_id)
    invalidate_cache(RECORD.VENUE, record_id=str(venue_id))