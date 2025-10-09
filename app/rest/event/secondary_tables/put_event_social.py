from app.query.execute import execute
from app.rest.event.secondary_tables.post_event_social import post_event_social
from uuid import UUID
from typing import Optional, List

def put_event_social(socials: Optional[List[str]], event_id: UUID, connection, cursor):
    execute(delete_existing_socials(), (str(event_id),), connection, cursor)
    post_event_social(socials, event_id, connection, cursor)
                

def delete_existing_socials(): 
    return """
        DELETE FROM EventSocial 
        WHERE EventID = %s
    """
    