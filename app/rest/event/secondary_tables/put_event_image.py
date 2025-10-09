from app.query.execute import execute
from app.rest.event.secondary_tables.post_event_image import post_event_image
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def put_event_image(images: Optional[list[ImageInsert]], event_id: UUID, connection, cursor):
    execute(delete_existing_images(), (str(event_id),), connection, cursor)
    post_event_image(images, event_id, connection, cursor)
                

def delete_existing_images(): 
    # Will implicitly delete associated rows from `EventImage` with a cascade once row is deleted 
    # from `Image`.

    return """
        DELETE FROM Image
        WHERE ImageID IN (
            SELECT ImageID FROM EventImage
            WHERE EventID = %s
        );
    """
    