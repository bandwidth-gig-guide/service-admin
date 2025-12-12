from app.query.execute_with_return import execute as execute_with_return
from app.db.connection import get_db_connection
from psycopg2 import DatabaseError

from app.rest.event.secondary_tables.post_event_type import post_event_type
from app.rest.event.secondary_tables.post_event_tag import post_event_tag
from app.rest.event.secondary_tables.post_event_social import post_event_social
from app.rest.event.secondary_tables.post_event_image import post_event_image
from app.rest.event.secondary_tables.post_event_price import post_event_price
from app.rest.event.secondary_tables.post_event_performance import post_event_performance

from app.model.event_insert import EventInsert
from uuid import UUID


def post(event: EventInsert) -> UUID:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                event_id: UUID = post_event(event, connection, cursor)
                post_event_type(event.Types, event_id, connection, cursor)
                post_event_tag(event.Tags, event_id, connection, cursor)
                post_event_social(event.Socials, event_id, connection, cursor)
                post_event_image(event.Images, event_id, connection, cursor)
                post_event_price(event.Prices, event_id, connection, cursor)
                post_event_performance(event.Performances, event_id, connection, cursor)
                connection.commit()
                return event_id
            except DatabaseError:
                connection.rollback()
                raise


def post_event(event: EventInsert, connection, cursor) -> UUID:
    response = execute_with_return(
    """
        INSERT INTO Event (
            VenueID,
            StageID,
            Title,
            Description,
            StartDateTime,
            OriginalPostURL,
            TicketSaleURL,
            IsFeatured
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING EventID
    """,
        (
            str(event.Venue.VenueID),
            str(event.Venue.StageID),
            event.Title,
            event.Description,
            event.StartDateTime,
            str(event.OriginalPostURL),
            str(event.TicketSaleURL),
            event.IsFeatured if event.IsFeatured else False
        ),       
        connection=connection,
        cursor=cursor
    )
    return response[0]