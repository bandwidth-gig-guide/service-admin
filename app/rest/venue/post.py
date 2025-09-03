from app.query.execute_with_return import execute as execute_with_return
from app.db.connection import get_db_connection
from psycopg2 import DatabaseError

from app.rest.venue.secondary_tables.post_venue_type import post_venue_type
from app.rest.venue.secondary_tables.post_venue_tag import post_venue_tag
from app.rest.venue.secondary_tables.post_venue_social import post_venue_social
from app.rest.venue.secondary_tables.post_venue_image import post_venue_image
from app.rest.venue.secondary_tables.post_venue_stages import post_venue_stages
from app.rest.venue.secondary_tables.post_venue_opening_hours import post_venue_opening_hours

from app.model.venue_insert import VenueInsert
from uuid import UUID


def post(venue: VenueInsert) -> UUID:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                venue_id: UUID = post_venue(venue, connection, cursor)
                post_venue_type(venue.Types, venue_id, connection, cursor)
                post_venue_tag(venue.Tags, venue_id, connection, cursor)
                post_venue_social(venue.Socials, venue_id, connection, cursor)
                post_venue_image(venue.Images, venue_id, connection, cursor)
                post_venue_stages(venue.VenueStages, venue_id, connection, cursor)
                post_venue_opening_hours(venue.OpeningHours, venue_id, connection, cursor)
                connection.commit()
                return venue_id
            except DatabaseError:
                connection.rollback()
                raise


def post_venue(venue: VenueInsert, connection, cursor) -> UUID:
    response = execute_with_return(
    """
        INSERT INTO Venue (
            Title,
            StreetAddress,
            City,
            StateCode,
            PostCode,
            Description,
            WebsiteURL,
            PhoneNumber,
            GoogleMapsEmbedURL
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING VenueID
    """,
        venue.Title,
        venue.StreetAddress,
        venue.City,
        venue.StateCode,
        venue.PostCode,
        venue.Description,
        str(venue.WebsiteURL) if venue.WebsiteURL else None,
        venue.PhoneNumber,
        str(venue.GoogleMapsEmbedURL),
        connection=connection,
        cursor=cursor
    )
    return response[0]