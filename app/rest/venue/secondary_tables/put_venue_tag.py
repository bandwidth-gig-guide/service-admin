from app.query.execute import execute
from app.rest.venue.secondary_tables.post_venue_tag import post_venue_tag
from uuid import UUID
from typing import Optional, List

def put_venue_tag(tags: Optional[List[str]], venue_id: UUID, connection, cursor):
    execute(delete_existing_tags(), (str(venue_id),), connection, cursor)
    post_venue_tag(tags, venue_id, connection, cursor)
                

def delete_existing_tags(): 
    return """
        DELETE FROM VenueTag
        WHERE VenueID = %s;
    """
    