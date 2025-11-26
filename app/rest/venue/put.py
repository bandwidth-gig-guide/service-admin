from app.query.execute import execute
from app.db.connection import get_db_connection

from app.rest.venue.secondary_tables.put_venue_type import put_venue_type
from app.rest.venue.secondary_tables.put_venue_tag import put_venue_tag
from app.rest.venue.secondary_tables.put_venue_social import put_venue_social
from app.rest.venue.secondary_tables.put_venue_image import put_venue_image
from app.rest.venue.secondary_tables.put_venue_stage import put_venue_stage
from app.rest.venue.secondary_tables.put_venue_opening_hours import put_venue_opening_hours

from app.model.venue_insert import VenueInsert
from uuid import UUID


def put(venue_id: UUID, venue: VenueInsert) -> None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                update_venue(venue_id, venue, connection, cursor)
                put_venue_type(venue.Types, venue_id, connection, cursor)
                put_venue_tag(venue.Tags, venue_id, connection, cursor)
                put_venue_social(venue.Socials, venue_id, connection, cursor)
                put_venue_image(venue.Images, venue_id, connection, cursor)
                put_venue_stage(venue.VenueStages, venue_id, connection, cursor)
                put_venue_opening_hours(venue.OpeningHours, venue_id, connection, cursor)
                connection.commit()
            except Exception:
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
            GoogleMapsEmbedURL = %s,
            IsFeatured = %s,
            IsMonitored = %s
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
        venue.IsFeatured,
        venue.IsMonitored,
        str(venue_id)
    ),
        connection=connection,
        cursor=cursor
    )
