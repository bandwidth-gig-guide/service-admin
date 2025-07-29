from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import Optional
from pydantic import  HttpUrl

def post_venue_image(imageUrls: Optional[list[HttpUrl]], venue_id: UUID, connection, cursor):
    if imageUrls:
        for index, url in enumerate(imageUrls):
            response = execute_with_return(
            """
                INSERT INTO Image (Url) 
                VALUES (%s)
                RETURNING ImageID
            """,
                (str(url)),
                connection=connection,
                cursor=cursor
            )
            image_id: UUID = response[0]

            execute(
            """
                INSERT INTO VenueImage (VenueID, ImageID, DisplayOrder)
                VALUES (%s, %s, %s)
            """,
                (venue_id, image_id, index + 1),
                connection=connection,
                cursor=cursor
            )