from app.query.execute import execute
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


def put(event_id: UUID, event: EventInsert) -> None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                update_event(event_id, event, connection, cursor)
                delete_related_event_data(event_id, connection, cursor)
                post_event_type(event.Types, event_id, connection, cursor)
                post_event_tag(event.Tags, event_id, connection, cursor)
                post_event_social(event.Socials, event_id, connection, cursor)
                post_event_image(event.Images, event_id, connection, cursor)
                post_event_price(event.Prices, event_id, connection, cursor)
                post_event_performance(event.Performances, event_id, connection, cursor)
                connection.commit()
            except DatabaseError:
                connection.rollback()
                raise


def update_event(event_id: UUID, event: EventInsert, connection, cursor) -> None:
    execute(
    """
        UPDATE Event SET
            VenueID = %s,
            StageID = %s,
            Title = %s,
            Description = %s,
            StartDateTime = %s,
            EndDateTime = %s,
            OriginalPostURL = %s,
            TicketSaleURL = %s
        WHERE EventID = %s
    """,
        (
            str(event.Venue.VenueID),
            str(event.Venue.StageID),
            event.Title,
            event.Description,
            event.StartDateTime,
            event.EndDateTime,
            str(event.OriginalPostURL),
            str(event.TicketSaleURL),
            str(event_id)
        ),
        connection=connection,
        cursor=cursor
    )

def delete_related_event_data(event_id: UUID, connection, cursor):
    execute("DELETE FROM EventType WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM EventTag WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM EventSocial WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM EventPrice WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM EventPerformance WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM Image WHERE ImageID IN (SELECT EventImage.ImageID FROM EventImage WHERE EventImage.EventID = %s)", (str(event_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM EventImage WHERE EventID = %s", (str(event_id),), connection=connection, cursor=cursor)
