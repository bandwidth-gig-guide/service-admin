from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_event_type(types: Optional[List[str]], event_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO EventType (EventID, Type) 
                VALUES (%s, %s)
            """,
                (str(event_id), type_),
                connection=connection,
                cursor=cursor
            )