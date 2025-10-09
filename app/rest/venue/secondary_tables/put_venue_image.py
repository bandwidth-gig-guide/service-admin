from app.query.execute import execute
from app.rest.venue.secondary_tables.post_venue_image import post_venue_image
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def put_venue_image(images: Optional[list[ImageInsert]], venue_id: UUID, connection, cursor):
    execute(delete_existing_images(), str(venue_id), connection, cursor)
    post_venue_image(images, venue_id, connection, cursor)
                

def delete_existing_images(): 
    # Will implicitly delete associated rows from `VenueImage` with a cascade once row is deleted 
    # from `Image`.

    return """
        DELETE FROM Image
        WHERE ImageID IN (
            SELECT ImageID FROM VenueImage
            WHERE VenueID = %s
        );
    """
    