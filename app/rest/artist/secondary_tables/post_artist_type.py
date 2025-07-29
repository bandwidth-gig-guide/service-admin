from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_artist_type(types: Optional[List[str]], artist_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO ArtistType (ArtistID, Type) 
                VALUES (%s, %s)
            """,
                (str(artist_id), type_),
                connection=connection,
                cursor=cursor
            )