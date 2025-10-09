from app.query.execute import execute
from app.db.connection import get_db_connection
from psycopg2 import DatabaseError

from app.rest.venue.secondary_tables.post_venue_type import post_venue_type
from app.rest.venue.secondary_tables.post_venue_tag import post_venue_tag
from app.rest.venue.secondary_tables.post_venue_social import post_venue_social
from app.rest.venue.secondary_tables.put_venue_image import put_venue_image
from app.rest.venue.secondary_tables.post_venue_stages import post_venue_stages
from app.rest.venue.secondary_tables.post_venue_opening_hours import post_venue_opening_hours

from app.model.venue_insert import VenueInsert
from uuid import UUID


def put(venue_id: UUID, venue: VenueInsert) -> None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                update_venue(venue_id, venue, connection, cursor)
                delete_related_venue_data(venue_id, connection, cursor)
                post_venue_type(venue.Types, venue_id, connection, cursor)
                post_venue_tag(venue.Tags, venue_id, connection, cursor)
                post_venue_social(venue.Socials, venue_id, connection, cursor)
                put_venue_image(venue.Images, venue_id, connection, cursor)
                post_venue_stages(venue.VenueStages, venue_id, connection, cursor)
                post_venue_opening_hours(venue.OpeningHours, venue_id, connection, cursor)
                connection.commit()
            except DatabaseError:
                connection.rollback()
                raise


def update_venue(venue_id: UUID, venue: VenueInsert, connection, cursor) -> None:
    execute(
    """
        UPDATE Venue SET
            Title = %s,
            StreetAddress = %s,
            City = %s,
            StateCode = %s,
            PostCode = %s,
            Description = %s,
            WebsiteURL = %s,
            PhoneNumber = %s,
            GoogleMapsEmbedURL = %s
        WHERE VenueID = %s
    """,
    (
        venue.Title,
        venue.StreetAddress,
        venue.City,
        venue.StateCode,
        venue.PostCode,
        venue.Description,
        str(venue.WebsiteURL) if venue.WebsiteURL else None,
        venue.PhoneNumber,
        str(venue.GoogleMapsEmbedURL),
        str(venue_id)
    ),
        connection=connection,
        cursor=cursor
    )

def delete_related_venue_data(venue_id: UUID, connection, cursor):
    execute("DELETE FROM VenueType WHERE VenueID = %s", (str(venue_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM VenueTag WHERE VenueID = %s", (str(venue_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM VenueSocial WHERE VenueID = %s", (str(venue_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM VenueOpeningHours WHERE VenueID = %s", (str(venue_id),), connection=connection, cursor=cursor)
    execute("DELETE FROM VenueStage WHERE VenueID = %s", (str(venue_id),), connection=connection, cursor=cursor)
