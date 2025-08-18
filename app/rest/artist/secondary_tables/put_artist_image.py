from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image import Image

def put_artist_image(images: Optional[list[Image]], artist_id: UUID, connection, cursor):
    if images:
        for image in images:
            execute(
            """
                UPDATE Image
                SET Url = %s
                WHERE ImageID = %s
            """,
                (str(image.Url), str(image.ImageID)),
                connection=connection,
                cursor=cursor
            )

            execute(
            """
                UPDATE ArtistImage
                SET DisplayOrder = %s
                WHERE ArtistID = %s 
                AND ImageID = %s
            """,
                (image.DisplayOrder, str(artist_id), str(image.ImageID)),
                connection=connection,
                cursor=cursor
            )