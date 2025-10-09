from app.query.execute import execute
from app.model.event_price import EventPrice
from app.rest.event.secondary_tables.post_event_price import post_event_price
from uuid import UUID
from typing import List

def put_event_price(prices: List[EventPrice], event_id: UUID, connection, cursor):
    execute(delete_existing_prices(), (str(event_id),), connection, cursor)
    post_event_price(prices, event_id, connection, cursor)
                

def delete_existing_prices(): 
    return """
        DELETE FROM EventPrice
        WHERE EventID = %s;
    """
    