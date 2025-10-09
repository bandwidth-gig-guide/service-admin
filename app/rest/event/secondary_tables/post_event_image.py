from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def post_event_image(images: Optional[list[ImageInsert]], event_id: UUID, connection, cursor):
    if images:
        for image in images:
            response = execute_with_return(insert_image(), value_image(image), connection, cursor)
            execute(insert_event_image(), value_event_image(event_id, response, image), connection, cursor)
            

# Image Table
def insert_image():
    return """
        INSERT INTO Image (Url) 
        VALUES (%s)
        RETURNING ImageID
    """

def value_image(image: ImageInsert):
    return (str(image.Url),)


# EventImage Table
def insert_event_image():
    return """
        INSERT INTO EventImage (EventID, ImageID, DisplayOrder)
        VALUES (%s, %s, %s)
    """

def value_event_image(event_id: UUID, response: tuple, image: ImageInsert):
    return (
        str(event_id),
        str(response[0]),
        image.DisplayOrder
    )
        