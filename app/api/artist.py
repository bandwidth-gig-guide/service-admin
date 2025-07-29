from fastapi import APIRouter, Query, status, Body

from typing import Optional
from uuid import UUID
from app.model.artist import Artist
from app.model.artist_insert import ArtistInsert

from app.rest.artist.get import get_complete
from app.rest.artist.get_all_id import get_all_id
from app.rest.artist.post import post
from app.rest.artist.delete import delete


artist = APIRouter()


# GET
@artist.get("/{artist_id}", response_model=Artist)
def get_complete_(artist_id: UUID):
    return get_complete(artist_id)

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
    return get_all_id(
        name=name,
        country=country,
        city=city,
        types=types,
        tags=tags,
        hasUpcomingPerformance=hasUpcomingPerformance,
    )

# POST
@artist.post("/", response_model=UUID, status_code=status.HTTP_201_CREATED)
def post_(artist: ArtistInsert = Body(...)):
    return post(artist)

# DELETE
@artist.delete("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_(artist_id: UUID):
    return delete(artist_id)