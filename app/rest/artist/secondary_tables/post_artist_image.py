from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def post_artist_image(images: Optional[list[ImageInsert]], artist_id: UUID, connection, cursor):
    if images:
        for image in images:
            response = execute_with_return(insert_image(), value_image(image), connection, cursor)
            execute(insert_artist_image(), value_artist_image(artist_id, response, image), connection, cursor)
            

# Image Table
def insert_image():
    return """
        INSERT INTO Image (Url) 
        VALUES (%s)
        RETURNING ImageID
    """

def value_image(image: ImageInsert):
    return (str(image.Url),)


# ArtistImage Table
def insert_artist_image():
    return """
        INSERT INTO ArtistImage (ArtistID, ImageID, DisplayOrder)
        VALUES (%s, %s, %s)
    """

def value_artist_image(artist_id: UUID, response: tuple, image: ImageInsert):
    return (
        str(artist_id),
        str(response[0]),
        image.DisplayOrder
    )
        