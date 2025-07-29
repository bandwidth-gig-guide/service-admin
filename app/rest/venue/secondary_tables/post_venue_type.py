from app.query.execute import execute
from uuid import UUID
from typing import Optional, List

def post_venue_type(types: Optional[List[str]], venue_id: UUID, connection, cursor):
    if types:
        for type_ in types:
            execute(
            """
                INSERT INTO VenueType (VenueID, Type) 
                VALUES (%s, %s)
            """,
                (venue_id, type_),
                connection=connection,
                cursor=cursor
            )