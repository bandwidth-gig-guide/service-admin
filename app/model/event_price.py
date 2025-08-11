from pydantic import BaseModel

class EventPrice(BaseModel):
    ticketType: str
    price: int
