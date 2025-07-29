from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_event_tag(tags: Optional[List[str]], event_id: UUID, connection, cursor):
    if tags:
        for tag in tags:
            execute(
            """
                INSERT INTO EventTag (EventID, Tag)
                VALUES (%s, %s)
            """,
                (str(event_id), tag),
                connection=connection,
                cursor=cursor
            )