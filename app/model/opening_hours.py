from pydantic import BaseModel
from datetime import time

class OpeningHours(BaseModel):
    monOpen: time
    monClose: time
    tueOpen: time
    tueClose: time
    wedOpen: time
    wedClose: time
    thurOpen: time
    thurClose: time
    friOpen: time
    friClose: time
    satOpen: time
    satClose: time
    sunOpen: time
    sunClose: time