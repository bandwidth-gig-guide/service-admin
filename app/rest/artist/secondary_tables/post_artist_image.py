from app.query.execute_with_return import execute as execute_with_return
from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image_insert import ImageInsert

def post_artist_image(images: Optional[list[ImageInsert]], artist_id: UUID, connection, cursor):
    if images:
        for image in images:
            response = execute_with_return(
            """
                INSERT INTO Image (Url) 
                VALUES (%s)
                RETURNING ImageID

            """,
                (str(image.Url)),
                connection=connection,
                cursor=cursor
            )
            image_id: UUID = response[0]

            execute(
            """
                INSERT INTO ArtistImage (ArtistID, ImageID, DisplayOrder)
                VALUES (%s, %s, %s)
            """,
                (str(artist_id), str(image_id), image.DisplayOrder),
                connection=connection,
                cursor=cursor
            )