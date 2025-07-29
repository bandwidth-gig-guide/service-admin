from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import Optional
from pydantic import HttpUrl

def post_artist_image(imageUrls: Optional[list[HttpUrl]], artist_id: UUID, connection, cursor):
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
                INSERT INTO ArtistImage (ArtistID, ImageID, DisplayOrder)
                VALUES (%s, %s, %s)
            """,
                (str(artist_id), str(image_id), index + 1),
                connection=connection,
                cursor=cursor
            )