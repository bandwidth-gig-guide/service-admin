from app.query.execute import execute
from app.rest.event.secondary_tables.post_event_type import post_event_type
from uuid import UUID
from typing import Optional, List

def put_event_type(types: Optional[List[str]], event_id: UUID, connection, cursor):
    execute(delete_existing_types(), str(event_id), connection, cursor)
    post_event_type(types, event_id, connection, cursor)
                

def delete_existing_types(): 
    return """
        DELETE FROM EventType
        WHERE EventID = %s;
    """
    