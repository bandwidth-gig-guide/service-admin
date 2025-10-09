from app.query.execute import execute
from app.rest.artist.secondary_tables.post_artist_image import post_artist_image
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def put_artist_image(images: Optional[list[ImageInsert]], artist_id: UUID, connection, cursor):
    execute(delete_existing_images(), str(artist_id), connection, cursor)
    post_artist_image(images, artist_id, connection, cursor)
                

def delete_existing_images(): 
    # Will implicitly delete associated rows from `ArtistImage` with a cascade once row is deleted 
    # from `Image`.

    return """
        DELETE FROM Image
        WHERE ImageID IN (
            SELECT ImageID FROM ArtistImage
            WHERE ArtistID = %s
        );
    """
    