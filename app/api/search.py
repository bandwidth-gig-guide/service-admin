from fastapi import APIRouter, Query

from typing import Optional, List

from app.rest.search.get import get


search = APIRouter()

# GET
@search.get("/id-and-title", response_model=dict)
def get_(
    recordTypes: Optional[List[str]] = Query(default=None),
    searchString: Optional[str] = None, 
    limit: Optional[int] = 6
):
    return get(record_types=recordTypes, search_string=searchString, limit=limit)
