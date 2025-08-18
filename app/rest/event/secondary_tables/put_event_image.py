from app.query.execute import execute
from uuid import UUID
from typing import Optional
from app.model.image import Image

def put_event_image(images: Optional[list[Image]], event_id: UUID, connection, cursor):
    if images:
        for image in images:
            execute(
            """
                UPDATE Image
                SET URL = %s
                WHERE ImageID = %s
            """,
                (str(image.Url), str(image.ImageID)),
                connection=connection,
                cursor=cursor
            )
            execute(
            """
                UPDATE EventImage
                SET DisplayOrder = %s
                WHERE EventID = %s
                AND ImageID = %s
            """,
                (image.DisplayOrder, str(event_id), str(image.ImageID)),
                connection=connection,
                cursor=cursor
            )