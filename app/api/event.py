from fastapi import APIRouter, Query

from typing import Optional
from uuid import UUID
from datetime import date
from app.model.event import Event

from app.rest.event.get import get_complete
from app.rest.event.get_all_id import get_all_id


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