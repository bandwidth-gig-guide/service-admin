from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_venue_tag(tags: Optional[List[str]], venue_id: UUID, connection, cursor):
    if tags:
        for tag in tags:
            execute(
            """
                INSERT INTO VenueTag (VenueID, Tag)
                VALUES (%s, %s)
            """,
                (str(venue_id), tag),
                connection=connection,
                cursor=cursor
            )