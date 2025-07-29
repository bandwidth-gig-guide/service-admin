from app.query.execute import execute
from app.model.event_price import EventPrice
from uuid import UUID
from typing import List

def post_event_price(prices: List[EventPrice], event_id: UUID, connection, cursor):
    if prices:
        for price in prices:
            execute(
            """
                INSERT INTO EventPrice (EventID, TicketType, Price)
                VALUES (%s, %s, %s)
            """,
                (str(event_id), price.TicketType, price.Price),
                connection=connection,
                cursor=cursor
            )