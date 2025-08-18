from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image import Image

def put_venue_image(images: Optional[list[Image]], venue_id: UUID, connection, cursor):
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
                UPDATE VenueImage
                SET DisplayOrder = %s
                WHERE VenueID = %s
                AND ImageID = %s
            """,
                (image.DisplayOrder, str(venue_id), str(image.ImageID)),
                connection=connection,
                cursor=cursor
            )