from fastapi import APIRouter, Query, Body, status

from typing import Optional
from uuid import UUID
from datetime import date
from app.model.event import Event
from app.model.event_insert import EventInsert

from app.rest.event.get import get_complete
from app.rest.event.get_all_id import get_all_id
from app.rest.event.post import post
from app.rest.event.put import put
from app.rest.event.delete import delete


event = APIRouter()

# GET
@event.get("/{event_id}", response_model=Event)
def get_complete_(event_id: UUID):
    return get_complete(event_id)

# GET IDs | Filterable
@event.get("/", response_model=list[UUID])
def get_all_id_(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[list[str]] = Query(default=None),
    maxPrice: Optional[int] = None,
    types: Optional[list[str]] = Query(default=None),
    tags: Optional[list[str]] = Query(default=None),
    dates: Optional[list[date]] = Query(default=None)
):
    return get_all_id(
        name=name,
        stateCode=stateCode,
        city=city,
        maxPrice=maxPrice,
        types=types,
        tags=tags,
        dates=dates
    )

# POST
@event.post("/", response_model=UUID, status_code=status.HTTP_201_CREATED)
def post_(event: EventInsert = Body(...)):
    return post(event)

# PUT
@event.put("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def put_(event_id: UUID, event: EventInsert = Body(...)):
    return put(event_id, event)

# DELETE
@event.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_(event_id: UUID):
    return delete(event_id)