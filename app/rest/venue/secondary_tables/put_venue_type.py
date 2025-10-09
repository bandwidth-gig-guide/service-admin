from app.query.execute import execute
from app.rest.venue.secondary_tables.post_venue_type import post_venue_type
from uuid import UUID
from typing import Optional, List

def put_venue_type(types: Optional[List[str]], venue_id: UUID, connection, cursor):
    execute(delete_existing_types(), str(venue_id), connection, cursor)
    post_venue_type(types, venue_id, connection, cursor)
                

def delete_existing_types(): 
    return """
        DELETE FROM VenueType
        WHERE VenueID = %s;
    """
    