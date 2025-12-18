from fastapi import APIRouter, Query, status, Body
from typing import Optional
from uuid import UUID
from app.model.artist import Artist
from app.model.artist_insert import ArtistInsert
from app.cache.redis import make_key, cache_wrap, invalidate_cache
from app.cache.key import RECORD, ARTIST

from app.rest.artist.get import get_complete
from app.rest.artist.get_all_id import get_all_id
from app.rest.artist.get_all_id_and_title import get_all_id_and_title
from app.rest.artist.get_all_id_and_title_where_unresearched import get_all_id_and_title_where_unresearched
from app.rest.artist.post import post
from app.rest.artist.put import put
from app.rest.artist.delete import delete

artist = APIRouter()


# GET IDs and Title | Unresearched
@artist.get("/id-and-title/unresearched", response_model=list[dict])
def get_all_id_and_title_where_unresearched_():
    key = make_key(ARTIST.ADMIN_UNRESEARCHED)
    return cache_wrap(key, lambda: get_all_id_and_title_where_unresearched())


# GET IDs and Title
@artist.get("/id-and-title", response_model=list[dict])
def get_all_id_and_title_():
    key = make_key(ARTIST.ADMIN_ID_AND_TITLE)
    return cache_wrap(key, lambda: get_all_id_and_title())


# GET Single Complete
@artist.get("/{artist_id}", response_model=Artist)
def get_complete_(artist_id: UUID):
    key = make_key(ARTIST.ADMIN_DETAILED, record_id=str(artist_id))
    return cache_wrap(key, lambda: get_complete(artist_id))


# GET IDs | Filterable
@artist.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None),
    hasUpcomingPerformance: Optional[bool] = None,
):
    filters = {
        "name": name,
        "country": country,
        "city": city,
        "types": types,
        "tags": tags,
        "hasUpcomingPerformance": hasUpcomingPerformance,
    }
    key = make_key(ARTIST.ADMIN_IDS, **filters)
    return cache_wrap(key, lambda: get_all_id(**filters))


# POST
@artist.post("/", response_model=UUID, status_code=status.HTTP_201_CREATED)
def post_(artist: ArtistInsert = Body(...)):
    artist_id = post(artist)
    invalidate_cache(RECORD.ARTIST)
    return artist_id


# PUT
@artist.put("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_(artist_id: UUID, artist: ArtistInsert = Body(...)):
    put(artist_id, artist)
    invalidate_cache(RECORD.ARTIST, record_id=str(artist_id))


# DELETE
@artist.delete("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_(artist_id: UUID):
    delete(artist_id)
    invalidate_cache(RECORD.ARTIST, record_id=str(artist_id))
