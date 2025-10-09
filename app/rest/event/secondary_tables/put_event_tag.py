from app.query.execute import execute
from app.rest.event.secondary_tables.post_event_tag import post_event_tag
from uuid import UUID
from typing import Optional, List

def put_event_tag(tags: Optional[List[str]], event_id: UUID, connection, cursor):
    execute(delete_existing_tags(), str(event_id), connection, cursor)
    post_event_tag(tags, event_id, connection, cursor)
                

def delete_existing_tags(): 
    return """
        DELETE FROM EventTag
        WHERE EventID = %s;
    """
    