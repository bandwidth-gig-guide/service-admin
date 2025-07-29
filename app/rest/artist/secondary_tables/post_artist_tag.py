from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_artist_tag(tags: Optional[List[str]], artist_id: UUID, connection, cursor):
    if tags:
        for tag in tags:
            execute(
            """
                INSERT INTO ArtistTag (ArtistID, Tag)
                VALUES (%s, %s)
            """,
                (str(artist_id), tag),
                connection=connection,
                cursor=cursor
            )